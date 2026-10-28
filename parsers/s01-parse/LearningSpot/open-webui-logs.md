Parser for Open WebUI Logs with Docker.

```yaml
---
source: docker
container_name:
 - open-webui
labels:
  type: open-webui
```

## About `source_ip`

`source_ip` is the client address logged by uvicorn, Open WebUI's web server (e.g. `1.2.3.4:0` or `1.2.3.4:51234`; the port is ignored).

- **Behind a reverse proxy**, the proxy must send `X-Forwarded-For` and uvicorn must trust it (`--forwarded-allow-ips`). Otherwise every request is logged with the proxy's address, and the brute-force scenario would ban your proxy.
- **Spoofing:** if uvicorn trusts forwarded headers from any source (`--forwarded-allow-ips '*'`) and Open WebUI can be reached without going through your proxy, a client can set `X-Forwarded-For` itself and choose the logged IP. Restrict `--forwarded-allow-ips` to your proxy's address, or don't expose Open WebUI directly.
