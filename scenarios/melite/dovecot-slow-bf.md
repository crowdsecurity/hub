## Description

Detects slow brute-force attacks on Dovecot (POP3/IMAP) where attackers space login attempts 7-30 minutes apart to evade standard detection.

This is Tier 2 of the Dovecot detection chain, complementing `crowdsecurity/dovecot-spam` (Tier 1, ~24min window) and `melite/dovecot-time-based-bf` (Tier 3, pattern-based).

Uses a leaky bucket with 60-minute (3600s) leak rate and capacity of 3. Triggers after 4 failed authentication attempts from the same IP. At 10-minute intervals, all 4 events arrive before the first leak, guaranteeing detection.

Includes a `_user-enum` variant that triggers when the same IP tries different Dovecot usernames slowly.

**Detection window**: 3 hours max (leakspeed 3600s x capacity 3), typically triggers within 30-60 minutes

## Remediation

Ban the attacking IP.

## Example

A distributed attacker tests Dovecot credentials with ~10-minute intervals:

```
Jan 15 08:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<abc001>
Jan 15 08:10:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<abc002>
Jan 15 08:20:00 server dovecot: pop3-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<abc003>
Jan 15 08:30:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<abc004>
```

## Dependencies

- Parser: `crowdsecurity/dovecot-logs`
