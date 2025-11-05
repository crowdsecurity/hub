## SMB collection

A collection to defend smb against common attacks:
 - smb failed authentication parser
 - smb successful authentication parser
 - detect bruteforce (fast attacks: 5 failures in ~50s)
 - detect slow bruteforce (slower attacks: 10 failures in ~10min)
 - detect time-based bruteforce (time-spaced attacks: 3 failures with >2min median interval, includes false positive reduction)


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/samba/log.*
labels:
  type: smb
```


notes :
 -  You may target a more specific log, usualy log.<DOMAIN>
 -  Be sure to have the appropriate log level in your smb.conf
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
