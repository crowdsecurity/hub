# sympa_ww-logs

Parse web service of [Sympa - Mailing List Management Software](https://www.sympa.community/)

and extract these cases:
- Unknown action "xyz"
- Unknown list "xyz"

and fill the meta "evt.Meta.sympa_warn" for scenario processing.

These cases are not present in http_access_log as 404 because Sympa replies with HTTP 200 and an user html error message.

## acquistion examples

 ```yaml
 filenames:
  - /var/log/sympa.log
 labels:
   type: syslog
 ```

 ```yaml
 source: journalctl
 journalctl_filter:
  - "_SYSTEMD_UNIT=wwsympa.service"
 labels:
   type: syslog
 ```
