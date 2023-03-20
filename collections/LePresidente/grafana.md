A collection to defend [Grafana](https://grafana.com) instance against common attacks :
 - Grafana parser
 - Grafana bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/grafana/grafana.log
labels:
  type: grafana
```

Directly monitoring Docker
```yaml
---
source: docker
container_name:
 - grafana
#container_id:
# - 843ee92d231b
labels:
  type: grafana
---
