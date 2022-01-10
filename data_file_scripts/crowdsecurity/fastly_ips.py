#!/usr/bin/env python3

import sys
import json
from itertools import chain

with open(sys.argv[1], "r+") as f:
    data = json.load(f)
    addresses = sorted(
        [address + "\n" for address in chain(data["addresses"], data["ipv6_addresses"])]
    )
    f.seek(0)
    f.truncate()
    f.writelines(addresses)

