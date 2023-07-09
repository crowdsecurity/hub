Keycloak support : parser and brute-force detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/keycloak/keycloak.log
labels:
  type: keycloak
```

Directly monitoring Docker
```yaml
---
source: docker
container_name:
 - keycloak
#container_id:
# - 843ee92d231b
labels:
  type: keycloak
---
