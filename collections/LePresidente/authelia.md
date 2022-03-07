A collection to defend [Authelia](https://www.authelia.com) instance against common attacks :
 - Authelia parser
 - Authelia bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/Authelia.log
labels:
  type: Authelia
```