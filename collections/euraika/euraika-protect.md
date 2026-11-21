Detects and blocks attacks against websites protected by [Euraika Protect](https://docs.protect.euraika.dev):
the `euraika/euraika-protect-logs` parser feeds the generic HTTP scenarios of `crowdsecurity/nginx`
(probing, crawling, brute force, known CVE probes).

Label the acquisition with `type: euraika-protect`. To also patch known CVEs inline, install
`crowdsecurity/appsec-virtual-patching` and point Euraika Protect's `CROWDSEC_APPSEC_URL` at the AppSec component.
