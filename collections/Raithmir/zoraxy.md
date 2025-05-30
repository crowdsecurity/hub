## Zoraxy collection

A collection to defend Zoraxy against common attacks :
 - [Zoraxy](https://github.com/tobychui/zoraxy) parser
 - base http scenarios (crawl, 404 scan, bf)

## Acquisition template

Example acquisition for this collection (/etc/crowdsec/acquis.d/zoraxy.yaml) :

Local install...
```yaml
---
filenames:
  - "/opt/zoraxy/log/zr_*.log" ## Wildcard all logs. Logs rollover each month.
labels:
  type: "zoraxy" ## Type defined in the parser
```

Docker install...
```yaml
source: docker
container_name:
  - zoraxy
labels:
  type: zoraxy
```

