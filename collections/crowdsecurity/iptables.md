## Iptables/Nftables collection

A collection for portscan detection via iptables/nftables :
 - iptables/nftables parser (like in `-j LOG`)
 - multi port scan detection

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - /var/log/kern.log
labels:
  type: syslog
```

notes :
 -  Depending on your distribution/OS, paths to log files might change
 -  Only relevant if you are manually installing collection
