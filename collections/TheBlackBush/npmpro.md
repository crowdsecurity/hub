## NPMpro collection

A collection to defend [NPMpro](https://github.com/TheBlackBush/NPMpro) against common attacks:
 - NPMpro access and error log parser
 - NPMpro web UI login bruteforce
 - base http scenarios (crawl, 404 scan, bf)
 - nginx request limit exceeded (needs the error log)
 - appsec virtual patching and generic rules

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /opt/npmpro/nginx/logs/access.log
  - /opt/npmpro/nginx/logs/error.log
labels:
  type: npmpro
---
listen_addr: 0.0.0.0:7422
appsec_config: crowdsecurity/appsec-default
name: appsec
source: appsec
labels:
  type: appsec
```

notes:
 -  NPMpro writes the access log to disk when Write log files (`LOGROTATE=true`) or traffic statistics are turned on, and the error log only with Write log files
 -  The error log is only needed for `crowdsecurity/nginx-req-limit-exceeded` and basic auth failures, you can leave it out
 -  Depending on your configuration, paths to log files might change
 -  The web UI login scenario matches the default admin port 81 (`NPM_PORT`), see `TheBlackBush/npmpro-login-bf`
 -  please read more [here](https://github.com/TheBlackBush/NPMpro/?tab=readme-ov-file#crowdsec)
