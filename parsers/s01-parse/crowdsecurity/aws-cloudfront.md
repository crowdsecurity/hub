# Description
A parser for AWS CloudFront access logs.

# Usage

Cloudfront delivers logs to S3, so you can use crowdsec [S3 datasource](https://docs.crowdsec.net/docs/next/data_sources/s3/) to read the logs.

An example of the configuration is:

```yaml
source: s3
polling_method: sqs
sqs_name: my-queue
sqs_format: s3notification
aws_region: eu-west-1
use_time_machine: true
labels:
  type: aws-cloudfront
```

Because CloudFront will not deliver the logs in real time, you *must* set the `use_time_machine` option to force crowdsec to use the timestamp in the log itself, or you are very likely to run into false positives.