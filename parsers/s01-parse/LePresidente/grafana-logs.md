Parser for [Grafana](https://grafana.com) Logs.

```yaml
---
filenames:
 - /var/log/grafana/grafana.log
labels:
  type: grafana
```

```yaml
---
source: docker
container_name:
 - grafana
#container_id:
# - 843ee92d231b
labels:
  type: grafana
```