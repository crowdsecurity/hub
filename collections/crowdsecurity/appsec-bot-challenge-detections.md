# AppSec Bot Challenge — Detections

Checks a fingerprint against the platform the visitor itself claims. Installed by the
[appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundles.

**Scoring** — contributes to the request total, so these can take a submission over the threshold:

 - `appsec-bot-challenge-detect-fonts` : whether the fonts installed match the OS claimed.
 - `appsec-bot-challenge-detect-codecs` : whether a browser's claimed H.264 hold.

**Staged** — scores 0, alert only, never rejects:

 - `appsec-bot-challenge-detect-form-factor` : whether the input stack matches the device claimed.
 - `appsec-bot-challenge-detect-headers` : whether `Sec-CH-UA-Platform` agrees with the user agent.

`appsec-bot-challenge-warn-experimental` raises a `crowdsecurity/suspicious-browser-submission`
alert naming what fired **but carries no remediation**.

Staged rules exist to be validated on real traffic before being promoted to main detection rules.

`appsec-bot-challenge-detect-cpu-arch` is not here — see
[appsec-bot-challenge-detections-extra](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-detections-extra).
