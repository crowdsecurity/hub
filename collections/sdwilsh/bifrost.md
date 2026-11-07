A collection to defend [Bifrost](https://github.com/maximhq/bifrost) against the following behaviors:
 - Brute force authentication attempts

## Acquisition Examples

### Docker
```yaml
---
source: docker
container_name:
 - bifrost
labels:
  type: bifrost
```

### Log File
```yaml
---
filenames:
 - /var/log/bifrost/*.log
labels:
  type: bifrost
```

Bifrost must log to stdout or a file as JSON, which is its default. The client
address comes from `X-Forwarded-For`, so a reverse proxy in front of Bifrost
must overwrite that header with the real client address.
