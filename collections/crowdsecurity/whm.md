## WHM collection

A collection to defend WHM on the various common services installed

## Acquisition template

To help you locate the logs specific to WHM or CPanel configuration refer to https://docs.cpanel.net/knowledge-base/cpanel-product/the-cpanel-log-files/

Example acquisition for this collection :


```yaml
# You can leave the default apache2 path in acquis.yaml as it will deal with your server logs
# this extra acquisition is for apache2 errors for your various users domains 
## put in /etc/crowdsec/acquis.d/apache2whm.yaml 
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
## and comment out cpanel acquis default config in /etc/crowdsec/acquis.yaml if necessary
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
## and comment out cpanel aqcuis default config in /etc/crowdsec/acquis.yaml if necessary
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
