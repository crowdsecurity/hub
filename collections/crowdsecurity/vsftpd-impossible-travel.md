## VSFTPD Impossible Travel collection

This collection detects impossible travel scenarios for FTP authentications - when a user successfully authenticates from geographically distant locations within a timeframe that makes physical travel impossible.

**Components:**
 - VSFTPD successful authentication parser
 - Impossible travel detection (by IP)
 - Impossible travel detection (by user)

**Use Cases:**
 - Detect compromised credentials being used from multiple locations
 - Identify potential account takeover attempts
 - Monitor for insider threats and credential sharing

**Requirements:**
 - GeoIP enrichment must be enabled
 - VSFTPD logging must capture successful authentications with "OK LOGIN"
 - VSFTPD must be configured with appropriate logging level

## Acquisition template

Example acquisition for this collection:

```yaml
filenames:
  - /var/log/vsftpd/*.log
labels:
  type: vsftpd
```

**Notes:**
 - If you are using `syslog`, set type to `syslog` instead
 - Depending on your distribution/OS, paths to log files might change
 - Only relevant if you are manually installing collection

