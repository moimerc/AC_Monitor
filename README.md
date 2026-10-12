# AC Monitor

## Script Overview

A lightweight Python utility that monitors the AC power status of a Windows laptop using the Windows API (`GetSystemPowerStatus`). It instantly triggers a Discord webhook alert the moment the power cable is disconnected.

**Note on OS Compatibility:**
This script is designed specifically for Windows 10 and has been tested on Windows 10 Version 1909. Compatibility with Windows 11 or other operating systems is unknown and not guaranteed.

## Primary Use Case (Anti-Theft Alarm)

This script is designed as an active security measure for when you need to temporarily step away from your laptop in public spaces like cafes, libraries, or school facilities. 

Since a potential thief must unplug the AC adapter to take the laptop, the script detects this immediate hardware state change and sends an instant alert to your phone via Discord. This allows the owner to quickly react and return to the workstation.

## Requirements

- Windows 10
- Python 3.x
- `requests` library

```bash
pip install requests
```

## Usage

1. Open `AC_Monitor.py` and replace `YOUR_WEBHOOK_URL_HERE` with your designated Discord webhook URL.
2. Run the script from the terminal:

```bash
python AC_Monitor.py
```

The script will monitor the power status at 1-second intervals. To stop monitoring and safely exit, press `Ctrl + C` in the terminal.

## Disclaimer & Liability

**USE AT YOUR OWN RISK.**
This script is provided "as is" without warranty of any kind. It is intended strictly as a supplementary warning system for very short absences while remaining in close proximity to the device. The author is not responsible for any stolen property, hardware damage, or loss of data that may occur while using this script. Do not leave your laptop unattended in public areas for extended periods relying solely on this tool.