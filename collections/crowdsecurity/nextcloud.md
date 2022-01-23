A collection to defend [Nextcloud](https://nextcloud.com) instance against common attacks :
 - Nextcloud parser
 - Nextcloud bruteforce & enumeration detection

## Acquisition template


 Example acquisition for this collection :

```yaml
---
filenames:
 - /var/www/nextcloud/data/nextcloud.log
labels:
  type: Nextcloud
```

```yaml
---
source: journalctl
journalctl_filter:
  - "SYSLOG_IDENTIFER=Nextcloud"
labels:
  type: Nextcloud
```
- Use the filename version if you have the default [setting](https://docs.nextcloud.com/server/stable/admin_manual/configuration_server/config_sample_php_parameters.html?highlight=loglevel#logging) of logging to file
- Use the journalctl version if you are sending logs to syslog or systemd and read the logs from journald
