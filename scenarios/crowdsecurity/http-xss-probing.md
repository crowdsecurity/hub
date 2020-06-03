The http XSS probing scenario aims at detecting, with very little false positive chances, XSS probing attempts.

XSS probing attempts will be characterized by the presence of specific XSS related patterns in uri/GET arguments (if and when this is where the injected parameter is), and this is what this scenario detects.


The [word list](https://raw.githubusercontent.com/crowdsecurity/sec-lists/master/web/xss_probe_patterns.txt) is picked specifically to limit false positives.
Furthermore, a `distinct` directive is present on the get parameters themselves to reduce false positive chances.


**WARNING** This scenario is _not_ a WAF, and this scenario does _not_ aims at replacing a WAF. A motivated attacker with knowledge of crowdsec will be able to bypass it. It is mostly meant to be a way to detect generic XSS probing.
