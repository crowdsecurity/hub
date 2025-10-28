## SFTPGo collection

A collection to defend SFTPGo against common attacks:
 - SFTPGo log parser (JSON format)
 - Bruteforce detection (FTP/SFTP/SSH protocols)
 - Impossible travel detection for compromised accounts

## Acquisition template

Example acquisition for this collection:

```yaml
filename: /var/log/sftpgo/sftpgo.log
labels:
  type: sftpgo
```

Notes:
 - SFTPGo logs in JSON format by default
 - Log path depends on your SFTPGo configuration
 - Supports detection of failed logins (with or without username)
 - Detects successful logins from geographically impossible locations
 - Only relevant if you are manually installing collection

