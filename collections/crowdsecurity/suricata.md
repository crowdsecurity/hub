## Suricata collection

A collection for the [Suricata](https://suricata.io/) IDS/IPS.
This collection contains :
 - Parsers for Suricata logs (both `fast.log` and `eve.json` formats)
 - Scenarios for Suricata alerts :
   - trigger ban on *Major* (severity:1) rules
   - trigger ban on >2 **distinct** rules of severity 2


Note: Tested with Suricata 6


## Acquisition template

Example acquisition for this collection :

```yaml
filenames:
 - /var/log/suricata/eve.json
labels:
  type: suricata-evelogs
```

**or**

```yaml
filenames:
 - /var/log/suricata/fast.log
labels:
  type: suricata-fastlogs
```

notes :
 - Using both acquisitions simultaneously will lead to double decisions or unpredictable behavior. `eve.json` should be preferred.
 - Depending on your distribution/OS, paths to log files might change
 - Only relevant if you are manually installing collection
