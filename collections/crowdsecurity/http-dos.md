## Detecting HTTP DOS

This collection of scenarios detects specific HTTP DoS tools that are not detected by default HTTP scenarios.

To work correctly, it requires the associated HTTP collection of your webserver to be present, such as [nginx](https://hub.crowdsec.net/author/crowdsecurity/collections/nginx) or [apache2](https://hub.crowdsec.net/author/crowdsecurity/collections/apache2).

Given the very nature of the scenarios, proper testing is advised to avoid false-positives:

 - By [replaying "cold" logs](https://doc.crowdsec.net/docs/next/user_guides/replay_mode) to ensure no false-positives are present
 - By setting the scenarios in ["simulation mode"](https://doc.crowdsec.net/docs/next/cscli/cscli_simulation/) for observability

