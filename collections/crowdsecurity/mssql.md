## MSSQL Collection

A collection for MSSQL :
 - mssql logs parser
 - bruteforce detection
 
 ## Acquisition template

Example acquisition for this collection :

```yaml
source: wineventlog
event_channel: Application
event_ids:
 - 18456
event_level: information
labels:
 type: eventlog
```

notes:
 -  You need to enable failed login logs (which should be on by default)