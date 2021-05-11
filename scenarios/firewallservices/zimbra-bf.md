Detect various authentication failures on Zimbra
- On the web login page
- On the SMTP server (SMTPS and SUBMISSION)
- On the IMAP server

This scenario uses two leaky buckets:
- leakspeed of 30s, capacity of 5 (per client IP)
- leakspeed of 2m, capacity of 5, on uniq target user (per client IP)
