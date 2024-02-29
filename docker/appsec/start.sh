#!/bin/bash
set -x

# set the API URL
sed -i "s@API_KEY=.*@API_KEY=${API_KEY}@" /etc/crowdsec/bouncers/crowdsec-openresty-bouncer.conf
sed -i "s@API_URL=.*@API_URL=${API_URL}@" /etc/crowdsec/bouncers/crowdsec-openresty-bouncer.conf
echo "APPSEC_URL=${APPSEC_URL}" | tee -a /etc/crowdsec/bouncers/crowdsec-openresty-bouncer.conf

cat /etc/crowdsec/bouncers/crowdsec-openresty-bouncer.conf

# Start OpenResty
exec openresty -g 'daemon off;'