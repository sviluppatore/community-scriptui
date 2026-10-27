#!/usr/bin/env python3
"""
Generate mock screenshots of the community-scriptui TUI for the README.
Rendered with PIL to simulate the terminal UI appearance.
"""

from PIL import Image, ImageDraw, ImageFont
import os

SCREENSHOT_DIR = "/home/hermes/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Colors (dark terminal theme)
BG = (20, 24, 42)          # dark blue-black background
HEADER_BG = (20, 24, 42)
ACCENT = (132, 217, 218)   # cyan-ish for highlights
SELECTION_BG = (31, 65, 120)
WHITE = (255, 255, 255)
GRAY = (158, 163, 184)
RED = (255, 128, 128)
YELLOW = (255, 230, 0)
GREEN = (100, 221, 69)
BLUE = (100, 149, 237)

class TUIScreenshot:
    def __init__(self, width=1200, height=800, font_path="DejaVuSansMono.ttf"):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), BG)
        self.draw = ImageDraw.Draw(self.image)
        # Try to find a decent monospace font
        self.font_mono = self._find_font(font_path, 18)
        self.font_small = self._find_font(font_path, 14)
        self.font_bold = self._find_font(font_path, 20)
        self.margin = 20
        self.lines = []

    def _find_font(self, name, size):
        sizes = [size, size+2, size-2]
        for sz in sizes:
            for path in [f"{name}", f"{name}.ttf", name]:
                try:
                    return ImageFont.truetype(path, sz)
                except (OSError, IOError):
                    pass
        try:
            return ImageFont.load_default()
        except Exception:
            return ImageFont.truetype(name, size)

    def _draw(self, text, x, y, color, font=None, bold=False, fill=None):
        font = font or self.font_mono
        self.draw.text((x, y), text, font=font, fill=color)

    def draw_box(self, y, h, title=None, color=WHITE):
        y0 = y
        y1 = y + h
        x0 = self.margin
        x1 = self.width - self.margin
        self.draw.rectangle([x0, y0, x1, y1], outline=color, width=2)
        if title:
            # title bar background
            self.draw.rectangle([x0, y0, x1, y0 + 22], fill=SELECTION_BG)
            self._draw(title, x0 + 24, y0 + 5, YELLOW, font=self.font_bold, bold=True)

    def render(self, filename):
        self.image.save(filename)
        print(f"Saved {filename} ({self.width}x{self.height})")

    # ---------------- Screen 1: Main list ----------------
    def screen_list(self, title="main"):
        w, h = self.width, self.height
        # Top banner
        self._draw("Curses TUI — Search, select, and install scripts from community-scripts.org",
                   40, 40, WHITE, font=self.font_bold)
        self._draw("Dark terminal UI with search, list navigation, and install functionality.",
                   40, 78, GRAY)

        # Header box
        self.draw_box(120, 38, title="Community Scripts TUI  |  / to search  |  q to quit")

        # Search bar
        self._draw("Search: ", 70, 185, BLUE)
        self._draw("scriptui_", 70, 185, BLUE, bold=True)

        # Script list items
        scripts = [
            ("proxmox-ve-post-install", "Post-install configuration for Proxmox VE"),
            ("lxc-container-setup", "Standard LXC container creation script"),
            ("vm-template-builder", "Build VM templates for Proxmox"),
            ("backup-automation", "Automated backup scheduling script"),
            ("network-config", "Network bridge and VLAN configuration"),
            ("dns-manager", "DNS zone management script"),
            ("certbot-ssl", "SSL certificate automation with Certbot"),
            ("firewall-rules", "Configure firewall rules for containers"),
            ("monitoring-setup", "Install monitoring agents (Prometheus/Grafana)"),
            ("update-automation", "Automatic system updates scheduler"),
        ]
        y = 210
        for i, (name, desc) in enumerate(scripts):
            if i == 3:  # Selected item
                self.draw_box(y - 3, 32, title=name)
                self._draw(f" > {name}      {desc}", 70, y + 4, GREEN, bold=True)
            else:
                self._draw(f"   {name:<32}  {desc}", 70, y + 4, WHITE)
            y += 34
        self._draw(f"Showing {len(scripts)} scripts — Selected: backup-automation — Enter to select — q to quit",
                   40, 650, WHITE, font=self.font_small)

        # Footer
        self._draw("Community Scripts TUI  |  Ctrl+C to exit  |  / to search  |  q to quit",
                   40, 735, GRAY, font=self.font_small)
        self.render(f"{SCREENSHOT_DIR}/screen1-list.png")

    # ---------------- Screen 2: Detail view ----------------
    def screen_detail(self, title="detail"):
        w, h = self.width, self.height
        self._draw("Curses TUI — Search, select, and install scripts from community-scripts.org",
                   40, 40, WHITE, font=self.font_bold)
        self._draw("Dark terminal UI with search, list navigation, and install functionality.",
                   40, 78, GRAY)

        self.draw_box(120, 38, title="Community Scripts TUI  |  / to search  |  q to quit")
        self._draw("Search: ", 70, 185, BLUE)
        self._draw("backup_", 70, 185, BLUE, bold=True)

        self.draw_box(210, 300, title="Script Details")
        y = 240
        self._draw("Name:  backup-automation", 70, y, GREEN, font=self.font_bold)
        y += 40
        self._draw("Desc:  Automated backup scheduling script", 70, y, WHITE)
        y += 40
        self._draw("URL:   https://community-scripts.org/scripts/backup-automation", 70, y, WHITE)
        y += 60
        self._draw("Actions: Press Enter to install  |  Esc to go back  |  q to quit", 70, y, BLUE, bold=True)
        self.render(f"{SCREENSHOT_DIR}/screen2-detail.png")

    # ---------------- Screen 3: Confirm install ----------------
    def screen_confirm(self, title="confirm"):
        w, h = self.width, self.height
        self._draw("Curses TUI — Search, select, and install scripts from community-scripts.org",
                   40, 40, WHITE, font=self.font_bold)
        self._draw("Dark terminal UI with search, list navigation, and install functionality.",
                   40, 78, GRAY)

        self.draw_box(120, 38, title="Community Scripts TUI  |  / to search  |  q to quit")
        self._draw("Search: ", 70, 185, BLUE)
        self._draw("backup_", 70, 185, BLUE, bold=True)

        self.draw_box(210, 220, title="Install Confirm", color=RED)
        y = 240
        self._draw("Install script: backup-automation", 70, y, RED, font=self.font_bold)
        y += 40
        self._draw("URL:   https://community-scripts.org/scripts/backup-automation", 70, y, WHITE)
        y += 60
        self._draw("Press Enter to proceed  |  Esc to cancel", 70, y, YELLOW, bold=True)
        self.render(f"{SCREENSHOT_DIR}/screen3-confirm.png")


if __name__ == "__main__":
    TUIScreenshot().screen_list()
    TUIScreenshot().screen_detail()
    TUIScreenshot().screen_confirm()
