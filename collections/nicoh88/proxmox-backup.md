# Proxmox Backup Server Collection

This collection supports Proxmox Backup Server (PBS) authentication monitoring.

## Content

- **Parser:** `nicoh88/proxmox-backup-auth-logs` — parses `/var/log/proxmox-backup/api/auth.log`
- **Scenario:** `nicoh88/proxmox-backup-auth-bf` — detects brute-force attacks

## Setup

Ensure your `acquis.yaml` / `acquis.d/pbs.yaml` is configured to read the PBS auth log file:

```yaml
filenames:
  - /var/log/proxmox-backup/api/auth.log
labels:
  type: proxmox-backup-auth

