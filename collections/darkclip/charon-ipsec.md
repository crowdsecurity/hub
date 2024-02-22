## Charon IPsec collection

A collection to defend Charon IPsec against bruteforce attacks:

- Charon IPsec parsers
- Charon IPsec scenarios

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /var/log/ipsec/latest.log
  - /var/log/ipsec.log
force_inotify: true
poll_without_inotify: true
labels:
  type: syslog
```
