## Mikrotik collection

A collection to defend [Mikrotik](https://mikrotik.com/) firewall against portscanning.
- Mikrotik parser
- Mikrotik portscan scenario

You need to set up a remote syslog server. There is no crowdsec client on the Mikrotik, so log parsing needs to be done on the rsyslog server.
Do not forget to set "Firewall" flag in the remote log settings and create a drop rule with logging active.
As bouncer you can use the [cs-mikrotik-bouncer](https://hub.crowdsec.net/author/funkolab/bouncers/cs-mikrotik-bouncer)

## Acquisition template

Example acquisition for this collection :

```yaml
---
filenames:
 - /var/log/rsyslog/10.10.10.1/syslog.log
labels:
  type: mikrotik
```
