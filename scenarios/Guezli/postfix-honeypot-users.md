## Postfix SASL honeypot-username instant ban

Instant-bans IPs that try postfix SASL authentication with a honeypot
username -- addresses that should never be used as actual SMTP-AUTH login
accounts. The wordlist covers four classes:

**Classic English role addresses:** `postmaster@`, `admin@`, `info@`,
`test@`, `support@`, `office@`, `sales@`, `contact@`, `webmaster@`,
`root@`, `noreply@`, `abuse@`, `hostmaster@`, `marketing@`, `mail@`,
`news@`, `sysadmin@`, `administrator@`, `user@`, `service@`, `helpdesk@`.

**Spanish / Portuguese i18n variants** (frequently seen in real-world
bot wordlists): `teste@`, `prueba@`, `contacto@`, `comercial@`.

**Accounting / billing role honeypots:** `billing@`, `accounts@`,
`account@`, `tech@`, `reception@`, `shared@`.

**Office-equipment honeypots:** `copier@`, `fax@`, `scanner@`,
`monitor@`, `mailtest@`, `testing@`.

**Auto-generated mailbox-probe patterns:** `nonexistent_user@`,
`nonexistent_user_<N>@` (where `<N>` is any digit sequence -- catches
stealth bots that probe with numbered test mailboxes).

The filter matches any SASL mechanism (LOGIN, PLAIN, CRAM-MD5, DIGEST-MD5)
parsed by `crowdsecurity/postfix-logs` -- attackers using PLAIN against
role-only addresses are just as much a clear signal as LOGIN.

### Why this complements other postfix scenarios

Distributed bruteforce bots iterate through a standard wordlist of role
addresses, making only 1-2 attempts per IP to stay below per-IP rate
thresholds. They escape:

- `crowdsecurity/postfix-spam` (capacity 5 / leakspeed 10s -- 6+ fast fails)
- `Guezli/postfix-sasl-bf` (capacity 2 / leakspeed 7200s -- 3+ fails per IP)

Since no legitimate mail setup logs in via SMTP with `postmaster@` or
`admin@`, a single attempt with such a username is high-confidence
attacker signal -- ban immediately (`type: trigger`, `confidence: 5`).

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

- The `behavior` label is `pop3/imap:bruteforce` because the hub taxonomy
  has no dedicated `smtp:bruteforce` entry. Same convention as the
  companion scenario `Guezli/postfix-sasl-bf`.
- Customize the honeypot username list to your environment: if you
  legitimately accept SASL-AUTH for any of the addresses above, fork the
  scenario and remove the matching entries from the filter regex.
- Tuning notes, installer and detailed background:
  https://github.com/Guezli/postfix-honeypot-users
