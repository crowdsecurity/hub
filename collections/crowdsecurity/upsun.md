## Upsun collection

A collection to defend Upsun applications against common attacks:
 - nginx parser (for Upsun nginx logs)
 - base http scenarios (crawl, 404 scan, brute force)

This collection detects base HTTP scenarios on Upsun nginx logs sent via HTTP logs.

For more info check out the UpSun project template //todo, add <url to repo>

## Acquisition template

Example acquisition for this collection:

```yaml
source: http
# Change the port if necessary
listen_addr: 127.0.0.1:8888
path: /
auth_type: headers
# Choose your header name and value
# And use them in your httplog-integration configuration
headers:
    crowdsecLogForward: yourHeaderHere
labels:
  type: upsun-httplog
log-level: warn
```

notes:
 - This collection is specifically designed for Upsun platform
 - Supported acquisition for files and HTTP Logs
 - Authentication is handled via custom headers for security
 - This collection is used in the crowdsec project template: //todo, add <url to repo>