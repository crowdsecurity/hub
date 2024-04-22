Parser for [Miniflux](https://github.com/miniflux/v2) Logs.

*Set `LOG_DATE_TIME=1` so Miniflux will timestamp the logs.*

```yaml
---
source: docker
container_name:
 - miniflux
labels:
  type: miniflux
```
