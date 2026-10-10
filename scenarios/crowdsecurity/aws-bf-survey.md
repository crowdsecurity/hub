# detect aws console user enumeration

This scenario needs the crowdsecurity/aws-cloudtrail parser and detects
attempts to guess IAM user names on the aws console sign-in page.

When someone tries to sign in to the console with an IAM user name that
does not exist in the account, CloudTrail logs a failed `ConsoleLogin`
event with the error message `No username found in supplied account`
(the user name itself is replaced by `HIDDEN_DUE_TO_SECURITY_REASONS`).
The scenario triggers when a single IP produces more than 5 of these
failures in a short time.

Failures for existing users (`Failed authentication`) are not counted
here. crowdsecurity/aws-bf counts every console login failure, this
scenario only flags the user name guessing part.

As for crowdsecurity/aws-bf, take extra care of your cloudtrail region
configuration: console sign-in events might not be logged in the region
you expect, see the
[documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html).
