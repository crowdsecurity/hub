
A parser for windows firewall logs.

This only handles logs that contains both `DROP` and `RECEIVE` to avoid false positives for outgoing traffic or logging for successful connections.

You need to enable logging for dropped packets (off by default): https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/configure-the-windows-firewall-log

Format is:
```
#Fields: date time action protocol src-ip dst-ip src-port dst-port size tcpflags tcpsyn tcpack tcpwin icmptype icmpcode info path pid
2022-01-31 12:24:51 DROP TCP 192.168.9.163 192.168.9.212 63619 445 64 S 1031365855 0 65535 - - - RECEIVE 4
```