## AWS CIS Benchmark collection

This collections provides scenario to comply with the various alarms requirements specified in the CIS AWS Foundation Benchmark (https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-cis.html)


## Acquisition template

Example acquisition for this collection :

```yaml
source: kinesis
stream_name: cloudtrail-stream
from_subscription: true
labels:
 type: aws-cloudtrail
```