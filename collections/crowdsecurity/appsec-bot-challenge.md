# AppSec Bot Challenge

Enables CrowdSec AppSec **challenge mode** for bot detection: visitors are served a lightweight
proof-of-work + browser-fingerprint challenge, each fingerprint mismatch signal adds a weighted score, and
submissions scoring **`>= 75`** (the balanced threshold) are rejected.

This is the recommended default. Two variants share the same scoring engine and exclusions, differing only
in the rejection threshold:

 - [appsec-bot-challenge-strict](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-strict)
   — rejects at `>= 45` (catches more bots, more false positives)
 - [appsec-bot-challenge-permissive](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-permissive)
   — rejects at `>= 100` (near-certain automation only)

## What it contains

**Sub-collections:**

 - [appsec-bot-challenge-scoring](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-scoring)
   — the scoring engine: serves the challenge and weights fingerprint signals into a request score.
 - [appsec-bot-challenge-good-bots](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-good-bots)
   — exempts network-verified good bots (search engines, AI crawlers, social, monitoring).
 - [appsec-bot-challenge-exclude-paths](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-exclude-paths)
   — exempts machine-facing paths (crawler files, static assets, API, feeds, webhooks).

**Threshold config:**

 - [appsec-bot-challenge-scoring-balanced](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-scoring-balanced)
   — rejects submissions scoring `>= 75`.

**Scenarios** (alert on challenge abuse):

 - [appsec-bot-challenge-too-many-requests](https://app.crowdsec.net/hub/author/crowdsecurity/scenarios/appsec-bot-challenge-too-many-requests)
 - [appsec-bot-challenge-too-many-submissions](https://app.crowdsec.net/hub/author/crowdsecurity/scenarios/appsec-bot-challenge-too-many-submissions)

**Parsers:**

 - [appsec-logs](https://app.crowdsec.net/hub/author/crowdsecurity/log-parsers/appsec-logs)
 - [appsec-bot-detection-logs](https://app.crowdsec.net/hub/author/crowdsecurity/log-parsers/appsec-bot-detection-logs)

**Contexts** (enrich alerts with `fsid`, OS, and the bot signals that fired):

 - [appsec_base](https://app.crowdsec.net/hub/author/crowdsecurity/configurations/appsec_base)
 - [appsec-bot-detection](https://app.crowdsec.net/hub/author/crowdsecurity/configurations/appsec-bot-detection)

## Tuning

To change restrictiveness, install a variant above, or swap the bundled threshold config for one of the
standalone `appsec-bot-challenge-scoring-{balanced,strict,permissive}` configs.

## Enabling bot challenge

Add the `crowdsecurity/appsec-bot-*` appsec-configs to your WAF acquisition:

```yaml
appsec_configs:
 - crowdsecurity/appsec-bot-*
labels:
  type: appsec
listen_addr: 127.0.0.1:7422
source: appsec
```
