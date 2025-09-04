**UniFi CEF logs collection**

Provides support for parsing UniFi device logs in CEF (Common Event Format).

Includes both base CEF parsing and UniFi-specific field extraction for admin and security events.

## Setup Notes

**Important:** The built-in CrowdSec syslog acquisition does not support CEF format. You must use rsyslog to collect and forward CEF logs from your UniFi devices.

### UniFi Device Configuration

Configure your UniFi devices to send CEF logs to your rsyslog server:

1. In UniFi Controller Settings → System → Remote Logging
2. Set the remote syslog server IP address and port (default: 514)
3. Select CEF format for log export
4. Enable the desired logging categories (Admin Events, Security Events, etc.)

### rsyslog Configuration

Create a configuration file `/etc/rsyslog.d/unifi-cef.conf`:

```bash
# Template to extract only CEF message content (no syslog headers)
template(name="CEF" type="string" string="%msg%\n")

# Rules for UniFi devices
if $fromhost-ip startswith '192.168.' then {
    action(type="omfile" file="/var/log/unifi-cef.log" template="CEF")
    stop
}
```

Restart rsyslog after configuration:
```bash
sudo systemctl restart rsyslog
```

### Log Rotation Configuration

To prevent CEF log files from growing too large, configure logrotate for the CEF logs. Create `/etc/logrotate.d/unifi-cef`:

```bash
/var/log/unifi-cef.log {
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

## Acquisition template

Example acquisition for this collection:

```yaml
---
filenames:
 - /var/log/unifi-cef.log
labels:
  type: cef
```

## Supported Event Types

This collection handles two main types of UniFi CEF events:

- **Admin Events**: Login attempts, configuration changes, device management
- **Security Events**: IPS alerts, blocked connections, threat detection

All events include rich metadata such as device information, source/destination details, and UniFi-specific context.
