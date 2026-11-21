Parser for [Owncloud](https://owncloud.com/) logs

If you have the default settings of logging to file, you need to add in acquisition (change filename to your log file location):

```yaml
---
filenames:
 - /var/www/owncloud/data/owncloud.log
labels:
  type: Owncloud
```

This parser requires ownCloud's default file logging (`log_type` set to `owncloud`), which writes JSON lines.
ownCloud's syslog output (`log_type` set to `syslog`) uses a different, non-JSON format and is not supported.
