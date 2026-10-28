A collection to defend your [Sonarr](https://github.com/Sonarr/Sonarr) instance against common attacks:
 - Sonarr parser
 - Sonarr brute-force & enumeration detection

## Acquisition template

Example acquisition for this collection:
```yaml
---
source: file
filenames:
 - /var/log/syslog
labels:
  type: syslog
---
source: file
filenames:
 - /var/log/sonarr.txt
labels:
  type: Sonarr
```
Depending on your installation method, you may need to change the acquisition template.
