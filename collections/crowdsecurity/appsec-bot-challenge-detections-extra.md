# AppSec Bot Challenge — Detections (extra)

Detections kept out of the
[appsec-bot-challenge](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge)
bundles because they are considered more experimental.

 - `appsec-bot-challenge-detect-cpu-arch` — reads the processor actually executing from a
   WebAssembly NaN bit pattern and checks it against an iOS or Android claim. Needs
   `wasm-unsafe-eval` in the challenge CSP, and takes a share of the challenge's shared
   client-side time budget away from fonts and codecs.
 - `appsec-bot-challenge-warn-experimental` — the alert policy, listed here as well so this
   collection works on its own.

Experimental like the other unvalidated signals: they are added with a `detect-experimental-*`
category and a weight of 0, so they only raise a `crowdsecurity/suspicious-browser-submission`
alert and never reject. See
[appsec-bot-challenge-detections](https://app.crowdsec.net/hub/author/crowdsecurity/collections/appsec-bot-challenge-detections)
for how a signal gets promoted out of that state.

```bash
cscli collections install crowdsecurity/appsec-bot-challenge-detections-extra
```

The documented `crowdsecurity/appsec-bot-*` wildcard in your AppSec acquisition picks both configs
up in the right order. Listing configs by name instead, `warn-experimental` goes last — after your
threshold config, whose `RejectSubmission` halts every later rule.
