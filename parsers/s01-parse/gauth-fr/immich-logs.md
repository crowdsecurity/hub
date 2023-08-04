Parser for [Immich](https://github.com/immich-app/immich) Logs.

```yaml
---
filenames:
 - /var/log/immich_server.log
labels:
  type: immich
```

```yaml
---
source: docker
container_name:
 - immich_server
#container_id:
# - 843ee92d231b
labels:
  type: immich
```
