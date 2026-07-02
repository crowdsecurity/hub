# AppSec Bot Challenge

This collection enables CrowdSec AppSec **challenge mode** for bot detection: visitors are served a
lightweight proof-of-work + browser-fingerprint challenge, and clients flagged as known bots by the
fast bot detection are rejected.

What it ships:

 - `crowdsecurity/appsec-bot-challenge-simple`: challenges incoming requests, skips verified good bots
   and rejects challenge submissions whose fingerprint trips the bot detection.
 - Verified-good-bot datafiles that back the exclusion above, split by family so you can enable only the
   ones you need:
   - `crowdsecurity/appsec-bot-legit-search-engines`: googlebot, bingbot, applebot, amazonbot, yandex,
     baidu, yahoo, sogou, qwant, babbar, duckduckbot
   - `crowdsecurity/appsec-bot-legit-ai-crawlers`: gptbot, openai-searchbot, openai-chatgpt-user,
     perplexitybot
   - `crowdsecurity/appsec-bot-legit-social`: meta, discord, telegram, twitterbot, pinterest
   - `crowdsecurity/appsec-bot-legit-monitoring`: uptimerobot, cookiebot, datadog, pagerduty

   A bot is exempted **only** when it can be network-verified (dns or ip range).
 - Path exclusion configs that let machine-facing or non-navigational requests through without a
   challenge:
   - `appsec-bot-challenge-exclude-crawler-files` — `/robots.txt`, `/.well-known/*`, `/security.txt`, …
   - `appsec-bot-challenge-exclude-feeds` — RSS/Atom feed paths
   - `appsec-bot-challenge-exclude-webhooks` — third-party webhook paths
   - `appsec-bot-challenge-exclude-static` — static assets and media
   - `appsec-bot-challenge-exclude-api` — programmatic endpoints
 - Scenarios that alert on detected bots and on challenge abuse.
 - A user-friendly alert context exposing `fsid`, OS, and the bot signals that fired.

## Enabling bot challenge

Add the `crowdsecurity/appsec-bot-*` appsec-configs to your WAF acquisition, plus any of the
well-known-path exclusion configs you need:

```yaml
appsec_configs:
 - crowdsecurity/appsec-bot-*
labels:
  type: appsec
listen_addr: 127.0.0.1:7422
source: appsec
```
