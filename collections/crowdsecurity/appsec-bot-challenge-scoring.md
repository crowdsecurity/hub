# AppSec Bot Challenge — Scoring engine

Part of the [appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundles. It serves the browser-fingerprint challenge and weights each fingerprint mismatch signal into a
request score — strong automation signals like `webdriver` / `cdp` score 100, down to weak signals like
`utc_timezone` scoring 5.

## What it contains

 - [appsec-bot-challenge-scoring](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-scoring)
   — serves the challenge and computes the weighted request score.

On its own it never rejects; it only challenges and scores. Pair it with a threshold config that decides
when a submission is rejected:

 - [appsec-bot-challenge-scoring-strict](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-scoring-strict)
   — reject at score `>= 45`
 - [appsec-bot-challenge-scoring-balanced](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-scoring-balanced)
   — reject at score `>= 75`
 - [appsec-bot-challenge-scoring-permissive](https://app.crowdsec.net/hub/author/crowdsecurity/waf-configurations/appsec-bot-challenge-scoring-permissive)
   — reject at score `>= 100`

## Usage

Most users should install a ready-made bundle
([appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
and its [strict](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-strict) /
[permissive](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-permissive)
variants) which wire this engine to a threshold for you, rather than composing it by hand.
