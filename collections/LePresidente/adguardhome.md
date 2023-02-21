A collection to defend [AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) instance against common attacks :
 - AdGuardHome parser
 - AdGuardHome bruteforce detection

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




