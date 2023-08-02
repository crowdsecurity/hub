A simple parser specifically for OpenVPN logs from OPNsense since the format differs from upstream OpenVPN. I've made it so it's easy to expand if needed with support for multiple nodes.
Currently only brute force attacks are detected and passed on to the scenario.

*NOTE: This is a work in progress. The most elegant way of doing this would be with a generic OpenVPN parser capable of parsing OpenVPN logs indepent of where the service runs. To do this it requires a bit of work to the generic syslog parser*

Example of entry in acquis.yaml:
```yaml
---
filenames:
 - /var/log/openvpn/openvpn.log
labels:
  type: opnsense-openvpn 
```

Thanks to Jostrus for inspiration.
