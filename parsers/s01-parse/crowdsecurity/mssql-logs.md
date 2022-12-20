Parser for MSSQL Logs via wineventlog OR MSSQL logs via [Azure-Edge-Sql](https://hub.docker.com/_/microsoft-azure-sql-edge) via docker

```yaml
---
source: wineventlog
event_channel: Application
event_ids:
 - 18456
event_level: information
labels:
 type: mssql
---
source: docker
container_id:
 - <Docker Container ID> #Azure-Edge-Sql container ID
container_name_regexp:
 - .*mssql*
labels:
  type: mssql
```
