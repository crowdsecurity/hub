A collection to protect a [Plex Media Server](https://www.plex.tv) that is exposed directly to the internet, for example through a port forward:

- `andrebrait/plex-logs`: parses Plex request logs into HTTP access events
- `andrebrait/plex-unauthorized-probing`: detects enumeration of Plex endpoints without a valid token
- `crowdsecurity/plex`: allowlist for normal Plex traffic that would otherwise look like probing

Plex writes request logs only when debug logging is enabled: Settings, Troubleshooting, "Enable Plex Media Server debug logging".

The parser produces standard HTTP access events, so any generic HTTP scenarios already installed (for example `crowdsecurity/base-http-scenarios`) also run on Plex traffic. They catch scanners probing for sensitive files, but they can also ban legitimate clients: Plex strips the query string from its log, so the `crowdsecurity/plex` allowlist rule for Plex Cast `POST /log` requests (which matches on query arguments) never applies, and those requests can trigger `LePresidente/http-generic-403-bf`.

If Plex is behind a reverse proxy that CrowdSec already reads, install `crowdsecurity/plex` instead: the proxy logs already cover the HTTP scenarios.

## Acquisition template

```yaml
---
filenames:
  - "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Logs/Plex Media Server.log"
labels:
  type: plex
```

With the Docker images, use the mounted `/config` directory: `/config/Library/Application Support/Plex Media Server/Logs/Plex Media Server.log`.
