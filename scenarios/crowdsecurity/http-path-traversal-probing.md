The http path traversal probing scenario aims at detecting, with very little false positive chances, path traversal probing attempts.

Path traversal attempts will be detected with the presence of specific path manipulation patterns in the URI or the `GET` parameter such as `../` , `%2Fetc%2Fpasswd` ...

:warning: This scenario is _not_ a WAF and this scenario does _not_ aims at replacing a WAF.