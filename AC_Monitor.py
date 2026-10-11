import ctypes
import time
import requests

# ==========================================
# 설정 영역
# ==========================================
DISCORD_WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"
CHECK_INTERVAL = 1  # 1초 간격 모니터링

# ==========================================
# Windows API 구조체 선언
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
        # @everyone 멘션 포함
        payload = {"content": f"@everyone\n{message}"}
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
        print(f"[-] 발송 완료: {message}")
    except Exception as e:
        print(f"[!] 발송 실패: {e}")

def is_ac_connected():
    try:
        status = SYSTEM_POWER_STATUS()
        ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status))
        # 1 = AC 전원 연결됨, 0 = 배터리
        return status.ACLineStatus == 1
    except Exception:
        return True

def main():
    print("==================================================")
    print(" AC 전원 단절 모니터링 시작 (종료: Ctrl + C)")
    print("==================================================")
    
    ac_was_connected = is_ac_connected()

    try:
        while True:
            time.sleep(CHECK_INTERVAL)
            current_ac = is_ac_connected()
            
            # AC 전원 끊김 감지
            if ac_was_connected and not current_ac:
                msg = "⚡ **경고**: AC 전원이 차단되었습니다!"
                print(f"\n[!] 상태 변경: {msg}")
                send_discord_alert(msg)
                
            # AC 전원 복구 감지
            elif not ac_was_connected and current_ac:
                msg = "✅ **복구**: AC 전원이 정상화되었습니다."
                print(f"\n[*] 상태 변경: {msg}")
                send_discord_alert(msg)
            
            ac_was_connected = current_ac

    except KeyboardInterrupt:
        print("\n==================================================")
        print(" 프로세스가 종료되었습니다.")
        print("==================================================")

if __name__ == "__main__":
    main()