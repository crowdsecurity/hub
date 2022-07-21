A collection of windows specific CVEs :

 - [MSDT CVE-2022-30190](https://nvd.nist.gov/vuln/detail/CVE-2022-30190)


:warning: This collection requires a working [sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) installation. This is still a proof-of-concept, and will gain more scenarios over time.

Example acquisition config:
```
source: wineventlog
pretty_name: sysmon
event_channel: "Microsoft-Windows-Sysmon/Operational"
labels:
 type: sysmon
```