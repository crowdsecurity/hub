# Bifrost

A log parser for [Bifrost](https://github.com/maximhq/bifrost), the LLM gateway.

It reads the JSON request log lines (`"message":"request completed"`).

## Failed authentication

A response is flagged as `bifrost_failed_auth` when it is HTTP 401 and
`http.request_duration_ms` is 10 or less. Bifrost rejects bad virtual keys and
unknown users in middleware before contacting any provider, so those responses
take about a millisecond. A 401 returned by an upstream provider (for example a
revoked provider key configured on the gateway) needs a network round trip and
takes longer, so it is not flagged.

The log has no field that separates gateway 401s from provider 401s, so this is
a heuristic with two known gaps:

- Checking the dashboard admin password uses bcrypt and takes longer than 10ms,
  so password guessing against the admin account is not flagged.
- A provider on the local network that answers a bad key in under 10ms is
  flagged, and repeated requests would ban the clients that sent them.

## Source IP

The source IP is `http.remote_addr`, unless that peer is a private, loopback or
CGNAT address, which is how a reverse proxy in front of Bifrost appears. In that
case the source IP is `http.forwarded_for`. When that value is not a plain IP
address, no source IP is set and the event is ignored, so the proxy is never
banned in place of the client. Bifrost exposed directly to the internet ignores
`http.forwarded_for`, so a client cannot choose the address that gets banned by
sending that header.

Bifrost logs only the first `X-Forwarded-For` entry, or `X-Real-IP` when that
header is absent. The proxy must overwrite these headers with the real client
address. A proxy that appends to them passes through whatever the client sent.

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
