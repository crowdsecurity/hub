# MailScanner Parser & Scenarios for CrowdSec

## Overview

This package integrates [MailScanner](https://www.mailscanner.info/) logs — including those used in the [Email Filter Appliance (E.F.A.)](https://efa-project.org) project — with CrowdSec.  

It provides:

- Two parsers to normalize MailScanner log entries.
- Two scenarios to detect and react to spam messages:
  - Blacklisted senders
  - High-scoring spam (spam_score > 20.0)

These components allow CrowdSec to automatically ban source IPs that MailScanner has already flagged as spammers.

---

## Components

### Parsers
- **`cbrandlehner/mailscanner-spam-blacklist`**
  - Extracts fields such as `source_ip`and `spam_reason`.
  - Sets `evt.Meta.log_type` to value `mailscanner_blacklist`.

- **`cbrandlehner/mailscanner-spam`**
  - Extracts fields such as `source_ip` and `spam_score`.
  - Sets `evt.Meta.log_type` to value `mailscanner_spam`.

### Scenarios
1. **`cbrandlehner/mailscanner-blacklisted`**
   - **Type**: `trigger`
   - Detects when `spam_reason == "blacklisted"`.
   - Immediately raises an alert, grouped by `source_ip`.
   - Labels the behavior as `smtp:spam`.

2. **`cbrandlehner/mailscanner-highscore-spam`**
   - **Type**: `leaky`
   - Detects when `spam_score > 20.0` in MailScanner logs (`evt.Meta.log_type == "mailscanner_spam"`).
   - Uses a leaky bucket: 1 event in 10s is enough to trigger, then silenced for 5m (via `blackhole`).
   - Labels the behavior as `smtp:spam`.

---

## Example Log Lines

```text
Sep 29 04:00:57 efa MailScanner[2129202]: Message 4cZktc2W3sz3bl4 from 85.17.179.32 (akkitbz@cobusan.com.tr) to brandlehner.at is spam (blacklisted)
Sep 29 10:28:25 efa MailScanner[2324063]: Message 4cZvTc05hqz3dT5 from 88.99.6.69 (nr136@rp.news.newsletter2.louis.de) to bechelaren.at is spam, SpamAssassin (nicht zwischen gespeichert, Wertung=11.11, benoetigt 4, BAYES_40 -0.20, DCC_CHECK 1.10, DKIM_SIGNED 0.01, DKIM_VALID -0.10, DMARC_PASS -0.00, HTML_FONT_LOW_CONTRAST 0.50, HTML_MESSAGE 0.00, MIME_HTML_ONLY 0.01, RCVD_IN_DNSWL_NONE -0.01, SPF_HELO_PASS -0.10, SPF_PASS -0.10, ZTL_RECEIVED_IP_LR_V1 10.00, ZTL_RELAYCOUNTRY_NOT_AT 2.50, ZTL_RELAYCOUNTRY_USA_DE_CH -2.50)
