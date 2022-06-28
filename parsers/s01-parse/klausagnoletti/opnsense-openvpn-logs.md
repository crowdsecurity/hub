A simple parser specifically for OpenVPN logs from OPNsense since the format differs from upstream OpenVPN. I've made it so it's easy to expand if needed with support for multiple nodes.
Currently only brute force attacks are detected and passed on to the scenario.

Example of entry in acquis.yaml:
```yaml
---
filenames:
 - /var/log/openvpn/openvpn.log
labels:
  type: opnsense-openvpn 
```

Thanks to Jostrus for inspiration.
