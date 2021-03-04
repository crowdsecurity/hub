A parser for iptables `-j LOG` logs :

 - Only parse kernel messages containing `IN=`
 - Skip lines if decisions is `ACCEPT`


All logged packets are considered as DROPs.

To make this parser relevant, you should have a `iptables -A INPUT  -m state --state NEW -j LOG` or similar into your configuration. This one will log all new connections, successful or not.

