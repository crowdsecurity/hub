Parser for [Radarr](https://github.com/Radarr/Radarr) Logs.

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
 - /var/log/radarr.txt
labels:
  type: Radarr
```
