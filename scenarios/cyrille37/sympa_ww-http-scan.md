# cyrille37/sympa_ww-http-scan

Sympa Web Service scan scenario based on Sympa log parser "cyrille37/sympa_ww-logs".

As Sympa reply HTTP 200 on unexisted files, we cannot detect http scan on http web server logs.

So this "leaky" scenario looks for errors signaled by "sympa_ww-logs" logs parser with meta "evt.Meta.sympa_warn" for blocking source after 1 attempt with a non existing action or list, except for files "robots.txt", "sitemap.xml" and "favicon.ico".
