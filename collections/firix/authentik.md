A collection to defend [Authentik](https://goauthentik.io) instance against common attacks :
 - Authentik parser
 - Authentik bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/authentik.log
labels:
  type: authentik
```

Directly monitoring Docker
```yaml
---
source: docker
container_name:
 - authentik
labels:
  type: authentik
```
