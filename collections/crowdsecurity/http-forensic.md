## HTTP Forensic

This collection is intended to be used while replaying logs.

It includes rules that detect exploitation attempts of known vulnerabilities, along with generic SQL injection and XSS attacks.

Unlike the main HTTP scenarios, which generally cover a broad range of traffic patterns, this collection specifically targets requests that resulted in a 200 OK response—i.e., cases where the server appeared to accept the request successfully. This makes it especially useful for spotting attacks that may have bypassed protections or gone unnoticed in normal traffic.

The collection does not ship any log parser directly, make sure the parser for your webserver (such as [nginx](https://hub.crowdsec.net/author/crowdsecurity/collections/nginx) or [apache2](https://hub.crowdsec.net/author/crowdsecurity/collections/apache2).) is installed.

