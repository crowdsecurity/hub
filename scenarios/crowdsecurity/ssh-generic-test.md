# ssh generic test

This scenario is meant to check if crowdsec is correctly configured, this will
trigger an alert, but no decision.


On the machine one wants to test
`ssh NtktlJHV4TfBSK3wvlhiOBnl@<your-ip>`

You will see in your crowdsec logs: 

```
time="2025-06-12T16:59:45+02:00" level=info msg="Ip <your-ip> performed 'crowdsecurity/ssh-generic-test' (1 events over 0s) at 2025-06-12 14:59:45.636887959 +0000 UTC"
time="2025-06-12T16:59:46+02:00" level=info msg="(<local API login>) alert : crowdsecurity/ssh-generic-test by ip <your-ip> xxxxxx"
time="2025-06-12T16:59:47+02:00" level=info msg="Signal push: 1 signals to push"
```

`cscli alert list` will present you this alert as well. Please note that this
scenario won't trigger any decision, and result in any remediation.

If you don't see anything in logs nor in the alerts list, then you can assume an
issue in your setup

Beware this WON'T work with local ips.
