A collection to defend your [Radarr](https://github.com/Radarr/Radarr) instance against common attacks:
 - Radarr parser
 - Radarr brute-force & enumeration detection

## Acquisition template

Example acquisition for this collection:
```yaml
---
source: file
filenames:
 - /var/log/syslog
labels:
  type: syslog
```
Depending on your installation method, you may need to change the acquisition template.
