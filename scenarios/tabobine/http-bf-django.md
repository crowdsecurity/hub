Detects bruteforce on django login page 'login'.

leakspeed of 10s, capacity of 5

To create test from crowdsec folder: 
```shell
export PATH=$PATH:`pwd`
sudo ln -s $PWD/config/patterns /etc/crowdsec/patterns
cscli -c dev.yaml --hub ../../hub hubtest create http-bf-django --type traefik --ignore-parsers
cscli -c dev.yaml --hub ../../hub hubtest run http-bf-django
cscli -c dev.yaml --hub ../../hub hubtest explain http-bf-django
```
