## NPMplus collection

A collection to defend nginx against common attacks:
 - [NPMplus](https://github.com/ZoeyVid/NPMplus) parser
 - base http scenarios (crawl, 404 scan, bf)

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /opt/npmplus/nginx/*.log
labels:
  type: npmplus
---
filenames:
  - /opt/npmplus/nginx/*.log
labels:
  type: modsecurity
---
listen_addr: 0.0.0.0:7422
appsec_config: crowdsecurity/appsec-default
name: appsec
source: appsec
labels:
  type: appsec
# if you use openappsec you can enable this
#---
#source: file
#filenames:
# - /opt/openappsec/logs/cp-nano-http-transaction-handler.log*
#labels:
#  type: openappsec
```


notes:
 -  Depending on your configuration, paths to log files might change
 -  please read more [here](https://github.com/ZoeyVid/NPMplus/?tab=readme-ov-file#crowdsec)
