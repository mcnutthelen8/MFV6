import redis

import time
import pyautogui
import requests
import base64
import os
import subprocess
from pywinauto import Desktop
# --- CONFIG ---
def get_farm_id(filepath="farmid.txt"):
    """Reads and prints the number from farmid.txt."""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read().strip()
            print(f"📍 Current Farm ID: {content}")
            return content
    return None

print("Getting Farm ID...")
farm_id = get_farm_id()
print("Farm ID obtained.")
print(f"Farm ID String: {farm_id}")

if farm_id is None:
    print("Error: farmid.txt not found or empty. Defaulting to Farm ID 1.")
    for i in range(59):
        time.sleep(999999)


MY_FARM_ID = farm_id  
AUTOSTART = True
MAIN_SCRIPT_PATH = r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\browser_configure.py"
CSB_SCRIPT_PATH = r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\csb_handle.py"
MAIN_DIR = r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main"

# Redis & API Config
R_HOST = '98.142.247.28'
R_PASS = 'pass123'
IMGBB_API_KEY = "1d7c60af23814f9b6245b4b7d6cee139"

r = redis.Redis(host=R_HOST, port=6379, password=R_PASS, decode_responses=True)
APPS = {
    "Tuxler": {
        "title": "Tuxler",
        "exe_name": "tuxlerVPN.exe",
        "path": r"C:\Program Files (x86)\tuxlerVPN\tuxlerVPN.exe"
    },
    "AdsPower": {
        "title": "AdsPower",
        "exe_name": "AdsPower Global.exe",
        "path": r"C:\Program Files\AdsPower Global\AdsPower Global.exe"
    }
}

def kill_apps():
    """Forcefully closes Tuxler and AdsPower processes."""
    for name, info in APPS.items():
        print(f"🛑 Killing {name}...")
        # /F is force, /IM is image name, /T kills child processes too
        os.system(f'taskkill /F /IM "{info["exe_name"]}" /T >nul 2>&1')

def launch_via_run_dialog(app_path):
    """Mimics a human pressing Win+R and typing the path."""
    print(f"⌨️ Mimicking human launch for: {app_path}")
    
    # 1. Open Run Dialog (Win + R)
    pyautogui.hotkey('win', 'r')
    time.sleep(1) # Wait for dialog to appear
    
    # 2. Type the path
    pyautogui.write(app_path)
    time.sleep(0.5)
    
    # 3. Press Enter
    pyautogui.press('enter')
    print("✅ Command sent to Windows Run dialog.")

def ensure_apps_running32():
    """Checks if windows exist; if not, launches them via Windows Shell."""
    try:
        for i in range(15):
            # 1. Check windows
            windows = Desktop(backend="uia").windows()
            existing_titles = [win.window_text().lower() for win in windows]
            
            tuxler_running = any("tuxler" in t for t in existing_titles)
            adspower_running = any("adspower" in t for t in existing_titles)

            # 2. Launch Tuxler if missing
            if not tuxler_running:
                path = APPS["Tuxler"]["path"]
                if os.path.exists(path):
                    print("🚀 Launching Tuxler via Shell...")
                    launch_via_run_dialog(path)
                    #os.startfile(path) # This is the "magic" line for Windows
                else:
                    print(f"❌ Tuxler path missing: {path}")

            # 3. Launch AdsPower if missing
            if not adspower_running:
                path = APPS["AdsPower"]["path"]
                if os.path.exists(path):
                    print("🚀 Launching AdsPower via Shell...")
                    launch_via_run_dialog(path)
                    #os.startfile(path) # Decouples from Python entirely
                else:
                    print(f"❌ AdsPower path missing: {path}")
            for i in range(15):
                time.sleep(1)
                # Re-check windows
                windows = Desktop(backend="uia").windows()
                existing_titles = [win.window_text().lower() for win in windows]
                
                tuxler_running = any("tuxler" in t for t in existing_titles)
                adspower_running = any("adspower" in t for t in existing_titles)
                if tuxler_running and adspower_running:
                    break
                else:
                    print("⏳ Waiting for apps to launch...")
                    print(f"Current windows: {tuxler_running}, {adspower_running}")

            if tuxler_running and adspower_running:
                print("✅ All apps are already running.")
                return True
        return False
            
    except Exception as e:
        print(f"Error in ensure_apps: {e}")

def kill_main_script():
    """Kills only the process running browser_configure.py using window title."""
    print("Targeting main script for termination...")
    # This command kills windows where the title contains 'MONEYFARM_TASK'
    os.system('taskkill /f /fi "windowtitle eq MONEYFARM_TASK*" /t')

