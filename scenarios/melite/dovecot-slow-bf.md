## Description

Detects slow brute-force attacks on Dovecot (POP3/IMAP) where distributed botnets or patient attackers space login attempts to evade standard detection.

Uses a leaky bucket with a 4-hour (14400s) leak rate and capacity of 4, creating a 20-hour detection window. Triggers after 5 failed authentication attempts from the same IP. The 4-hour leak rate catches attackers doing bursts of events with 5+ hour pauses between bursts.

Includes a `_user-enum` variant that triggers when the same IP tries different Dovecot usernames slowly.

**Detection window**: 20 hours (leakspeed 14400s × 5 events)

## Remediation

Ban the attacking IP.

## Example

A distributed attacker tests Dovecot credentials with 2-4 hour intervals:

```
Jan 15 08:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<abc123>
Jan 15 11:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<info@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<def456>
Jan 15 14:00:00 server dovecot: pop3-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<ghi789>
Jan 15 17:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<webmaster@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<jkl012>
Jan 15 20:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=192.0.2.1, lip=10.0.0.1, TLS, session=<mno345>
```

## Dependencies

- Parser: `crowdsecurity/dovecot-logs`
