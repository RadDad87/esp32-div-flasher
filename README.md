# C3RB3RU5 Web Flasher

Browser-based firmware flasher for the **C3RB3RU5** pentesting firmware on ESP32-DIV hardware.

Flash directly from your browser — no drivers, no CLI, no setup.

## Supported Boards

| Board | Status |
|-------|--------|
| ESP32-DIV V2 (ESP32-D0WD-V3, 16MB) | **Ready** |
| ESP32-DIV S3 (ESP32-S3, 16MB, native USB) | **Ready** |
| ESP32-DIV V1 | Coming soon |
| CYD (Cheap Yellow Display) | Coming soon |

## How to Flash

1. Visit **[raddad87.github.io/C3RB3RU5](https://raddad87.github.io/C3RB3RU5/)**
2. Connect your ESP32-DIV via USB
3. If the board doesn't auto-enter download mode, hold **BOOT**, tap **RESET**, then release BOOT (the **S3** has native USB and usually needs no BOOT hold)
4. Click **Install** and select the serial port
5. Wait for the flash to complete (~30 seconds)

Requires a Chromium-based browser (Chrome, Edge, Brave) with Web Serial API support.

## What is C3RB3RU5?

C3RB3RU5 is custom pentesting firmware for the ESP32-DIV platform. It runs a full suite of 2.4GHz WiFi, Bluetooth/BLE, RF/SubGHz, NFC, and detection modules across both the ESP32 (V2) and ESP32-S3 boards — built for testing your own equipment.

## Credits & Acknowledgments

C3RB3RU5 didn't start from scratch — it stands on two projects, and this build takes the best of both and expands on them:

- **[CiferTech](https://github.com/cifertech)** — created the **ESP32-DIV hardware** *and* the **original ESP32-DIV firmware**. The device and its base software are entirely CiferTech's work; C3RB3RU5 is a firmware built for that platform. ([ESP32-DIV repo](https://github.com/cifertech/ESP32-DIV) · MIT · [cifertech.net](https://cifertech.net/))
- **[HaleHound-CYD](https://github.com/JesseCHale/HaleHound-CYD)** by JesseCHale — elements and feature ideas were borrowed and adapted from its firmware.
- **[RadDad87](https://github.com/RadDad87)** — **C3RB3RU5**: combined the strongest parts of both firmwares, then expanded them with additional modules, a full UI overhaul, and the C3RB3RU5 branding.

Web flasher powered by [ESP Web Tools](https://esphome.github.io/esp-web-tools/).

## License

MIT. C3RB3RU5 firmware © 2024–2026 RadDad87, built on CiferTech's ESP32-DIV (MIT). For authorized security testing only.
