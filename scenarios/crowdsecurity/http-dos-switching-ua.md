## HTTP DOS Changing User-Agent

This scenario detects specific DoS tools that issue a high number of requests, while changing the `User-Agent` every request.

Directly inspired by some specific DoS tools TTP.

:warning: This scenario might trigger false positives, proper testing is advised :warning:


:warning: The Hub item name is `crowdsecurity/http-dos-switching-ua`, but the internal runtime name is `crowdsecurity/http-dos-swithcing-ua`. The misspelling is kept for compatibility. Use the internal name in local configuration, including `cscli simulation enable`. :warning:
