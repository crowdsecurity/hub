## ShieldPM collection

A collection to defend nginx against common attacks:
 - [ShieldPM](https://github.com/shedowe19/ShieldPM) parser
 - base http scenarios (crawl, 404 scan, bf)
 - modsecurity support

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /data/shieldpm/nginx/*.log
labels:
  type: shieldpm
---
filenames:
  - /data/shieldpm/nginx/*.log
labels:
  type: modsecurity
---
listen_addr: 0.0.0.0:7422
appsec_config: crowdsecurity/appsec-default
name: appsec
source: appsec
labels:
  type: appsec
```

## Notes
- Depending on your configuration, paths to log files might change
- Please read more at [ShieldPM GitHub](https://github.com/shedowe19/ShieldPM)
