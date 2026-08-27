## Description

Detects SSH brute-force attacks that are slower than the standard `crowdsecurity/ssh-slow-bf` scenario and spread repeated failed authentications across most of a day.

Uses a leaky bucket with a 12-hour leak rate and capacity of 9. Triggers on the 10th failed authentication attempt from the same IP when the previous events have not leaked enough from the bucket, for example 10 failures over roughly 10 to 12 hours.

Includes a `_user-enum` variant that triggers when the same IP tries different usernames over the same period.

**Typical triggering pattern**: 10 failed authentications from the same IP over less than 12 hours.

## Remediation

Ban the attacking IP.

## Example

An attacker spreads SSH login attempts across the day:

```
Jan 15 01:00:00 server sshd[1001]: Failed password for root from 198.51.100.1 port 54321 ssh2
Jan 15 02:10:00 server sshd[1002]: Failed password for mayalink from 198.51.100.1 port 54322 ssh2
Jan 15 03:20:00 server sshd[1003]: Failed password for ubuntu from 198.51.100.1 port 54323 ssh2
Jan 15 04:30:00 server sshd[1004]: Failed password for root from 198.51.100.1 port 54324 ssh2
Jan 15 05:40:00 server sshd[1005]: Failed password for admin from 198.51.100.1 port 54325 ssh2
Jan 15 06:50:00 server sshd[1006]: Failed password for test from 198.51.100.1 port 54326 ssh2
Jan 15 08:00:00 server sshd[1007]: Failed password for root from 198.51.100.1 port 54327 ssh2
Jan 15 09:10:00 server sshd[1008]: Failed password for user from 198.51.100.1 port 54328 ssh2
Jan 15 10:20:00 server sshd[1009]: Failed password for root from 198.51.100.1 port 54329 ssh2
Jan 15 11:30:00 server sshd[1010]: Failed password for admin from 198.51.100.1 port 54330 ssh2
```

## Dependencies

- Parser: `crowdsecurity/sshd-logs`
