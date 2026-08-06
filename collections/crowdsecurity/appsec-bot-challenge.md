# AppSec Bot Challenge

This collection enables CrowdSec AppSec **challenge mode** for bot detection: visitors are served a
lightweight proof-of-work + browser-fingerprint challenge, and clients flagged as known bots by the
fast bot detection are rejected.

What it ships:

 - `crowdsecurity/simple-bot-challenge`: challenges incoming requests, skips verified good bots
   (forward-confirmed rDNS), and rejects challenge submissions whose fingerprint trips the fast bot
   detection.
 - Well-known-path exclusion configs (`challenge-exclude-crawler-files`, `-feeds`, `-webhooks`) that
   let machine-facing endpoints (`/robots.txt`, `/.well-known/*`, feeds, webhooks) through without a
   challenge. The exclusion is strictly per-request and is never persisted to a cookie or across
   requests, so it cannot be abused to whitelist a session for other paths.
 - A dedicated bot-detection parser tracking the fingerprint session id (`fsid`) and OS.
 - Scenarios that alert on detected bots and on challenge abuse.
 - A user-friendly alert context exposing `fsid`, OS, and the bot signals that fired.

## Enabling bot challenge

Add the `crowdsecurity/simple-bot-challenge` appsec-config to your WAF acquisition, plus any of the
well-known-path exclusion configs you need:

```yaml
appsec_configs:
 - crowdsecurity/simple-bot-challenge
 - crowdsecurity/challenge-exclude-crawler-files
 - crowdsecurity/challenge-exclude-feeds
 - crowdsecurity/challenge-exclude-webhooks
labels:
  type: appsec
listen_addr: 127.0.0.1:7422
source: appsec
```
