## Windows Suspicious Process Creation

This collection is an import from SigmaHQ (core) project rules related to Windows Process Creation.

Release: `r2024-11-10`

## Pre Requisites

The process creation detection relies on Sysmon.

 - [Sysmon Download & Installation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
 - [Example Sysmon configuration by @SwiftOnSecurity](https://github.com/SwiftOnSecurity/sysmon-config)

## Acquisition template

Example acquisition for this collection:

```yaml
source: wineventlog
pretty_name: sysmon
event_channel: "Microsoft-Windows-Sysmon/Operational"
labels:
 type: sysmon
```
