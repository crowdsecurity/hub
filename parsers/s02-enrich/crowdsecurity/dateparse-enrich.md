Parses timestamp strings in logs to be used in [forensic mode](https://doc.crowdsec.net/Crowdsec/v1/user_guide/forensic_mode/). The parser supports the following formats :

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

If a date layout is present in the `StrTimeFormat` field of the event, it will take precedence over the list above. The date layout must be ([valid in the golang's `time.Parse` layout format](https://pkg.go.dev/time#Parse)). This allows a parser to indicate the date format so that it can be parsed later.


The `StrTime` item of the event is parsed by default. See [crowdsecurity/syslog-logs](https://hub.crowdsec.net/author/crowdsecurity/configurations/syslog-logs) as an example of a parser setting this field for `crowdsecurity/dateparse-enrich`.
