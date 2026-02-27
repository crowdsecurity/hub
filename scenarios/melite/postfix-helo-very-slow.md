## Description

Detects evasive spammers sending invalid HELO/EHLO commands at a rate of less than 1 attempt per hour. The standard `crowdsecurity/postfix-helo-rejected` scenario has only a ~10-minute detection window, allowing patient spammers to fly under the radar.

Uses a leaky bucket with a 4-hour leak rate and capacity of 5, creating a 24-hour detection window. Triggers after 6 HELO rejections from the same IP.

**Note**: Unlike brute-force scenarios, `reprocess` is set to `false` since HELO rejections are a spam indicator, not credential attacks.

**Detection window**: 24 hours (leakspeed 4h × 6 events)

## Remediation

Ban the attacking IP.

## Example

A spammer sends invalid HELO commands ~70 minutes apart to avoid detection:

```
Jan 15 08:00:00 server postfix/smtpd[1001]: NOQUEUE: reject: RCPT from unknown[203.0.113.1]: 504 5.5.2 <invalid>: Helo command rejected: need fully-qualified hostname; from=<sender@spam.example> to=<user@example.com>
Jan 15 09:10:00 server postfix/smtpd[1002]: NOQUEUE: reject: RCPT from unknown[203.0.113.1]: 504 5.5.2 <invalid>: Helo command rejected: need fully-qualified hostname; from=<sender2@spam.example> to=<user2@example.com>
Jan 15 10:20:00 server postfix/smtpd[1003]: NOQUEUE: reject: RCPT from unknown[203.0.113.1]: 504 5.5.2 <invalid>: Helo command rejected: need fully-qualified hostname; from=<sender3@spam.example> to=<user3@example.com>
Jan 15 11:30:00 server postfix/smtpd[1004]: NOQUEUE: reject: RCPT from unknown[203.0.113.1]: 504 5.5.2 <invalid>: Helo command rejected: need fully-qualified hostname; from=<sender4@spam.example> to=<user4@example.com>
Jan 15 12:40:00 server postfix/smtpd[1005]: NOQUEUE: reject: RCPT from unknown[203.0.113.1]: 504 5.5.2 <invalid>: Helo command rejected: need fully-qualified hostname; from=<sender5@spam.example> to=<user5@example.com>
Jan 15 13:50:00 server postfix/smtpd[1006]: NOQUEUE: reject: RCPT from unknown[203.0.113.1]: 504 5.5.2 <invalid>: Helo command rejected: need fully-qualified hostname; from=<sender6@spam.example> to=<user6@example.com>
```

## Dependencies

- Parser: `crowdsecurity/postfix-logs`
