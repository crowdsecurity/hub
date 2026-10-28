# Description

A collection to defend [Sharry](https://github.com/eikek/sharry)
deployments against common attacks:

- Sharry parser
- Sharry bruteforce detection

## Acquisition template

Example acquisition for this collection:

```yaml
---
filenames:
  - /var/log/sharry/*.log
labels:
  type: sharry
```
