Detect scan of tabobicode :
 - Alert on 404 or 403 http status for the page /wp-content/themes/tabobine/tabobicode/get_uid.php
 - leakspeed of 90s, capacity of 5 from same IP

To create test from crowdsec folder: 
```shell
export PATH=$PATH:`pwd`
sudo ln -s $PWD/config/patterns /etc/crowdsec/patterns
cscli -c dev.yaml --hub ../../hub hubtest create get-uid-scan --type traefik --ignore-parsers
cscli -c dev.yaml --hub ../../hub hubtest run get-uid-scan
cscli -c dev.yaml --hub ../../hub hubtest explain get-uid-scan
```
