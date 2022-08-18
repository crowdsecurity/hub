A collection to defend [MongoDB](https://www.mongodb.com/) against common attacks:
 - MongoDB parser
 - MongoDB brute-force & enumeration detection

MongoDB version 4.4 or higher is required.

## Acquisition template

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