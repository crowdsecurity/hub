A collection to defend [Miniflux](https://miniflux.app/) instance against common attacks :
 - Miniflux parser
 - Miniflux bruteforce detection

## Acquisition template

Example acquisition for this collection :

```yaml
---
source: docker
container_name:
 - miniflux
labels:
  type: miniflux
```

Note:
- Miniflux doesn't write timestamps in logs by default. You must set `LOG_DATE_TIME=1` to enable timestamps.
