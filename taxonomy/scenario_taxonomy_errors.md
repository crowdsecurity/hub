**andreasbrett/baikal-bf**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: baikal:bruteforce

**andreasbrett/baikal-bf_user-enum**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: baikal:bruteforce

**andreasbrett/paperless-ngx-bf**:
  - Unknown behaviors: paperless-ngx:bruteforce

**andreasbrett/paperless-ngx-bf_user-enum**:
  - Unknown behaviors: paperless-ngx:bruteforce

**andreasbrett/webmin-bf**:
  - Unknown behaviors: webmin:bruteforce

**andreasbrett/webmin-bf_user-enum**:
  - Unknown behaviors: webmin:bruteforce

**crowdsecurity/exim-spam**:
  - `attack` not found in labels.classification

**crowdsecurity/palo-alto-threat**:
  - `attack` not found in labels.classification
  - `spoofable` key not found in labels
  - `confidence` key not found in labels
  - Unknown behaviors: :

**crowdsecurity/postfix-spam**:
  - `attack` not found in labels.classification

**crowdsecurity/postscreen-rbl**:
  - `attack` not found in labels.classification

**crowdsecurity/wireguard-auth**:
  - Unknown behaviors: wireguard:bruteforce

**gauth-fr/immich-bf**:
  - Unknown behaviors: immich:bruteforce

**gauth-fr/immich-bf_user-enum**:
  - Unknown behaviors: immich:bruteforce

**inherent-io/keycloak-bf**:
  - Unknown behaviors: keycloak:bruteforce

**inherent-io/keycloak-user-enum-bf**:
  - Unknown behaviors: keycloak:bruteforce

**inherent-io/keycloak-slow-bf**:
  - Unknown behaviors: keycloak:bruteforce

**inherent-io/keycloak-user-enum-slow-bf**:
  - Unknown behaviors: keycloak:bruteforce


Information about mitre attack can be found [here](https://attack.mitre.org/techniques/enterprise/).
As an example, some common mitre attack techniques:
 - T1110 for bruteforce attacks
 - T1595 and T1190 for exploitation of public vulnerabilities
 - T1595 for generic scanning of exposed applications

[Here](https://docs.crowdsec.net/docs/next/scenarios/format#labels) is the CrowdSec documentation on how to fill those labels
