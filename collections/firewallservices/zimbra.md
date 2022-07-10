## Zimbra collection

A collection to parse Zimbra's logs and detect brut force on the following services
- web authentication form
- SMTP
- IMAP

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /opt/zimbra/log/mailbox.log
labels:
  type: zimbra
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
