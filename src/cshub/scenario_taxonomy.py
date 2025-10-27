import argparse
import contextlib
import csv
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from itertools import chain
from pathlib import Path
from typing import override

import yaml
from tap import Tap
from yaml.loader import SafeLoader

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}")
CWE_RE = re.compile(r"CWE-\d{2,6}")
author = os.environ.get("AUTHOR", "ghost")

OK_STR = f"""
Hello @{author},

Scenarios/AppSec Rule are compliant with the taxonomy, thank you for your contribution!
"""

INTRO_STR = f"""
Hello @{author} and thank you for your contribution!

I'm a bot that helps maintainers to validate scenarios and ensure they include all the required information.
I've found some errors in your scenarios, please fix them and re-submit your PR, or ask for help if you need it.

The following items have errors:

"""

HELP_STR = """


## Mitre ATT&CK

Information about mitre attack can be found [here](https://attack.mitre.org/techniques/enterprise/).
As an example, some common mitre attack techniques:
 - T1110 for bruteforce attacks
 - T1595 and T1190 for exploitation of public vulnerabilities
 - T1595 for generic scanning of exposed applications

Expected format is (where `XXXX` is the technique ID):

```yaml
labels:
  classification:
    - attack.TXXXX
```

## CVEs

If your scenario covers a specific CVE (Common Vulnerabilities and Exposures), please add it.

Expected format is (where `CVE-XXX-XXX` is the CVE ID):

```yaml
labels:
  classification:
    - cve.CVE-XXX-XXX
```

## Behaviors

Please identify the behavior(s) your scenario is targeting. You can find the list of available behaviors [here](https://docs.crowdsec.net/docs/next/cti_api/taxonomy/behaviors).

Expected format is (where `<behavior>` is the behavior you want to target):

```yaml
labels:
  behavior: <behavior>
```

See [the labels documentation](https://docs.crowdsec.net/docs/next/scenarios/format#labels) for more information.
"""


def get_behavior_from_label(labels):
    service = ""
    attack_type = ""

    if "behavior" in labels:
        return labels["behavior"]

    if "service" in labels:
        service = labels["service"]

    if "type" in labels:
        attack_type = labels["type"]

    if "target" in labels:
        for t in labels["target"]:
            if t.startswith("protocol"):
                service = t.split(".")[-1]

    if service == "" and "os" in labels:
        service = labels["os"]

    return f"{service}:{attack_type}"


def get_mitre_tactic_from_technique(technique, mitre_data):
    for tactic, tactic_info in mitre_data.items():
        for tech in tactic_info["techniques"]:
            if technique == tech["name"]:
                return tactic
    return None


def get_mitre_techniques_from_label(labels, mitre_data):
    ret = []
    errors = []
    if "classification" not in labels or not labels["classification"]:
        return ret, errors

    for classification in labels["classification"]:
        split_attack = classification.split(".")
        if split_attack[0] != "attack":
            continue
        if len(split_attack) < 2:
            errors.append(f"bad mitre format: {classification}")
            continue
        technique = split_attack[1]
        tactic = get_mitre_tactic_from_technique(technique, mitre_data)
        if tactic is None:
            errors.append(f"unknown mitre technique: {technique}")
            continue
        ret.append(f"{tactic}:{technique}")

    return ret, errors


def get_cwe_from_label(labels):
    ret = []
    errors = []
    if "classification" not in labels or not labels["classification"]:
        return ret, errors

    for classification in labels["classification"]:
        split_cwe = classification.split(".")
        if split_cwe[0] != "cwe":
            continue
        cwe = split_cwe[1].upper()

        if CWE_RE.match(cwe) is None:
            errors.append(f"bad CWE format: {cwe}")
            continue
        ret.append(cwe)

    return ret, errors


