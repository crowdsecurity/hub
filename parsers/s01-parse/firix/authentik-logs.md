Parser for [Authentik](https://goauthentik.io) Logs.

```yaml
---
filenames:
 - /var/log/authentik.log
labels:
  type: authentik
```

```yaml
---
source: docker
container_name:
 - authentik
labels:
  type: authentik
```
