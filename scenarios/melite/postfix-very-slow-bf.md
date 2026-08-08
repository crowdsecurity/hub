## Description

Detects very slow Postfix SMTP AUTH brute-force attacks where attackers space SASL authentication attempts ~30+ minutes apart to evade the standard `melite/postfix-slow-bf` scenario (15-minute leak rate).

Uses a leaky bucket with a 4-hour leak rate and capacity of 5, creating a 24-hour detection window. Triggers after 6 failed SASL authentication attempts from the same IP.

Includes a `_user-enum` variant for slow SASL username enumeration.

**Detection window**: 24 hours (leakspeed 4h × 6 events)

## Remediation

Ban the attacking IP.

## Example

An attacker spaces SMTP auth attempts ~45 minutes apart:

```
Jan 15 08:00:00 server postfix/smtpd[1001]: warning: unknown[198.51.100.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 08:45:00 server postfix/smtpd[1002]: warning: unknown[198.51.100.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 09:30:00 server postfix/smtpd[1003]: warning: unknown[198.51.100.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 10:15:00 server postfix/smtpd[1004]: warning: unknown[198.51.100.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 11:00:00 server postfix/smtpd[1005]: warning: unknown[198.51.100.1]: SASL LOGIN authentication failed: authentication failure
Jan 15 11:45:00 server postfix/smtpd[1006]: warning: unknown[198.51.100.1]: SASL LOGIN authentication failed: authentication failure
```

## Dependencies

- Parser: `crowdsecurity/postfix-logs`
