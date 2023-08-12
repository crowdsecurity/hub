A collection to defend [Cowrie](http://github.com/cowrie/cowrie) against common attacks:
 - Cowrie parser
 - Cowrie Code Execution detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /home/cowrie/cowrie/var/log/cowrie/cowrie.log
labels:
  type: cowrie
```
