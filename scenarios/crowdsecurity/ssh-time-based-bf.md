Detect time-based ssh bruteforce attempts that evade traditional rate limiting with false positive reduction:

 - Uses conditional type with capacity -1 (unlimited)
 - Triggers when at least 4 failed authentication attempts occur
 - Median interval between failed attempts exceeds 10 minutes
 - **False positive reduction**: Uses `cancel_on` to cancel bucket if user successfully authenticates
   - Prevents "forgot password" scenarios from triggering alerts
   - Standard variant: Cancels on ANY successful login from same IP
   - User-enum variant: Only cancels for same IP + same username combination
   - Attackers trying multiple usernames won't be excused by one success (in user-enum variant)
 - Leakspeed of 2h naturally caps maximum interval (~40-60 minutes for 3 events)
 - Remediation disabled (labels set to `remediation: false`)
 - Uses `MedianInterval()` helper to detect consistent timing patterns (more robust against outliers)
 - Requires `crowdsecurity/sshd-success-logs` parser for cancel_on functionality

**Two variants:**
1. **ssh-time-based-bf**: Standard bruteforce detection (4 failed logins from same IP)
2. **ssh-time-based-bf_user-enum**: User enumeration detection (4 distinct usernames from same IP)

This scenario complements the standard ssh-bf (capacity 5, leakspeed 10s) and ssh-slow-bf (capacity 10, leakspeed 60s) scenarios with no overlap:
- ssh-bf catches 5 failures within ~50 seconds (rate-based)
- ssh-slow-bf catches 10 failures within ~10 minutes (rate-based)
- ssh-time-based-bf catches 4 failures with median interval >10 minutes (time-pattern-based, naturally capped by 2h leakspeed)
