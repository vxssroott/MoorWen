# MOORWEN — The Ultimate USB Weapon

**One USB. One plug. Total compromise.**

## Overview

MoorWen is a self-contained, auto-executing USB payload that combines the capabilities of every major hacking device into a single, portable package.

## Capabilities

| Device | Capability | MoorWen Integration |
|--------|------------|---------------------|
| **Rubber Ducky** | Keystroke injection | Auto-runs payload on insertion |
| **WiFi Pineapple** | Evil Twin / Handshake capture | WiFi emulation + credential harvesting |
| **Flipper Zero** | RFID/NFC/Sub-GHz/IR | SDR + NFC emulation |
| **LAN Turtle** | Reverse shell / Packet capture | Persistent C2 backdoor |
| **Bash Bunny** | Multi-payload USB | Multiple payload switching |
| **Proxmark3** | RFID cloning | NFC/RFID software tools |
| **HackRF Pro** | SDR (100kHz-6GHz) | SDR software suite |
| **T-Embed CC1101** | Sub-GHz / 2.4GHz | RF emulation |
| **Cardputer ADV** | WiFi/Bluetooth attacks | WiFi/BLE exploit tools |
| **Bus Pirate 6** | Hardware debugging | Protocol analyzers |

## Deployment

1. Copy `autorun.inf` and `setup.exe` to a USB drive.
2. Plug the USB into the target machine.
3. Auto-run executes `setup.exe`.
4. MoorWen installs silently and persists across reboots.

## Modules

| Module | Purpose |
|--------|---------|
| **setup.exe** | Windows installer |
| **setup.elf** | Linux installer |
| **setup.app** | macOS installer |
| **autorun.inf** | Windows auto-run |
| **payload_loader.ps1** | PowerShell loader |
| **payload_loader.sh** | Bash loader |
| **wifi_pineapple.py** | WiFi Pineapple emulation |
| **rubber_ducky.ps1** | Keystroke injection |
| **lan_turtle.py** | Reverse shell / packet capture |
| **flipper_zero.py** | RFID/NFC emulation |
| **sdr_tools.py** | Software-defined radio |
| **rfid_cloner.py** | RFID cloning |
| **wifi_attacks.py** | Evil Twin / Deauth |
| **ble_attacks.py** | Bluetooth exploits |
| **hardware_debug.py** | Bus Pirate emulation |

## Watermark

All code is watermarked with 𝕍𝕠𝕤𝕤🥷 and contains a proprietary license. Do not remove.

## License

Proprietary — See LICENSE.md

---

𝕍𝕠𝕤𝕤🥷
Systems Engineer, Security Architect & Operations Manager
