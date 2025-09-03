# ModSecurity CRS

This collection enables **BLOCKING** [OWASP CRS](https://owasp.org/www-project-modsecurity-core-rule-set/): 

> The OWASP CRS is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. It aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts. CRS provides protection against many common attack categories, including SQL Injection, Cross Site Scripting, Local File Inclusion, etc.

 - Requests triggering CRS rules will be blocked, alert generated.
 - IP get banned after 3 requests blocked (leakspeed 10s)