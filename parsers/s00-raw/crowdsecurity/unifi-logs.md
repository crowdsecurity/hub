# Unifi syslog parser

This is a parser for syslog logs received from an Unifi device.

Those logs are sligthly non-conformant to the syslog standard, hence the need for a custom parser.

## Example configuration

As crowdsec does not run easily directly on an UDM, you'll likely want to setup syslog export on your UDM, and use the following acquisition config:

```
source: syslog
listen_addr: 0.0.0.0
listen_port: 4242
labels:
 type: unifi
```