A collection to defend your [Uptime Kuma](https://github.com/louislam/uptime-kuma) instance against common attacks:
 - Uptime Kuma parser
 - Uptime Kuma brute-force & enumeration detection

**Uptime Kuma version 1.15.0 or higher is required.**

## Acquisition template

Example acquisition for this collection:
```yaml
---
source: docker
container_name:
 - my_container_name
labels:
  type: uptime-kuma
```
Depending on your installation method, you may need to change the acquisition template.