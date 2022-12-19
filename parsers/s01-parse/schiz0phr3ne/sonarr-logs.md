Parser for [Sonarr](https://github.com/Sonarr/Sonarr) Logs.

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
