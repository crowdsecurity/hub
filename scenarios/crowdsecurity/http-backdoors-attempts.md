Detect attempts to access common backdoors such as c99.php ...

## Configuration

This scenario will be trigger if an attacker requests a minimum of two differents file of [the list](https://dud8c11oe0bga.cloudfront.net/web/backdoors.txt)/

Configuration:

`distinct` : `evt.Parsed.request` (HTTP request URI)

`leakspeed` : 5 secondes

`group_by` : `evt.Meta.source_ip`


### Data

This scenario use the [following list backdoors.txt](https://dud8c11oe0bga.cloudfront.net/web/backdoors.txt) from [danielmiessler](https://github.com/danielmiessler/SecLists)