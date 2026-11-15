## NPMpro collection

A collection to defend [NPMpro](https://github.com/TheBlackBush/NPMpro) against common attacks:
 - NPMpro log parser (access log in the classic or JSON format, stream log, and the `limit_req` lines of the error log)
 - NPMpro web UI login bruteforce
 - NPMpro bad requests (400, and 444 from the default site)
 - NPMpro stream connection flood
 - base http scenarios (crawl, 404 scan, bf)
 - nginx request limit exceeded (needs the error log)
 - appsec virtual patching and generic rules
 - alert context: the NPMpro request id (`request_id`, the access log field) in AppSec alerts

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /opt/npmpro/nginx/logs/access.log
  - /opt/npmpro/nginx/logs/error.log
  - /opt/npmpro/nginx/logs/stream.log
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
 -  The error log is only needed for `crowdsecurity/nginx-req-limit-exceeded`, you can leave it out. Failed basic auth is read from the access log (the 401 line)
 -  The stream log is only needed for `TheBlackBush/npmpro-stream-flood`, and only exists when you use streams
 -  Both log formats (Log format setting in NPMpro) use the same `type: npmpro`, and a file may even hold both
 -  Depending on your configuration, paths to log files might change
 -  The web UI login scenario matches the admin UI by its host id `npmpro` (any `NPM_PORT`), and the default port 81 for older NPMpro lines without a host id, see `TheBlackBush/npmpro-login-bf`
 -  The request id in AppSec alerts needs CrowdSec 1.6.4 or newer and an NPMpro image that sends `X-Npmpro-Request-Id` to the AppSec; other alerts carry no request id. CrowdSec 1.6.3 and older refuse to start with this context (`unknown name req`): update CrowdSec before installing the collection
 -  please read more [here](https://github.com/TheBlackBush/NPMpro/?tab=readme-ov-file#crowdsec)
