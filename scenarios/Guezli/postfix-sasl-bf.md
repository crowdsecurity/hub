## Postfix SASL slow / distributed bruteforce

Detects slow or distributed SASL authentication bruteforce attempts against
postfix. Covers all SASL mechanisms parsed by `crowdsecurity/postfix-logs`
(LOGIN, PLAIN, CRAM-MD5, DIGEST-MD5).

The official `crowdsecurity/postfix-spam` scenario is tuned for fast spam waves
(`capacity: 5`, `leakspeed: 10s`). This scenario covers the opposite threat
model: distributed attackers each performing 1-2 SASL auth attempts per hour
across many IPs in a /24, where the fast-pattern bucket leaks faster than it
fills.

Threshold: **3 SASL auth failures from the same IP within ~2h** -> ban.

### Requirements

- `crowdsecurity/postfix-logs` parser (part of the `crowdsecurity/postfix`
  collection)

### Acquisition example

For Mailcow's postfix container:

```yaml
source: docker
container_name:
  - mailcowdockerized-postfix-mailcow-1
labels:
  type: syslog
```

For a standalone postfix with file-based syslog:

```yaml
filenames:
  - /var/log/mail.log
labels:
  type: syslog
```

### Notes

- The `behavior` label is `pop3/imap:bruteforce` because the hub taxonomy has
  no dedicated `smtp:bruteforce` entry. This follows the precedent set by
  `hitech95/email-generic-bf`.
- Companion to `crowdsecurity/postfix-spam`, which catches fast-pattern spam
  waves; this one fills the slow / distributed gap.
- Tuning notes, installer and detailed background:
  https://github.com/Guezli/postfix-sasl-bf
