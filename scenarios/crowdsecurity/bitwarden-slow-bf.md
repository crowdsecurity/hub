Detect super slow bitwarden bruteforce attempts that evade traditional rate limiting:

 - Uses conditional type with capacity -1 (unlimited)
 - Triggers when at least 3 failed authentication attempts occur
 - Median interval between attempts exceeds 2 minutes
 - Leakspeed of 2h naturally caps maximum interval (~40-60 minutes for 3 events)
 - Uses `MedianInterval()` helper to detect consistent timing patterns (more robust against outliers)

This scenario complements the standard bitwarden-bf scenario (capacity 3, leakspeed 20s) by catching attackers who deliberately slow their attempts to avoid detection. The standard scenario catches 3 failures within ~60 seconds, while this catches 3 failures with median interval >2 minutes (naturally capped by 2h leakspeed).

