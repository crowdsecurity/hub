A collection to defend [Redmine](https://www.redmine.org) instance against common attacks :
 - Redmine parser
 - Redmine bruteforce detection

## Acquisition template

Example acquisition for this collection :

If using LOG_FILE environment variable:
```yaml
---
filenames:
 - /var/log/production.log
labels:
  type: redmine
```

Directly monitoring Docker
```yaml
---
source: docker
container_name:
 - Redmine
#container_id:
# - 843ee92d231b
labels:
  type: redmine
```