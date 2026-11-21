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

This parser requires ownCloud's default file logging (`log_type` set to `owncloud`), which writes JSON lines.
ownCloud's syslog output (`log_type` set to `syslog`) uses a different, non-JSON format and is not supported.
