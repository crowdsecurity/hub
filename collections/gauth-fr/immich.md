A collection to defend [Immich](https://immich.app) instance against common attacks :
 - Immich parser
 - Immich bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/immich/immich_server.log
labels:
  type: immich
```

For Docker directly
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
