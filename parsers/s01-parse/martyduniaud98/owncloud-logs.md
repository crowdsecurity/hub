Parser for [Owncloud](https://owncloud.com/) logs

If you have the default settings of logging to file, you need to add in acquisition (change filename to your log file location):

```yaml
---
filenames:
 - /var/www/owncloud/data/owncloud.log
labels:
  type: Owncloud
```

If you are sending logs to syslog or systemd and read from journald, add:
```yaml
---
source: journalctl
journalctl_filter:
  - "SYSLOG_IDENTIFIER=Owncloud"
labels:
  type: syslog
```
