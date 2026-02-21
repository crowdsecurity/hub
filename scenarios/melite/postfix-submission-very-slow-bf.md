## Description

Detects very slow brute-force attacks on the Postfix submission port (587). These attacks are invisible to standard Postfix scenarios because port 587 with STARTTLS does not log explicit "SASL authentication failed" messages — failures only appear as `auth=0/N` in disconnect lines.

Uses a leaky bucket with a 4-hour leak rate and capacity of 5, creating a 24-hour detection window. Triggers after 6 failed submission auth attempts from the same IP.

**Requires** the `melite/postfix-submission-auth` parser (s02-enrich) to extract auth failure information from disconnect lines.

**Detection window**: 24 hours (leakspeed 4h × 6 events)

## Remediation

Ban the attacking IP.

## Example

An attacker targets the submission port with STARTTLS, auth failures only visible in disconnect lines:

```
Jan 15 10:00:00 server postfix/submission/smtpd[1001]: disconnect from unknown[192.0.2.1] ehlo=1 auth=0/1 quit=1 commands=2/3
Jan 15 11:30:00 server postfix/submission/smtpd[1002]: disconnect from unknown[192.0.2.1] ehlo=1 auth=0/2 quit=1 commands=2/4
Jan 15 13:00:00 server postfix/submission/smtpd[1003]: disconnect from unknown[192.0.2.1] ehlo=1 auth=0/1 quit=1 commands=2/3
Jan 15 14:30:00 server postfix/submission/smtpd[1004]: disconnect from unknown[192.0.2.1] ehlo=1 auth=0/1 quit=1 commands=2/3
Jan 15 16:00:00 server postfix/submission/smtpd[1005]: disconnect from unknown[192.0.2.1] ehlo=1 auth=0/3 quit=1 commands=2/5
Jan 15 17:30:00 server postfix/submission/smtpd[1006]: disconnect from unknown[192.0.2.1] ehlo=1 auth=0/1 quit=1 commands=2/3
```

## Dependencies

- Parser: `crowdsecurity/postfix-logs` (s01-parse)
- Parser: `melite/postfix-submission-auth` (s02-enrich, **required**)
