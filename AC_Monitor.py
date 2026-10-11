import ctypes
import time
import requests

# ==========================================
# Configuration
# ==========================================
DISCORD_WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"
CHECK_INTERVAL = 1  # 1-second interval monitoring

# ==========================================
# Windows API Structure
# ==========================================
class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', ctypes.c_byte),
        ('BatteryFlag', ctypes.c_byte),
        ('BatteryLifePercent', ctypes.c_byte),
        ('Reserved1', ctypes.c_byte),
        ('BatteryLifeTime', ctypes.c_ulong),
        ('BatteryFullLifeTime', ctypes.c_ulong),
    ]

def send_discord_alert(message):
    try:
        # Include @everyone mention
        payload = {"content": f"@everyone\n{message}"}
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
        print(f"[-] Alert sent: {message}")
    except Exception as e:
        print(f"[!] Alert failed: {e}")

def is_ac_connected():
    try:
        status = SYSTEM_POWER_STATUS()
        ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status))
        # 1 = AC power connected, 0 = Battery
        return status.ACLineStatus == 1
    except Exception:
        return True

def main():
    print("==================================================")
    print(" AC Power Monitor Started (Press Ctrl+C to stop)")
    print("==================================================")
    
    ac_was_connected = is_ac_connected()

    try:
        while True:
            time.sleep(CHECK_INTERVAL)
            current_ac = is_ac_connected()
            
            # AC power loss detected
            if ac_was_connected and not current_ac:
                msg = "⚡ **WARNING**: AC power disconnected!"
                print(f"\n[!] Status Change: {msg}")
                send_discord_alert(msg)
                
            # AC power restored
            elif not ac_was_connected and current_ac:
                msg = "✅ **RESTORED**: AC power reconnected."
                print(f"\n[*] Status Change: {msg}")
                send_discord_alert(msg)
            
            ac_was_connected = current_ac

    except KeyboardInterrupt:
        print("\n==================================================")
        print(" Process terminated.")
        print("==================================================")

if __name__ == "__main__":
    main()