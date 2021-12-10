A collection to defend fastly against common http attacks :
 - fastly default log format parser
 - base http scenarios (crawl, 404 scan, bf etc.)

 **Mandatory** You need to add those labels on the acquisition:
```yaml
labels:
  type: syslog
  external_format: fastly
```