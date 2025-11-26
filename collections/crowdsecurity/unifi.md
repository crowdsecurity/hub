## Unifi collection

A collection to defend Unifi gear against common attacks :
- Unifi syslog parser: `crowdsecurity/unifi-logs`
- CEF logs parser: `crowdsecurity/cef-logs`
- Unifi CEF parser: `crowdsecurity/unifi-cef`
- Dropbear parser: `crowdsecurity/dropbear-logs`
- SSH bruteforce scenario : `crowdsecurity/ssh-bf`
- Iptables parser: `crowdsecurity/iptables-logs`
- Port scan detection: `crowdsecurity/iptables-scan-multi_ports`

## Log Format Support

This collection supports both standard syslog and CEF (Common Event Format) logs from UniFi devices.

### CEF Format (Recommended for Security Monitoring)

UniFi devices can send logs in CEF format, which provides structured security events with rich metadata.

#### UniFi Device Configuration

Configure your UniFi devices to send CEF logs:

1. In UniFi Controller Settings → System → Remote Logging
2. Set the remote syslog server IP address and port (default: 514)
3. Enable the desired logging categories (Admin Events, Security Events, etc.)

> Note: While UniFi calls this "CEF format", it actually sends logs with CEF headers but without the full CEF structure. The collection handles this properly.

#### rsyslog Configuration

For CEF format, you need to use rsyslog to receive and process the logs (CrowdSec's built-in syslog acquisition doesn't support CEF format).

Create a configuration file `/etc/rsyslog.d/unifi-cef.conf`:

```bash
module(load="imudp")

# Only allow your senders (legacy-style; applies to all UDP inputs)
$AllowedSender UDP, 192.168.1.0/24, 192.168.11.1/32

# Templates
template(name="CEF"    type="string" string="%msg%\n")
template(name="Syslog" type="string" string="%timegenerated% %hostname% %programname%[%procid%]: %msg%\n")

# Bind the UDP/4242 input to a ruleset so only those messages hit the UniFi actions
input(
  type="imudp"
  name="unifi_in"
  port="4242"
  ruleset="unifi"
)

ruleset(name="unifi") {
    if $rawmsg startswith "CEF:" then {
        action(type="omfile" file="/var/log/unifi-cef.log" template="CEF")
    } else {
        action(type="omfile" file="/var/log/unifi-syslog.log" template="Syslog")
    }
    stop
}

```

Restart rsyslog after configuration:
```bash
sudo systemctl restart rsyslog
```

Verify UDP port is listening:
```bash
sudo netstat -uln | grep 4242
```

#### Log Rotation Configuration

To prevent log files from growing too large, configure logrotate for both CEF and syslog files. Create `/etc/logrotate.d/unifi`:

```bash
/var/log/unifi-cef.log /var/log/unifi-syslog.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true
    endscript
}
```

This configuration will:
- Rotate logs daily
- Keep 7 days of logs
- Compress rotated logs
- Reload rsyslog after rotation

Test the logrotate configuration:
```bash
sudo logrotate -d /etc/logrotate.d/unifi
```

And run it manually if needed:
```bash
sudo logrotate -f /etc/logrotate.d/unifi
```

#### CEF Acquisition Template

Example acquisition for CEF logs (recommended for security monitoring):

```yaml
---
filenames:
 - /var/log/unifi-cef.log
labels:
  type: cef
```

Optional: If you also want to monitor non-CEF syslog messages from UniFi devices:

```yaml
---
filenames:
 - /var/log/unifi-syslog.log
labels:
  type: unifi
```

## Standard Syslog Support

For basic syslog support (non-CEF format), use CrowdSec's built-in syslog acquisition:

```yaml
source: syslog
listen_addr: 0.0.0.0
listen_port: 4242
labels:
 type: unifi
```

**Notes:**
- While the unifi gear uses syslog to send the logs, the format is non-compliant with the RFC, so you need to set the type to `unifi`
- CEF format is recommended for security monitoring as it provides structured data with rich metadata

## Supported Event Types

This collection handles multiple types of UniFi events:

### CEF Format Events
- **Admin Events**: Login attempts, configuration changes, device management
- **Security Events**: IPS alerts, blocked connections, threat detection

All CEF events include rich metadata such as device information, source/destination details, and UniFi-specific context.

### Standard Syslog Events
- General device logs and system messages
- Basic connectivity and operational events

## Testing the Configuration

After setup, test that logs are being received and properly processed:

```bash
# Send a test CEF message (if using CEF format)
echo "CEF:0|Ubiquiti|UniFi Network|9.4.19|201|Threat Detected and Blocked|7|proto=TCP src=10.0.0.100 spt=52331 dst=192.168.0.233 dpt=443 UNIFIcategory=Security UNIFIsubCategory=Intrusion Prevention UNIFIhost=Express 7 UNIFIdeviceMac=84:78:48:80:0d:86 UNIFIdeviceName=Express 7 UNIFIdeviceModel=UX7 UNIFIdeviceIp=192.168.0.1 UNIFIdeviceVersion=4.3.9 UNIFIrisk=medium UNIFIipsSessionId=54725290909450 UNIFIipsSignature=ET DROP Dshield Block Listed Source group 1 UNIFIipsSignatureId=2402000 UNIFIutcTime=2025-08-30T17:53:21.915Z msg=A network intrusion attempt has been detected and blocked." | nc -u -w1 localhost 4242

# Send a test syslog message
echo "test syslog message from unifi device" | nc -u -w1 localhost 4242

# Check that messages are being logged
tail -f /var/log/unifi-cef.log
tail -f /var/log/unifi-syslog.log
```
