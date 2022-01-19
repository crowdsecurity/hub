# Description

A simple parser for Proxmox VE Web interface.
Proxmox VE is listening on port 8006/tcp and write ssh fails into syslog 

# Logs

  - Error

```
Jan  4 17:34:08 hypervisor pvedaemon[3663339]: authentication failure; rhost=::ffff:172.21.10.2 user=toor@pam msg=no such user ('toor@pam')
Jan  4 17:34:22 hypervisor pvedaemon[3483744]: authentication failure; rhost=::ffff:172.21.10.2 user=root@pam msg=Authentication failure
```

> In the first string, the user does not exist.
> In the second user exists but auth fail.

  - Success

```
Jan  4 17:34:27 hypervisor pvedaemon[2891825]: <root@pam> successful auth for user 'root@pam'
```

# To be done

  - ?

# Explain output

  - Proxmox-logs parser is used only for authentication failures.

```
line: Jan  4 17:34:08 hypervisor pvedaemon[3663339]: authentication failure; rhost=::ffff:172.21.10.2 user=toor@pam msg=no such user ('toor@pam')
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/proxmox-logs (+8)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/proxmox-bf

line: Jan  4 17:34:01 hypervisor pvedaemon[3663339]: authentication failure; rhost=::ffff:172.21.10.2 user=toor@pam msg=no such user ('toor@pam')
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/proxmox-logs (+8)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/proxmox-bf

line: Jan  4 17:34:08 hypervisor pvedaemon[3663339]: authentication failure; rhost=::ffff:172.21.10.2 user=toor@pam msg=no such user ('toor@pam')
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/proxmox-logs (+8)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/proxmox-bf

line: Jan  4 17:34:07 hypervisor pvedaemon[3483744]: authentication failure; rhost=::ffff:172.21.10.2 user=root@pam msg=Authentication failure
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/proxmox-logs (+8)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/proxmox-bf

line: Jan  4 17:34:08 hypervisor pvedaemon[2891825]: <root@pam> successful auth for user 'root@pam'
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🔴 fulljackz/proxmox-logs
	└-------- parser failure 🔴

line: Jan  4 17:34:08 hypervisor pvedaemon[3663339]: authentication failure; rhost=::ffff:172.21.10.2 user=toor@pam msg=no such user ('toor@pam')
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/proxmox-logs (+8)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/proxmox-bf

line: Jan  4 17:34:11 hypervisor pvedaemon[2891825]: <root@pam> successful auth for user 'root@pam'
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🔴 fulljackz/proxmox-logs
	└-------- parser failure 🔴

line: Jan  4 17:34:12 hypervisor pvedaemon[3483744]: authentication failure; rhost=::ffff:172.21.10.2 user=root@pam msg=Authentication failure
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/proxmox-logs (+8)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/proxmox-bf

line: Jan  4 17:34:13 hypervisor pvedaemon[2891825]: <root@pam> successful auth for user 'root@pam'
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🔴 fulljackz/proxmox-logs
	└-------- parser failure 🔴

line: Jan  4 17:34:02 hypervisor pvedaemon[3483744]: authentication failure; rhost=::ffff:172.21.10.2 user=root@pam msg=Authentication failure
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🟢 fulljackz/proxmox-logs (+8)
	├-------- parser success 🟢
	├ Scenarios
		└ 🟢 fulljackz/proxmox-bf

line: Jan  4 17:34:03 hypervisor pvedaemon[2891825]: <root@pam> successful auth for user 'root@pam'
	├ s00-raw
	|	└ 🟢 crowdsecurity/syslog-logs (first_parser)
	├ s01-parse
	|	└ 🔴 fulljackz/proxmox-logs
	└-------- parser failure 🔴
``` 
