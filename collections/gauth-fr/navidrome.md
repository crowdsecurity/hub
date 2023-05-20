A collection to defend [navidrome](https://www.navidrome.org) instance against common attacks :
 - navidrome parser
 - navidrome bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/navidrome/navidrome.log
labels:
  type: navidrome
```

For Docker directly
```yaml
---
source: docker
container_name:
 - navidrome
#container_id:
# - 843ee92d231b
labels:
  type: navidrome
```