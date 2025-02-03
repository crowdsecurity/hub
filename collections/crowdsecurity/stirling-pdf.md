### Stirling-pdf collection

This collection contains a parser and scenario to detect authentication bruteforce attacks against the Stirling PDF login panel.

Example acquisition:

```yaml
filenames:
  - /path/to/logs/invalid-auths.log
  - /path/to/logs/info-*.log
labels:
  type: stirling-pdf
```
