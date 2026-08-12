# AppSec Bot Challenge (strict)

Strict variant of [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge).
Same scoring engine and exclusions, but rejects challenge submissions scoring `>= 45` — it **catches more bots** than the
balanced default at the cost of more **potential false positives**. Use it when bot pressure matters more than the
occasional wrongly-challenged visitor.

For less strict options, see:
 - [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge) (`>= 75`)
 - [appsec-bot-challenge-permissive](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-permissive) (`>= 100`).

## What it contains

**Sub-collections:**

 - [appsec-bot-challenge-scoring](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-scoring)
   — the scoring engine: serves the challenge and weights fingerprint signals into a request score.
 - [appsec-bot-challenge-good-bots](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-good-bots)
   — exempts network-verified good bots (search engines, AI crawlers, social, monitoring).
 - [appsec-bot-challenge-exclude-paths](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-exclude-paths)
   — exempts machine-facing paths (crawler files, static assets, API, feeds, webhooks).

**Threshold config:**

 - [appsec-bot-challenge-scoring-strict](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-scoring-strict)
   — rejects submissions scoring `>= 45`.

**Scenarios** (alert on challenge abuse):

 - [appsec-bot-challenge-too-many-requests](https://app.crowdsec.net/hub/author/crowdsecurity/scenarios/appsec-bot-challenge-too-many-requests)
 - [appsec-bot-challenge-too-many-submissions](https://app.crowdsec.net/hub/author/crowdsecurity/scenarios/appsec-bot-challenge-too-many-submissions)

**Parsers:**

 - [appsec-logs](https://app.crowdsec.net/hub/author/crowdsecurity/log-parsers/appsec-logs)
 - [appsec-bot-detection-logs](https://app.crowdsec.net/hub/author/crowdsecurity/log-parsers/appsec-bot-detection-logs)

**Contexts** (enrich alerts with `fsid`, OS, and the bot signals that fired):

 - [appsec_base](https://app.crowdsec.net/hub/author/crowdsecurity/configurations/appsec_base)
 - [appsec-bot-detection](https://app.crowdsec.net/hub/author/crowdsecurity/configurations/appsec-bot-detection)

See [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
for setup and WAF acquisition details.
