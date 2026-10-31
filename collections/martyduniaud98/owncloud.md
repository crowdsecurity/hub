A collection to defend [Owncloud](https://owncloud.com) instance against common attacks :
 - Owncloud parser
 - Owncloud bruteforce, enumeration and trusted domain detection

> Contributed by eShard - based on Nextcloud collection Håvard Moen and a1ad

## Acquisition template


 Example acquisition for this collection :

```yaml
---
filenames:
 - /var/www/owncloud/data/owncloud.log
labels:
  type: Owncloud
```

```yaml
---
source: journalctl
journalctl_filter:
  - "SYSLOG_IDENTIFIER=Owncloud"
labels:
  type: syslog
```
- Use the filename version if you have the default settings of logging to file
- Use the journalctl version if you are sending logs to syslog or systemd and read the logs from journald
