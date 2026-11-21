---

author: xulianh
classification:

* AppSec
* Proxy
tags:
* xray
* brute-force

---

# 🛡️ X-ray Log Parser

## 📝 Description

This parser is designed to extract relevant security events from X-ray proxy service logs. It targets incoming log strings to identify connection outcomes and safely isolate structural metadata such as source IP addresses and destination ports.

## ⚙️ Acquisition Configuration

To allow this parser to ingest logs in a production environment, the following configuration must be provisioned in the acquisition file (e.g., `/etc/crowdsec/acquis.d/xray.yaml`):

filenames:

* /var/log/xray/access.log
labels:
type: xray

## 🔍 Extraction Logic

The component utilizes optimized Grok patterns to process the `message` field of raw incoming lines matching the `xray` program identifier.

* **Target Variables:**
* `evt.Parsed.action`: Captures the connection state outcome (e.g., `rejected`, `accepted`).
* `evt.Parsed.source_ip`: Isolates the originating IPv4 or IPv6 address.
* `evt.Parsed.source_port`: Extracts the source ephemeral port for granular logging.


* **Chronological Synchronization:**
* The parser formats and concatenates raw time components (`year`, `month`, `day`, `hour`, `minute`, `second`) into the `evt.StrTime` variable. This allows the downstream `crowdsecurity/dateparse-enrich` component to shift the event clock from the current system time to the actual historical log timestamp, unlocking flawless forensic and time-machine execution.



### 📊 Architecture Flow

[Raw X-ray Log] --> [s00-raw (non-syslog Ingestion)] --> [s01-parse (xulianh/xray-logs)]
│
▼
[Available for Scenarios] <── [s02-enrich (dateparse-enrich)] <── [Extracted Fields & StrTime]

## 🧪 Validation and Testing

To validate the extraction logic within an isolated development environment without risking production services, utilize the integrated `hubtest` framework rather than global binary commands.

Run the ordinary simulation test using:

cscli hubtest run xray-brute-force

To inspect the synchronized step-by-step state transitions, Grok pattern matches, and variable updates (the strict equivalent to `cscli explain`), execute the detailed interactive diagnostic:

cscli hubtest explain xray-brute-force --verbose

### 🔒 Verification and Best Practices

A successful validation is achieved when all lines are labeled with a green success indicator (`🟢`), and the computed variables match the frozen signatures inside the local `parser.assert` file.

Security Requirements for Test Vectors:
When populating or updating the testing vector file `xray_sample.log` under `.tests/xray-brute-force/`, it is strictly forbidden to include real, un-anonymized operational production IP addresses. All network data must undergo an obfuscation process.

It is mandatory to use standard documentation IP networks defined by RFC 5737 (such as `192.0.2.0/24` or `198.51.100.0/24`). This prevents the leakage of private server topology to public community repositories and ensures consistent, portable integration testing across continuous integration (CI) environments.
