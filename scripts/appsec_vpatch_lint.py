import os
import yaml
import argparse
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


def file_in_pathlist(filename, path_list):
    for path in path_list:
        if filename in path:
            return True
    return False


def main():
    args = parse_args()
    if args.hub == "":
        print("[-] Please provide the hub path with the --hub argument")
        sys.exit(1)

    changed_files = os.environ.get("changed_files", "").split(",")
    if (
        changed_files == [""]
        or WORKFLOW_FILEPATH
        in changed_files  # if the workflow file has been modified, we want to run the script on all rules
        or SCRIPT_FILEPATH
        in changed_files  # if the script has been modified, we want to run it on all rules
    ):
        changed_files = []
        print("[-] No changed files found, run on all files.")
    else:
        print("[+] Changed files: {}".format(changed_files))

    vpatch_collection = yaml.load(
        open(VPATCH_COLLECTION_FILEPATH, "r"), Loader=SafeLoader
    )
    vpatch_collection_rules = vpatch_collection["appsec-rules"]
    missing_rules = list()

    hub_appsecrules_path = os.path.join(args.hub, "appsec-rules")
    for r, d, f in os.walk(hub_appsecrules_path):
        for file in f:
            if file.endswith(".yaml") or file.endswith(".yml"):
                if len(changed_files) == 0 or (
                    len(changed_files) > 0 and file_in_pathlist(file, changed_files)
                ):
                    if not file.startswith("vpatch-"):
                        continue
                    f = open(os.path.join(r, file), "r")
                    data = list(yaml.load_all(f, Loader=SafeLoader))
                    print("[*] Processing rule '{}'".format(file))
                    for rule in data:
                        if rule["name"] not in vpatch_collection_rules:
                            missing_rules.append(rule["name"])

    f = open(args.errors, "w")
    if len(missing_rules) > 0:
        f.write(INTRO_STR)
        for rule in missing_rules:
            f.write(":red_circle: **{}** :red_circle:\n".format(rule))
    else:
        f.write(OK_STR)

    f.close()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate CrowdSec Scenarios taxonomy file"
    )
    parser.add_argument("--hub", type=str, help="Hub folder path", default=".")
    parser.add_argument(
        "-e",
        "--errors",
        type=str,
        help="Output errors file path",
        default="./appsec_vpatch_cve_error.md",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Verbose mode", default=False
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
