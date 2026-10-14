# AC Monitor

## Overview
A lightweight Windows utility that watches AC power status via the Windows API (`GetSystemPowerStatus`) and fires a Discord webhook alert when the power cable is disconnected.

Tested on Windows 10 (1909). Windows 11 and other operating systems are untested.

## Use Case: Anti-Theft Alarm
Designed for short absences from a laptop in public spaces. A thief must unplug the AC adapter to take the machine — this script detects that state change and pushes an alert to your phone via Discord, giving you a chance to react.

## Requirements
- Windows 10
- Python 3.x
- `requests`

```bash
pip install requests
```

## Usage
1. Open `AC_Monitor.py` and replace `YOUR_WEBHOOK_URL_HERE` with your Discord webhook URL.
2. Run:

```bash
python AC_Monitor.py
```

Polls at 1-second intervals. Press `Ctrl + C` to stop.

## Disclaimer

**USE AT YOUR OWN RISK.**
Provided as-is, with no warranty. It is intended strictly as a supplementary warning system for very short absences while remaining in close proximity to the device. The author is not responsible for any stolen property, hardware damage, or data loss.