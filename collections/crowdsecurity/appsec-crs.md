# ModSecurity CRS

This collection enables non blocking [OWASP CRS](https://owasp.org/www-project-modsecurity-core-rule-set/): 

> The OWASP CRS is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. It aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts. CRS provides protection against many common attack categories, including SQL Injection, Cross Site Scripting, Local File Inclusion, etc.

 - The OWASP CRS are loaded in [out-of-band](https://app.crowdsec.net/hub/author/crowdsecurity/appsec-configurations/crs). Requests matching CRS rules won't be blocked but will generate alerts.

 - The collection contains a scenario that will [ban IPs that triggers more than 5 rules](https://app.crowdsec.net/hub/author/crowdsecurity/scenarios/crowdsec-appsec-outofband).

This collection intends to offer a balance between risk of false positives and security: Suspicious requests aren't blocked immediately, but repeating offenders will be banned.
