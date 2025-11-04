Detect time-based ssh bruteforce attempts that evade traditional rate limiting with false positive reduction:

 - Uses conditional type with capacity -1 (unlimited)
 - Grouped by source_ip with distinct on target_user (prevents cross-user false positives)
 - Triggers when at least 3 failed authentication attempts occur
 - Median interval between failed attempts exceeds 5 minutes
 - **False positive reduction**: Uses `cancel_on` to cancel bucket if user successfully authenticates
   - Prevents "forgot password" scenarios from triggering alerts
   - Only cancels for same IP + same username combination
   - Attackers trying multiple usernames won't be excused by one success
 - Leakspeed of 2h naturally caps maximum interval (~40-60 minutes for 3 events)
 - Uses `MedianInterval()` helper to detect consistent timing patterns (more robust against outliers)
 - Requires `crowdsecurity/sshd-success-logs` parser for cancel_on functionality

This scenario complements the standard ssh-bf (capacity 3, leakspeed 10s) and ssh-slow-bf (capacity 5, leakspeed 60s) scenarios with no overlap:
- ssh-bf catches 3 failures within ~30 seconds (rate-based)
- ssh-slow-bf catches 5 failures within ~5 minutes (rate-based)
- ssh-time-based-bf catches 3 failures with median interval >5 minutes (time-pattern-based, naturally capped by 2h leakspeed)

Note: The standard variant (without distinct username) was removed in favor of the user-enum variant for better precision and fewer false positives.

