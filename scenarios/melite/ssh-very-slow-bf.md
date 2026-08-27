## Description

Detects SSH brute-force attacks that are slower than the standard `crowdsecurity/ssh-slow-bf` scenario but still produce several failed authentications over a few hours.

Uses a leaky bucket with a 4-hour leak rate and capacity of 5. Triggers on the 6th failed authentication attempt from the same IP when the previous events have not leaked enough from the bucket, for example 6 failures over roughly 3 to 4 hours.

Includes a `_user-enum` variant that triggers when the same IP tries different usernames slowly (using `distinct` on `target_user`).

**Typical triggering pattern**: 6 failed authentications from the same IP over less than 4 hours.

## Remediation

Ban the attacking IP.

## Example

An attacker spaces SSH login attempts around 40 minutes apart to stay under the radar of standard brute-force detection:

```
Jan 15 01:00:00 server sshd[1001]: Failed password for root from 192.0.2.1 port 54321 ssh2
Jan 15 01:40:00 server sshd[1002]: Failed password for root from 192.0.2.1 port 54322 ssh2
Jan 15 02:20:00 server sshd[1003]: Failed password for admin from 192.0.2.1 port 54323 ssh2
Jan 15 03:00:00 server sshd[1004]: Failed password for root from 192.0.2.1 port 54324 ssh2
Jan 15 03:40:00 server sshd[1005]: Failed password for ubuntu from 192.0.2.1 port 54325 ssh2
Jan 15 04:20:00 server sshd[1006]: Failed password for root from 192.0.2.1 port 54326 ssh2
```

## Dependencies

- Parser: `crowdsecurity/sshd-logs`
