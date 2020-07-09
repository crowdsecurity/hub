This apache2 parser support access and error logs in the HTTPD COMBINED LOG standard format.

*note : * If you are aggregating logs from several domains, prefix your logline with the target FQDN. HTTP based scenarios should take this into account so that buckets are _per_ source IP per target FQDN, limiting false positives due to logs multiplexing.
