### Postfix helo rejected

Postfix helo rejected is a log message generated when a client sends a HELO or EHLO command that is rejected by the server. This can happen for a variety of reasons, such as the client using an invalid hostname or the server being configured to reject certain types of HELO commands.

You can see the configuration for the restrictions placed on HELO commands within https://www.postfix.org/postconf.5.html#smtpd_helo_restrictions
