A parser for proxmox iptables format `-j NFLOG --nflog-prefix '$vmid:$loglevel:$chain: $msg'`:

 - Only parse kernel messages containing `-IN=`, specific to proxmox (<chain>-IN)
 - Skip lines if decisions is `ACCEPT` or `PVEFW-SET-ACCEPT-MARK`
 - All logged packets are considered as DROPs.
