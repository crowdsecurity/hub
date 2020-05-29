The http sqli probing scenario aims at detecting, with very little false positive chances, SQL injection probing attempts.

SQL injection probing attempts will be characterized by the presence of specific SQL-related patterns in uri/GET arguments (if and when this is where the injected parameter is), and this is what this scenario detects.


The [word list](https://raw.githubusercontent.com/crowdsecurity/sec-lists/master/web/sqli_probe_patterns.txt) is picked specifically to limit false positives.
Furthermore, a `distinct` directive is present on the get parameters themselves to reduce false positive chances.

You can test the behavior of the scenario by launching the excellent [sqlmap](https://sqlmap.org) on one of your pages.

**WARNING** This scenario is _not_ a WAF, and this scenario does _not_ aims at replacing a WAF. A motivated attacker with knowledge of crowdsec will be able to bypass it. It is mostly meant to be a way to detect generic SQL injection probing such as performed by open-source or commercial scanners.

