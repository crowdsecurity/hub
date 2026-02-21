## Description

Detects slow Postfix SMTP AUTH brute-force attacks where distributed botnets or patient attackers test SASL credentials with 2-5 minute intervals on port 25.

Uses a leaky bucket with a 15-minute (900s) leak rate and capacity of 7, creating a 2-hour detection window. Triggers after 8 failed SASL authentication attempts from the same IP.

Includes a `_user-enum` variant that triggers when the same IP tries different SASL usernames.

**Detection window**: 2 hours (leakspeed 900s × 8 events)

## Remediation

Ban the attacking IP.

## Example

A distributed botnet tests SMTP credentials with 2-5 minute intervals:

```
Jan 15 10:00:00 server postfix/smtpd[1001]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:03:00 server postfix/smtpd[1002]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:06:00 server postfix/smtpd[1003]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:10:00 server postfix/smtpd[1004]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:14:00 server postfix/smtpd[1005]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:18:00 server postfix/smtpd[1006]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:22:00 server postfix/smtpd[1007]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:26:00 server postfix/smtpd[1008]: warning: unknown[192.0.2.1]: SASL LOGIN authentication failed: authentication failure
```

## Dependencies

- Parser: `crowdsecurity/postfix-logs`
