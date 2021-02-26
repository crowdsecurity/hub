The GeoIP module relies on geolite database to provide enrichment on source ip.

The following informations will be added to the event :
 - `Meta.IsoCode` : two-letters country code
 - `Meta.IsInEU` : a boolean indicating if IP is in EU
 - `Meta.GeoCoords` : latitude & longitude of IP
 - `Meta.ASNNumber` : Autonomous System Number
 - `Meta.ASNOrg` : Autonomous System Name
 - `Meta.SourceRange` : The public range to which the IP belongs


This configuration includes GeoLite2 data created by MaxMind available from [https://www.maxmind.com](https://www.maxmind.com), it includes two data files: 
* [GeoLite2-City.mmdb](https://crowdsec-statics-assets.s3-eu-west-1.amazonaws.com/GeoLite2-City.mmdb)
* [GeoLite2-ASN.mmdb](https://crowdsec-statics-assets.s3-eu-west-1.amazonaws.com/GeoLite2-ASN.mmdb)

