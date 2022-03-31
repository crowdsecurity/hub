## Magento collection

This Magento collection supports :
 - Parser for the [CrowdSec Magento Extension](https://hub.crowdsec.net/author/crowdsecurity/bouncers/cs-magento-bouncer)
 - Web authentication bruteforce detection


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/www/html/magento2/var/log/crowdsec-events.log
labels:
  type: magento-extension
```

notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
