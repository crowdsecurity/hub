# Parser for cloudtrail logs

Parse with the cloudtrail parser logs with type `aws-cloudtrail`. You may want to use the transform feature of crowdsec with the following configuration: `map(JsonExtractSlice(evt.Line.Raw, "Records"), ToJsonString(#))`.

Example of `acquis.yaml` using s3 s3notifications through sqs:
```
source: s3
polling_method: sqs
sqs_name: <sqs_queue>
sqs_format: s3notification 
polling_interval: 30
aws_region: eu-west-1
transform: map(JsonExtractSlice(evt.Line.Raw, "Records"), ToJsonString(#))
max_buffer_size: 10000000
use_time_machine: true
labels:
  type: aws-cloudtrail
```
