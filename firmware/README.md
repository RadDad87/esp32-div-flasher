# Firmware Binaries

Run `python download_firmware.py` from the project root to auto-download all firmware bins.

Or manually download from:

- **CiferTech:** https://github.com/cifertech/ESP32-DIV/releases
- **HaleHound:** https://github.com/JesseCHale/HaleHound-CYD/releases

Each firmware folder needs these files:
- `bootloader.bin`
- `partitions.bin`
- `boot_app0.bin`
- `[firmware].bin` (the main application binary)
