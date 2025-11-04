Detect super slow ssh bruteforce attempts that evade traditional rate limiting:

 - Uses conditional type with capacity -1 (unlimited)
 - Triggers when at least 3 failed authentication attempts occur
 - Median interval between attempts is between 2-30 minutes
 - Leakspeed of 2h to track patterns over longer timeframe
 - Uses `MedianInterval()` helper to detect consistent timing patterns (more robust against outliers)
 - Also detects user enumeration with the same slow pattern

This scenario complements the standard ssh-bf (capacity 3, leakspeed 10s) and ssh-slow-bf (capacity 5, leakspeed 60s) scenarios:
- ssh-bf catches 3 failures within ~30 seconds
- ssh-slow-bf catches 5 failures within ~5 minutes
- ssh-slowest-bf catches 3 failures spread over 2-30 minutes

