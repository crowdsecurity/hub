# AppSec Bot Challenge — Path exclusions

Part of the [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundles. It lets machine-facing / non-navigational requests through without a challenge, since clients on
these paths typically cannot solve one.

## What it contains

Per-purpose path exclusion configs:

 - [appsec-bot-challenge-exclude-crawler-files](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-crawler-files)
   — `/robots.txt`, `/.well-known/*`, `/security.txt`, `/sitemap.xml`, …
 - [appsec-bot-challenge-exclude-static](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-static)
   — static assets and media (css, js, images, fonts, video, audio)
 - [appsec-bot-challenge-exclude-api](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-api)
   — programmatic endpoints (`/api/`, `/graphql`, `/wp-json/`, `/oauth/`, …)
 - [appsec-bot-challenge-exclude-feeds](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-feeds)
   — RSS/Atom feed paths
 - [appsec-bot-challenge-exclude-webhooks](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-exclude-webhooks)
   — third-party webhook paths (`/webhooks/`)

## Usage

Installed automatically by the [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundle and its [strict](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-strict) /
[permissive](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-permissive) variants.
Install it on its own to add just these exemptions, or enable individual configs if you don't want them all.
