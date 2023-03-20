A collection to defend [Jellyfin](https://jellyfin.org) instance against common attacks :
 - Jellyfin parser
 - Jellyfin bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/jellyfin/log_*.log
labels:
  type: jellyfin
```

For Docker directly
```yaml
---
source: docker
container_name:
 - jellyfin
#container_id:
# - 843ee92d231b
labels:
  type: jellyfin
```