def kill_csb_script():
    """Kills only the process running browser_configure.py using window title."""
    print("Targeting CSB script for termination...")
    # This command kills windows where the title contains 'CSB Handle'
    os.system('taskkill /f /fi "windowtitle eq CSB Handle*" /t')

def run_main_script(script_path):
    print(f"Starting script: {script_path}")
    # We use 'cmd /k' to set a title so we can find and kill it specifically later
    cmd_command = f'start "MONEYFARM_TASK" python "{script_path}"'
    subprocess.Popen(cmd_command, shell=True)


def run_csb_script(script_path):
    print(f"Starting CSB script: {script_path}")
    # We use 'cmd /k' to set a title so we can find and kill it specifically later
    cmd_command = f'start "CSB Handle" python "{script_path}"'
    subprocess.Popen(cmd_command, shell=True)

def handle_command(cmd, data=None):
    print(f"Executing: {cmd}")
    
    if cmd == "CMD_RESTART_SCRIPT":
        kill_main_script()
        time.sleep(2)
        run_main_script(MAIN_SCRIPT_PATH)

    elif cmd == "CMD_RESET_CSB":
        kill_csb_script()
        time.sleep(3)  # Wait for apps to stabilize

        run_csb_script(CSB_SCRIPT_PATH)


    elif cmd == "CMD_HARD_RESET_SCRIPT":
        kill_main_script()
        time.sleep(2)
        # Additional reset logic can be added here
        kill_apps()
        ensure_apps_running32()
        time.sleep(3)  # Wait for apps to stabilize

        run_main_script(MAIN_SCRIPT_PATH)

    elif cmd == "CMD_RESTART_RDP":
            os.system("shutdown /r /t 0")
    elif cmd == "CMD_SCREENSHOT":
            # --- TELEGRAM CONFIG ---
            # Replace these with your actual details
            TELE_TOKEN = "8521229618:AAHRmS6xTG3SvlzOvsc6GUOR10RTMC0npTA" #"YOUR_BOT_TOKEN_HERE"
            CHAT_ID = "7670314322" 
            
            pic_path = "status.png"
            pyautogui.screenshot(pic_path)
            print("📸 Screenshot taken. Sending directly to Telegram...")

            try:
                url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendPhoto"
                with open(pic_path, "rb") as photo:
                    payload = {
                        "chat_id": CHAT_ID,
                        "caption": f"📸 *Farm {MY_FARM_ID} Status Report*" ,
                        "parse_mode": "Markdown"
                    }
                    files = {"photo": photo}
                    res = requests.post(url, data=payload, files=files)

                if res.status_code == 200:
                    print("✅ Screenshot sent directly to Telegram.")
                    # Optional: Still notify Redis that it's done
                    r.publish("bot_reports", f"✅ Farm {MY_FARM_ID} screenshot delivered.")
                else:
                    print(f"❌ Telegram API Error: {res.status_code} - {res.text}")

            except Exception as e:
                print(f"⚠️ Direct Upload Error: {e}")
            finally:
                if os.path.exists(pic_path):
                    os.remove(pic_path)

    elif cmd == "CMD_UPDATE_CODE":
        kill_main_script()
        url = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/refs/heads/main/main.py"
        res = requests.get(url)
        with open(MAIN_SCRIPT_PATH, "wb") as f:
            f.write(res.content)
        run_main_script(MAIN_SCRIPT_PATH)

    elif cmd == "CMD_UPDATE_IMAGES":
        if data:
            links = [l.strip() for l in data.split(',')]
            for link in links:
                filename = link.split('/')[-1]
                save_path = os.path.join(MAIN_DIR, filename)
                res = requests.get(link)
                with open(save_path, "wb") as f:
                    f.write(res.content)
            print(f"Updated {len(links)} images.")

    elif cmd == "CMD_RUN_MISC":
        kill_main_script()
        misc_url = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/refs/heads/main/main3.py"
        misc_path = os.path.join(MAIN_DIR, "main3.py")
        res = requests.get(misc_url)
        with open(misc_path, "wb") as f:
            f.write(res.content)
        run_main_script(misc_path)

def listen():
    pubsub = r.pubsub()
    pubsub.subscribe(f"farm_{MY_FARM_ID}")
    print(f"📡 Farm {MY_FARM_ID} Agent Active.")
    
    if AUTOSTART: 
        run_main_script(MAIN_SCRIPT_PATH)
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            raw = message['data']
            cmd, data = raw.split("|", 1) if "|" in raw else (raw, None)
            handle_command(cmd, data)

if __name__ == "__main__":
    listen()
