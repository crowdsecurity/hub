This parser checks if the source IP is an IPv6 address and if yes, will force the IPv6 address's lower 64 bits to zeros. The upper 64 bits are retained. This mean every IPv6 address in a given /64 range will be transformed into the same IPv6 address and will count towards the same bucket. This prevents an attacker from using one addresses in a /64 to fill up a bucket without causing it to overflow and then moving on to another address in the same /64 repeatedly allowing a practically infinite number of attempts. 

This parser must be used with the crowdsecurity/ipv6_to_range postoverflow so that when the shared IPv6 bucket overflows the remediation applies to the entire /64 range.

Example effects on source_ip:

2001:db8:1234:5678::abcd               => 2001:db8:1234:5678::  
2001:db8:1234:5678::1234               => 2001:db8:1234:5678::  
2001:db8:1234:5678::5678               => 2001:db8:1234:5678::  
2001:db8:1234:5678:abcd:1234:ef10:5678 => 2001:db8:1234:5678::  
2001:db8:1234:5678:4545:cdcd:6868:dada => 2001:db8:1234:5678::  
2001:db8:abcd:2020:abcd:1234:ef10:5678 => 2001:db8:abcd:2020::
