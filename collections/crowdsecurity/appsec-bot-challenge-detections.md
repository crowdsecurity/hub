# AppSec Bot Challenge — Detections

Checks a fingerprint against the platform the visitor itself claims. Installed by the
[appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundles.

**Scoring** — contributes to the request total, so these can take a submission over the threshold:

 - `appsec-bot-challenge-detect-fonts` — whether the fonts installed match the OS claimed: Segoe UI
   on Windows, Helvetica on Apple, Roboto on Android, each platform's emoji font, and a Linux
   desktop face turning up under a non-Linux claim. A process cannot produce another OS's fonts.
   Also catches advance widths all landing on whole pixels, which no mainstream desktop stack does.
 - `appsec-bot-challenge-detect-codecs` — whether a browser's claimed H.264 playback agrees with its
   own WebRTC codec list, and whether a Firefox claiming Windows or macOS can decode H.264 at all —
   on those it would, through the OS.

**Staged** — scores 0, alert only, never rejects:

 - `appsec-bot-challenge-detect-form-factor` — whether the input stack matches the device claimed: a
   "phone" reporting a mouse and hover is a desktop browser wearing a mobile user agent, and a
   desktop-sized screen with no pointing device at all is a headless one. Also Blink's
   `window.chrome` appearing on iOS, where every browser is WebKit.
 - `appsec-bot-challenge-detect-headers` — whether `Sec-CH-UA-Platform` agrees with the user agent
   string. A UA override that forgot `userAgentMetadata` leaves the platform hint telling the truth.

`appsec-bot-challenge-warn-experimental` raises a `crowdsecurity/suspicious-browser-submission`
alert naming what fired. It carries no remediation, and a rejected submission gets no flag — its
own `request_score_reasons` already lists the staged detections.

Staged rules exist to be validated on real traffic. Once one shows no false positives, promote it
by moving it from the `detect-experimental` category to `detect` and restoring the weight in its
trailing comment.

`appsec-bot-challenge-detect-cpu-arch` is not here — see
[appsec-bot-challenge-detections-extra](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-detections-extra).
