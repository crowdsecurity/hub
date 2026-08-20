# AppSec Bot Challenge — Good bots

Part of the [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundles. It exempts **network-verified** good bots from the challenge — a bot is exempted only when it can
be verified by dns or ip range, so a spoofed user-agent alone is never enough.

## What it contains

Per-family exclusion configs (each declares its datafiles and exempts the matching bots):

 - [appsec-bot-challenge-exclude-search-engines](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-search-engines)
   — googlebot, bingbot, applebot, amazonbot, yandex, baidu, yahoo, sogou, qwant, babbar, duckduckbot
 - [appsec-bot-challenge-exclude-ai-crawlers](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-ai-crawlers)
   — gptbot, openai-searchbot, openai-chatgpt-user, perplexitybot
 - [appsec-bot-challenge-exclude-social](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-social)
   — meta, discord, telegram, twitterbot, pinterest
 - [appsec-bot-challenge-exclude-monitoring](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-monitoring)
   — uptimerobot, cookiebot, datadog, pagerduty

## Usage

Installed automatically by the [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundle and its [strict](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-strict) /
[permissive](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-permissive) variants.
Install it on its own to add just these exemptions, or enable individual family configs if you don't want
them all.
