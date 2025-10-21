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
  - Extracts fields such as `source_ip` and `spam_reason`.
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
