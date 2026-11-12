Parser for [Plex Media Server](https://www.plex.tv) request logs.

It reads the `Completed:` lines Plex writes for every finished HTTP request and turns them into standard HTTP access events (`service: http`, `log_type: http_access-log`), so the generic HTTP scenarios can run on traffic that reaches Plex directly, without a reverse proxy in front of it.

Plex writes these lines only when **debug logging** is enabled: Settings, Troubleshooting, "Enable Plex Media Server debug logging". Plex strips the query string from the logged path, so `X-Plex-Token` values are never read.

```
Nov 12, 2026 11:15:45.555 [23290034416440] DEBUG - Completed: [198.51.100.7:52812] 401 GET / (3 live) #13b64 TLS 0ms 400 bytes (pipelined: 1)
```

Plex logs local time without a time zone, so the parsed timestamp is interpreted as UTC.

## Acquisition template

```yaml
---
filenames:
  - "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/Plex Media Server.log"
labels:
  type: plex
```

With the Docker images (linuxserver.io, plexinc/pms-docker), the file is under the mounted `/config` directory: `/config/Library/Application Support/Plex Media Server/Logs/Plex Media Server.log`. Plex does not write request logs to the container output, so the `docker` data source cannot be used.
