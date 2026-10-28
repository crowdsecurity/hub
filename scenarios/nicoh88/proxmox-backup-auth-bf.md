# Proxmox Backup Server Auth BF

Detects brute-force attacks against Proxmox Backup Server (PBS) authentication.

## Logic

- **Trigger:** 6 failed authentication attempts within 10 seconds.
- **Target:** Same source IP.
- **Log type:** `proxmox-backup-auth` (failed auth).
