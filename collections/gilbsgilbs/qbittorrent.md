## QBittorrent Collection

A collection for QBittorrent:
 - QBittorrent logs parser
 - Bruteforce detection on the WebUI

**Important note:** if you use a reverse proxy, make sure you configure your
“trusted proxies list” in the WebUI options to avoid accidentally banning
yourself.

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /config/qBittorrent/logs/qbittorrent.log
labels:
  type: qbittorrent
```
