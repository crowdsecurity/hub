## Description

Detects extremely slow SSH brute-force attacks where attackers perform only ~1 attempt every 8 hours over 3 days. These attackers evade even the `melite/ssh-ultra-slow-bf` scenario which requires 10 events (too many for such a low rate).

Uses a leaky bucket with an 18-hour leak rate and capacity of 3, creating a 72-hour (3-day) detection window. Triggers after just 4 failed authentication attempts from the same IP.

Includes a `_user-enum` variant for slow username enumeration over 3 days.

**Detection window**: 72 hours / 3 days (leakspeed 18h × 4 events)

## Remediation

Ban the attacking IP.

## Example

An attacker targets ISPConfig-related usernames with ~8 hour intervals:

```
Jan 15 06:00:00 server sshd[1001]: Failed password for ispconfig from 203.0.113.1 port 54321 ssh2
Jan 15 14:00:00 server sshd[1002]: Failed password for admin from 203.0.113.1 port 54322 ssh2
Jan 16 00:00:00 server sshd[1003]: Failed password for webmaster from 203.0.113.1 port 54323 ssh2
Jan 16 08:00:00 server sshd[1004]: Failed password for root from 203.0.113.1 port 54324 ssh2
```

## Dependencies

- Parser: `crowdsecurity/sshd-logs`
- Optional: `melite/sshd-preauth-disconnect` (doubles event count from key-scanning attempts)
