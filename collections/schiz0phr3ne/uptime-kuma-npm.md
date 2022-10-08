A collection to defend your [Uptime Kuma](https://github.com/louislam/uptime-kuma) instance, runned directly with `npm`, against common attacks:
 - Uptime Kuma parser
 - Uptime Kuma brute-force & enumeration detection

**Uptime Kuma version 1.15.0 or higher is required.**

## Acquisition template

Example acquisition for this collection:
```yaml
---
filenames:
  - /var/log/syslog
labels:
  type: syslog
---
```
Depending on your installation method, you may need to change the acquisition template.
