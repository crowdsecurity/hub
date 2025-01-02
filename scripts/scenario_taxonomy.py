import os
import re
import sys
import csv
import json
import yaml
import argparse
from yaml.loader import SafeLoader
from itertools import chain


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

    return "{service}:{attack_type}".format(service=service, attack_type=attack_type)


def get_mitre_tactic_from_technique(technique, mitre_data):
    for tactic, tactic_info in mitre_data.items():
        for tech in tactic_info["techniques"]:
            if technique == tech["name"]:
                return tactic
    return None


def get_mitre_techniques_from_label(labels, mitre_data):
    ret = list()
    errors = list()
    if "classification" not in labels or not labels["classification"]:
        return ret, errors

    for classification in labels["classification"]:
        split_attack = classification.split(".")
        if split_attack[0] != "attack":
            continue
        if len(split_attack) < 2:
            errors.append("bad mitre format: {}".format(classification))
            continue
        technique = split_attack[1]
        tactic = get_mitre_tactic_from_technique(technique, mitre_data)
        if tactic is None:
            errors.append("unknown mitre technique: {}".format(technique))
            continue
        ret.append("{}:{}".format(tactic, technique))

    return ret, errors


def get_cwe_from_label(labels):
    ret = list()
    errors = list()
    if "classification" not in labels or not labels["classification"]:
        return ret, errors

    for classification in labels["classification"]:
        split_cwe = classification.split(".")
        if split_cwe[0] != "cwe":
            continue
        cwe = split_cwe[1].upper()

        if CWE_RE.match(cwe) == None:
            errors.append("bad CWE format: {}".format(cwe))
            continue
        ret.append(cwe)

    return ret, errors


def get_cve_from_label(labels):
    ret = list()
    errors = list()
    if "classification" not in labels or not labels["classification"]:
        return ret, errors

    for classification in labels["classification"]:
        split_cve = classification.split(".")
        if split_cve[0] != "cve":
            continue
        cve = split_cve[1].upper()

        if CVE_RE.match(cve) == None:
            errors.append("bad CVE format: {}".format(cve))
            continue
        ret.append(cve)

    return ret, errors


