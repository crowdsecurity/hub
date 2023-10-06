**crowdsecurity/CVE-2023-4911**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: :

**crowdsecurity/auditd-suid-crash**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: linux:exploitation

**xs539/bookstack-bf**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: bookstack:bruteforce

**xs539/bookstack-bf_user-enum**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: bookstack:bruteforce

**xs539/joplin-server-bf**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: joplin:bruteforce

**xs539/joplin-server-bf_user-enum**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: joplin:bruteforce


Information about mitre attack can be found [here](https://attack.mitre.org/techniques/enterprise/).
As an example, some common mitre attack techniques:
 - T1110 for bruteforce attacks
 - T1595 and T1190 for exploitation of public vulnerabilities
 - T1595 for generic scanning of exposed applications

[Here](https://docs.crowdsec.net/docs/next/scenarios/format#labels) is the CrowdSec documentation on how to fill those labels
[Here](https://github.com/crowdsecurity/hub/blob/master/taxonomy/behaviors.json) are the available behaviors
