# Description

A simple parser for Pureftpd.

# Logs

  - Error

```
Jan  7 14:19:35 ftpcdr pure-ftpd: (?@172.21.10.2) [WARNING] Authentication failed for user [root]
Jan  7 14:19:36 ftpcdr pure-ftpd: (?@172.21.10.2) [WARNING] Authentication failed for user [root]
```

  - Success

```
Jan  7 14:20:06 ftpcdr pure-ftpd: (?@172.21.10.2) [INFO] user@test.com is now logged in
```

# To be done

  - ?

# Explain output

  - Pureftpd-logs parser is used only for authentication failures.

```
line: Jan  7 14:20:01 ftpcdr pure-ftpd: (?@172.21.10.2) [WARNING] Authentication failed for user [root]
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/pureftpd-logs (+6)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/pureftpd-bf

line: Jan  7 14:20:06 ftpcdr pure-ftpd: (?@172.21.10.2) [INFO] user@test.com is now logged in
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🔴 fulljackz/pureftpd-logs
	└-------- parser failure 🔴

line: Jan  7 14:19:31 ftpcdr pure-ftpd: (?@172.21.10.2) [WARNING] Authentication failed for user [root]
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/pureftpd-logs (+6)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/pureftpd-bf
``` 
