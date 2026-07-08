# C3RB3RU5 Web Flasher

Browser-based firmware flasher for the **C3RB3RU5** pentesting firmware on ESP32-DIV hardware.

Flash directly from your browser — no drivers, no CLI, no setup.

## Supported Boards

| Board | Status |
|-------|--------|
| ESP32-DIV V2 (ESP32-D0WD-V3, 16MB) | **Ready** |
| ESP32-DIV V1 | Coming soon |
| CYD (Cheap Yellow Display) | Coming soon |

## How to Flash

1. Visit **[raddad87.github.io/esp32-div-flasher](https://raddad87.github.io/esp32-div-flasher/)**
2. Connect your ESP32-DIV via USB
3. Put the board in download mode (hold BOOT, power on, release after 3s)
4. Click **Install** and select the serial port
5. Wait for the flash to complete (~30 seconds)

Requires a Chromium-based browser (Chrome, Edge, Brave) with Web Serial API support.

## What is C3RB3RU5?

C3RB3RU5 is custom pentesting firmware for the ESP32-DIV platform by [CiferTech](https://github.com/cifertech). It includes 40+ security testing modules spanning WiFi, Bluetooth, RF, SubGHz, NFC, and more — built for testing your own equipment.

## Credits

- **C3RB3RU5 firmware** — [RadDad87](https://github.com/RadDad87)
- **ESP32-DIV hardware & base software** — [CiferTech](https://github.com/cifertech)
- **Web flasher** powered by [ESP Web Tools](https://esphome.github.io/esp-web-tools/)

## License

MIT