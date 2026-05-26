## Mailcow F2B cross-layer ban feed

Propagates **Mailcow's internal F2B bans** into the local Crowdsec LAPI, so
the host-side nftables-bouncer (and any other Crowdsec consumer) sees
and acts on bans that Mailcow detects but Crowdsec wouldn't catch by itself.

### Why this exists

Mailcow ships its own Fail2Ban-equivalent (`netfilter-mailcow`) which subscribes
to a Redis channel populated by SOGo, dovecot, postfix, the Mailcow admin UI
and rspamd. It implements iptables-level bans inside Mailcow's Docker network.

The catch: those bans live **only** in Mailcow's container network. They never
reach Crowdsec, so:

- The host-side **nftables-bouncer** doesn't know about them.
- They aren't logged as **Crowdsec alerts**, so cross-instance sharing,
  CAPI propagation and unified alerting (Loki, Gotify, etc.) miss them.
- A SOGo-webmail bruteforce -- which Crowdsec out-of-the-box doesn't parse --
  gets banned by Mailcow only at the Docker network level, while the
  bruteforcer can keep hitting other host-level services.

This scenario closes the gap. It triggers on each parsed Mailcow-F2B
ban line and produces a Crowdsec LAPI decision for the banned IP.

### Requirements

- Companion parser `Guezli/mailcow-f2b-bans` (provided in the same PR)
- Acquisition of the `netfilter-mailcow` Docker container's stdout

### Acquisition example

```yaml
source: docker
container_name:
  - mailcowdockerized-netfilter-mailcow-1
labels:
  type: mailcow-f2b
```

### Notes

- The `behavior` label is `generic:bruteforce` because the underlying ban can
  come from any of the layers Mailcow's F2B watches (SMTP, IMAP, webmail UI,
  admin UI, rspamd UI), not just one specific protocol.
- `blackhole: 1h` prevents bucket spam from repeated ban-renew lines on the
  same IP within an hour -- the actual Crowdsec decision lifetime is set by
  your profile, not by `blackhole`.
- Trigger-style on purpose: Mailcow already did the threshold detection,
  this scenario just propagates the verdict.
- Project repository with installer and detailed background:
  https://github.com/Guezli/crowdsec-mailcow-f2b-feed
