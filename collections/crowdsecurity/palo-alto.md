## Palo Alto collection

This collection support:
 - Parser for [Palo Alto Threat Log](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/threat-log-fields)
 - Scenario trigger for IP reported with a threat severity higher or equal than `medium`

Note: It is expected for the admin to forward Palo Alto logs to an existing facility (or directly to CrowdSec syslog server) to read the logs of Palo Alto with CrowdSec.

## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
  - <path_to_palo_alto_log_file>
labels:
  type: palo-alto-threat
```

