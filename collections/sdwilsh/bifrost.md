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

Bifrost must log as JSON to stdout or a file, which is its default. When a
reverse proxy runs in front of Bifrost on a private address, the proxy must
overwrite `X-Forwarded-For` with the real client address. See the parser
documentation for how the source IP is chosen and which authentication failures
are detected.

For example, with nginx:

```nginx
proxy_set_header X-Forwarded-For $remote_addr;
```

Do not use `$proxy_add_x_forwarded_for`: it appends to the header the client
sent, so Bifrost would log an address chosen by the client, and that address
would be banned.
