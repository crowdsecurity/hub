# Bifrost

A log parser for [Bifrost](https://github.com/maximhq/bifrost), the LLM gateway.

It reads the JSON request log lines (`"message":"request completed"`) and
flags HTTP 401 responses as failed authentication. The source IP comes from
`http.forwarded_for` (first entry) and falls back to `http.remote_addr` when
that header is missing, empty, or not a plain IP address.

The first `X-Forwarded-For` entry is client-controlled unless your proxy
overwrites the header. Configure the proxy to replace it with the real client
address, or an attacker can pick the address that gets banned.

## Acquisition Examples

### Docker
```yaml
---
source: docker
container_name:
 - bifrost
container_id:
 - 00deadbeef00
labels:
  type: bifrost
```

### Kubernetes (Loki)
```yaml
---
source: loki
url: http://loki.domain:3100/
query: |
  {namespace="bifrost", container="bifrost"}
labels:
  type: bifrost
```
