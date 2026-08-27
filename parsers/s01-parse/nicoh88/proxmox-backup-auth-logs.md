# Proxmox Backup Server Auth Logs

Parses authentication logs from Proxmox Backup Server (PBS).

## Acquisition

This parser expects logs with the label `type: proxmox-backup-auth`.

By default, PBS logs authentication events to `/var/log/proxmox-backup/api/auth.log`.

**Example `acquis.yaml`:**

```yaml
filenames:
  - /var/log/proxmox-backup/api/auth.log
labels:
  type: proxmox-backup-auth
```

## Debug

### successful

```
cscli explain --type proxmox-backup-auth --log "2026-02-25T11:07:24+01:00: successful auth for user 'root@pam'"
line: 2026-02-25T11:07:24+01:00: successful auth for user 'root@pam'
        ├ s00-raw
        |       ├ 🔴 crowdsecurity/syslog-logs
        |       └ 🟢 crowdsecurity/non-syslog (+5 ~8)
        ├ s01-parse
        |       ├ 🔴 crowdsecurity/apache2-logs
        |       ├ 🔴 crowdsecurity/mysql-logs
        |       ├ 🔴 crowdsecurity/nginx-logs
        |       ├ 🔴 crowdsecurity/postfix-logs
        |       ├ 🔴 crowdsecurity/postscreen-logs
        |       ├ 🔴 proftpd-logs
        |       └ 🟢 nicoh88/proxmox-backup-auth-logs (+6 ~2)
        ├ s02-enrich
        |       ├ 🟢 crowdsecurity/dateparse-enrich (+2 ~2)
        |       ├ 🔴 crowdsecurity/geoip-enrich
        |       ├ 🔴 crowdsecurity/http-logs
        |       ├ 🟢 crowdsecurity/public-dns-allowlist (unchanged)
        |       └ 🔴 crowdsecurity/whitelists
        ├-------- parser success 🟢
        ├ Scenarios
```

### failure

```
cscli explain --type proxmox-backup-auth --log "2026-02-25T11:07:18+01:00: authentication failure; rhost=[::ffff:31.54.38.23]:47414 user=
rootasdasdasd@pbs msg=user account disabled or expired."
line: 2026-02-25T11:07:18+01:00: authentication failure; rhost=[::ffff:31.54.38.23]:47414 user=rootasdasdasd@pbs msg=user account disabled or expired.
        ├ s00-raw
        |       ├ 🔴 crowdsecurity/syslog-logs
        |       └ 🟢 crowdsecurity/non-syslog (+5 ~8)
        ├ s01-parse
        |       ├ 🔴 crowdsecurity/apache2-logs
        |       ├ 🔴 crowdsecurity/mysql-logs
        |       ├ 🔴 crowdsecurity/nginx-logs
        |       ├ 🔴 crowdsecurity/postfix-logs
        |       ├ 🔴 crowdsecurity/postscreen-logs
        |       ├ 🔴 proftpd-logs
        |       └ 🟢 nicoh88/proxmox-backup-auth-logs (+10 ~2)
        ├ s02-enrich
        |       ├ 🟢 crowdsecurity/dateparse-enrich (+2 ~2)
        |       ├ 🟢 crowdsecurity/geoip-enrich (+13)
        |       ├ 🔴 crowdsecurity/http-logs
        |       ├ 🟢 crowdsecurity/public-dns-allowlist (unchanged)
        |       └ 🔴 crowdsecurity/whitelists
        ├-------- parser success 🟢
        ├ Scenarios
                └ 🟢 nicoh88/proxmox-backup-auth-bf
```
```
cscli explain --type proxmox-backup-auth --log "2026-02-25T11:07:33+01:00: authentication failure; rhost=[::ffff:31.54.38.23]:41322 user=
root@pam msg=authentication error - AUTH_ERR (7)"
line: 2026-02-25T11:07:33+01:00: authentication failure; rhost=[::ffff:31.54.38.23]:41322 user=root@pam msg=authentication error - AUTH_ERR (7)
        ├ s00-raw
        |       ├ 🔴 crowdsecurity/syslog-logs
        |       └ 🟢 crowdsecurity/non-syslog (+5 ~8)
        ├ s01-parse
        |       ├ 🔴 crowdsecurity/apache2-logs
        |       ├ 🔴 crowdsecurity/mysql-logs
        |       ├ 🔴 crowdsecurity/nginx-logs
        |       ├ 🔴 crowdsecurity/postfix-logs
        |       ├ 🔴 crowdsecurity/postscreen-logs
        |       ├ 🔴 proftpd-logs
        |       └ 🟢 nicoh88/proxmox-backup-auth-logs (+10 ~2)
        ├ s02-enrich
        |       ├ 🟢 crowdsecurity/dateparse-enrich (+2 ~2)
        |       ├ 🟢 crowdsecurity/geoip-enrich (+13)
        |       ├ 🔴 crowdsecurity/http-logs
        |       ├ 🟢 crowdsecurity/public-dns-allowlist (unchanged)
        |       └ 🔴 crowdsecurity/whitelists
        ├-------- parser success 🟢
        ├ Scenarios
                └ 🟢 nicoh88/proxmox-backup-auth-bf
```
```
cscli explain --type proxmox-backup-auth --log "2026-02-25T11:07:25+01:00: authentication failure; rhost=[::ffff:31.54.38.23]:41318 user=root@pbs msg=user account disabled or expired."
line: 2026-02-25T11:07:25+01:00: authentication failure; rhost=[::ffff:31.54.38.23]:41318 user=root@pbs msg=user account disabled or expired.
        ├ s00-raw
        |       ├ 🔴 crowdsecurity/syslog-logs
        |       └ 🟢 crowdsecurity/non-syslog (+5 ~8)
        ├ s01-parse
        |       ├ 🔴 crowdsecurity/apache2-logs
        |       ├ 🔴 crowdsecurity/mysql-logs
        |       ├ 🔴 crowdsecurity/nginx-logs
        |       ├ 🔴 crowdsecurity/postfix-logs
        |       ├ 🔴 crowdsecurity/postscreen-logs
        |       ├ 🔴 proftpd-logs
        |       └ 🟢 nicoh88/proxmox-backup-auth-logs (+10 ~2)
        ├ s02-enrich
        |       ├ 🟢 crowdsecurity/dateparse-enrich (+2 ~2)
        |       ├ 🟢 crowdsecurity/geoip-enrich (+13)
        |       ├ 🔴 crowdsecurity/http-logs
        |       ├ 🟢 crowdsecurity/public-dns-allowlist (unchanged)
        |       └ 🔴 crowdsecurity/whitelists
        ├-------- parser success 🟢
        ├ Scenarios
                └ 🟢 nicoh88/proxmox-backup-auth-bf
```
