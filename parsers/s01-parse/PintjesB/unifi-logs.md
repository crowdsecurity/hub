Parsing of Unifi firewall logs

Example acquisition for this collection:
```yaml
---
filenames:
  - /syslog-server/unifi-firewall.log
labels:
  type: unifi
```

TODO:
- [x] Firewall WAN rule hits
- [ ] Firewall IPS logs
- [ ] Firewall IDS logs
- [ ] Firewall auth logs (?)