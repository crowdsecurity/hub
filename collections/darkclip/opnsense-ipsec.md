## OPNSense IPSEC collection

A collection to defend OPNSense IPSEC against bruteforce attacks:

- OPNSense IPSEC parser
- OPNSense IPSEC scenario

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /var/log/ipsec/latest.log
force_inotify: true
poll_without_inotify: true
labels:
  type: syslog
```
