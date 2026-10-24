# DECTRAX Syslog Enricher Parser

Enriches syslog and CEF events originating from DECTRAX autonomous deception sensors and decoy hosts (RDP, LDAP, Modbus, SCADA, SSH, SMB).

## Parsed Attributes

- `evt.Meta.source_ip`: Attacking host IP address interacting with the decoy asset.
- `evt.Meta.service`: Target decoy service breached (e.g. `rdp`, `ldap`, `modbus`).
- `evt.Meta.dest_port`: Target port probed.
- `evt.Meta.threat_level`: DECTRAX threat severity (`CRITICAL`, `HIGH`).
- `evt.Meta.log_type`: Sets `dectrax-decoy-breach` to feed downstream CrowdSec scenarios.
