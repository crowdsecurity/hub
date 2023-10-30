import json
import requests
import argparse


TACTIC_TYPE = "x-mitre-tactic"
TECHNIQUES_TYPE = "attack-pattern"
IS_SUBTECHNIQUE_KEY = "x_mitre_is_subtechnique"

MAP_TACTICS_ID_NAME = dict()


def get_tactics(data):
    ret = dict()

    for obj in data["objects"]:
        if "type" not in obj:
            continue

        type = obj["type"]
        if type == TACTIC_TYPE:
            tactic_id = obj["external_references"][0]["external_id"]
            ret[tactic_id] = {
                "id" : tactic_id,
                "name" : obj["name"],
                "description" : obj["description"],
                "references" : [obj["external_references"][0]["url"]],
                "techniques" : []
            }

            # we do this to attribute techniques to tactics later
            short_name = obj["x_mitre_shortname"]
            MAP_TACTICS_ID_NAME[short_name] = tactic_id

    return ret

def get_techniques(data, tactics):
    for obj in data["objects"]:
        if "type" not in obj:
            continue

        type = obj["type"]
        if type != TECHNIQUES_TYPE:
            continue
        
        if obj[IS_SUBTECHNIQUE_KEY]:
            continue

        if "revoked" in obj and obj["revoked"] is True:
            continue
    
        if "x_mitre_deprecated" in obj and obj["x_mitre_deprecated"] is True:
            continue

        technique = {
            "name" : obj["external_references"][0]["external_id"],
            #"references" : [obj["external_references"][0]["url"]],
            "label" : obj["name"],
            "description" : obj["description"]
        }

        for kc_phases in obj["kill_chain_phases"]:
            phase_name = kc_phases["phase_name"]
            if phase_name not in MAP_TACTICS_ID_NAME:
                print("Unknown phase name: {}".format(phase_name))
                continue
            
            tactic_id = MAP_TACTICS_ID_NAME[phase_name]

            tactics[tactic_id]["techniques"].append(technique)

    return tactics


def download_data(url):
    r = requests.get(url)
    return r.json()


def main():
    args = parse_args()
    data = download_data(args.url)

    # we need to get tactics before techniques, and I'm not sure about how the enterprise-attack.json file is sorted
    # thats why we iterate the file two times
    tactics = get_tactics(data)
    tactics = get_techniques(data, tactics)


    f = open(args.output, "w")
    f.write(json.dumps(tactics, indent=2))
    f.close()

    nb_tactics = len(tactics.keys())
    print("[*] Found {} tactics".format(nb_tactics))
    for tactic_id, tactic_info in tactics.items():
        print("  - {}: {}".format(tactic_id, tactic_info["name"]))
        if args.verbose:
            for technique in tactic_info["techniques"]:
                print("    - {}  : {}".format(technique["id"], technique["name"]))


def parse_args():
    parser = argparse.ArgumentParser(description='Generate mitre attacks tactics and techniques file')

    parser.add_argument('-u', '--url', type=str, help="URL of the Mitre Attack database file", default="https://github.com/mitre/cti/raw/master/enterprise-attack/enterprise-attack.json")
    parser.add_argument('-o', '--output', type=str, help="Output file path", default="./mitre_attack.json")
    parser.add_argument('-v', '--verbose', action="store_true", help="Verbose mode", default=False)
    return parser.parse_args()


if __name__ == "__main__":
    main()