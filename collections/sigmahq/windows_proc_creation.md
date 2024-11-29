## Windows Suspicious Process Creation

This collection is an import from SigmaHQ (core) project rules related to Windows Process Creation.

Release: `r2024-11-10`

## Acquisition template

Example acquisition for this collection:

```yaml
source: wineventlog
pretty_name: sysmon
event_channel: "Microsoft-Windows-Sysmon/Operational"
labels:
 type: sysmon
```
