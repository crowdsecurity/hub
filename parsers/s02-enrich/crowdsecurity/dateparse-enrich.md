Parses timestamp strings in logs to be used in [forensic mode](https://doc.crowdsec.net/Crowdsec/v1/user_guide/forensic_mode/). The following formats are currently supported :

 - RFC3339
 - `02/Jan/2006:15:04:05 -0700`
 - `Mon Jan 2 15:04:05 2006`
 - `02-Jan-2006 15:04:05 europe/paris`
 - `01/02/2006 15:04:05`
 - `2006-01-02 15:04:05.999999999 -0700 MST`
 - `Jan  2 15:04:05`
 - `Mon Jan 02 15:04:05.000000 2006`
 - `2006-01-02T15:04:05Z07:00`
 - `2006/01/02`
 - `2006/01/02 15:04`
 - `2006-01-02`
 - `2006-01-02 15:04`

The `StrTime` item of the event is parsed by default. See [crowdsecurity/syslog-logs](https://hub.crowdsec.net/author/crowdsecurity/configurations/syslog-logs) as an example of a parser setting this field for `crowdsecurity/dateparse-enrich`.
