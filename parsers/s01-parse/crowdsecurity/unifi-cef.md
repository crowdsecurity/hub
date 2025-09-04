# Unifi CEF parser

This parser specifically handles CEF logs from Ubiquiti UniFi Network devices, filtering by vendor and product to ensure it only processes relevant logs.

## Purpose

The parser extracts Unifi-specific CEF extension fields that contain valuable metadata about network events, device information, and security alerts from UniFi devices.

It uses comprehensive grok patterns that parse the entire CEF extension message in the expected field order, ensuring compatibility with the Go grok implementation.

## Parser Structure

The parser uses a single configuration with two grok patterns, each optimized for different types of Unifi CEF events with pattern-specific statics:

### Pattern Organization
- **Admin/System Pattern** (`UNIFI_ADMIN_PATTERN`): Handles administrative actions like logins and system access
- **Security/Threat Pattern** (`UNIFI_SECURITY_PATTERN`): Handles security alerts and intrusion prevention

### Event Types Handled

#### Admin/System Events
Pattern matches logs like:
```
UNIFIcategory=System UNIFIsubCategory=Admin UNIFIhost=Unifi Dream Machine UNIFIaccessMethod=web UNIFIadmin=Secure Admin src=10.72.1.222 UNIFIutcTime=2025-09-04T08:32:58.445Z msg=...
```

**Admin pattern extracts and sets:**
- `admin_user` - Admin user who performed the action
- `access_method` - How access was performed (web, API, etc.)
- `timestamp` - UTC timestamp of the event
- Common fields: vendor, product, category, subcategory, host, severity, etc.

#### Security/Threat Events
Pattern matches logs like:
```
proto=TCP src=192.168.0.1 spt=54587 dst=192.168.0.233 dpt=80 UNIFIcategory=Security UNIFIsubCategory=Intrusion Prevention UNIFIhost=Express 7 UNIFIdeviceMac=... msg=...
```

**Security pattern extracts and sets:**
- `device_name`, `device_model`, `device_mac`, `device_ip` - Device information
- `protocol`, `source_port`, `destination_ip`, `destination_port` - Network details
- `risk_level`, `ips_signature`, `ips_signature_id`, `ips_session_id` - Threat information
- Common fields: vendor, product, category, subcategory, host, severity, etc.

## Filtering

The parser automatically filters for logs where:
- `cef_device_vendor` equals "Ubiquiti"
- `cef_device_product` equals "UniFi Network"

This ensures the parser only processes actual Unifi CEF logs and doesn't interfere with other CEF sources.

## Extracted metadata

The parser extracts the following Unifi-specific fields into metadata:

### Device Information
- `device_name` - Name of the Unifi device
- `device_model` - Model of the device (e.g., UX7, USG)
- `device_mac` - MAC address of the device
- `device_version` - Firmware version
- `host` - Hostname of the device

### Network Information
- `source_ip` - Source IP address
- `protocol` - Network protocol (TCP, UDP, etc.)
- `source_port` - Source port
- `destination_port` - Destination port

### Security & Events
- `category` - Event category (System, Security, etc.)
- `subcategory` - Event subcategory
- `risk_level` - Risk level (high, medium, low)
- `event_severity` - CEF severity level
- `admin_user` - Admin user who performed action
- `access_method` - How access was performed (web, API, etc.)

### IPS/Threat Information
- `ips_signature` - IPS signature that triggered
- `ips_signature_id` - IPS signature ID
- `ips_session_id` - IPS session identifier

## Usage

This parser should be used after the `cef-logs` parser in the s00-raw stage. It will automatically filter and enrich Unifi CEF logs with structured metadata for use in scenarios and correlation rules.
