# Description

A collection to defend [Audiobookshelf Self Hosted](https://github.com/advplyr/audiobookshelf)
deployments against common attacks:

- Audiobookshelf parser
- Audiobookshelf bruteforce detection

## Acquisition template

Example acquisition for this collection:

```yaml
---
filenames:
  - /var/log/audiobookshelf/*.txt
labels:
  type: audiobookshelf
```
