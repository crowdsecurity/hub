## Axigen log parser

Parses native Axigen mail server logs and correlates authentication messages
with the remote address recorded when the session was accepted. It supports
SMTP, IMAP, POP3 and WebMail service logs.

Extracted events include connection attempts, authentication failures and
successes, native WebMail login results, SMTP EHLO/SPF probes, TLS alerts, and
session closures. WebMail request events are correlated with the public remote
address through Axigen's session identifier.

### Acquisition example

```yaml
filenames:
  - /var/opt/axigen/log/everything.txt
labels:
  type: axigen
```

Axigen collection rules can write services to separate files. Add those files
to `filenames` when using custom rules. The default working directory is
`/var/opt/axigen/` on Linux and `/axigen/var/` in the Axigen container. Keep
the `type: axigen` label because it selects this parser.

See the [Axigen working directory documentation](https://www.axigen.com/documentation/axigen-working-directory-p47120596)
and [log collection rule documentation](https://www.axigen.com/documentation/log-collection-rules-p1373442843).

The session-to-IP cache has a ten-minute TTL. Authentication messages without
a preceding connection line in that interval are parsed but cannot be used by
IP-based scenarios.
