Detects pods creation mounting a sensitive host folder in a K8S cluster, using the cluster audit logs.

Folders or files considered sensitive are:
 - `/`
 - `/etc`
 - `/etc/kubernetes`
 - `/etc/kubernetes/manifests`
 - `/proc`
 - `/root`
 - `/home/admin`
 - `/var/lib/kubelet`
 - `/var/lib/kubelet/pki`
 - `/var/run/docker.sock` 
 - `/var/run/crio/crio.sock`

The scenario needs logs from the `pods` resources at the `Request` level at a minimum.

No decision will be taken based on this scenario, it is only intented for notification purposes.