A collection to defend [Gitea](https://gitea.io) instance against common attacks:
 - Gitea parser
 - Gitea bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
---
filenames:
 - /var/log/gitea.log
labels:
  type: gitea
```