## Description

Parse Postfix submission port (587) authentication failures from disconnect log lines.

When using STARTTLS on port 587, Postfix does **not** log explicit "SASL authentication failed" messages. Auth failures only appear as `auth=0/N` in disconnect summary lines, which standard parsers (`crowdsecurity/postfix-logs`) do not match.

This parser runs in **s01-parse** because `crowdsecurity/postfix-logs` does not parse disconnect lines at all — they would be dropped before reaching s02-enrich.

## Detected Pattern

```
postfix/submission/smtpd[PID]: disconnect from host[IP] ehlo=1 auth=0/1 quit=1 commands=2/3
```

The `auth=0/N` pattern indicates N authentication attempts with 0 successes.

## Metadata Set

- `log_type`: `postfix`
- `log_type_enh`: `submission-auth-failed`
- `source_ip`: extracted from the disconnect line

## Remediation

Used by `melite/postfix-submission-very-slow-bf` scenario to detect evasive brute-force attacks on port 587.

## Example

```
Jan 15 10:00:00 mail postfix/submission/smtpd[1234]: disconnect from unknown[203.0.113.1] ehlo=1 auth=0/1 quit=1 commands=2/3
```

## Dependencies

- `crowdsecurity/syslog-logs` (s00-raw)
- `crowdsecurity/dateparse-enrich` (s02-enrich, for timestamp parsing)
