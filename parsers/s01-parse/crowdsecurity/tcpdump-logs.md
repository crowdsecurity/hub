A parser for tcpdump logs.

To make this parser relevant, you should have add tcpdump command that log tcp scan :

An example:
```bash
cat <<EOF > /etc/systemd/system/tcpdump.service
[Unit]
Description=TCPDUMP

[Service]
Type=simple
User=root
ExecStart=/bin/sh -c 'tcpdump -l -n -i eth0 "tcp[tcpflags] & (tcp-syn) != 0" >> /var/log/tcpdump.out'
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable tcpdump.service
service tcpdump start
```

