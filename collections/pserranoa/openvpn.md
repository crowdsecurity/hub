## OpenVPN collection

A collection for OpenVPN failed authentification:

## Acquisition template

Example acquisition for this collection :

```yaml
source: file
filename: /var/log/openvpn/*.log
labels:
  type: openvpn
force_inotify: true
```
