### Stirling-pdf parser

Currently this parser only parses authentication failure logs

Example acquisition:

```yaml
filenames:
  - /path/to/logs/invalid-auths.log
  - /path/to/logs/info-*.log
labels:
  type: stirling-pdf
```
