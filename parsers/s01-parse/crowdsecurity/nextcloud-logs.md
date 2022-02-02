Parser for [Nextcloud](https://nextcloud.com/) logs

If you have the default [setting](https://docs.nextcloud.com/server/stable/admin_manual/configuration_server/config_sample_php_parameters.html?highlight=loglevel#logging)
of logging to file, you need to add in acquisition (change filename to your log file location):

```yaml
---
filenames:
 - /var/www/nextcloud/data/nextcloud.log
labels:
  type: Nextcloud
```

If you are sending logs to syslog or systemd and read from journald, add:
```yaml
---
source: journalctl
journalctl_filter:
  - "SYSLOG_IDENTIFER=Nextcloud"
labels:
  type: Nextcloud
```
