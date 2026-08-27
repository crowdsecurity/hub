## Description

Detects SSH brute-force attacks that are slower than the standard `crowdsecurity/ssh-slow-bf` scenario and generate only a few failed authentications over many hours.

Uses a leaky bucket with an 18-hour leak rate and capacity of 3. Triggers on the 4th failed authentication attempt from the same IP when the previous events have not leaked enough from the bucket, for example 4 failures over roughly 15 to 18 hours.

Includes a `_user-enum` variant for slow username enumeration over the same period.

**Typical triggering pattern**: 4 failed authentications from the same IP over less than 18 hours.

## Remediation

Ban the attacking IP.

## Example

An attacker targets ISPConfig-related usernames with several hours between attempts:

```
Jan 15 01:00:00 server sshd[1001]: Failed password for ispconfig from 203.0.113.1 port 54321 ssh2
Jan 15 06:00:00 server sshd[1002]: Failed password for admin from 203.0.113.1 port 54322 ssh2
Jan 15 11:00:00 server sshd[1003]: Failed password for webmaster from 203.0.113.1 port 54323 ssh2
Jan 15 16:00:00 server sshd[1004]: Failed password for root from 203.0.113.1 port 54324 ssh2
```

## Dependencies

- Parser: `crowdsecurity/sshd-logs`
