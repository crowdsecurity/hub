## Axigen collection

Adds CrowdSec support for the Axigen mail server. The collection includes the
native-log parser and scenarios for authentication brute force, account
enumeration, native WebMail login brute force, suspicious SMTP probes, TLS
scanner behavior, and connection floods.

### Acquisition

```yaml
filenames:
  - /var/opt/axigen/log/everything.txt
labels:
  type: axigen
```

If custom log collection rules split services into separate files, add every
configured file to `filenames`. The default working directory is
`/var/opt/axigen/` on Linux and `/axigen/var/` in the Axigen container. The
`type: axigen` label is required.

See the [Axigen working directory documentation](https://www.axigen.com/documentation/axigen-working-directory-p47120596)
and [log collection rule documentation](https://www.axigen.com/documentation/log-collection-rules-p1373442843).

The TLS scenario is deliberately conservative: it requires three distinct TLS
failure types from one address within the bucket window. Repeated instances of
one failure type, which can be caused by a misconfigured legitimate client, do
not trigger it.
