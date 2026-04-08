# ESP32-DIV Web Flasher

Flash firmware to your ESP32-DIV (v1 or v2) directly from the browser using Web Serial.

**Live flasher:** [https://RadDad87.github.io/esp32-div-flasher](https://RadDad87.github.io/esp32-div-flasher)

## Supported Firmware

| Firmware | Author | Features |
|----------|--------|----------|
| **CiferTech Original** v1.5.0 | [CiferTech](https://github.com/cifertech/ESP32-DIV) | Wi-Fi deauth, beacon spam, probe sniffing, BLE tools, packet monitor, SD logging |
| **HaleHound** v2.5.0 | [JesseCHale](https://github.com/JesseCHale/HaleHound-CYD) | 30+ attack modules, PMKID capture, Karma AP, NRF24, MouseJack, AirTag suite |

## How It Works

Uses [ESP Web Tools](https://esphome.github.io/esp-web-tools/) to flash via the browser Web Serial API. No drivers or desktop tools needed.

## Requirements

- Chrome 89+ or Edge 89+ (Web Serial support)
- USB cable to ESP32-DIV
- Hold BOOT button if device is not detected

## Credits

- [CiferTech](https://github.com/cifertech) — ESP32-DIV hardware and original firmware
- [JesseCHale](https://github.com/JesseCHale) — HaleHound firmware
- [ESP Web Tools](https://esphome.github.io/esp-web-tools/) — Browser flashing engine
