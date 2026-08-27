## Description

Parses SSH preauth disconnect lines that the standard `crowdsecurity/sshd-logs` parser misses completely.

Some SSH preauth activity can generate several related log lines:

1. `Disconnected from authenticating user root IP port N [preauth]` → parsed by `crowdsecurity/sshd-logs` ✅
2. `Received disconnect from IP port N:11: [preauth]` → **silently dropped** ❌

This parser captures the second line and tags it as `ssh_preauth-disconnect`. It intentionally uses a distinct log type because a client disconnect before authentication is not, by itself, equivalent to a failed SSH authentication.

**Stage**: `s01-parse` (these lines fail at s01, no standard parser recognizes them)

## Example

```
Jan 15 10:30:45 server sshd-session[4175140]: Received disconnect from 45.227.254.10 port 15948:11:  [preauth]
Jan 15 10:30:46 server sshd[12345]: Received disconnect from 1.2.3.4 port 54321:11: Bye Bye [preauth]
```

Both lines are parsed and tagged with:
- `log_type: ssh_preauth-disconnect`
- `source_ip`: extracted from the log line
- `service: ssh`

## Dependencies

- Parser: `crowdsecurity/syslog-logs` (for initial syslog parsing)
