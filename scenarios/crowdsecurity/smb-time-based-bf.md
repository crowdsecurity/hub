Detect time-based SMB bruteforce attempts that evade traditional rate limiting (with false positive reduction):

 - Uses conditional type with capacity -1 (unlimited)
 - Triggers when at least 3 failed authentication attempts occur
 - Median interval between attempts exceeds 5 minutes
 - Leakspeed of 2h naturally caps maximum interval (~40-60 minutes for 3 events)
 - Uses `MedianInterval()` helper to detect consistent timing patterns (more robust against outliers)

This scenario complements the standard smb-bf scenario (capacity 5, leakspeed 10s) and smb-slow-bf scenario (capacity 10, leakspeed 60s) by catching attackers who deliberately use time-based attacks to avoid detection. The standard scenario catches 5 failures within ~50 seconds, the slow-bf catches 10 failures within ~10 minutes, while this catches 3 failures with median interval >5 minutes (naturally capped by 2h leakspeed).

SMB is a common target for lateral movement in enterprise environments, and sophisticated adversaries often use slow bruteforce techniques to evade detection and avoid account lockouts.

