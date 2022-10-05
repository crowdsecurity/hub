## WHM collection

A collection to defend WHM on the various common services installed

## Acquisition template

To help you locate the logs specific to WHM or CPanel configuration refer to https://docs.cpanel.net/knowledge-base/cpanel-product/the-cpanel-log-files/

Example acquisition for this collection :

```yaml
# apache2 typical WHM override : 
## put in /etc/crowdsec/acquis.d/apache2.yaml 
## and comment out apache aqcuis default config in /etc/crowdsec/acquis.yaml
filenames: 
  - /var/log/apache2/domlogs/*
exclude_regexps:
  - ".*ftpxferlog.*"
  # you can excluse other regexp that are not apache2 log files
labels:
  type: apache2
```

```yaml
# ftpxfer typical WHM override : 
## put in /etc/crowdsec/acquis.d/ftpxfer.yaml 
filenames: 
  - /usr/local/apache2/domlogs/ftpxferlog
labels:
  type: syslog
  # depending on your ftp service the type can also be proftpd or vsftpd
```

```yaml
# cpanel typical WHM override : 
## put in /etc/crowdsec/acquis.d/cpanel.yaml 
## and comment out cpanel aqcuis default config in /etc/crowdsec/acquis.yaml
filenames: 
  - /usr/local/cpanel/logs/login_log
  - /usr/local/cpanel/logs/error_log
  - /usr/local/cpanel/logs/access_log
labels:
  type: cpanel
```

```yaml
# In case your Dovecot logs into syslog
# syslog will likely route mail logs to maillog
## put in /etc/crowdsec/acquis.d/dovecot.yaml 
## and comment out cpanel aqcuis default config in /etc/crowdsec/acquis.yaml
## depending on your OS the file might be /var/log/maillog or /var/log/mail.log
filenames: 
  - /var/log/maillog
labels:
  type: syslog
```

notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
