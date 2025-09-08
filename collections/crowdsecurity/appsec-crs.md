# ModSecurity CRS

This collection enables non blocking [OWASP CRS](https://owasp.org/www-project-modsecurity-core-rule-set/): 

> The OWASP CRS is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. It aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts. CRS provides protection against many common attack categories, including SQL Injection, Cross Site Scripting, Local File Inclusion, etc.

 - The OWASP CRS are loaded in [out-of-band](https://app.crowdsec.net/hub/author/crowdsecurity/appsec-configurations/crs). Requests matching CRS rules won't be blocked but will generate alerts.

 - The collection contains a scenario that will [ban IPs that triggers more than 5 rules](https://app.crowdsec.net/hub/author/crowdsecurity/scenarios/crowdsec-appsec-outofband).

This collection intends to offer a balance between risk of false positives and security: Suspicious requests aren't blocked immediately, but repeating offenders will be banned.

## Enabling OWASP CRS

Add the `crowdsecurity/crs` appsec-config to your WAF acquisition:

```yaml
appsec_configs:
 - ...
 - crowdsecurity/crs
labels:
  type: appsec
listen_addr: 127.0.0.1:7422
source: appsec

```

## Restricting generated alerts

You can restrict out-of-band alerts to OWASP CRS, by adding the following `appsec-config`:

```yaml
on_match:
 - filter: IsOutBand == true and len(evt.Appsec.MatchedRules.ByID(980170)) == 0
   apply:
     - CancelAlert()
```

