
Hello @buixor and thank you for your contribution!

I'm a bot that helps maintainers to validate scenarios and ensure they include all the required information.
I've found some errors in your scenarios, please fix them and re-submit your PR, or ask for help if you need it.

The following scenarios have errors:
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



## Mitre ATT&CK

Information about mitre attack can be found [here](https://attack.mitre.org/techniques/enterprise/).
As an example, some common mitre attack techniques:
 - T1110 for bruteforce attacks
 - T1595 and T1190 for exploitation of public vulnerabilities
 - T1595 for generic scanning of exposed applications

Expected format is (where XXXX is the technique ID):

```yaml
labels:
  classification:
    - attack.TXXXX
```
 
## CVEs

If your scenario covers a specific CVE (Common Vulnerabilities and Exposures), please add it.

Expected format is (where CVE-XXX-XXX is the CVE ID):

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
