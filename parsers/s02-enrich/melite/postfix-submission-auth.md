## Description

Parses Postfix submission port (587) authentication failures from disconnect log lines.

Standard Postfix parsers (`crowdsecurity/postfix-logs`) don't extract authentication failure information from disconnect lines. When using port 587 with STARTTLS, Postfix does not log explicit "SASL authentication failed" messages. Instead, auth failures only appear as `auth=0/N` in the disconnect summary line.

This parser runs in `s02-enrich` stage (after `crowdsecurity/postfix-logs` parses the line in s01) and extracts the `auth=0/N` pattern, tagging matching lines with `log_type_enh: submission-auth-failed` for use by the `melite/postfix-submission-very-slow-bf` scenario.

**Stage**: `s02-enrich` (requires prior s01-parse by `crowdsecurity/postfix-logs`)

## Example

```
Jan 15 10:30:45 server postfix/submission/smtpd[1234]: disconnect from unknown[192.0.2.1] ehlo=1 auth=0/1 quit=1 commands=2/3
Jan 15 11:00:00 server postfix/submission/smtpd[5678]: disconnect from attacker.example[198.51.100.1] ehlo=2 starttls=1 auth=0/3 quit=1 commands=4/7
```

The parser extracts:
- `auth_failed: 0` (successes)
- `auth_attempts: 1` or `3` (total attempts)
- Tags: `log_type: postfix`, `log_type_enh: submission-auth-failed`

## Dependencies

- Parser: `crowdsecurity/postfix-logs` (s01-parse, must run first)
