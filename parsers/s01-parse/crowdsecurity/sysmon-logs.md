A parser for [sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) events.

Example acquisition config:
```yaml
source: wineventlog
pretty_name: sysmon
event_channel: "Microsoft-Windows-Sysmon/Operational"
labels:
 type: sysmon
```