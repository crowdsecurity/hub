## Unifi collection

A collection to defend Unifi gear against common attacks :
- Unifi syslog parser: `crowdsecurity/unifi-logs`
- Dropbear parser: `crowdsecurity/dropbear-logs`
- SSH bruteforce scenario : `crowdsecurity/ssh-bf`
- Iptables parser: `crowdsecurity/iptables-logs`
- Port scan detection: `crowdsecurity/iptables-scan-multi_ports`

## Acquisition template

Example acquisition for this collection :

```yaml
source: syslog
listen_addr: 0.0.0.0
listen_port: 4242
labels:
 type: unifi
```


notes :
 -  While the unifi gear uses syslog to send the logs, the format is non-compliant with the RFC, so you need to set the type to `unifi`
