A collection to defend [Bitwarden Self Hosted](https://bitwarden.com/help/install-and-deploy-unified-beta/) deployments against common attacks :
 - Bitwarden parser
 - Bitwarden bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
---
filenames:
  - /etc/bitwarden/logs/identity.log
labels:
  type: bitwarden
```
