## Description

Detects very slow SSH brute-force attacks where attackers space login attempts more than 1 hour apart to evade standard detection scenarios like `crowdsecurity/ssh-slow-bf` (which has a ~10 minute detection window).

Uses a leaky bucket with a 4-hour leak rate and capacity of 5, creating a 24-hour detection window. Triggers after 6 failed authentication attempts from the same IP within 24 hours.

Includes a `_user-enum` variant that triggers when the same IP tries different usernames slowly (using `distinct` on `target_user`).

**Detection window**: 24 hours (leakspeed 4h × 6 events)

## Remediation

Ban the attacking IP.

## Example

An attacker spaces SSH login attempts ~70 minutes apart to stay under the radar of standard brute-force detection:

```
Jan 15 01:00:00 server sshd[1001]: Failed password for root from 192.0.2.1 port 54321 ssh2
Jan 15 02:10:00 server sshd[1002]: Failed password for root from 192.0.2.1 port 54322 ssh2
Jan 15 03:20:00 server sshd[1003]: Failed password for admin from 192.0.2.1 port 54323 ssh2
Jan 15 04:30:00 server sshd[1004]: Failed password for root from 192.0.2.1 port 54324 ssh2
Jan 15 05:40:00 server sshd[1005]: Failed password for ubuntu from 192.0.2.1 port 54325 ssh2
Jan 15 06:50:00 server sshd[1006]: Failed password for root from 192.0.2.1 port 54326 ssh2
```

## Dependencies

- Parser: `crowdsecurity/sshd-logs`
- Optional: `melite/sshd-preauth-disconnect` (doubles event count from key-scanning attempts)
