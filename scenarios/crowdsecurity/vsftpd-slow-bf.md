Detect slow FTP bruteforce attempts:

 - leakspeed of 60s, capacity of 10

This scenario complements the standard vsftpd-bf scenario (capacity 5, leakspeed 10s) by catching slower attacks. The standard scenario catches 5 failures within ~50 seconds, while this catches 10 failures over ~10 minutes.

FTP is a common target for credential attacks, and attackers may slow their attempts to avoid detection.

