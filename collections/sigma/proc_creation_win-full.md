## sigma windows processus creation scenarios "full"

Collection of suspicious process creation (windows) from  [the sigma project](https://github.com/SigmaHQ/sigma).
Scenarios are relying on [sysmon logs](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) and more specifically ID 1 (enabled by default).

This collections contains **all** the scenarios from sigma's repository for windows processus creation category. You can as well refer to the following sub-collections for more granulariy :
 - proc_creation_win-stable : all scenarios flagged as "stable" by sigma
 - proc_creation_win-experimental : all scenarios flagged as "experimental" by sigma
 - proc_creation_win-test : all scenarios flagged as "test" by sigma


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

