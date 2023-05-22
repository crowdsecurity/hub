# detect aws bruteforce login

This scenario needs the crowdsecurity/aws-cloudtrail parser and detects
bruteforce of the aws console

Following the
[https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html](documentation)
take an extra care of your cloudtrail region configuration when
dealing with console signing event capture and please keep in mind
that event successful and failed login attempts might not be sent in
the same cloudtrail region.

Please keep in mind that only console signing regardind existing users
are captured in cloudtrail. This makes this scenario useful for
existing users and the root user.
