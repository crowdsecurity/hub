**UniFi CEF logs collection**

Provides support for parsing UniFi device logs in CEF (Common Event Format).

Includes both base CEF parsing and UniFi-specific field extraction for admin and security events.

## Setup Notes

**Important:** The built-in CrowdSec syslog acquisition does not support CEF format. You must use rsyslog to collect and forward CEF logs from your UniFi devices.

### UniFi Device Configuration

Configure your UniFi devices to send CEF logs to your rsyslog server:

1. In UniFi Controller Settings → System → Remote Logging
2. Set the remote syslog server IP address and port (default: 514)
3. Enable the desired logging categories (Admin Events, Security Events, etc.)

### rsyslog Configuration

Create a configuration file `/etc/rsyslog.d/unifi-cef.conf`:

```bash
module(load="imudp")
input(type="imudp" port="4242")
# Template to extract only CEF message content (no syslog headers)
template(name="CEF" type="string" string="%msg%\n")

# Template for standard syslog format (preserves full syslog structure)
template(name="Syslog" type="string" string="%timegenerated% %hostname% %syslogtag%%msg%\n")

# Rules for UniFi devices
if $fromhost-ip != '127.0.0.1' then {
    # Check if message starts with CEF
    if $msg startswith 'CEF' then {
        # CEF messages go to unifi-cef.log
        action(type="omfile" file="/var/log/unifi-cef.log" template="CEF")
    } else {
        # Non-CEF syslog messages go to unifi-syslog.log
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

### Log Rotation Configuration

To prevent log files from growing too large, configure logrotate for both CEF and syslog files. Create `/etc/logrotate.d/unifi-cef`:

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
sudo logrotate -d /etc/logrotate.d/unifi-cef
```

And run it manually if needed:
```bash
sudo logrotate -f /etc/logrotate.d/unifi-cef
```

## Acquisition templates

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

## Supported Event Types

This collection handles two main types of UniFi CEF events:

- **Admin Events**: Login attempts, configuration changes, device management
- **Security Events**: IPS alerts, blocked connections, threat detection

All events include rich metadata such as device information, source/destination details, and UniFi-specific context.

The configuration also separates CEF-formatted messages from standard syslog messages, allowing you to monitor both structured security events and general device logs.

## Testing the Configuration

After setup, test that logs are being received and properly separated:

```bash
# Send a test CEF message
echo "CEF:0|Test|Test|1.0|TEST|Test Event|5|src=192.168.1.100" | nc -u -w1 localhost 514

# Send a test syslog message
echo "test syslog message from unifi device" | nc -u -w1 localhost 514

# Check that messages went to correct files
tail -f /var/log/unifi-cef.log
tail -f /var/log/unifi-syslog.log
```
