Parser for [Uptime Kuma](https://github.com/louislam/uptime-kuma) Logs.

**Uptime Kuma version 1.15.0 or higher is required.**

Example acquisition for Docker:
```yaml
---
source: docker
container_name:
 - my_container_name
labels:
  type: uptime-kuma
```