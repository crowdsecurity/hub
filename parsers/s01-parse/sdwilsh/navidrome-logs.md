# Navidrome

A log parser for [Navidrome](https://www.navidrome.org/).

## Acquisition Examples

### Docker
```yaml
---
source: docker
container_name:
 - navidrome
container_id:
 - 00deadbeef00
labels:
  type: navidrome
```

### Log File
```yaml
---
filenames:
 - /var/log/navidrome/navidrome.log
labels:
  type: navidrome
```

### Loki Query
```yaml
---
source: loki
url: http://loki.domain:3100/
query: |
  {namespace="navidrome", container="navidrome"}
labels:
  type: navidrome
```