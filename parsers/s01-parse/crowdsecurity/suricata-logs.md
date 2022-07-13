## Suricata logs parser

This parser supports both formats :
 - the JSON `eve.json` format (`type: suricata-evelogs`)
 - the text `fast.log` format (`type: suricata-fastlogs`)

The parser only parses logs that are `alerts`.
