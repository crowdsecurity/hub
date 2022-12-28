This will parse your packet filter logs. Tested with PfSense, sending its log to a remote syslog server, where crowdsec can parse them. OPNsense style logs are also supported.

### How to enable OPNsense pf log ingestion

- Login to a shell on opnsense
- Add `/var/log/filter/latest.log` to `/usr/local/etc/crowdsec/acquis.yaml` into the already existing syslog block
    
  - Example: 
    ```yaml
    filenames:
        - /var/log/auth.log
        - /var/log/syslog
        - /var/log/filter/latest.log
    labels:
         type: syslog
       ```