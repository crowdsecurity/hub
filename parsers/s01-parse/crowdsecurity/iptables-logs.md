A parser for iptables `-j LOG` logs.

All logged packets are considered as DROPs.

To make this parser relevant, you should have a `iptables -A INPUT  -m state --state NEW -j LOG` or similar into your configuration. This one will log all new connections, successful or not.

