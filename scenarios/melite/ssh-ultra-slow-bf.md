## Description

Detects ultra-slow SSH brute-force attacks where sophisticated bots perform micro-bursts of login attempts every 9+ hours over multiple days. These attackers calibrate their timing to evade both standard `crowdsecurity/ssh-slow-bf` and the `melite/ssh-very-slow-bf` scenario.

Uses a leaky bucket with a 12-hour leak rate and capacity of 9, creating a 5-day detection window. Triggers after 10 failed authentication attempts from the same IP.

Includes a `_user-enum` variant that triggers when the same IP tries different usernames over multiple days.

**Detection window**: 5 days (leakspeed 12h × 10 events)

## Remediation

Ban the attacking IP.

## Example

A sophisticated bot does 3 attempts (root, mayalink, ubuntu) every 9 hours for 5 days:

```
Jan 15 02:00:00 server sshd[1001]: Failed password for root from 198.51.100.1 port 54321 ssh2
Jan 15 02:00:05 server sshd[1002]: Failed password for mayalink from 198.51.100.1 port 54322 ssh2
Jan 15 02:00:10 server sshd[1003]: Failed password for ubuntu from 198.51.100.1 port 54323 ssh2
Jan 15 11:00:00 server sshd[1004]: Failed password for root from 198.51.100.1 port 54324 ssh2
Jan 15 11:00:05 server sshd[1005]: Failed password for admin from 198.51.100.1 port 54325 ssh2
Jan 15 11:00:10 server sshd[1006]: Failed password for test from 198.51.100.1 port 54326 ssh2
Jan 15 20:00:00 server sshd[1007]: Failed password for root from 198.51.100.1 port 54327 ssh2
Jan 15 20:00:05 server sshd[1008]: Failed password for user from 198.51.100.1 port 54328 ssh2
Jan 16 05:00:00 server sshd[1009]: Failed password for root from 198.51.100.1 port 54329 ssh2
Jan 16 05:00:05 server sshd[1010]: Failed password for admin from 198.51.100.1 port 54330 ssh2
```

## Dependencies

- Parser: `crowdsecurity/sshd-logs`
- Optional: `melite/sshd-preauth-disconnect` (doubles event count from key-scanning attempts)
