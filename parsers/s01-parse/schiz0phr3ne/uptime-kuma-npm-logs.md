Parser for [Uptime Kuma](https://github.com/louislam/uptime-kuma) logs when runned with `npm` (logs are in `syslog`).

**Uptime Kuma version 1.15.0 or higher is required.**

Example acquisition for Docker:
```yaml
---
filenames:
  - /var/log/syslog
labels:
  type: syslog
---
