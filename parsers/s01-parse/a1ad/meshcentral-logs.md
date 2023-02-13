Parser for [Meshcentral](https://www.meshcommander.com/meshcentral2) Auth Logs.

You need to add the following in the Meshcentral config file before Meshcentral starts logging:
"authLog": "/opt/meshcentral/meshcentral-data/auth.log"

```yaml
---
filenames:
 - /opt/meshcentral/meshcentral-data/auth.log
labels:
  type: meshcentral
```
