## sigmahq windows processus creation for lolbins

Collection of [lolbins process creation (windows)](https://lolbas-project.github.io/) from  [the sigmaHQ project](https://github.com/SigmaHQ/sigma).
Scenarios are relying on [sysmon logs](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) and more specifically ID 1 (enabled by default).

This collections contains scenarios all scenarios flagged as lolbins/lolbas from the sigmaHQ repository.


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