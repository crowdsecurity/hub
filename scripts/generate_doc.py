import os
import json
import argparse

from mdutils.mdutils import MdUtils

BEHAVIORS_DOC_FILE = "behaviors.md"
SCENARIOS_DOC_FILE = "scenarios.md"


def generate_behaviors_doc(filepath, data):
    md = MdUtils(file_name=filepath, title="Behaviors Taxonomy")
    rows = ["Name", "Label", "Description"]
    nb_headers = len(rows)

    data_keys = list(data.keys())
    data_keys.sorted()
    for key in data_keys:
        info = data[key]
        rows.extend([info["name"], info["label"], info["description"]])

    md.new_line()
    md.new_table(columns=nb_headers, rows=len(data)+1, text=rows, text_align='center')

    md.create_md_file()


def generate_scenarios_doc(filepath, data):
    md = MdUtils(file_name=filepath, title="Scenarios Taxonomy")
    rows = ["Name", "Label", "Description", "Behaviors", "Mitre ATT&CK", "CVES", "Spoofable", "Confidence"]
    nb_headers = len(rows)

    data_keys = list(data.keys())
    data_keys.sorted()
    for key in data_keys:
        info = data[key]
        rows.extend([
            info["name"],
            info["label"],
            info["description"],
            "<br />".join(info["behaviors"]),
            "<br />".join(info["mitre_attacks"]),
            "<br />".join(info["cves"]) if "cves" in info else "",
            info["spoofable"],
            info["confidence"],
        ])

    md.new_line()
    md.new_table(columns=nb_headers, rows=len(data)+1, text=rows, text_align='center')

    md.create_md_file()



def main():
    args = parse_args()
    mitre_data = json.load(open(args.mitre, "r"))
    behavior_data = json.load(open(args.behaviors, "r"))
    scenario_data = json.load(open(args.scenarios, "r"))
    
    behaviors_doc_filepath = os.path.join(args.output, BEHAVIORS_DOC_FILE)
    scenarios_doc_filepath = os.path.join(args.output, SCENARIOS_DOC_FILE)

    generate_behaviors_doc(behaviors_doc_filepath, behavior_data)
    generate_scenarios_doc(scenarios_doc_filepath, scenario_data)


def parse_args():
    parser = argparse.ArgumentParser(description='Generate CrowdSec Scenarios taxonomy file')

    parser.add_argument('--hub', type=str, help="Hub folder path", default="")
    parser.add_argument('-o', '--output', type=str, help="Output folder", default="./")
    parser.add_argument('-b', '--behaviors', type=str, help="behaviors.json filepath", default="./behaviors.json")
    parser.add_argument('-m', '--mitre', type=str, help="mitre_attack.json filepath", default="./mitre_attack.json")
    parser.add_argument('-s', '--scenarios', type=str, help="scenario.json filepath", default="./scenarios.json")
    parser.add_argument('-v', '--verbose', action="store_true", help="Verbose mode", default=False)
    return parser.parse_args()




if __name__ == "__main__":
    main()