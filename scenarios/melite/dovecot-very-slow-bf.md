## Description

Detects very slow Dovecot brute-force attacks where attackers space POP3/IMAP login attempts more than 1 hour apart to evade the `melite/dovecot-slow-bf` scenario.

Uses a leaky bucket with a 12-hour leak rate and capacity of 6, creating an 84-hour (~3.5 day) detection window. Triggers after 7 failed authentication attempts from the same IP.

At 1 attempt/hour, the `dovecot-slow-bf` bucket (4h leak) never fills because it leaks faster than events arrive. This scenario uses a 12-hour leak to catch these slower attackers.

Includes a `_user-enum` variant for very slow Dovecot username enumeration.

**Detection window**: 84 hours / ~3.5 days (leakspeed 12h × 7 events)

## Remediation

Ban the attacking IP.

## Example

An attacker spaces Dovecot login attempts ~6 hours apart over 3 days:

```
Jan 15 00:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<aaa111>
Jan 15 06:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<info@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<bbb222>
Jan 15 12:00:00 server dovecot: pop3-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<ccc333>
Jan 15 18:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<webmaster@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<ddd444>
Jan 16 00:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<root@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<eee555>
Jan 16 06:00:00 server dovecot: imap-login: Disconnected (auth failed, 1 attempts): user=<test@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<fff666>
Jan 16 12:00:00 server dovecot: pop3-login: Disconnected (auth failed, 1 attempts): user=<admin@example.com>, method=PLAIN, rip=198.51.100.1, lip=10.0.0.1, TLS, session=<ggg777>
```

## Dependencies

- Parser: `crowdsecurity/dovecot-logs`
