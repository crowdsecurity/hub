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
appsec_config: crowdsecurity/appsec-default
name: appsec
source: appsec
labels:
  type: appsec
```


notes:
 -  Depending on your configuration, paths to log files might change
 -  please read more [here](https://github.com/ZoeyVid/NPMplus/?tab=readme-ov-file#crowdsec)
