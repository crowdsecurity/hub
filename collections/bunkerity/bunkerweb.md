A collection to defend [BunkerWeb](https://www.bunkerweb.io/) instances against common attacks:
 - BunkerWeb log parser (supports both legacy and current formats with request ID)
 - Base HTTP scenarios from nginx collection (crawl, 404 scan, brute-force)

## Acquisition template

Example acquisition for this collection:

```yaml
---
filenames:
  - /var/log/bunkerweb/access.log
labels:
  type: bunkerweb
```

notes:
 - The parser extracts the optional `request_id` field when present
 - Depending on your BunkerWeb configuration, log paths might vary
