Detect super slow bitwarden bruteforce attempts that evade traditional rate limiting:

 - Uses conditional type with capacity -1 (unlimited)
 - Triggers when at least 3 failed authentication attempts occur
 - Median interval between attempts is between 2-30 minutes
 - Leakspeed of 2h to track patterns over longer timeframe
 - Uses `MedianInterval()` helper to detect consistent timing patterns (more robust against outliers)

This scenario complements the standard bitwarden-bf scenario (capacity 3, leakspeed 20s) by catching attackers who deliberately slow their attempts to avoid detection. The standard scenario catches 3 failures within ~60 seconds, while this catches 3 failures spread over 2-30 minutes.

