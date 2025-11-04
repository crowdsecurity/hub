Detect time-based ssh bruteforce attempts that evade traditional rate limiting:

 - Uses conditional type with capacity -1 (unlimited)
 - Triggers when at least 3 failed authentication attempts occur
 - Median interval between attempts exceeds 5 minutes
 - Leakspeed of 2h naturally caps maximum interval (~40-60 minutes for 3 events)
 - Uses `MedianInterval()` helper to detect consistent timing patterns (more robust against outliers)
 - Also detects user enumeration with the same timing pattern

This scenario complements the standard ssh-bf (capacity 3, leakspeed 10s) and ssh-slow-bf (capacity 5, leakspeed 60s) scenarios with no overlap:
- ssh-bf catches 3 failures within ~30 seconds (rate-based)
- ssh-slow-bf catches 5 failures within ~5 minutes (rate-based)
- ssh-time-based-bf catches 3 failures with median interval >5 minutes (time-pattern-based, naturally capped by 2h leakspeed)

