Parser for [Mealie](https://mealie.io/) Logs.

```yaml
---
filenames:
 - /var/log/mealie.log
labels:
  type: mealie
```

```yaml
---
source: docker
container_name:
 - mealie
#container_id:
# - 843ee92d231b
labels:
  type: mealie
