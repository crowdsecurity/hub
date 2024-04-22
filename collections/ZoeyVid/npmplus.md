## NPMplus collection

A collection to defend nginx against common attacks:
 - [NPMplus](https://github.com/ZoeyVid/NPMplus) parser
 - base http scenarios (crawl, 404 scan, bf)

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /opt/npm/nginx/access.log
labels:
  type: npmplus
---
source: docker
container_name:
 - npmplus
labels:
  type: npmplus
---
source: docker
container_name:
 - npmplus
labels:
  type: modsecurity
---
listen_addr: 0.0.0.0:7422
appsec_config: crowdsecurity/virtual-patching
name: myAppSecComponent
source: appsec
labels:
  type: appsec
```


notes:
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your configuration, paths to log files might change
 -  Only relevant if you are manually installing collection
