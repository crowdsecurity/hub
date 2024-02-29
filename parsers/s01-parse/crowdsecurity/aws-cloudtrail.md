# Parser for cloudtrail logs

Parser for cloudtrail logs with type `aws-cloudtrail`. 

# S3

As cloudtrail logs that are sent to s3 are stored in a json array
object called `Records`, you may want to use the transform feature of
crowdsec with the following configuration:
`map(JsonExtractSlice(evt.Line.Raw, "Records"), ToJsonString(#))`.


Example of `acquis.yaml` using s3 s3notifications through sqs:
```yaml
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

A direct acquisition method is supported using s3 by directly listing
new object in the bucket. In case of high cloudtrail traffic, this is
discouraged, because it will require some significant compute
resources.

Cloudtrail logs are arriving every few minutes, thus, we can't use the
real time feature of crowdsec. That's the reason we are suggesting
to use the time machine feature, to take into account the time when
they occurred and not when they are sent to CrowdSec.

Please have a look at the documentation
https://docs.crowdsec.net/docs/next/data_sources/s3

# Kinesis

Cloudtrail logs can be sent to kinesis as well, and crowdsec supports
such a source for cloudtrail logs:

```yaml
source: kinesis
stream_name: cloutrail_stream
aws_region: eu-west-1
from_subscription: true
labels:
  type: aws-cloudtrail
```
