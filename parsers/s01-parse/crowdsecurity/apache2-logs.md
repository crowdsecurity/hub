This apache2 parser support access and error logs in the HTTPD COMBINED LOG standard format, with the following possible modifications :
 - An optional IP or FQDN can be present as the first element of line, and will be stored in `target_fqdn`. This is meant for multi-tenant / aggregated logs.
 - `referrer` and `user_agent` have been made optional for more epurated logging formats


*note :* If you are aggregating logs from several domains, prefix your logline with the target FQDN. HTTP based scenarios should take this into account so that buckets are _per_ source IP per target FQDN, limiting false positives due to logs multiplexing.
