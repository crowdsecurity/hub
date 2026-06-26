## Description

Parses SSH preauth disconnect lines that the standard `crowdsecurity/sshd-logs` parser misses completely.

Each SSH key-scanning attempt generates **two** log lines:

1. `Disconnected from authenticating user root IP port N [preauth]` → parsed by `crowdsecurity/sshd-logs` ✅
2. `Received disconnect from IP port N:11: [preauth]` → **silently dropped** ❌

This parser captures the second line and tags it as `ssh_failed-auth`, effectively doubling the event count for all SSH brute-force scenarios. This makes detection faster and more reliable, especially for slow brute-force scenarios where every event matters.

**Stage**: `s01-parse` (these lines fail at s01, no standard parser recognizes them)

## Example

```
Jan 15 10:30:45 server sshd-session[4175140]: Received disconnect from 45.227.254.10 port 15948:11:  [preauth]
Jan 15 10:30:46 server sshd[12345]: Received disconnect from 1.2.3.4 port 54321:11: Bye Bye [preauth]
```

Both lines are parsed and tagged with:
- `log_type: ssh_failed-auth`
- `source_ip`: extracted from the log line
- `service: ssh`

## Dependencies

- Parser: `crowdsecurity/syslog-logs` (for initial syslog parsing)
