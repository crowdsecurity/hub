Parser for [Prowlarr](https://github.com/Prowlarr/Prowlarr) Logs.

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
 - /var/log/prowlarr.txt
labels:
  type: Prowlarr
```
