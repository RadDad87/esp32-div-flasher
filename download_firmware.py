#!/usr/bin/env python3
"""
download_firmware.py — Fetch ESP32-DIV firmware binaries from GitHub releases.

Run this once to populate the firmware/ directory, then the web flasher
will have everything it needs to work from GitHub Pages.

Usage:
    python download_firmware.py
"""

import os
import sys
import json
import urllib.request
import urllib.error

FIRMWARE_DIR = os.path.join(os.path.dirname(__file__), "firmware")

# ── Sources ──────────────────────────────────────────────────────────────────
# Each entry: (local_dir, github_api_url, list_of (asset_name_contains, save_as))
# We pull from GitHub Releases API to get the latest asset URLs.

SOURCES = {
    "cifertech": {
        "api": "https://api.github.com/repos/cifertech/ESP32-DIV/releases/latest",
        "assets": {
            "bootloader.bin": "bootloader.bin",
            "partitions.bin": "partitions.bin",
            "boot_app0.bin": "boot_app0.bin",
            "ESP32-DIV.ino.bin": "ESP32-DIV.bin",
        },
    },
    "halehound": {
        "api": "https://api.github.com/repos/JesseCHale/HaleHound-CYD/releases/latest",
        "assets": {
            "bootloader.bin": "bootloader.bin",
            "partitions.bin": "partitions.bin",
            "boot_app0.bin": "boot_app0.bin",
            # HaleHound names vary — match partial
            "HaleHound": "HaleHound.bin",
        },
    },
}


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ESP32-DIV-Flasher"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def download_file(url, dest):
    print(f"  ↓ {os.path.basename(dest)}")
    req = urllib.request.Request(url, headers={
        "User-Agent": "ESP32-DIV-Flasher",
        "Accept": "application/octet-stream",
    })
    with urllib.request.urlopen(req) as resp:
        with open(dest, "wb") as f:
            f.write(resp.read())


def download_source(name, config, target_dirs):
    """Download assets for a firmware source into one or more target dirs."""
    print(f"\n{'='*50}")
    print(f"  {name.upper()}")
    print(f"{'='*50}")

    try:
        release = fetch_json(config["api"])
        print(f"  Release: {release.get('tag_name', 'unknown')}")
    except urllib.error.HTTPError as e:
        print(f"  ✗ Could not fetch release info: {e}")
        print(f"  → You may need to manually download bins from GitHub.")
        return False

    assets = release.get("assets", [])
    if not assets:
        print(f"  ✗ No assets found in latest release.")
        print(f"  → Check: {config['api'].replace('/releases/latest', '/releases')}")
        return False

    # Build lookup: asset_name -> download_url
    available = {a["name"]: a["browser_download_url"] for a in assets}
    print(f"  Available assets: {', '.join(available.keys())}")

    downloaded = 0
    for match_str, save_as in config["assets"].items():
        # Find the asset that contains match_str in its name
        url = None
        for asset_name, asset_url in available.items():
            if match_str in asset_name:
                url = asset_url
                break

        if not url:
            print(f"  ⚠ No asset matching '{match_str}' — skipping")
            continue

        for target_dir in target_dirs:
            os.makedirs(target_dir, exist_ok=True)
            dest = os.path.join(target_dir, save_as)
            try:
                download_file(url, dest)
                downloaded += 1
            except Exception as e:
                print(f"  ✗ Failed to download {save_as}: {e}")

    return downloaded > 0


def main():
    print("ESP32-DIV Firmware Downloader")
    print("Fetching latest binaries from GitHub releases...\n")

    # CiferTech — same bins go to both v1 and v2 dirs
    # (the firmware is compiled for the target chip, so we use what's available)
    cifertech_dirs = [
        os.path.join(FIRMWARE_DIR, "cifertech-v1"),
        os.path.join(FIRMWARE_DIR, "cifertech-v2"),
    ]
    download_source("CiferTech ESP32-DIV", SOURCES["cifertech"], cifertech_dirs)

    # HaleHound — single dir, manifests for v1/v2 both point here
    halehound_dirs = [
        os.path.join(FIRMWARE_DIR, "halehound"),
    ]
    download_source("HaleHound", SOURCES["halehound"], halehound_dirs)

    print(f"\n{'='*50}")
    print("Done! Firmware files are in: firmware/")
    print()
    print("If any downloads failed, manually grab the bins from:")
    print("  • https://github.com/cifertech/ESP32-DIV/releases")
    print("  • https://github.com/JesseCHale/HaleHound-CYD/releases")
    print()
    print("Place them in the matching firmware/ subdirectory,")
    print("then push to GitHub and enable Pages.")


if __name__ == "__main__":
    main()
