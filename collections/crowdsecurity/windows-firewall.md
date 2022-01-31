## Windows firewall collection

A collection for portscan detection via windows firewall logs :
 - Windows firewall logs parser
 - multi port scan detection

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - C:\\Windows\\System32\\LogFiles\\Firewall\\pfirewall.log
labels:
  type: windows-firewall
```

notes :
 - This collection uses the `crowdsecurity/iptables-scan-multi_ports` scenario because we are bad at naming :) 
 - Because Windows enables stealth mode by default, only scan targeted to port that have a listeners will be logged, so we will probably miss some attacks (we do NOT recommand disabling stealth mode) 
