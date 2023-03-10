## freeswitch collection

### Description

This collection will parse freeswitch logs and act upon the following information:

* `freeswitch-user-enumeration` : when an IP tries to enumerate users
* `freeswitch-slow-user-enumeration` : when an IP tries to enumerate users slowly
* `freeswitch-bf` : when an IP has more than 5 failed attempts to authenticate
* `freeswitch-slow-bf` : when an IP has more than 20 failed attempts to authenticate
* `freeswitch-acl-reject` : when an IP is rejected by the ACL 15 times

### Example acquis.yaml
    
```yaml
filename: /var/log/freeswitch/freeswitch.log
labels:
    type: freeswitch
```