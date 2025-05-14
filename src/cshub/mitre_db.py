import argparse
import json
from pathlib import Path
from typing import override

import requests
from tap import Tap

TACTIC_TYPE = "x-mitre-tactic"
TECHNIQUES_TYPE = "attack-pattern"
IS_SUBTECHNIQUE_KEY = "x_mitre_is_subtechnique"

MAP_TACTICS_ID_NAME = {}


def get_tactics(data):
    ret = {}

    for obj in data["objects"]:
        if "type" not in obj:
            continue

        typ = obj["type"]
        if typ == TACTIC_TYPE:
            tactic_id = obj["external_references"][0]["external_id"]
            ret[tactic_id] = {
                "id": tactic_id,
                "name": obj["name"],
                "description": obj["description"],
                "references": [obj["external_references"][0]["url"]],
                "techniques": [],
            }

            # we do this to attribute techniques to tactics later
            short_name = obj["x_mitre_shortname"]
            MAP_TACTICS_ID_NAME[short_name] = tactic_id

    return ret


def get_techniques(data, tactics):
    for obj in data["objects"]:
        if "type" not in obj:
            continue

        typ = obj["type"]
        if typ != TECHNIQUES_TYPE:
            continue

        if obj[IS_SUBTECHNIQUE_KEY]:
            continue

        if "revoked" in obj and obj["revoked"] is True:
            continue

        if "x_mitre_deprecated" in obj and obj["x_mitre_deprecated"] is True:
            continue

        technique = {
            "name": obj["external_references"][0]["external_id"],
            # "references" : [obj["external_references"][0]["url"]],
            "label": obj["name"],
            "description": obj["description"],
        }

        for kc_phases in obj["kill_chain_phases"]:
            phase_name = kc_phases["phase_name"]
            if phase_name not in MAP_TACTICS_ID_NAME:
                print(f"Unknown phase name: {phase_name}")
                continue

            tactic_id = MAP_TACTICS_ID_NAME[phase_name]

            tactics[tactic_id]["techniques"].append(technique)

    return tactics


def download_data(url: str):
    r = requests.get(url)
    return r.json()


def main():
    parser = Parser(
        description="Generate mitre attacks tactics and techniques file", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    args = parser.parse_args()

    data = download_data(args.url)

    # we need to get tactics before techniques, and I'm not sure about how the enterprise-attack.json file is sorted
    # thats why we iterate the file two times
    tactics = get_tactics(data)
    tactics = get_techniques(data, tactics)

    with Path(args.output).open("w") as f:
        json.dump(tactics, f, indent=2)

    nb_tactics = len(tactics.keys())
    print(f"[*] Found {nb_tactics} tactics")
    for tactic_id, tactic_info in tactics.items():
        print("  - {}: {}".format(tactic_id, tactic_info["name"]))
        if args.verbose:
            for technique in tactic_info["techniques"]:
                print("    - {}  : {}".format(technique["id"], technique["name"]))


class Parser(Tap):
    url: str
    output: str
    verbose: bool

    @override
    def configure(self) -> None:
        self.add_argument(
            "-u",
            "--url",
            help="URL of the Mitre Attack database file",
            default="https://github.com/mitre/cti/raw/master/enterprise-attack/enterprise-attack.json",
        )
        self.add_argument("-o", "--output", help="Output file path", default="./mitre_attack.json")
        self.add_argument("-v", "--verbose", action="store_true", help="Verbose mode", default=False)
