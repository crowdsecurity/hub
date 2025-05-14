import argparse
import os
import sys
from pathlib import Path
from typing import override

import yaml
from tap import Tap
from yaml.loader import SafeLoader

VPATCH_COLLECTION_FILEPATH = "./collections/crowdsecurity/appsec-virtual-patching.yaml"
VPATCH_COLLECTION_NAME = "crowdsecurity/appsec-virtual-patching"
WORKFLOW_FILEPATH = ".github/workflows/appsec_vpatch_lint.yaml"
SCRIPT_FILEPATH = "scripts/appsec_vpatch_lint.py"
author = os.environ.get("AUTHOR", "ghost")

INTRO_STR = f"""
Hello @{author} and thank you for your contribution!

:heavy_exclamation_mark: It seems that the following scenarios are not part of the '{VPATCH_COLLECTION_NAME}' collection:

"""

OK_STR = f"""
Hello @{author},

:white_check_mark: The new VPATCH Rule is compliant, thank you for your contribution!
"""


def file_in_pathlist(filename: str, path_list: list[str]) -> bool:
    return any(filename in path for path in path_list)


class Parser(Tap):
    hub: str
    errors: str

    @override
    def configure(self) -> None:
        self.add_argument("--hub", help="Hub folder path", default=".")

        self.add_argument(
            "-e",
            "--errors",
            help="Output errors file path",
            default="./appsec_vpatch_cve_error.md",
        )

        self.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            help="Verbose mode",
            default=False,
        )


def main() -> None:
    parser = Parser(
        description="Generate CrowdSec Scenarios taxonomy file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    args = parser.parse_args()

    if args.hub == "":
        print("[-] Please provide the hub path with the --hub argument")
        sys.exit(1)

    changed_files = os.environ.get("changed_files", "").split(",")
    if (
        changed_files == [""]
        or WORKFLOW_FILEPATH in changed_files  # if the workflow file has been modified, we want to run the script on all rules
        or SCRIPT_FILEPATH in changed_files  # if the script has been modified, we want to run it on all rules
    ):
        changed_files = []
        print("[-] No changed files found, run on all files.")
    else:
        print(f"[+] Changed files: {changed_files}")

    with Path(VPATCH_COLLECTION_FILEPATH).open() as f:
        vpatch_collection = yaml.load(f, Loader=SafeLoader)

    vpatch_collection_rules = vpatch_collection["appsec-rules"]
    missing_rules: list[str] = []

    hub_appsecrules_path = os.path.join(args.hub, "appsec-rules")
    for r, d, f in os.walk(hub_appsecrules_path):
        for file in f:
            if file.endswith((".yaml", ".yml")):
                if len(changed_files) == 0 or (len(changed_files) > 0 and file_in_pathlist(file, changed_files)):
                    if not file.startswith("vpatch-"):
                        continue

                    with Path(os.path.join(r, file)).open() as f:
                        data = list(yaml.load_all(f, Loader=SafeLoader))

                    print(f"[*] Processing rule '{file}'")
                    for rule in data:
                        if rule["name"] not in vpatch_collection_rules:
                            missing_rules.append(rule["name"])

    with Path(args.errors).open("w") as f:
        if len(missing_rules) > 0:
            _ = f.write(INTRO_STR)
            for rule in missing_rules:
                _ = f.write(f":red_circle: **{rule}** :red_circle:\n")
        else:
            _ = f.write(OK_STR)


