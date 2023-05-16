A collection to defend [Harbor](https://goharbor.io/) instance against common attacks:
 - Harbor parser
 - Harbor bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
---
filenames:
 - /var/log/harbor/core.log
labels:
  type: harbor
```