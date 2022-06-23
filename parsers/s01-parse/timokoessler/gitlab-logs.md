Parser for [GitLab](https://about.gitlab.com) Logs. Tested with the Omnibus package v14 and v15.

Example acquisition for a log file:
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