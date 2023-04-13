# Non working hour / non working day login

This scenario needs the crowdsecurity/aws-cloudtrail parser and
detects non working hours/days login in the aws console. You may want to
adapt the hours to your specific needs. As an example, the scenario is
written for UTC+2 working hours.

Following the
[https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html](documentation)
take an extra care of your cloudtrail region configuration when
dealing with console signing event capture.
