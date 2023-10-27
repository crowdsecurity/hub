Whilst CrowdSecurity designed this collection, we highly discourage the use of it (Yes we know very odd). Wireguard is designed to be high performant and secure by default protocol using key pairs. The logs were only designed to be for debugging purposes then turned back off. If a user wishes to use this collection go ahead but no support will be offered from the team if you run into issues with wireguard or the collection.

In order for CrowdSec to detect attacks on Wireguard it needs logs and since Wireguard by default logs close to nothing we need to enable Wireguard's dyndbg logging which sends log messages to the Linux kernel message buffer, `kmsg`. 
These will be picked up by your Linux distro's syslog service (at least on Debian, probably also on most others) and logged in `/var/kern.log`. On other distros they will be logged to `/var/log/messages`.

To enable Wireguard's dyndbg logging:
```console
$ sudo modprobe wireguard
$ echo module wireguard +p | sudo tee /sys/kernel/debug/dynamic_debug/control
```

More details on what we're looking for, why and other ways to do logging on Wireguard, please go to:
https://www.procustodibus.com/blog/2021/03/wireguard-logs/
