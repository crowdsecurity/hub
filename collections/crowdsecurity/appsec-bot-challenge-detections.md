# AppSec Bot Challenge — Detections

Checks a fingerprint against the platform the visitor itself claims, adding signals on top of the
ones the engine collects natively. Installed by the
[appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundles.

 - `appsec-bot-challenge-detect-fonts` — whether the fonts installed match the OS claimed.
 - `appsec-bot-challenge-detect-codecs` — whether a browser's claimed H.264 support holds.
 - `appsec-bot-challenge-detect-headers` — whether `Sec-CH-UA-Platform` agrees with the user agent.
 - `appsec-bot-challenge-detect-form-factor` — whether the input stack matches the device claimed.

## Experimental signals

These signals are **experimental**: they are added with a `detect-experimental-*` score category and
a weight of `0`, so they contribute nothing to the request score and can never reject a submission.
`appsec-bot-challenge-warn-experimental` turns them into a
`crowdsecurity/suspicious-browser-submission` alert naming what fired, **with no remediation**.

The point is to validate a signal against real traffic before it is given a weight. A signal that
holds up is promoted: its weight becomes non-zero and its category becomes `detect`.

To tell which state a signal is in on your own install, read the category prefix in an alert's
`score_reasons` — `detect-experimental-fonts:os_font_missing_windows` is still experimental,
`detect:os_font_missing_windows` has been promoted and counts toward your threshold.

`appsec-bot-challenge-detect-cpu-arch` is not here — see
[appsec-bot-challenge-detections-extra](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-detections-extra).
