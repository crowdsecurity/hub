import argparse
import base64
import collections
import enum
import json
import sys
import textwrap
import time
import tomllib
import typing
from http import HTTPMethod
from pathlib import Path
from typing import override

import jsonschema
import requests
import yaml
from tap import Tap

RED = ""
GREEN = ""
YELLOW = ""
BLUE = ""
RESET = ""
UNDERLINE = ""

BOL = "\r"
ERASETOEOL = "\033[0K"

# TODO:
# --file-only to check only the modified files
#      (if an item has the file path, it's checked, otherwise it's skipped)
# --item-only to check only the specified items, with a glob pattern
# tests
# publish comment on PR
# markdown report: error and warning must keep track of the item (proper class!)
# review linter names, descriptions and defaults
# separate index linters (to run in CI) from the others, which can be run before committing (with an out-of-date index)
#   - linter name prefix?
#   - separate config section?
#   - flag to skip them?


isatty = sys.stdout.isatty


def init_colors(force: str) -> None:
    global RED, GREEN, YELLOW, BLUE, RESET, UNDERLINE
    if force == "always" or (force == "auto" and isatty()):
        RED = "\033[91m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        BLUE = "\033[94m"
        RESET = "\033[0m"
        UNDERLINE = "\033[4m"


# tweaked from https://github.com/yaml/pyyaml/issues/456
class TrackingLoader(yaml.SafeLoader):
    def __init__(self, stream: str) -> None:
        super().__init__(stream)
        self.locations: dict[int, tuple[int, int] | None] = {}

    def compose_node(self, parent, index):
        # Get the start position before composing the node
        start_line, start_column = self.line, self.column
        node = super().compose_node(parent, index)
        # Attach the start position to the node itself
        node._myloader_start_location = (start_line, start_column)
        return node

    def construct_object(self, node, deep=False):
        # Construct the object first
        obj = super().construct_object(node, deep=deep)
        key = id(obj)
        # Use the start location attached to the node
        if hasattr(node, "_myloader_start_location"):
            self.locations[key] = node._myloader_start_location
        else:
            self.locations[key] = None
        return obj

    @classmethod
    def load(cls, stream):
        loader = cls(stream)
        try:
            return loader.get_single_data(), loader.locations
        finally:
            loader.dispose()


class Linter:
    def __init__(self) -> None:
        # XXX: this is mandatory
        self.index = None
        cls = self.__class__.__name__
        if not hasattr(self, "name"):
            raise ValueError(f"Linter {cls} must have a name")
        if not hasattr(self, "description"):
            raise ValueError(f"Linter {cls} must have a description")
        if not hasattr(self, "enabled"):
            raise ValueError(f"Linter {cls} must have a default 'enabled' attribute")
        if not hasattr(self, "error"):
            raise ValueError(f"Linter {cls} must have a default 'error' attribute")
        if not callable(self):
            raise ValueError(f"Linter {cls} must have a __call__ method")

    def err(self, message: str, ob=None):
        location = None
        if ob:
            location = self.index.locate(ob)
        return Issue(self, message, Severity.ERROR, location)

    def warn(self, message: str, ob=None):
        location = None
        if ob:
            location = self.index.locate(ob)
        return Issue(self, message, Severity.WARNING, location)


class Index:
    def __init__(self, index_content: str, enabled_linters: list[Linter]) -> None:
        # self._index = json.loads(index_content)
        self._index, self._yaml_locations = TrackingLoader.load(index_content)
        self.hubtypes = list(self._index.keys())
        # cache for http requests, by method and url
        self._http_cache: dict[tuple[str, str], requests.Response] = {}
        # some linter may skip some checks if they are covered by others
        self.enabled_linters = enabled_linters
        # eager creation of items, so we can store stuff if needed
        self._items = []
        for hubtype, content in self._index.items():
            for key, spec in content.items():
                self._items.append(Item(hubtype, key, spec))

    def __iter__(self):
        yield from self._items

    def locate(self, ob):
        # TODO: return file path too
        return self._yaml_locations.get(id(ob))

    def proxy(self, method: HTTPMethod, url: str) -> requests.Response:
        """Return a cached reponse, if it exists"""
        try:
            return self._http_cache[(url, method)]
        except KeyError:
            r = requests.request(method, url)
            self._http_cache[(url, method)] = r
            return r


class Severity(enum.StrEnum):
    WARNING = "warning"
    ERROR = "error"


class Issue:
    def __init__(self, linter: Linter, message: str, severity: Severity, location=None) -> None:
        self.linter: Linter = linter
        self.message: str = message
        self.location = location
        self._reported_severity: Severity = severity
        # set by the Item after the Issue is created
        self.item = None

    @property
    def severity(self) -> Severity:
        # the severity can be ERROR only if the linter is in error mode
        if self.linter.error:
            return self._reported_severity
        return Severity.WARNING

    # TODO: __str__ ?


class Item:
    def __init__(self, hubtype, key, spec):
        self.hubtype = hubtype
        self.key = key
        self._spec = spec
        self._issues = []

    def __str__(self):
        return f"{self.hubtype}:{self.key}"

    def validate(self, linters):
        for linter in linters:
            for issue in linter(self):
                issue.item = self
                self._issues.append(issue)

    def yaml_content(self) -> str:
        try:
            pth = self._spec["path"]
        except KeyError:
            return ""

        try:
            with Path(pth).open() as file:
                return file.read()
        except FileNotFoundError:
            return ""

    # XXX: loading documents can have errors, how to handle them?
    def yaml_docs(self):
        content = self.yaml_content()
        if not content:
            return
        yield from yaml.safe_load_all(content)

    def data_urls(self):
        for doc in self.yaml_docs():
            data = doc.get("data", [])
            for data in data:
                if "source_url" in data:
                    yield data["source_url"]


# yeah, it's a joke/example
class NotLinux(Linter):
    name: str = "not-linux"
    description: str = "Item name must not contain 'linux'"
    enabled: bool = False
    error: bool = False

    def __call__(self, item):
        if "linux" in item.key:
            yield self.err(
                f"Name contains 'linux': {item.key}",
                self.index._index[item.hubtype][item.key],
            )


class OnlyCollectionHaveDependencies(Linter):
    name: str = "only-collection-have-dependencies"
    description: str = "Only collections can have dependencies"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        if item.hubtype == "collections":
            return
        for typ in self.index.hubtypes:
            deps = item._spec.get(typ, [])
            if deps:
                yield self.err(
                    f"Item declares dependencies but it's not a collection: {typ}={deps}",
                    self.index._index[item.hubtype][item.key][typ],
                )


class EmptyDependencies(Linter):
    name: str = "empty-dependencies"
    description: str = "An item (collection) contains an explicit empty dependency (ex. parsers=[])"
    enabled: bool = True
    error: bool = False

    def __call__(self, item):
        for typ in self.index.hubtypes:
            if item._spec.get(typ) == []:
                yield self.err(
                    f"Empty dependency: {typ}=[]",
                    self.index._index[item.hubtype][item.key][typ],
                )


class OneDocumentPerYAMLFile(Linter):
    name: str = "one-document-per-yaml-file"
    description: str = "Each YAML file must contain only one document"
    enabled: bool = False
    error: bool = False

    def __call__(self, item):
        names = [doc.get("name") for doc in item.yaml_docs()]
        if len(names) > 1:
            yield self.err(f"File {item._spec['path']} contains more than one document: {names}")


class MissingAuthor(Linter):
    name: str = "missing-author"
    description: str = "Each item must have an author field"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        if not item._spec.get("author"):
            yield self.err("Missing 'author' field", self.index._index[item.hubtype][item.key])


class MissingItemFile(Linter):
    name: str = "missing-item-file"
    description: str = "The item file is missing"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        try:
            with Path(item._spec["path"]).open():
                pass
        except FileNotFoundError:
            yield self.err(f"File '{item._spec['path']}' does not exist")
        except KeyError:
            yield self.err("Missing 'path' field", self.index._index[item.hubtype][item.key])


class MissingDependencies(Linter):
    name: str = "missing-dependencies"
    description: str = "An item declares a dependency that does not exist"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        for typ in self.index.hubtypes:
            for dep_idx, dep in enumerate(item._spec.get(typ, [])):
                if dep not in self.index._index.get(typ, {}):
                    yield self.err(
                        f"Dependency '{typ}:{dep}' does not exist",
                        self.index._index[item.hubtype][item.key][typ][dep_idx],
                    )


class BadPath(Linter):
    name: str = "bad-path"
    description: str = "The path must match the item type, stage (if it exists) and name"
    enabled: bool = True
    error: bool = False

    def __call__(self, item):
        stage = item._spec.get("stage")
        basedir = f"{item.hubtype}/{stage}" if stage else item.hubtype
        expected_paths = [
            f"{basedir}/{item.key}.yml",
            f"{basedir}/{item.key}.yaml",
        ]
        pth = item._spec.get("path")
        if pth not in expected_paths:
            ob = self.index._index[item.hubtype][item.key]
            if "path" in ob:
                ob = ob["path"]
            yield self.err(
                f"Path '{pth}' does not match item type/stage/name (must be one of: {expected_paths})",
                ob,
            )


class MissingPath(Linter):
    name: str = "missing-path"
    description: str = "Each item must have a path field"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        if not item._spec.get("path"):
            yield self.err("Missing 'path' field", self.index._index[item.hubtype][item.key])


class AuthorMatchkey(Linter):
    name: str = "author-match-key"
    description: str = "The author field must match the item key"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        author = item._spec.get("author", "")
        if not item.key.startswith(author + "/"):
            ob = self.index._index[item.hubtype][item.key]
            if "author" in ob:
                ob = ob["author"]
            yield self.err(f"Author field '{author}' does not match the item key '{item.key}'", ob)


class DocumentWithoutName(Linter):
    name: str = "document-without-name"
    description: str = "Each section of a YAML file must have a name (only scenarios)"
    enabled: bool = True
    error: bool = True
    # XXX: we could make linters configurable from the toml file
    config: typing.ClassVar = {"hubtypes": ["scenarios"]}

    def __call__(self, item):
        if item.hubtype not in self.config["hubtypes"]:
            return
        for doc in item.yaml_docs():
            if not doc.get("name"):
                yield self.err(f"YAML document without name: {item._spec['path']}")


class DocumentNameMatchingItem(Linter):
    name: str = "document-name-matching-item"
    description: str = "The name of the document must match the item name (only scenarios+appsec-configs)"
    enabled: bool = False
    error: bool = False
    config: typing.ClassVar = {"hubtypes": ["scenarios", "appsec-configs"]}

    def __call__(self, item):
        if item.hubtype not in self.config["hubtypes"]:
            return
        for doc in item.yaml_docs():
            if doc.get("name") == item.key:
                return
        yield self.err(f"YAML file {item._spec.get('path')} does not have a document named: {item.key}")


class ItemSchema(Linter):
    name: str = "item-schema"
    description: str = "Validate item files against their YAML schema"
    enabled: bool = False
    error: bool = False
    config: typing.ClassVar = {
        "collections": {
            "url": "https://raw.githubusercontent.com/crowdsecurity/crowdsec-yaml-schemas/main/collection_schema.yaml",
        },
        "parsers": {
            "url": "https://raw.githubusercontent.com/crowdsecurity/crowdsec-yaml-schemas/main/parser_schema.yaml",
        },
        "scenarios": {
            "url": "https://raw.githubusercontent.com/crowdsecurity/crowdsec-yaml-schemas/main/scenario_schema.yaml",
        },
        "postoverflows": {
            "url": "https://raw.githubusercontent.com/crowdsecurity/crowdsec-yaml-schemas/main/parser_schema.yaml",
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._schemas = {}

    def __call__(self, item):
        if item.hubtype not in self.config:
            return

        if item.hubtype not in self._schemas:
            try:
                yaml_schema = requests.get(self.config[item.hubtype]["url"]).text
                self._schemas[item.hubtype] = yaml.safe_load(yaml_schema)
            except requests.RequestException as e:
                yield self.err(f"Failed to fetch schema for {item.hubtype}: {e}")
                return

        schema = self._schemas[item.hubtype]
        for doc in item.yaml_docs():
            try:
                jsonschema.validate(doc, schema)
            except jsonschema.ValidationError as e:
                yield self.err(f"File {item._spec.get('path')} does not match the schema: {e.message}")


class DataFilesExist(Linter):
    name: str = "data-files-exist"
    description: str = "Check the source_url of the data files declared in the item"
    enabled: bool = False
    error: bool = True

    def __call__(self, item):
        for url in item.data_urls():
            try:
                if isatty():
                    print(f"Checking {url}{ERASETOEOL}{BOL}", end="")
                try:
                    r = self.index.proxy(HTTPMethod.HEAD, url)
                    r.raise_for_status()
                except requests.HTTPError as e:
                    yield self.err(f"HTTP error for data file {url}: {e}")
                    continue

            except requests.RequestException as e:
                yield self.err(f"Failed to fetch data file {url}: {e}")


class DataFilesLastModified(Linter):
    """This is implemented as a separate linter to allow for a warning instead of an error"""

    name: str = "data-files-last-modified"
    description: str = "Check the last-modified header of the data files declared in the item"
    enabled: bool = False
    error: bool = False

    def __call__(self, item):
        for url in item.data_urls():
            try:
                if isatty():
                    print(f"Checking {url}{ERASETOEOL}{BOL}", end="")
                r = self.index.proxy(HTTPMethod.HEAD, url)
                r.raise_for_status()
                if not r.headers.get("last-modified"):
                    yield self.err(f"Data file {url} does not have a 'last-modified' header")
            except requests.RequestException as e:
                # if the other linter is enabled, we don't report the error here
                if DataFilesExist.name in self.index.enabled_linters:
                    yield self.err(f"Failed to fetch data file {url}: {e}")


class NoDebugMode(Linter):
    name: str = "no-debug-mode"
    description: str = "The item must not be in debug mode"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        for doc in item.yaml_docs():
            if doc.get("debug"):
                # TODO: add location (needs file name support if it's other than the index file)
                yield self.err(f"Item file {item._spec.get('path')} in debug mode")


class ContentMatchFile(Linter):
    name: str = "content-match-file"
    description: str = "The content of the item must match the file"
    enabled: bool = True
    error: bool = True

    def __call__(self, item):
        # TODO: handle file or field not present
        from_file = item.yaml_content()
        from_file = from_file.encode("utf-8")
        from_file = base64.b64encode(from_file).decode("utf-8")
        from_field = item._spec.get("content")
        if from_field != from_file:
            yield self.err(f"Content field does not match the file: {item._spec.get('path')}")


# --------------------------------------------------------------------- #


# validate configuration and create linters
def linters_from_config(config):
    cfg_linters = config.get("linters", {})
    # create a default configuration for all linters
    for linter_class in Linter.__subclasses__():
        # see if the class can be instantiated, or defaults are missing
        linter_class()
        if linter_class.name not in cfg_linters:
            cfg_linters[linter_class.name] = {}

    for linter_name, linter_cfg in cfg_linters.items():
        for linter_class in Linter.__subclasses__():
            # TODO: check for duplicates
            if linter_class.name == linter_name:
                linter = linter_class()
                if linter_cfg.get("enabled") is not None:
                    linter.enabled = linter_cfg.get("enabled")
                if linter_cfg.get("error") is not None:
                    linter.error = linter_cfg.get("error")
                # XXX: default config for _each_ linter is not written to the TOML file
                if linter_cfg.get("config") is not None:
                    linter.config = linter_cfg.get("config")
                yield linter
                break
        else:
            raise ValueError(f"Unknown linter: {linter_name}")


class TTYReporter:
    spinner: typing.ClassVar = ["▹▹▹▹▹", "▸▹▹▹▹", "▹▸▹▹▹", "▹▹▸▹▹", "▹▹▹▸▹", "▹▹▹▹▸"]

    def __init__(self, no_warnings, show_location, print_ok=False):
        self.no_warnings = no_warnings
        self.show_location = show_location
        # leave feedback for successful checks too?
        self.print_ok = print_ok

    def item(self, item):
        pass

    def update_status(self, idx, tot, item):
        wheel = self.spinner[idx % len(self.spinner)]
        if isatty():
            print(f" {wheel} [{idx}/{tot}] {item}{ERASETOEOL}{BOL}", end="")

    def item_feedback(self, item, index, index_path: Path):
        print_feedback = False

        if any(i.severity == Severity.ERROR for i in item._issues):
            check = RED + "✗"
            print_feedback = True
        elif any(i.severity == Severity.WARNING for i in item._issues):
            check = YELLOW + "⚠"
            print_feedback = True
        else:
            check = GREEN + "✓"
            if not isatty():
                print_feedback = False

        if print_feedback or self.print_ok:
            print(f" {check}{RESET} {item}{ERASETOEOL}", end="")
            if self.print_ok:
                print()
            else:
                print(BOL, end="")

        if item._issues:
            if print_feedback or self.print_ok:
                print()
            for issue in item._issues:
                file = index_path.name
                if issue.location and self.show_location:
                    location = f" {file}:{issue.location[0] + 1}:{issue.location[1] + 1}:"
                else:
                    location = ""
                sev = RED if issue.severity == Severity.ERROR else YELLOW
                print(f"{sev}{issue.linter.name}:{RESET}{location} {issue.message}")


class MarkDownReporter:
    def __init__(self, outfile):
        self.outfile = outfile

    def write_report(self, index, enabled_linters):
        if not self.outfile:
            return

        self.outfile.write(self.report(index, enabled_linters))

    def report(self, index, enabled_linters):
        linters_desc = {linter.name: linter.description for linter in enabled_linters}

        errors = [i for item in index for i in item._issues if i.severity == Severity.ERROR]
        warnings = [i for item in index for i in item._issues if i.severity == Severity.WARNING]

        report = [
            "# Hublint Validation Report",
            "",
            f" Checked {len(enabled_linters)} linters: {len(errors)} errors, {len(warnings)} warnings",
            "",
        ]

        item_per_type = collections.defaultdict(list)
        for item in index:
            if not item._issues:
                continue
            item_per_type[item.hubtype].append(item)

        report.append("Issues were found by the following linters.")
        report.append("")

        failed_linters = {i.linter.name for i in errors + warnings}

        for linter in failed_linters:
            report.append(f"## {linter}")
            report.append(f"  {linters_desc[linter]}")

        for hubtype, items in item_per_type.items():
            for item in items:
                report.append(f"### {hubtype}:{item.key}")
                for issue in item._issues:
                    if issue.severity == Severity.ERROR:
                        report.append(f"  - :x: {issue.linter.name}: {issue.message}")
                    elif issue.severity == Severity.WARNING:
                        report.append(f"  - :warning: {issue.linter.name}: {issue.message}")

        return "\n".join(report)


def run_linters(index_path: Path, enabled_linters, no_warnings, show_location, markdown, quick):
    ttyrep = TTYReporter(no_warnings, show_location)
    mdrep = MarkDownReporter(markdown)

    t0 = time.time()

    try:
        index_content = index_path.read_text()
        index = Index(index_content, enabled_linters=enabled_linters)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)

    all_items = list(index)
    tot = len(all_items)

    tot_warnings = 0
    tot_errors = 0

    errors_by_linter = collections.defaultdict(int)
    warnings_by_linter = collections.defaultdict(int)

    # XXX: clean this mess
    for linter in enabled_linters:
        linter.index = index

    for idx, item in enumerate(all_items):
        ttyrep.update_status(idx, tot, item)
        item.validate(enabled_linters)

        ttyrep.item_feedback(item, index, index_path)

        errors = [i for i in item._issues if i.severity == Severity.ERROR]
        tot_errors += len(errors)
        for e in errors:
            errors_by_linter[e.linter.name] += 1
        warnings = [i for i in item._issues if i.severity == Severity.WARNING]
        for w in warnings:
            warnings_by_linter[w.linter.name] += 1
        tot_warnings += len(warnings)

        if not quick and isatty():
            # fake delay to show the cute spinner
            time.sleep(0.01)

            # but why? here's why.
            #
            # Psychological Perspective
            #
            #    Cognitive Processing Time: Users need time to process the
            #    information presented on the screen. An artificial pause can
            #    ensure that users have adequate time to read and understand
            #    the output before the application proceeds to the next step.
            #    This is especially crucial for complex outputs or instructions
            #    that require user attention and comprehension.
            #
            #    Reduced Cognitive Load: Rapidly updating the screen with new
            #    information can overwhelm users, leading to a higher cognitive
            #    load. By introducing a pause, the application allows the
            #    user's cognitive processes to catch up with the information
            #    flow, reducing the risk of information overload.
            #
            #    User Experience and Satisfaction: A pause can contribute to a
            #    more pleasant user experience by making the interaction feel
            #    less rushed and more deliberate. This pacing can make the
            #    application feel more responsive to the user's need for time
            #    to think and make decisions, potentially increasing overall
            #    user satisfaction.
            #
            #    Anticipation and Engagement: Strategic pauses can create a
            #    sense of anticipation, making the interaction more engaging.
            #    In scenarios where the application performs a complex task, a
            #    brief pause before displaying the result can enhance the
            #    perceived value of the outcome.
            #
            #  Other practical reasons can be provided on request.
            #  More importantly, it allows the developer to make the application faster in a new version.

    elapsed = time.time() - t0
    print(f"Checked {tot} items: {tot_warnings} warnings, {tot_errors} errors in {elapsed:.2}s{ERASETOEOL}")
    print()

    if len(errors_by_linter) > 0:
        print("Errors by linter:")
    for linter, count in sorted(errors_by_linter.items()):
        print(f" {linter}: {count}")

    if len(warnings_by_linter) > 0:
        print("Warnings by linter:")
    for linter, count in sorted(warnings_by_linter.items()):
        print(f" {linter}: {count}")

    mdrep.write_report(index, enabled_linters)

    return tot_errors


def read_config(config: Path):
    with config.open("rb") as config_file:
        try:
            return tomllib.load(config_file)
        except tomllib.TOMLDecodeError as e:
            print(f"Error parsing TOML: {e}", file=sys.stderr)
            sys.exit(1)


def print_linters(linters):
    init_colors("auto")
    print("Available linters:")
    for linter in linters:
        enabled = f"{GREEN}✓{RESET}" if linter.enabled else f"{RED}✗{RESET}"
        print(f" {enabled} {linter.name}: {linter.description}")
        if linter.enabled:
            if linter.error:
                print("   error")
            else:
                print("   warning")


def print_default_config():
    linters = list(Linter.__subclasses__())
    for linter in linters:
        print(f"# {linter.description}")
        print(f"[linters.{linter.name}]")
        print(f"enabled = {linter.enabled.__str__().lower()}")
        print(f"error = {linter.error.__str__().lower()}")
        print()


class LinterParser(Tap):
    config: Path

    @override
    def configure(self) -> None:
        self.add_argument("--config", default=".hublint.toml", help="The configuration file")


class CheckParser(Tap):
    config: Path
    index: Path
    color: str
    no_warning_details: bool
    show_location: bool
    markdown: Path
    quick: bool
    lint_only: list[str]

    @override
    def configure(self):
        self.add_argument("--config", default=".hublint.toml", help="The configuration file")

        self.add_argument("--index", default=".index.json", help="The index file to validate")

        self.add_argument("--color", choices=["always", "never", "auto"], default="auto", help="Force colored output")

        self.add_argument(
            "--no-warning-details",
            default=False,
            action="store_true",
            help="Do not show warning details (still, count them)",
        )

        self.add_argument("--show-location", default=False, action="store_true", help="Show the location of the error/warning")

        self.add_argument("--markdown", required=False, help="Generate a markdown report")

        self.add_argument("--quick", default=False, action="store_true", help="Quick mode (default when stdout is redirected)")

        self.add_argument("--lint-only", required=False, nargs="+", help="Run only the specified linters")


class DefaultsParser(Tap):
    pass


class Parser(Tap):
    @override
    def configure(self) -> None:
        self.add_subparsers(dest="command")
        self.add_subparser("linters", LinterParser, help="Show all the available linters")
        self.add_subparser(
            "check", CheckParser, help="Validate an index file", formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        self.add_subparser(
            "defaults",
            DefaultsParser,
            help="Show the default configuration",
            formatter_class=argparse.RawTextHelpFormatter,
            epilog=textwrap.dedent("""
                                      Example:

                                        # generate an initial configuration file
                                        hublint defaults > .hublint.toml
                                      """),
        )


def main():
    parser = Parser(
        description="Validate hub index files",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent("""
                        Example:

                        # generate the initial configuration
                        hublint defaults > .hublint.toml

                        # validate an index file
                        hublint check --index .index.json
                        """),
    )

    args = parser.parse_args()

    if args.command not in [None, "defaults"]:
        print(f"Using config: {args.config.name}")
        config = read_config(args.config)
        all_linters = list(linters_from_config(config))

    if args.command == "linters":
        print_linters(all_linters)
        sys.exit(0)
    elif args.command == "check":
        init_colors(args.color)
        print(f"Validating: '{args.index.name}'")
        print()

        for linter in args.lint_only or []:
            if linter not in [linter.name for linter in all_linters]:
                print(f"Unknown linter: {linter}", file=sys.stderr)
                sys.exit(1)

        for linter in all_linters:
            if args.lint_only:
                linter.enabled = linter.name in args.lint_only

        tot_errors = run_linters(
            args.index,
            [linter for linter in all_linters if linter.enabled],
            no_warnings=args.no_warning_details,
            show_location=args.show_location,
            markdown=args.markdown,
            quick=args.quick,
        )
        sys.exit(tot_errors > 0)
    elif args.command == "defaults":
        print_default_config()
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(1)
