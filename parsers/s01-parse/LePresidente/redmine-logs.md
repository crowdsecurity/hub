Parser for [Redmine](https://www.redmine.org) Logs.

```yaml
---
filenames:
 - /var/log/production.log
labels:
  type: redmine
```

```yaml
---
source: docker
container_name:
 - Redmine
#container_id:
# - 843ee92d231b
labels:
  type: redmine
```