def main():
    args = parse_args()
    if args.hub == "":
        print("[-] Please provide the hub path with the --hub argument")
        sys.exit(1)

    changed_files = os.environ.get("changed_files", "").split(",")
    if changed_files == [""]:
        changed_files = []
        print("[-] No changed files found, run on all files.")
    else:
        print("[+] Changed files: {}".format(changed_files))
    mitre_data = json.load(open(args.mitre, "r"))
    behavior_data = json.load(open(args.behaviors, "r"))

    stats = {"scenarios_ok": [], "scenarios_nok": [], "mitre": [], "behaviors": []}
    hub_scenarios_path = os.path.join(args.hub, "scenarios")
    hub_appsecrules_path = os.path.join(args.hub, "appsec-rules")
    ignore_list = list()
    if os.path.exists(args.ignore):
        ignore_list = open(args.ignore).read().split("\n")

    errors = dict()
    scenarios_taxonomy = dict()
    filepath_list = []

    for r, d, f in chain.from_iterable(
        os.walk(path) for path in [hub_scenarios_path, hub_appsecrules_path]
    ):
        for file in f:
            if file.endswith(".yaml") or file.endswith(".yml"):
                filepath_list.append(os.path.join(r, file))

    filepath_list.sort()
    cpt = 0
    mitres = dict()
    for filepath in filepath_list:
        print("[+] Processing {}".format(filepath))
        f = open(filepath, "r")
        data = list(yaml.load_all(f, Loader=SafeLoader))

        for scenario in data:
            if scenario["name"] in ignore_list:
                continue

            cpt += 1
            scenario_errors = list()
            if "labels" not in scenario:
                scenario_errors.append("`labels` not found")
                errors[scenario["name"]] = scenario_errors
                stats["scenarios_nok"].append(scenario["name"])
                continue

            labels = scenario["labels"]
            behavior = get_behavior_from_label(labels)
            mitre_techniques, mitre_errors = get_mitre_techniques_from_label(
                labels, mitre_data
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
                    mitres[ta] = dict()

                if te not in mitres[ta]:
                    mitres[ta][te] = dict()

                if "scenarios" not in mitres[ta][te]:
                    mitres[ta][te]["scenarios"] = list()

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
                tmp = list()
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

            behaviors = list()
            if behavior not in behavior_data:
                scenario_errors.append("Unknown behaviors: {}".format(behavior))
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
            }

            if len(cves) > 0:
                scenarios_taxonomy[scenario["name"]]["cves"] = cves
            if len(cwes) > 0:
                scenarios_taxonomy[scenario["name"]]["cwes"] = cwes

    f = open(args.output, "w")
    f.write(json.dumps(scenarios_taxonomy, indent=2))
    f.close()

    if len(errors) > 0:
        f = open(args.errors, "w")
        f.write(INTRO_STR)
        for scenario, errors in errors.items():
            f.write("**{}**:\n".format(scenario))
            for error in errors:
                f.write("  - {}\n".format(error))
            f.write("\n")
        f.write(HELP_STR)
        f.close()
    else:
        f = open(args.errors, "w")
        f.write(OK_STR)
        f.close()

    print("Supported Mitre ATT&CK Techniques:")
    for technique in stats["mitre"]:
        print("\t{}".format(technique))

    total_scenario = len(stats["scenarios_ok"]) + len(stats["scenarios_nok"])
    print("\nStats:")
    print("\tScenarios OK  : {}/{}".format(len(stats["scenarios_ok"]), total_scenario))
    print("\tScenarios NOK : {}/{}".format(len(stats["scenarios_nok"]), total_scenario))
    print("\tMitre Att&ck  : {}".format(len(stats["mitre"])))
    print("\tBehaviors     : {}".format(len(stats["behaviors"])))

    # write the report about the supported techniques only if the path is specified
    if args.report != "":
        CSV_HEADERS = [
            "Tactic ID",
            "Tactic Name",
            "Technique",
            "Technique Name",
        ]

        rows = list()
        for tactic, tactic_info in mitres.items():
            ta_info = lookup_tactic(tactic, mitre_data)
            if len(ta_info) == 0:
                print("Tactic {} not found, skipping".format(tactic))
                continue
            for technique, technique_info in tactic_info.items():
                tec_info = lookup_technique(technique, mitre_data)
                rows.append([tactic, ta_info["name"], technique, tec_info["label"]])

        with open(args.report, "w", encoding="UTF-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
            writer.writerows(rows)


def lookup_tactic(tactic_id, mitre_db):
    return mitre_db.get(tactic_id, {})


def lookup_technique(technique_id, mitre_db):
    for tactic, tactic_info in mitre_db.items():
        for technique in tactic_info["techniques"]:
            if technique_id == technique["name"]:
                return technique


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate CrowdSec Scenarios taxonomy file"
    )

    parser.add_argument("--hub", type=str, help="Hub folder path", default="")
    parser.add_argument(
        "-o", "--output", type=str, help="Output file path", default="./scenarios.json"
    )
    parser.add_argument("-r", "--report", type=str, help="Report file path", default="")
    parser.add_argument(
        "-e",
        "--errors",
        type=str,
        help="Output errors file path",
        default="./scenario_taxonomy_errors.md",
    )
    parser.add_argument(
        "-b",
        "--behaviors",
        type=str,
        help="behaviors.json filepath",
        default="./behaviors.json",
    )
    parser.add_argument(
        "-m",
        "--mitre",
        type=str,
        help="mitre_attack.json filepath",
        default="./mitre_attack.json",
    )

    parser.add_argument(
        "-i",
        "--ignore",
        type=str,
        help="File where ignored scenarios are specified",
        default="{}/.scenariosignore".format(
            os.path.dirname(os.path.realpath(__file__))
        ),
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Verbose mode", default=False
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
