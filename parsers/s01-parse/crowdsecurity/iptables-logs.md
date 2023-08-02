A parser for iptables `-j LOG` logs :

 - Only parse kernel messages containing `IN=`
 - Skip lines if decisions is `ACCEPT`
 - All parsed `TCP` and `UDP` packets are considered as DROPs.
 - ICMP packets are parsed and sets the following meta attributes: (Note we do not have scenarios around ICMP as they are FPs prone)
   - `icmp_type`
   - `icmp_code`
- If you wish to code your own scenarios around ICMP, you can use the following [link as a reference](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml). Please note you are solely responsible for the scenarios you write.


To make this parser relevant, you should have a `iptables -A INPUT  -m state --state NEW -j LOG` or similar into your configuration. This one will log all new connections, successful or not.

