A collection to defend your [Prowlarr](https://github.com/Prowlarr/Prowlarr) instance against common attacks:
 - Prowlarr parser
 - Prowlarr brute-force & enumeration detection

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
