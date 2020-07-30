The GeoIP module relies on geolite database to provide enrichment on source ip :
 - IsoCode : the two-letters country code
 - ASNNumber : the AS Number
 - ASNOrg : the full name of AS organization

This configuration includes GeoLite2 data created by [MaxMind](https://www.maxmind.com/en/home), it includes two data files: 
* [GeoLite2-City.mmdb](https://crowdsec-statics-assets.s3-eu-west-1.amazonaws.com/GeoLite2-City.mmdb)
* [GeoLite2-ASN.mmdb](https://crowdsec-statics-assets.s3-eu-west-1.amazonaws.com/GeoLite2-ASN.mmdb)