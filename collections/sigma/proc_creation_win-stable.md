## sigma windows processus creation scenarios "full"

Collection of suspicious process creation (windows) from  [the sigma project](https://github.com/SigmaHQ/sigma).
Scenarios are relying on [sysmon logs](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) and more specifically ID 1 (enabled by default).

This collections contains scenarios flagged as "stable" by the sigma project.


## Acquisition template

Example acquisition for this collection :

```yaml
source: wineventlog
event_channel: Microsoft-Windows-Sysmon/Operational
labels:
 type: eventlog
```

notes :
 -  This collecttion exclusively relies on sysmon events with ID 1

