Parser to ingest [BunkerWeb](https://www.bunkerweb.io/) access and error logs, extracting the optional request identifier when present.

## Acquisition

Ensure the parser is loaded together with `crowdsecurity/http-logs` and `crowdsecurity/dateparse-enrich`.  
Typical acquisition for the default file target:

```yaml
---
filenames:
  - /var/log/bunkerweb/access.log
labels:
  type: bunkerweb
```

## Log format

The parser accepts both legacy (without `$request_id`) and current BunkerWeb formats:

```
$host $remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
$host $remote_addr - $request_id $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
```

If you customise the format, keep the virtual host and (when enabled) the request identifier in the leading fields so the parser can extract `target_fqdn` and `request_id`.
