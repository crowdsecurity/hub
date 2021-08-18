A generic parser for nginx, support both access and error logs.
This parser support also ingress nginx controller default [log_format](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/log-format/)


*note : * If you are aggregating logs from several domains, prefix your logline with the target FQDN. HTTP based scenarios should take this into account so that buckets are _per_ source IP per target FQDN, limiting false positives due to logs multiplexing.

