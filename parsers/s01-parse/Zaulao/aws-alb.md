# Description
A parser for AWS Application Load Balancer (ALB) access logs. Extracts HTTP request fields from the raw message, which are used for further enrichment and processing. ALB log format is well defined [here](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html#access-log-entry-format).

# Usage
Application Load Balancers access logs are stored in S3 buckets, as indicated in the [official documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html). Therefore, the collection of these logs must start from this data source initially.

> The user can collect the logs using the AWS S3 data source, available from version 1.5 of Crowdsec, or use alternatives, such as, for example, other log collection tools that allow saving in a file or any other destinations (in this case, the data source must be specified according to the chosen alternative).

The use of this parser follows the [default configuration](https://docs.crowdsec.net/docs/next/concepts#acquisition), that is, it is performed from the `acquis.yaml` file. Therefore, after configuring the correct [data source](https://docs.crowdsec.net/docs/next/data_sources/intro) of the logs, its `type` must be specified as indicated below:

```yaml
labels:
  type: aws-alb
```

# Metadata
The information extracted from the raw log is:
- `time`: The time when the load balancer generated a response to the client;
- `remote_addr`: The IP address of the requesting client;
- `elb_status_code`: The status code of the response from the load balancer;
- `host`: The host name from the request;
- `port`: The port of the request;
- `request`: The request line URI (i.e. the `path`) from the client;
- `verb`: The request HTTP method from the client;
- `http_user_agent`: A User-Agent string that identifies the client that originated the request.

This information is exported for use in common threat detection scenarios from HTTP requests.
