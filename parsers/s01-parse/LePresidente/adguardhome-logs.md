Parser for [AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) Logs.

```yaml
---
filenames:
 - /var/log/AdGuardHome.log
labels:
  type: adguardhome
```

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
