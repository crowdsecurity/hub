A collection to defend your [GitLab](https://about.gitlab.com) Web UI against common attacks:
 - GitLab parser
 - GitLab brute-force & enumeration detection

Tested with the Omnibus package v14.9.

## Acquisition template

Example acquisition for this collection:
```yaml
---
filenames:
 - /var/log/gitlab/gitlab-rails/production_json.log
labels:
  type: gitlab
```

or for Docker:
```yaml
---
source: docker
container_name:
 - my_container_name
labels:
  type: gitlab
```
Depending on your gitlab installation method, paths to log files might change.
Tip: Don't forget to add GitLabs Nginx logs to CrowdSec.