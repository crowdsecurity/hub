Detect atempts to common backdoors such as c99.php ...

## Configuration

This scenario will be trigger if an attacker requests minimum two differents file of [the list](https://raw.githubusercontent.com/crowdsecurity/sec-lists/master/web/backdoors.txt)

`distinct` : `evt.Parsed.request` (HTTP request URI)
`leakspeed` : 5 secondes
`group_by` : `evt.Meta.source_ip`


### Data

This scenario use the [following list backdoors.txt](https://raw.githubusercontent.com/crowdsecurity/sec-lists/master/web/backdoors.txt)