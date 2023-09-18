A collection to defend [AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) instance against common attacks :
 - AdGuardHome parser
 - AdGuardHome bruteforce detection

## AdGuard Home - Configuration
Add into AdGuardHome.yaml the follow arguments (per default Adguard write into stdout or syslog [Doku AdGuard Home](https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration#command-line)

```
log:
  file: /var/log/AdGuardHome.log
  verbose: false
```

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/AdGuardHome.log
labels:
  type: adguardhome
```

Directly monitoring Docker
```yaml
---
source: docker
container_name:
 - AdGuardHome
#container_id:
# - 843ee92d231b
labels:
  type: adguardhome
```




