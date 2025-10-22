Parser to ingest [BunkerWeb](https://www.bunkerweb.io/) access and error logs when using the default format that exposes the request identifier.

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

The parser expects the default BunkerWeb format:

```
$host $remote_addr - $request_id $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
```

If you customise the format, keep the request identifier and virtual host at the beginning of the line so the parser can extract `request_id` and `target_fqdn`.
