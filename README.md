# community-scriptui

A terminal-based TUI (Text User Interface) for browsing, searching, and installing scripts from [community-scripts.org](https://community-scripts.org).

## Overview

`community-scriptui` is a lightweight, keyboard-driven tool that lets you explore and install scripts from the [community-scripts.org](https://community-scripts.org) repository directly from your terminal. It provides a dark-themed interface with search, list navigation, and install functionality.

## Features

- **Search** — Type `/` or `s` to search for scripts by name or description
- **Navigate** — Use `j`/`k` or arrow keys to scroll through the script list
- **View Details** — Press `Enter` to see script metadata (name, description, URL)
- **Install** — Press `Enter` again to save a script reference to your local machine
- **Quit** — Press `q` or `Esc` to exit
- **Runsheet Generation** — Optional automatic creation of Markdown documentation after install

## Installation

### Prerequisites

- Python 3.13+ (for curses support)
- Internet connection (optional — falls back to curated defaults if offline)

### Setup

```bash
# Clone the repository
cd /home/hermes

# Make the script executable
chmod +x community-scriptui

# Run the TUI
TERM=xterm-256color python3 community-scriptui
```

## Usage

### Basic Workflow

1. **Launch** the TUI with `python3 community-scriptui`
2. **Search** — Type `/` or `s` followed by keywords (e.g., `backup`, `vm`, `proxy`)
3. **Browse** — Use `j`/`k` or arrow keys to navigate the list
4. **View Details** — Press `Enter` on a script to see its name, description, and source URL
5. **Install** — Press `Enter` again to save the script reference to `/home/hermes/community_script_<name>.sh`
6. **Quit** — Press `q` or `Esc`

### Example

```
$ TERM=xterm-256color python3 community-scriptui
Curses TUI — Search, select, and install scripts from community-scripts.org
Dark terminal UI with search, list navigation, and install functionality.

Searching for "backup"...

  proxmox-ve-post-install          Post-install configuration for Proxmox VE
  backup-automation                Automated backup scheduling script
  certbot-ssl                       SSL certificate automation with Certbot
  ...

Enter to view details
```

## Scripts Included

The tool includes a curated list of useful scripts from community-scripts.org:

| Name | Description |
|------|-------------|
| `proxmox-ve-post-install` | Post-install configuration for Proxmox VE |
| `lxc-container-setup` | Standard LXC container creation script |
| `vm-template-builder` | Build VM templates for Proxmox |
| `backup-automation` | Automated backup scheduling script |
| `network-config` | Network bridge and VLAN configuration |
| `dns-manager` | DNS zone management script |
| `certbot-ssl` | SSL certificate automation with Certbot |
| `firewall-rules` | Configure firewall rules for containers |
| `monitoring-setup` | Install monitoring agents (Prometheus/Grafana) |
| `update-automation` | Automatic system updates scheduler |

## Offline Mode

If the internet is unavailable, the tool falls back to a curated list of 10 essential scripts (defined in `FALLBACK_SCRIPTS`). These cover common Proxmox and homelab use cases.

## Customization

Edit the `FALLBACK_SCRIPTS` list in `community-scriptui.py` to add or remove default scripts.

To disable runsheet generation, edit the script and set:
```python
GENERATE_RUNSHEET = False
```

## License

MIT — feel free to modify and distribute.

## Contributing

Pull requests are welcome. Please ensure:
- All scripts in `FALLBACK_SCRIPTS` are from community-scripts.org
- New scripts follow the same naming convention (`{name}-{desc}`)
- Update the README with any new default scripts

## Troubleshooting

- **Curses not initializing** — Ensure you're running in a real terminal (not a pipe or non-X environment)
- **Connection errors** — The tool will automatically fall back to curated defaults
- **Missing dependencies** — Python 3.13+ is required; curses is included in standard library

## Project Structure

```
community-scriptui/
├── community-scriptui       # Main TUI script (Python)
├── screenshots/             # ASCII art screenshots
│   ├── screenshot1-main-list.txt
│   ├── screenshot2-detail-view.txt
│   ├── screenshot3-confirm-install.txt
│   └── generate_screenshots.py
└── README.md                # This README
```

## Related

- [community-scripts.org](https://community-scripts.org) — Source of scripts
- [Proxmox VE Documentation](https://wiki.proxmox.com/) — Many of the included scripts target Proxmox

## Screenshots

Due to environment limitations (no screenshot tools available), the TUI interface has been documented using ASCII art screenshots. See `/home/hermes/screenshots/` for the three key screens.

## Screenshot 1: Main Script List (screenshot1-main-list.txt)
Shows the main search/navigation screen with script names, descriptions, and a highlighted selected item (`backup-automation`).

## Screenshot 2: Script Detail View (screenshot2-detail-view.txt)
Shows the selected script with its name (`backup-automation`), description, source URL, and action instructions.

## Screenshot 3: Install Confirmation (screenshot3-confirm-install.txt)
Shows the confirm screen with the script being installed (`backup-automation`), its URL, and instructions to proceed.

## Runsheet Feature

When `GENERATE_RUNSHEET = True` (default), the tool automatically creates a Markdown runsheet document after installing a script. The runsheet is saved to `/home/hermes/runsheet_<script_name>.md` and includes:

- Script name and description
- Source URL
- Saved file path
- Installation steps
- How to run the script

Example runsheet content:

```
# Runsheet — proxmox-ve-post-install

**Generated:** 2026-10-08 14:30:22

**Status:** ✅ Installed

---

## Script Details

- **Name:** proxmox-ve-post-install
- **Description:** Post-install configuration for Proxmox VE
- **Source URL:** https://community-scripts.org/scripts/proxmox-ve-post-install
- **Saved File:** /home/hermes/community_script_proxmox_ve_post_install.sh

## Actions Log

1. Selected script: proxmox-ve-post-install
2. Fetched from: https://community-scripts.org/scripts/proxmox-ve-post-install
3. Saved reference to: /home/hermes/community_script_proxmox_ve_post_install.sh
4. Runsheet generated: /home/hermes/runsheet_proxmox_ve_post_install.md

## Next Steps

- Visit: https://community-scripts.org/scripts/proxmox-ve-post-install
- Make executable: `chmod +x /home/hermes/community_script_proxmox_ve_post_install.sh`
- Execute: `./home/hermes/community_script_proxmox_ve_post_install.sh` or `sudo ./home/hermes/community_script_proxmox_ve_post_install.sh`

## Notes

- This runsheet was auto-generated by community-scriptui.
- If the script was saved as a reference, visit the source URL to get the actual script.
- The runsheet is for documentation purposes only; the actual script execution requires manual review.
```

## Quick Reference

| Command | Action |
|---------|----------|
| `python3 community-scriptui` | Launch TUI |
| `TERM=xterm-256color python3 community-scriptui` | Force xterm-256color terminal |
| `q` or `Esc` | Quit |
| `/` or `s` | Search |
| `j`/`k` or arrows | Navigate |
| `Enter` | View details / Install |

## Support

If you encounter issues, please open an issue on the GitHub repository.