def get_git_creation_dates(paths: list[str]) -> dict[str, str]:
    """Return a mapping of file path -> first commit author date (ISO 8601).

    Paths must be normalized (i.e. no leading "./").

    If a file was removed and re-added, the first addition counts.
    If a file is not committed, it's returned with "now".
    """

    if not paths:
        raise ValueError("paths list cannot be empty")

    cmd = [
        "git",
        "log",
        "--diff-filter=A",
        "--pretty=format:%aI",
        "--name-only",
        "--",
        *paths,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    dates: dict[str, str] = {}
    current_date: str | None = None
    expecting_date = True

    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            expecting_date = True
            continue

        if expecting_date:
            dt = datetime.fromisoformat(line)
            dt_utc = dt.astimezone(tz=timezone.utc).replace(microsecond=0)
            current_date = dt_utc.isoformat().replace("+00:00", "")
            expecting_date = False
        elif current_date:
            dates[line] = current_date

    # fill in the blanks
    now_str = datetime.now(tz=timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "")
    for path in paths:
        if path not in dates:
            dates[path] = now_str

    return dates


def get_cve_from_label(labels):
    ret = []
    errors = []
    if "classification" not in labels or not labels["classification"]:
        return ret, errors

    for classification in labels["classification"]:
        split_cve = classification.split(".")
        if split_cve[0] != "cve":
            continue
        cve = split_cve[1].upper()

        if CVE_RE.match(cve) is None:
            errors.append(f"bad CVE format: {cve}")
            continue
        ret.append(cve)

    return ret, errors


def main():
    parser = Parser(
        description="Generate CrowdSec Scenarios taxonomy file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    args = parser.parse_args()

    if args.hub == "":
        print("[-] Please provide the hub path with the --hub argument")
        sys.exit(1)

    changed_files = os.environ.get("changed_files", "").split(",")
    if changed_files == [""]:
        changed_files = []
        print("[-] No changed files found, run on all files.")
    else:
        print(f"[+] Changed files: {changed_files}")

    with Path(args.mitre).open() as f:
        mitre_data = json.load(f)

    with Path(args.behaviors).open() as f:
        behavior_data = json.load(f)

    stats = {"scenarios_ok": [], "scenarios_nok": [], "mitre": [], "behaviors": []}
    hub_scenarios_path = os.path.join(args.hub, "scenarios")
    hub_appsecrules_path = os.path.join(args.hub, "appsec-rules")
    ignore_list = []

    print(f"Ignoring: {args.ignore}")
    with contextlib.suppress(FileNotFoundError), Path(args.ignore).open() as f:
        ignore_list = f.read().split("\n")

    errors: dict[str, list[str]] = {}
    scenarios_taxonomy = {}
    filepath_list = []

    for r, d, f in chain.from_iterable(
        os.walk(path) for path in [hub_scenarios_path, hub_appsecrules_path]
    ):
        for file in f:
            if file.endswith((".yaml", ".yml")):
                filepath_list.append(os.path.join(r, file))

    filepath_list.sort()
    filepath_list = [str(Path(p).resolve().relative_to(Path.cwd())) for p in filepath_list]
    cpt = 0
    mitres = {}

    creation_dates = get_git_creation_dates(filepath_list)

    for filepath in filepath_list:
        print(f"[+] Processing {filepath}")
        with Path(filepath).open() as f:
            data = list(yaml.load_all(f, Loader=SafeLoader))

        for scenario in data:
            if scenario["name"] in ignore_list:
                continue

            cpt += 1
            scenario_errors: list[str] = []
            if "labels" not in scenario:
                scenario_errors.append("`labels` not found")
                errors[scenario["name"]] = scenario_errors
                stats["scenarios_nok"].append(scenario["name"])
                continue

            labels = scenario["labels"]
            behavior = get_behavior_from_label(labels)
            mitre_techniques, mitre_errors = get_mitre_techniques_from_label(
                labels,
                mitre_data,
            )
            scenario_errors.extend(mitre_errors)
            if behavior == "":
                scenario_errors.append("`behavior` key not found in labels")

            if len(mitre_techniques) == 0:
                scenario_errors.append("`attack` not found in labels.classification")
            service = labels.get("service", None)

            for m in mitre_techniques:
                if m not in stats["mitre"]:
                    stats["mitre"].append(m)
                ta, te = m.split(":")[0], m.split(":")[1]
                if ta not in mitres:
                    mitres[ta] = {}

                if te not in mitres[ta]:
                    mitres[ta][te] = {}

                if "scenarios" not in mitres[ta][te]:
                    mitres[ta][te]["scenarios"] = []

                mitres[ta][te]["scenarios"].append(scenario["name"])

            cves, cves_errors = get_cve_from_label(labels)
            scenario_errors.extend(cves_errors)
            cwes, cwes_errors = get_cwe_from_label(labels)
            scenario_errors.extend(cwes_errors)

            scenario_label = ""
            confidence = 0
            spoofable = 0
            in_cti = True

            if "label" in labels:
                scenario_label = scenario["labels"]["label"]
            if "spoofable" in labels:
                spoofable = labels["spoofable"]
            else:
                scenario_errors.append("`spoofable` key not found in labels")
            if "confidence" in labels:
                if not isinstance(labels["confidence"], int):
                    scenario_errors.append("`confidence` key should be an integer")
                elif labels["confidence"] < 0 or labels["confidence"] > 3:
                    scenario_errors.append("`confidence` key should be between 0 and 3")
                else:
                    confidence = labels["confidence"]
            else:
                scenario_errors.append("`confidence` key not found in labels")

            if "cti" in labels:
                if not labels["cti"]:
                    in_cti = False

            if scenario_label == "":
                desc = scenario["description"].lower()
                if desc.startswith("detect "):
                    desc = desc.replace("detect ", "")
                desc_words = desc.split(" ")
                tmp: list[str] = []
                for w in desc_words:
                    if len(w) <= 3:
                        w = w.upper()
                    else:
                        w = w.capitalize()
                    if "cve" in w:
                        w = w.replace("cve", "CVE")
                    tmp.append(w)
                scenario_label = " ".join(tmp)

            if scenario_label == "":
                scenario_errors.append("`label` key not found in labels")

            behaviors = []
            if behavior not in behavior_data:
                scenario_errors.append(f"Unknown behaviors: {behavior}")
            else:
                behaviors.append(behavior)

            if behavior not in stats["behaviors"]:
                stats["behaviors"].append(behavior)
            # strip the ./ that is generated by walk but not present in the changed_files from github
            if len(scenario_errors) > 0 and filepath[2:] in changed_files:
                errors[scenario["name"]] = scenario_errors
                stats["scenarios_nok"].append(scenario["name"])
            else:
                stats["scenarios_ok"].append(scenario["name"])

            scenarios_taxonomy[scenario["name"]] = {
                "name": scenario["name"],
                "description": scenario["description"],
                "label": scenario_label,
                "behaviors": behaviors,
                "mitre_attacks": mitre_techniques,
                "confidence": confidence,
                "spoofable": spoofable,
                "cti": in_cti,
                "service": service,
                "created_at": creation_dates[filepath],
            }

            if len(cves) > 0:
                scenarios_taxonomy[scenario["name"]]["cves"] = cves
            if len(cwes) > 0:
                scenarios_taxonomy[scenario["name"]]["cwes"] = cwes

    with Path(args.output).open("w") as f:
        json.dump(scenarios_taxonomy, f, indent=2)

    if len(errors) > 0:
        with Path(args.errors).open("w") as f:
            f.write(INTRO_STR)
            for scenario, errorlist in errors.items():
                f.write(f"**{scenario}**:\n")
                for error in errorlist:
                    f.write(f"  - {error}\n")
                f.write("\n")
            f.write(HELP_STR)
    else:
        with Path(args.errors).open("w") as f:
            f.write(OK_STR)

    print("Supported Mitre ATT&CK Techniques:")
    for technique in stats["mitre"]:
        print(f"\t{technique}")

    total_scenario = len(stats["scenarios_ok"]) + len(stats["scenarios_nok"])
    print("\nStats:")
    print("\tScenarios OK  : {}/{}".format(len(stats["scenarios_ok"]), total_scenario))
    print("\tScenarios NOK : {}/{}".format(len(stats["scenarios_nok"]), total_scenario))
    print("\tMitre Att&ck  : {}".format(len(stats["mitre"])))
    print("\tBehaviors     : {}".format(len(stats["behaviors"])))

    # write the report about the supported techniques only if the path is specified
    if args.report != "":
        csv_headers = [
            "Tactic ID",
            "Tactic Name",
            "Technique",
            "Technique Name",
        ]

        rows: list[list[str]] = []
        for tactic, tactic_info in mitres.items():
            ta_info = lookup_tactic(tactic, mitre_data)
            if len(ta_info) == 0:
                print(f"Tactic {tactic} not found, skipping")
                continue
            for technique in tactic_info:
                tec_info = lookup_technique(technique, mitre_data)
                rows.append([tactic, ta_info["name"], technique, tec_info["label"]])

        with Path(args.report).open("w", encoding="UTF-8") as f:
            writer = csv.writer(f)
            writer.writerow(csv_headers)
            writer.writerows(rows)


def lookup_tactic(tactic_id, mitre_db):
    return mitre_db.get(tactic_id, {})


def lookup_technique(technique_id, mitre_db):
    for tactic_info in mitre_db.values():
        for technique in tactic_info["techniques"]:
            if technique_id == technique["name"]:
                return technique
    return None


class Parser(Tap):
    hub: str
    output: str
    report: str
    errors: str
    behaviors: str
    mitre: str
    ignore: str
    verbose: bool

    @override
    def configure(self) -> None:
        self.add_argument("--hub", help="Hub folder path", default="")
        self.add_argument(
            "-o", "--output", help="Output file path", default="./scenarios.json"
        )
        self.add_argument("-r", "--report", help="Report file path", default="")
        self.add_argument(
            "-e",
            "--errors",
            help="Output errors file path",
            default="./scenario_taxonomy_errors.md",
        )
        self.add_argument(
            "-b",
            "--behaviors",
            help="behaviors.json filepath",
            default="./behaviors.json",
        )
        self.add_argument(
            "-m",
            "--mitre",
            help="mitre_attack.json filepath",
            default="./mitre_attack.json",
        )

        self.add_argument(
            "-i",
            "--ignore",
            help="File where ignored scenarios are specified",
            default=f"{Path(os.path.realpath(__file__)).parent}/.scenariosignore",
        )

        self.add_argument(
            "-v", "--verbose", action="store_true", help="Verbose mode", default=False
        )
