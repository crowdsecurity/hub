## Description

Detects time-based Dovecot brute-force attacks where evasive attackers space POP3/IMAP login attempts 20 minutes or more apart.

This is Tier 3 of the Dovecot detection chain, catching attacks that evade both `crowdsecurity/dovecot-spam` (Tier 1) and `melite/dovecot-slow-bf` (Tier 2).

Uses a conditional bucket that triggers when at least 4 failed authentication attempts from the same IP have a median interval of 20 minutes or more. The 4-hour leakspeed defines the maximum bucket lifetime, keeping memory usage bounded.

Remediation is disabled by default because the `dovecot-logs` parser does not capture successful logins, so `cancel_on` cannot be used to reduce false positives (unlike `crowdsecurity/ssh-time-based-bf` which benefits from `sshd-success-logs`).

Includes a `_user-enum` variant for time-based Dovecot username enumeration.

**Detection**: 4+ failures with median interval >= 20 minutes (within 4h window)

## Remediation

Alert only (remediation disabled). Operators can enable remediation via CrowdSec profiles if desired.

## Example

An evasive attacker spaces Dovecot login attempts ~30 minutes apart:

```
Jan 15 08:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<def001>
Jan 15 08:30:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<info@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<def002>
Jan 15 09:00:00 server dovecot: pop3-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<def003>
Jan 15 09:30:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<webmaster@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<def004>
```

## Dependencies

- Parser: `crowdsecurity/dovecot-logs`
