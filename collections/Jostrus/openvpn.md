## Apache2 collection

A collection to detect failed OpenVPN authentification:

## Acquisition template

Example acquisition for this collection :

```yaml
source: file
filename: /var/log/openvpn/*.log
labels:
  type: openvpn
force_inotify: true
```


notes :
 -  If you are using `syslog`, set type to `syslog` instead
 -  Depending on your configuration, paths to log files might change
 -  Only relevant if you are manually installing collection
