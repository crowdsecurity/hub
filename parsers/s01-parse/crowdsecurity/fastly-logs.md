Parser for fastly logs with default format [(see faslty documentation)](https://docs.fastly.com/en/guides/integrations#_logging-endpoints)

**Mandatory** You need to add those labels on the acquisition:
```
labels:
  type: syslog
  external_format: fastly
```