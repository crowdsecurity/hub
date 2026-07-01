# AppSec Bot Challenge

This collection enables CrowdSec AppSec **challenge mode** for bot detection: visitors are served a
lightweight proof-of-work + browser-fingerprint challenge, and clients flagged as known bots by the
fast bot detection are rejected.

What it ships:

 - `crowdsecurity/appsec-bot-challenge-simple`: challenges incoming requests, skips verified good bots
   (forward-confirmed rDNS), and rejects challenge submissions whose fingerprint trips the fast bot
   detection.
 - Verified-good-bot datafiles that back the exclusion above, split by family so you can enable only the
   ones you need:
   - `crowdsecurity/appsec-bot-legit-search-engines`: googlebot, bingbot, applebot, amazonbot, yandex,
     baidu, yahoo, sogou, qwant, babbar, duckduckbot
   - `crowdsecurity/appsec-bot-legit-ai-crawlers`: gptbot, openai-searchbot, openai-chatgpt-user,
     perplexitybot
   - `crowdsecurity/appsec-bot-legit-social`: meta, discord, telegram, twitterbot, pinterest
   - `crowdsecurity/appsec-bot-legit-monitoring`: uptimerobot, cookiebot

   A bot is exempted **only** when it can be network-verified — forward-confirmed rDNS or a published IP
   range. User-Agent-only bots (e.g. CommonCrawl/CCBot) are intentionally left challenged, since a
   spoofed User-Agent must not bypass the challenge.
 - Well-known-path exclusion configs (`appsec-bot-challenge-exclude-crawler-files`, `-feeds`, `-webhooks`) that
   let machine-facing endpoints (`/robots.txt`, `/.well-known/*`, feeds, webhooks) through without a
   challenge. The exclusion is strictly per-request and is never persisted to a cookie or across
   requests, so it cannot be abused to whitelist a session for other paths.
 - A dedicated bot-detection parser tracking the fingerprint session id (`fsid`) and OS.
 - Scenarios that alert on detected bots and on challenge abuse.
 - A user-friendly alert context exposing `fsid`, OS, and the bot signals that fired.

## Enabling bot challenge

Add the `crowdsecurity/appsec-bot-challenge-simple` appsec-config to your WAF acquisition, plus any of the
well-known-path exclusion configs you need:

```yaml
appsec_configs:
 - crowdsecurity/appsec-bot-challenge-simple
 - crowdsecurity/appsec-bot-challenge-exclude-crawler-files
 - crowdsecurity/appsec-bot-challenge-exclude-feeds
 - crowdsecurity/appsec-bot-challenge-exclude-webhooks
labels:
  type: appsec
listen_addr: 127.0.0.1:7422
source: appsec
```
