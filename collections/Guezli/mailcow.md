## Mailcow comprehensive protection

One-command install of a layered Crowdsec stack for [Mailcow](https://mailcow.email/)
running on the host (not inside the Mailcow Docker network). Covers SMTP-AUTH,
IMAP/POP-AUTH, and propagation of Mailcow-internal F2B bans into the local LAPI
so the nftables-bouncer enforces them on Layer 3.

### Installation

```bash
sudo cscli collections install Guezli/mailcow
sudo systemctl reload crowdsec
```

You still need acquisition stanzas that read the relevant container logs
(see below).

### What's inside

**Official Hub coverage (pulled in via `collections:`)**

- `crowdsecurity/postfix` — postfix-logs parser + `postfix-spam`,
  `postfix-helo-rejected`, `postfix-relay-denied`, `postfix-non-smtp-command`
- `crowdsecurity/dovecot` — dovecot-logs parser + `dovecot-spam`

**Slow / distributed / honeypot patterns (mine)**

- `Guezli/postfix-sasl-bf` — slow / distributed SASL bruteforce
  (capacity 2, leakspeed 2h). Companion to `crowdsecurity/postfix-spam`'s
  fast-pattern detection.
- `Guezli/postfix-honeypot-users` — instant-ban for SASL attempts against
  role/admin usernames (`postmaster@`, `admin@`, `info@`, ...).
- `Guezli/mailcow-f2b-bans` (parser) + `Guezli/mailcow-f2b-feed` (scenario)
  — pull Mailcow's internal `netfilter-mailcow` bans into the Crowdsec
  LAPI so they propagate to the host-side bouncer.

**IMAP / POP slow-pattern coverage (third-party)**

- `melite/dovecot-slow-bf` — slow IMAP/POP bruteforce
- `melite/dovecot-time-based-bf` — time-distributed IMAP/POP bruteforce
- `hitech95/mail-generic-bf` — unified mail-auth bruteforce (SMTP+IMAP+POP)

### Acquisition examples

Add the following to `/etc/crowdsec/acquis.d/mailcow.yaml`:

```yaml
# postfix container
source: docker
container_name:
  - mailcowdockerized-postfix-mailcow-1
labels:
  type: syslog
---
# dovecot container
source: docker
container_name:
  - mailcowdockerized-dovecot-mailcow-1
labels:
  type: syslog
---
# netfilter-mailcow container (Mailcow-internal F2B)
source: docker
container_name:
  - mailcowdockerized-netfilter-mailcow-1
labels:
  type: mailcow-f2b
```

### Notes

- Crowdsec runs on the Mailcow **host**, not inside a Mailcow container.
  The host-side nftables-bouncer enforces bans on Layer 3 before they
  reach Mailcow's Docker network.
- `mailcow-f2b-feed` is what makes Crowdsec see SOGo-webmail, rspamd-admin
  and dovecot-cluster bruteforces that Crowdsec out-of-the-box doesn't parse.
- The honeypot user list in `Guezli/postfix-honeypot-users` is customizable
  for your environment — fork the scenario if you legitimately use any of
  the listed addresses for SMTP-AUTH.
- Project home with installer scripts and tuning notes:
  https://github.com/Guezli/postfix-sasl-bf
  https://github.com/Guezli/postfix-honeypot-users
  https://github.com/Guezli/crowdsec-mailcow-f2b-feed
