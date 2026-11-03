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

Staged like the other unvalidated detections: the rules score 0 and only raise a
`crowdsecurity/suspicious-browser-submission` alert.

```bash
cscli collections install crowdsecurity/appsec-bot-challenge-detections-extra
```

The documented `crowdsecurity/appsec-bot-*` wildcard in your AppSec acquisition picks both configs
up in the right order. Listing configs by name instead, `warn-experimental` goes last — after your
threshold config, whose `RejectSubmission` halts every later rule.
