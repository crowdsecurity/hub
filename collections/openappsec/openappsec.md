## Open-appsec collection

A collection for open-appsec that allow to ban IPs that made requests that open-appsec blocked in the waf.
This collection handle most of the `waapIncidentType` that open-appsec can generate.
 - `SQL Injection`
 - `Path Traversal`
 - `LDAP Injection`
 - `Remote Code Execution`
 - `Vulnerability Scanning`
 - `Cross Site Scripting`


## Acquisition template

Example acquisition for this collection :

```yaml
source: file
filenames:
  - /var/log/nano_agent/cp-nano-http-transaction-handler.log*
labels:
  type: openappsec
```