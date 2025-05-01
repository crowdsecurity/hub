# marvac/filebrowser

## Description

This collection provides support for detecting brute-force login attempts against [FileBrowser](https://filebrowser.org/).  
It includes:
- A parser to extract failed login attempts from FileBrowser logs
- A scenario to detect bruteforce behavior and trigger remediation

## Content

| Type     | Name                               | Description                               |
|----------|------------------------------------|-------------------------------------------|
| Parser   | `MrShippeR/filebrowser-logs`   | Parse failed authentication logs from FileBrowser |
| Scenario | `MrShippeR/filebrowser_bf`     | Detect brute-force login attempts detection       |

## Alert log example
2025/04/10 12:34:56 /api/login: 403 192.168.1.100 <nil>

## Installation
You can install this collection with:

```bash
sudo cscli collections install MrShippeR/filebrowser
```

## Usage
add to end of your /etc/crowdsec/acquis.yaml
```yaml
filenames:
  - /var/log/filebrowser.log
labels:
  type: filebrowser
```

## Test collection against your log
```bash
sudo cscli explain -t filebrowser -f /path/to/your/filebrowser.log
```

## Support

This collection is created and maintained by marek@vach.cz Feel free to message me with any ideas or user experience if you wish to help improve this.



