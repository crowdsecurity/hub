import os
import sys
import json
import yaml
import argparse
from yaml.loader import SafeLoader


FILES_LIST = [
    "apache_log4j2_cve-2021-44228.yaml",
    "auditd-postexploit-exec-from-net.yaml",
    "ssh-bf.yaml",
    "windows-CVE-2022-30190-msdt.yaml"
]


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
            if technique == tech["id"]:
                return tactic
    return None


def get_mitre_attacks_from_label(labels, mitre_data):
    ret = list()
    errors = list()
    if "classification" not in labels:
        return ret, errors

    for attack in labels["classification"]:
        split_attack = attack.split(".")
        technique = split_attack[1]
        tactic = get_mitre_tactic_from_technique(technique, mitre_data)
        if tactic is None:
            errors.append("unknown mitre technique: {}".format(technique))
            continue
        ret.append("{}:{}".format(tactic, technique))

    return ret, errors

def main():
    args = parse_args()
    if args.hub == "":
        print("[-] Please provide the hub path with the --hub argument")
        sys.exit(1)

    mitre_data = json.load(open(args.mitre, "r"))
    behavior_data = json.load(open(args.behaviors, "r"))

    hub_scenarios_path = os.path.join(args.hub, "scenarios")
    errors = dict()
    scenarios_taxonomy = dict()
    filepath_list = []
    for r, d, f in os.walk(hub_scenarios_path):
        for file in f:
            if file in FILES_LIST:
                filepath_list.append(os.path.join(r, file))

    for filepath in filepath_list:
        f = open(filepath, "r")
        data = list(yaml.load_all(f, Loader=SafeLoader))
        for scenario in data:
            scenario_errors = list()
            labels = scenario["labels"]
            behaviors = get_behavior_from_label(labels)        
            mitre_attacks, mitre_errors = get_mitre_attacks_from_label(labels, mitre_data)
            scenario_errors.extend(mitre_errors)
            if behaviors == "":
                scenario_errors.append("`behaviors` key not found in labels")

            if len(mitre_attacks) == 0:
                scenario_errors.append("`mitre_attack` key not found in labels")

            scenario_label = ""
            confidence = ""
            spoofable = ""
            if "labels" in scenario:
                labels = scenario["labels"]
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

            if behaviors not in behavior_data:
                scenario_errors.append("Unknown behaviors: {}".format(behaviors))

            if len(scenario_errors) > 0:
                errors[scenario["name"]] = scenario_errors

            scenarios_taxonomy[scenario["name"]] = {
                "name" : scenario["name"],
                "description" : scenario["description"],
                "label": scenario_label,
                "behaviors": [behaviors],
                "mitre_attacks": mitre_attacks,
                "confidence": confidence,
                "spoofable" : spoofable
            }
    

    f = open(args.output, "w")
    f.write(json.dumps(scenarios_taxonomy, indent=2))
    f.close()

    if len(errors) > 0:
        f = open(args.errors, "w")
        for scenario, errors in errors.items():
            f.write("**{}**:\n".format(scenario))
            for error in errors:
                f.write("  - {}\n".format(error))
        f.close()


def parse_args():
    parser = argparse.ArgumentParser(description='Generate CrowdSec Scenarios taxonomy file')

    parser.add_argument('--hub', type=str, help="Hub folder path", default="")
    parser.add_argument('-o', '--output', type=str, help="Output file path", default="./scenarios.json")
    parser.add_argument('-e', '--errors', type=str, help="Output errors file path", default="./scenario_taxonomy_errors.md")
    parser.add_argument('-b', '--behaviors', type=str, help="behaviors.json filepath", default="./behaviors.json")
    parser.add_argument('-m', '--mitre', type=str, help="mitre_attack.json filepath", default="./mitre_attack.json")
    parser.add_argument('-v', '--verbose', action="store_true", help="Verbose mode", default=False)
    return parser.parse_args()




if __name__ == "__main__":
    main()