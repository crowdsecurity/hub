## NPMplus collection

A collection to defend [NPMplus](https://github.com/ZoeyVid/NPMplus) against common attacks:
 - NPMplus access log parser
 - base http scenarios (crawl, 404 scan, bf)
 - appsec virtual patching and generic rules

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /opt/npmplus/nginx/logs/access.log
labels:
  type: npmplus
---
listen_addr: 0.0.0.0:7422
appsec_config: crowdsecurity/appsec-default
name: appsec
source: appsec
labels:
  type: appsec
```

notes:
 -  NPMplus only writes this log file when `LOGROTATE` is set to `true`
 -  Depending on your configuration, paths to log files might change
 -  please read more [here](https://github.com/ZoeyVid/NPMplus/?tab=readme-ov-file#crowdsec)
