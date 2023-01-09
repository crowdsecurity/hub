This is a parser for [MongoDB](https://www.mongodb.com/) logs. MongoDB version 4.4 or higher is required.

Example acquisition for a docker container:
```yaml
---
source: docker
container_name:
 - my_container_name
labels:
  type: mongodb
```

or for a log file:
```yaml
---
filenames:
 - /var/log/mongodb/mongodb.log
labels:
  type: mongodb
```
Depending on your installation method, paths to log files might change.