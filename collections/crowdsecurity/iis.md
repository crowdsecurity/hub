## IIS collection

A collection for IIS :
 - ISS parser (only W3C format is supported, with the default format)
 - base http scenarios for crawl, scan etc.

Note:
 - IIS will buffer the logs in memory before writing them to the log file (or the event log). The flush is done every minute or every 64kB by default, this can lead to some false positives on low traffic websites, as crowdsec will be a surge of logs every minute. This can be mitigated by setting the `use_time_machine` settings to true in the relevant section of your acquisition config.

## Acquisition template

Example acquisition for this collection if you log to a file:

```yaml
use_time_machine: true #Process logs as if we were replaying them to get the timestamp from the 
filenames:
  - C:\\inetpub\\logs\\LogFiles\\*\\*.log
labels:
  type: iis
```

Example acquisition for this collection if you log to windows events:
```yaml
source: wineventlog
event_channel: Microsoft-IIS-Logging/Logs
event_ids:
 - 6200
event_level: information
labels:
 type: iis
```
