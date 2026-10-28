# CEF parser

This parser handles logs in the Common Event Format (CEF), a standardized logging format used by various security devices and applications.

The parser extracts key CEF fields including the device vendor (manufacturer), product, version, signature ID, event name, and severity level.

## CEF Format

The parser handles the standard CEF format:

```
CEF:Version|Device Vendor|Device Product|Device Version|Signature ID|Name|Severity|Extension
```

## Requirements

When using this parser, you need to specify `type: cef` in your `acquis.yaml` configuration. The parser will automatically extract the manufacturer from the `Device Vendor` field and set it as the `program` field for downstream processing.

## Example configuration

```yaml
source: file
filenames:
  - /var/log/cef/*.log
labels:
  type: cef
```

## Extracted fields

The parser extracts the following CEF fields:

- `cef_device_vendor` - The device manufacturer/vendor
- `cef_device_product` - The product name
- `cef_device_version` - The product version
- `cef_signature_id` - Unique event signature identifier
- `cef_event_name` - Human-readable event name
- `cef_severity` - Event severity level (0-10)
- `message` - Any additional extension data or message content

The `cef_device_vendor` field is also mapped to the `program` field for compatibility with other parsers.
