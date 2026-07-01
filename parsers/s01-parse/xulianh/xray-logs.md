---
author: xulianh
classification:
  - AppSec
  - Proxy
tags:
  - xray
  - brute-force
---

# X-ray Log Parser

## Description
This parser is designed to extract relevant security events from X-ray proxy service logs. It specifically targets connection logs to identify connection states and source IP addresses.

## Acquisition Configuration
To allow this parser to process the logs, add the following configuration to your `/etc/crowdsec/acquis.d/xray.yaml` file:

filenames:
  - /var/log/xray/access.log
labels:
  type: xray

## Extraction Logic

The component utilizes Grok patterns to process the `message` field of incoming logs matching the `xray` program identifier.

* **Target Variables:**
  * `evt.Parsed.action`: Captures the connection outcome (e.g., `rejected`).
  * `evt.Parsed.source_ip`: Isolates the originating IPv4/IPv6 address.

### Architecture Flow

    [Raw X-ray Log] --> [xulianh/xray-logs Parser] --> [Extracted Meta-fields]
                                                              |
                                                              v
                                                 [Available for Scenarios]

## Validation and Testing
To validate the extraction logic against a local log file, utilize the CrowdSec CLI explain command:

cscli explain --parser ./parsers/s01-parse/xulianh/xray-logs.yaml --log ./tests/xray_sample.log

Ensure that the output explicitly shows the `action` and `source_ip` fields populated correctly.
