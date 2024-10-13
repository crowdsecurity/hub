## Mikrotik collection

A collection to defend [Mikrotik](https://mikrotik.com/) firewall against portscanning and brute force attempts
- Mikrotik parser
- Mikrotik portscan scenario
- Mikrotik brute force scenario

Do not forget to set "Firewall" flag in the remote log settings and create a drop rule with logging active.
For brute force detection you need to set the "error" flag.

As bouncer you can use the [cs-mikrotik-bouncer](https://hub.crowdsec.net/author/funkolab/bouncers/cs-mikrotik-bouncer)

## Acquisition template

Example acquisition for this collection :

Option number 1:
Setup local Syslog server to feed the Syslog to the crowdsec parser

```yaml
---
filenames:
 - /var/log/rsyslog/10.10.10.1/syslog.log
labels:
  type: mikrotik
```

Option number 2:
Using built-in [Crowdsec&ensp;SyslogServer](https://docs.crowdsec.net/docs/data_sources/syslog) to receive events, for style compatibility, enable BSD syslog style in crowdsec log action in your RouterOS.

```yaml
---
source: syslog
listen_addr: #IP_ADDRESS_of_Crowdsec
listen_port: #Portnumber_you_want_syslog_listen_on_it
labels:
 type: mikrotik
```