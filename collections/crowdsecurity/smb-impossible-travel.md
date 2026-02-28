## SMB Impossible Travel collection

This collection detects impossible travel scenarios for SMB authentications - when a user successfully authenticates from geographically distant locations within a timeframe that makes physical travel impossible.

**Components:**
 - SMB successful authentication parser
 - Impossible travel detection (by IP)
 - Impossible travel detection (by user)

**Use Cases:**
 - Detect compromised credentials being used from multiple locations
 - Identify potential account takeover attempts
 - Monitor for insider threats and credential sharing

**Requirements:**
 - GeoIP enrichment must be enabled
 - SMB logging must capture successful authentications with `NT_STATUS_OK`
 - Samba `log level` must be set to capture authentication events

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /var/log/samba/log.*
labels:
  type: smb
```

**Notes:**
 - You may target a more specific log, usually log.<DOMAIN>
 - Be sure to have the appropriate log level in your smb.conf
 - If you are using `syslog`, set type to `syslog` instead
 - Depending on your distribution/OS, paths to log files might change
 - Only relevant if you are manually installing collection

