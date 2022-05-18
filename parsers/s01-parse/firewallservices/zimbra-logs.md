Zimbra failed authentication parser. To use it, you should add an acquisition like
```yaml
---
filenames:
  - /opt/zimbra/log/mailbox.log
labels:
  type: zimbra
```
Note that if you run Zimbra on several servers :
- Acquisition should be done on the mailbox servers
- You should set zimbraMailTrustedIP to the list of IP of your Zimbra proxy to ensure the original client IP will appear in the logs. For example:
```bash
zmprov mcf +zimbraMailTrustedIP 10.30.1.13
```
