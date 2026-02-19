
print("Version 10.5.8 loaded.")
import pyautogui
import time
import win32gui
from pywinauto import Desktop
import random
import clipboard
import pygetwindow as gw
import string
import cv2
import numpy as np
import pyautogui
from PIL import Image
import re
import clipboard
from pymongo import MongoClient
import pytesseract
from datetime import datetime
import pytz
import datetime
from PIL import ImageGrab
import win32con
import psutil
import subprocess
import requests
import difflib
import os
Mysterium_Mode = False
time.sleep(99999)

def get_farm_id(filepath="farmid.txt"):
    """Reads and prints the number from farmid.txt."""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read().strip()
            fid = int(content)
            print(f"📍 Current Farm ID: {fid}")
            return fid
    return None

print("Getting Farm ID...")
farm_id = get_farm_id()
print("Farm ID obtained.")
print(f"Farm ID String: {farm_id}")

if farm_id is None:
    print("Error: farmid.txt not found or empty. Defaulting to Farm ID 1.")
    for i in range(59):
        time.sleep(999999)
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

def kill_apps32():
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


ensure_apps_running32()






# =========================
ipqs_key = "Bfg1dzryVqbpSwtbxgWb1uVkXLrr1Nzr"
ipqs_website = ''
ipqs_key_list = []
tuxlermail1 = ''
tuxlermail2 = ''

if farm_id == 1:
    ipqs_key = "BEPgiVi4XCx0URXqigTXonNwsLbkRdez"
    ipqs_key_list = [   'BEPgiVi4XCx0URXqigTXonNwsLbkRdez',
                        'dbc9HvEsf01t7gMOqUfuBAYiCLuypVWw',
                        '8rDBKBsyjRgSLZi5yCQBkH8CeeOsHZ3Q',
                     "8zov88lxoNuxxyJD0kxGGHVEaNz6XxGH"]
    #ipqs_website = "https://miecombee.pythonanywhere.com/check_ip?ip="
    tuxlermail1 = ['captaingranda@gmail.com:RiverSky2711@',
                   'ddilakshi232@gmail.com:RiverSky2711@',            
                   ]

    
if farm_id == 2:
    ipqs_key = "Bfg1dzryVqbpSwtbxgWb1uVkXLrr1Nzr"
    ipqs_key_list =[ "Bfg1dzryVqbpSwtbxgWb1uVkXLrr1Nzr",
                        'HJkgzwepCeYrUmatnhnw44l6jWbN7wf4',
                        'fQWQBoVuB8lPdF4H1w7CgxroPlPy5qJt',
                        'n9XAVMzqrVBnC5m56wEyH6UhkhrZYerX',
                        'UlPZUl4wpmyGMfgOurtJeAsaQWuQ7Aav',
                        'Zh4YINxS8EMCay8zk5kcazvHO7RUr3U2',
                    ]
    #ipqs_website = "https://grandag.pythonanywhere.com/check_ip?ip="

    tuxlermail1 = ['metroboom910@gmail.com:RiverSky2711@',
                   'khabibmakanzie@gmail.com:RiverSky2711@',                
                   ]

if farm_id == 3:
    ipqs_key = "sNNv3D3V9sV6RpUZCE624HG3mBU4LA49"

    ipqs_key_list =  [  
                        'sNNv3D3V9sV6RpUZCE624HG3mBU4LA49',
                        'XkhStwjpwBr1ZdDJVNhGzV15Z4Yypjo8',
                        'PTs1opkyR03frP4WDTpdaJw0lZQqi3am',
                        'fpU11C6VAc3NU9z8ginB0vdwJbwl9N40',
                        'cz8EIxAjXHrjoW0tTAqLmpz6XZmDcwA2',
                        '78tIGyfFpiuC9pVSZKmESYgCxAQVJAUg',
                        'LB2sjKV0VpTE26tzjMAU0TnaqxHPiBaO',
                        'Jd2a3cAV9PJux2q8u4iD4MiOUKtDCDMI',
                        '2bZ4xCzEsqPtICe4vxFQuaqVuEYdxwPV'

                    ]
    
    tuxlermail1 = [
                    'grandkolla@gmail.com:RiverSky2711@',
                    'amberodum721@gmail.com:RiverSky2711@',                
                   ]


if farm_id == 4:
    ipqs_key = "pG8Dc3X2VpOjMPWMuOJEPTLe1i720XzU"


    ipqs_key_list =     ['2l3cJk7GyKFSWu7LZd1clgoE9dvNxWmh',
                        'tm1zWA4hPqJwGB1qikTqbEfUPXlJhhoH',
                        '0mmf279wgUOpytQcOBPkxl7clEhRR26e',
                        'pG8Dc3X2VpOjMPWMuOJEPTLe1i720XzU',
                        'fDE1p8Io25XKrw3oMATMfDUC2ColaYvr',
                        'IRe3aOK3aXEx94pUXenTgzciuDEf7ML7',
                        '0PbcHbEWfyleC3hjhlinvGJFnuIELoBK',
                        '8CpbBqRf5GUr9C0owoS6SJbdhRXJVsXe'
                    ]
    
    tuxlermail1 =  [ 'mcnutthelen8@gmail.com:RiverSky2711@',
                    'gihanfer907@gmail.com:RiverSky2711@',
                    ]
    
###############################################################
if farm_id == 5:
    ipqs_key = "54p3TiceCXhsAhyMXmyjwMoEANIBKAWV"

    ipqs_key_list =  ['54p3TiceCXhsAhyMXmyjwMoEANIBKAWV',
                        'js1IaBOeCXOXMd50DgdlEItOJmLQl6Ds',
                        'NIqMqxIgpVpEbygPhp8lWuNnx1RFgCf8',
                        '6fOFXRU5Fqb4jXYuM5dnW01hsPqwG1Zg',
                        'O29mRZEotzDmSWbfNDiryKpOc0mxIrW8',
                        'xzMwMsRxllx1XNJV5BSUPfyDbO0Urg4b',
                        'gJck1zdD7WF0aiV3Is6sqqDwLkD18bYw',
                        'cMI7YKt6nKk6c314r5MOh62d36BhLCH0',
                        'xLIo7P6vvVi35YMPxMMmwzpuRafjilU6'
                    ]
    
    tuxlermail1 =  [
                    'grandkolla77@gmail.com:RiverSky2711@',
                    'adaavery972@gmail.com:RiverSky2711@']
    

if farm_id == 6:
    ipqs_key = "sNNv3D3V9sV6RpUZCE624HG3mBU4LA49"

    ipqs_key_list =  ['sNNv3D3V9sV6RpUZCE624HG3mBU4LA49',
                    'XkhStwjpwBr1ZdDJVNhGzV15Z4Yypjo8',
                    'PTs1opkyR03frP4WDTpdaJw0lZQqi3am',
                    'fpU11C6VAc3NU9z8ginB0vdwJbwl9N40',
                    'cz8EIxAjXHrjoW0tTAqLmpz6XZmDcwA2',
                    '78tIGyfFpiuC9pVSZKmESYgCxAQVJAUg',

                    'LB2sjKV0VpTE26tzjMAU0TnaqxHPiBaO',
                    'Jd2a3cAV9PJux2q8u4iD4MiOUKtDCDMI',
                    '2bZ4xCzEsqPtICe4vxFQuaqVuEYdxwPV',
                    '2l3cJk7GyKFSWu7LZd1clgoE9dvNxWmh',
                    'tm1zWA4hPqJwGB1qikTqbEfUPXlJhhoH',
                    '0mmf279wgUOpytQcOBPkxl7clEhRR26e'
                    ]
    
    tuxlermail1 = ['ashenrox1997@gmail.com:RiverSky2711@',
                   'redgta36@gmail.com:RiverSky2711@']
if farm_id == 7:
    ipqs_key = "sNNv3D3V9sV6RpUZCE624HG3mBU4LA49"

    ipqs_key_list =  ['sNNv3D3V9sV6RpUZCE624HG3mBU4LA49',
                    'XkhStwjpwBr1ZdDJVNhGzV15Z4Yypjo8',

                    '0mmf279wgUOpytQcOBPkxl7clEhRR26e'
                    ]
    
    tuxlermail1 = ['sumithrohan244@gmail.com:RiverSky2711@',
                   'pererashemi@gmail.com:RiverSky2711@']

if farm_id == 8:
    ipqs_key = "sNNv3D3V9sV6RpUZCE624HG3mBU4LA49"

    ipqs_key_list =  ['sNNv3D3V9sV6RpUZCE624HG3mBU4LA49',
                    'XkhStwjpwBr1ZdDJVNhGzV15Z4Yypjo8',

                    '0mmf279wgUOpytQcOBPkxl7clEhRR26e'
                    ]
    
    tuxlermail1 = ['pererashemi2@gmail.com:RiverSky2711@',
                   'pererashemi3@gmail.com:RiverSky2711@']
    
if farm_id == 9:
    ipqs_key = "sNNv3D3V9sV6RpUZCE624HG3mBU4LA49"

    ipqs_key_list =  ['sNNv3D3V9sV6RpUZCE624HG3mBU4LA49',
                    'XkhStwjpwBr1ZdDJVNhGzV15Z4Yypjo8',

                    '0mmf279wgUOpytQcOBPkxl7clEhRR26e'
                    ]
    
    tuxlermail1 = ['sandrameloson@gmail.com:RiverSky2711@',
                   'sandrameloson1@gmail.com:RiverSky2711@']

if farm_id == 10:
    ipqs_key = "sNNv3D3V9sV6RpUZCE624HG3mBU4LA49"

    ipqs_key_list =  ['sNNv3D3V9sV6RpUZCE624HG3mBU4LA49',
                    'XkhStwjpwBr1ZdDJVNhGzV15Z4Yypjo8',

                    '0mmf279wgUOpytQcOBPkxl7clEhRR26e'
                    ]
    
    tuxlermail1 = ['adaavery972g2@gmail.com:RiverSky2711@',
                   'adaavery972g3@gmail.com:RiverSky2711@']

print("tuxlermail1:", tuxlermail1)
print("Connecting to MongoDB...")
mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"

#client = MongoClient(mongo_uri)

import certifi


client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
db = client['MoneyFarmV10'] 
maindb_collection = db["maindb"]

###################################################
########## Window handling #########################
######################################################
pyautogui.FAILSAFE = False
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
FILENAME = r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\data.txt"


###############################################
def ocr_screen_region(x, y, w, h):
    try:
        left = x
        top = y
        right = x + w
        bottom = y + h

        # Capture
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        
        # OCR
        text = pytesseract.image_to_string(screenshot)
        print("OCR Result:\n", text.strip())
        return text.strip()
    except Exception as e:
        print('OCR ResultER',e)

def ocrcaptchaadlink(x, y, w, h):
    try:
        # --- Coordinates for capture ---
        left = x
        top = y
        right = x + w
        bottom = y + h

        # --- Capture screen region ---
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        cv2.imwrite("screenshot.png", cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR))

        # --- Run PaddleOCR ---
        results = ''#paddleocrg.predict(r"screenshot.png")
        #print(results)

        # --- Extract and return recognized text ---
        for res in results:
            rec_texts = res.get("rec_texts", [])
            for text in rec_texts:
                print("OCR Result:", text)
                return text

        # If no text detected
        print("OCR Result: None")
        return ""

    except Exception as e:
        print("OCR ResultER:", e)
        return ""


def extract_expire_and_location(ocr_text):
    """
    Extract Expiration date and Location changes as integers from OCR text.
    """
    expire = 1
    location_changes = None

    # Regex to find expiration date
    expire_match = re.search(r'Expiration\s*date:\s*(\d+)', ocr_text, re.IGNORECASE)
    if expire_match:
        expire = int(expire_match.group(1))

    # Regex to find location changes
    location_match = re.search(r'Location\s*changes:\s*(\d+)', ocr_text, re.IGNORECASE)
    if location_match:
        location_changes = int(location_match.group(1))

    return expire, location_changes



def add_farm_activity(farmid, country, ipaddress, duration, sites, fingerprints_id, tuxler_left, expiredate):
    """
    Adds a new farm activity record to the MongoDB document with type 'farm_activity'.
    """
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
    # Build new record
    new_record = {
        "farm": farmid,
        "country": country,
        "ip": ipaddress,
        "duration": duration,
        "sites": sites,
        "time": now,  # e.g., "08-24 | 14:10"
        "fingerprint": fingerprints_id
    }

    query = {"type": "farm_activity"}
    update = {"$push": {"records": new_record}}
    


    # Add record or create document if it doesn't exist
    maindb_collection.update_one(query, update, upsert=True)
    print(f"Added farm activity: {farmid}")
    update_farm_stat(farmid, tuxler_left, expiredate )

def update_content_extension():
    pymongo_or_git = 'git'
    if pymongo_or_git == 'pymongo':
        query = {"type": "main"}
        document = maindb_collection.find_one(query)

        if document and "extension_updates" in document:
            js_content = document["extension_updates"]

            # Path to content.js
            file_path = r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\extension\content.js"

            # Write the content to content.js
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(js_content)
            
            print(f"[Success] content.js updated with extension_updates from MongoDB.")
        else:
            print("[Error] No document found or 'extension_updates' field missing.")

    # URL to the raw GitHub file
    url = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/refs/heads/main/content.js"
    
    # Path to your local content.js
    file_path = r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\extension\content.js"

    try:
        # Fetch the content from GitHub
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            js_content = response.text

            # Write the content to content.js
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(js_content)
            
            print(f"[Success] content.js updated from GitHub.")
        else:
            print(f"[Error] Failed to fetch file. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")


        
def convert_numeric(value):
    """
    Convert a value to int or float if it's a numeric string.
    If it's already numeric, leave as is.
    """
    if isinstance(value, str):
        # Try int first
        try:
            return int(value)
        except ValueError:
            # Try float
            try:
                return float(value)
            except ValueError:
                return value  # non-numeric string stays as is
    return value  # already numeric
def update_farm_stat(farmid, tuxler_left, expiredate):

    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
    query = {"type": "farmstat"}
        
    #views_td = maindb_collection.find_one(query)
    #views_td_prev = views_td[f"views_td_farm{farm_id}"]

    # Split into two numbers
    #a, b = views_td_prev.split(" | ")

    # Convert to int and modify
    #a = int(a) + 1   # add 1 → 22 becomes 23
    #b = tuxler_left

    # Rebuild string
    views_td_prev = f"Exp: {expiredate} | Left: {tuxler_left}"
    views_at_prev = views_td_prev
    #views_at_prev = convert_numeric(views_at_prev)
    #views_td_prev +=1
    #views_at_prev +=1
    
    update = {
        "$set": {
            f"lastres_farm{farm_id}": now,
            f"views_td_farm{farm_id}": views_td_prev,
            f"views_at_farm{farm_id}": views_at_prev
        }
    }
    result = maindb_collection.update_one(query, update, upsert=True)
    if result.modified_count:
        print(f"  ? Farm{farm_id}: Updated stats")
    elif result.upserted_id is not None:
        print(f"  ? Farm{farm_id}: Inserted new stats doc ({result.upserted_id})")
    else:
        print(f"  ? Farm{farm_id}: stats already up to date")

    #####################
    query = {"type": "main"}
    mainset = maindb_collection.find_one(query)

    if not mainset:  
        # initialize if doc missing
        mainset = {"views_td": 0, "views_at": 0, "earn_td": 0.0, "earn_at": 0.0}

        # Read values from Mongo document


    # Example usage with your Mongo values
    views_td = convert_numeric(mainset.get("views_td", 0))
    views_at = convert_numeric(mainset.get("views_at", 0))
    earn_td  = convert_numeric(mainset.get("earn_td", 0.0))
    earn_at  = convert_numeric(mainset.get("earn_at", 0.0))


    # Update values
    views_td += 1
    views_at += 1
    earn_td  += 0.025
    earn_at  += 0.025

    # Write back to Mongo
    update = {
        "$set": {
            "views_td": views_td,
            "views_at": views_at,
            "earn_td": earn_td,
            "earn_at": earn_at
        }
    }
    result = maindb_collection.update_one(query, update, upsert=True)

    if result.modified_count:
        print(f"  ? Farm{farm_id}: Updated stats")
    elif result.upserted_id is not None:
        print(f"  ? Farm{farm_id}: Inserted new stats doc ({result.upserted_id})")
    else:
        print(f"  ? Farm{farm_id}: stats already up to date")






#############################################

def human_click(x, y, duration=1):
    # Add random offset between -5 and +5
    rand_x = x + random.randint(-5, 5)
    rand_y = y + random.randint(-5, 5)

    pyautogui.click(rand_x, rand_y, duration=duration)


def close_window_by_name(window_name: str):
    """Closes the first window that matches the given name (case-insensitive)."""
    windows = gw.getWindowsWithTitle(window_name)
    if not windows:
        print(f"No window found with name: {window_name}")
        return False
    
    for win in windows:
        try:
            win.close()
            print(f"Closed window: {win.title}")
            return True
        except Exception as e:
            print(f"Failed to close window: {win.title} | Error: {e}")
    
    return False

def save_variables(var1, var2):
    """Save a pair of variables (IP, ID) to the file."""
    with open(FILENAME, "a") as file:
        file.write(f"{var1} | {var2}\n")
    print(f"Saved: {var1} | {var2}")

def get_ocr_from_screen_area(left, top, width, height, lang='eng'):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    #text = pytesseract.image_to_string(screenshot, lang=lang)
    return text.strip()


def get_focused_window_title():
    hwnd = win32gui.GetForegroundWindow()
    
    return win32gui.GetWindowText(hwnd)
    #text = get_ocr_from_screen_area(65, 6, 185, 35)
    #print("Detected Text:", text)
    #return text

def get_focused_window_id():
    return win32gui.GetForegroundWindow()

def switch_to_window(hwnd):
    """Brings the given window to the foreground if it exists."""
    if win32gui.IsWindow(hwnd):
        win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
        win32gui.ShowWindow(hwnd, 3)  # SW_MAXIMIZE (or similar state)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.5)
        return True
    return False
def close_window(hwnd):
    """Closes the given window by sending WM_CLOSE if it exists."""
    if win32gui.IsWindow(hwnd):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        return True
    return False

def check_windows(hwnd_list):
    """
    Checks if all hwnds in the list still exist.
    Returns a dict with hwnd -> True/False for existence.
    """
    return {hwnd: win32gui.IsWindow(hwnd) for hwnd in hwnd_list}
def color_exists_in_region(target_rgb, region):

    screenshot = pyautogui.screenshot(region=region)
    pixels = screenshot.load()

    width, height = screenshot.size

    for x in range(width):
        for y in range(height):
            if pixels[x, y][:3] == target_rgb:
                screen_x = region[0] + x
                screen_y = region[1] + y
                print(f"Color {target_rgb} found at ({screen_x}, {screen_y})")
                return True
    return False

def region_is_only_color_fast(target_rgb, region):
    screenshot = pyautogui.screenshot(region=region)
    img_array = np.array(screenshot)

    # Compare all pixels to the target color
    return np.all(img_array[:, :, :3] == target_rgb)



#title = get_focused_window_title()    # → returns window title
#print("Focused window title:", title)
#hwnd = get_focused_window_id()       # → returns HWND (int)
#print("Focused window title:", hwnd)
#switch_to_window(hwnd)        # → activates that window

def extract_id_ip(text):
    """Extract ID and IP from a multiline string."""
    id_match = re.search(r'(?i)\bID\b\s*[\n:]*\s*([a-zA-Z0-9]+)', text)
    ip_match = re.search(r'(?i)\bIP\b\s*[\n:]*\s*([\d\.]+)', text)

    if id_match and ip_match:
        extracted_id = id_match.group(1)
        extracted_ip = ip_match.group(1)
        return extracted_id, extracted_ip
    else:
        return None, None

def fingerpint():

    try:
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.typewrite('https://fingerprint.com/demo/')
        pyautogui.press('enter')
        time.sleep(5)
        clipboard.copy("")  # Clear clipboard before starting
        for i in range(15):
            try:
                x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                if x and y: 
                    try:
                        x, y = pyautogui.locateCenterOnScreen('bookmarksggg.png', confidence=0.7)
                        if x and y:
                            pyautogui.rightClick(334,96)
                            time.sleep(1)
                            pyautogui.click(388,573)    
                            time.sleep(1)                
                    except Exception as e:
                        pass
            except Exception as e:
                pass

            pyautogui.click(462,692)
            time.sleep(1)
            pyautogui.mouseDown(462,692)
            time.sleep(1)
            pyautogui.moveTo(578,832, duration=1)
            time.sleep(1)
            pyautogui.mouseUp(578,832)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            ip, id = extract_id_ip(clipboard.paste())
            print(f"Extracted IP: {ip}, ID: {id}")
            if ip and id:
                #save_variables(id, ip)
                return ip
            try:
                x, y = pyautogui.locateCenterOnScreen('error_fingerpitn.png', region=[435,653,603,288], confidence=0.8)
                if x and y:
                    print("Adblock found")
                    pyautogui.press('f5')

            except Exception as e:
                pass
    except Exception as e:
        pass
def focus_and_maximize_window(partial_title):
    try:
        windows = Desktop(backend="uia").windows()
        for win in windows:
            title = win.window_text()
            if partial_title.lower() in title.lower():
                win.set_focus()
                win.maximize()
                print(f"Activated and maximized: {title}")
                return True
        print(f"No matching window found for: {partial_title}")
    except Exception as e:
        print(f"Error: {e}")
def window_exists(partial_title):
    try:
        windows = Desktop(backend="uia").windows()
        for win in windows:
            title = win.window_text()
            if partial_title.lower() in title.lower():
                return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
def focus_and_close_window(partial_title):
    try:
        windows = Desktop(backend="uia").windows()
        for win in windows:
            title = win.window_text()
            if partial_title.lower() in title.lower():
                win.set_focus()
                win.maximize()
                win.close()  # Close the window after maximizing
                print(f"Activated and maximized: {title}")
                return True
        print(f"No matching window found for: {partial_title}")
    except Exception as e:
        print(f"Error: {e}")


def open_detatch_tab():
    focus_and_maximize_window('Chromium')
    time.sleep(1)  # Wait for the window to be focused
    pyautogui.click(290, 22) # New Tab
    time.sleep(1) 
    pyautogui.click(350, 22)
    time.sleep(1) 
    pyautogui.mouseDown(350, 22) # 
    time.sleep(1)  # Hold for 1 second
    pyautogui.moveTo(400, 400, duration=1)
    pyautogui.mouseUp()  # Release the mouse button
    time.sleep(1)
    fid = get_focused_window_id()
    print("Focused window ID:", fid)
    return fid


def generate_username():
    # Generate 7 random lowercase letters
    letters = ''.join(random.choices(string.ascii_lowercase, k=7))
    # Generate 3 random digits
    numbers = ''.join(random.choices(string.digits, k=3))
    return letters + numbers

def create_new_fingerprint_browser(settings = False):
    partial_title = 'Undetectable'
    windows = gw.getWindowsWithTitle(partial_title)
    if windows:
        win = windows[0]
        win.activate()
        time.sleep(1)  # Allow time for window to activate
        win.moveTo(300, 200)
        print("Window moved and resized.")
        time.sleep(1)
        pyautogui.rightClick(540,397) #option rightclick
        time.sleep(3)
        pyautogui.click(590,730) # Delete
        time.sleep(3)
        pyautogui.click(1060,508) # Yeas
        time.sleep(2)
        pyautogui.click(460,325) # Click on the 'Create New Profile' button
        time.sleep(2)
        pyautogui.click(460,325) # Click on the 'Create New Profile' button
        time.sleep(2)

        if settings:
            pyautogui.click(753, 367)  # poxy
            time.sleep(1)
            pyautogui.click(795, 474) #options
            time.sleep(1)
            pyautogui.click(795, 516) #NO PROXY
            time.sleep(1)


            pyautogui.click(815, 369)  # fingerpint
            time.sleep(1)
            pyautogui.click(715, 455)  # emulation
            time.sleep(1)
            pyautogui.click(940, 555)  # geo optio
            time.sleep(1)
            pyautogui.click(940, 650)  # off
            time.sleep(1)
            pyautogui.click(940, 630)  # timezone option
            time.sleep(1)
            pyautogui.click(940, 720)  # timezone
            time.sleep(1)

            pyautogui.click(795, 455)  # emulation
            time.sleep(1)
            pyautogui.click(940, 658)  # window size options
            time.sleep(1)
            pyautogui.click(940, 725)  # window size system
            time.sleep(1)
            
            pyautogui.click(875, 455)  # Noises
            time.sleep(1)
            pyautogui.click(950, 500) #canvas
            time.sleep(1)
            pyautogui.click(950, 540) #click canvas noise
            time.sleep(1)
            pyautogui.click(950, 555) #audio
            time.sleep(1)
            pyautogui.click(950, 595) #click audio noise
            time.sleep(1)
            pyautogui.click(950, 610) #webgl
            time.sleep(1)
            pyautogui.click(950, 650) #click webgl noise
            time.sleep(1)
            pyautogui.click(950, 665) #clientrect
            time.sleep(1)
            pyautogui.click(950, 705) #click clientrect noise
            time.sleep(1)

        pyautogui.click(770, 263)  # Name
        time.sleep(1)
        username = generate_username()
        print("Generated username:", username)
        pyautogui.typewrite(username)
        time.sleep(1)

        pyautogui.click(980, 860)  # Open

    else:
        print(f"No window found with title containing '{partial_title}'")


def create_browser_old():
    created = False
    for i in range(50):
        print('goin again',i)

        time.sleep(1)
        try:
            focus_and_maximize_window('MoreLogin')
            time.sleep(1)  # Wait for the window to be focused
            try:
                x, y = pyautogui.locateCenterOnScreen('stop_browser.png', region=[438,115,662,320], confidence=0.95)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
                    continue
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('stop_browser2.png', region=[438,115,662,320], confidence=0.95)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
                    continue
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('del_confrim.png', region=[940,190,345,170], confidence=0.95)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
                    continue
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('igotit_browser.png', region=[695,115,625,215], confidence=0.95)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(3)
                    pyautogui.click(78, 295)  #emulation
                    time.sleep(2)
                    continue
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('start_browser.png', region=[438,115,662,320], confidence=0.95)
                if x and y:
                    if created == True:
                        pyautogui.click(x,y)
                        time.sleep(5)
                        return True

                    pyautogui.click(812, 221)
                    time.sleep(1)
                    pyautogui.click(787, 532) 
                    time.sleep(1)
                    pyautogui.moveTo(787, 532) 
                    time.sleep(1)
                    pyautogui.click(787, 532, duration=1)  # Hold the mouse button down
                    time.sleep(3)
                    pyautogui.click(1150, 267)
                    time.sleep(7)
                    continue
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('start_browser2.png', region=[438,115,662,320], confidence=0.95)
                if x and y:
                    if created == True:
                        pyautogui.click(x,y)
                        time.sleep(5)
                        return True

                    pyautogui.click(768, 221)
                    time.sleep(1)
                    pyautogui.click(768, 532) 
                    time.sleep(1)
                    pyautogui.moveTo(768, 532) 
                    time.sleep(1)
                    pyautogui.click(768, 532, duration=1)  # Hold the mouse button down
                    time.sleep(3)
                    pyautogui.click(1150, 267)
                    time.sleep(7)
                    continue
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('empty_browser.png', region=[575,460,1033,345], confidence=0.8)
                if x and y:
                    pyautogui.click(101, 137)  # Click on the 'Create New Profile' button
                    time.sleep(2)
                    pyautogui.click(437, 183) #advaced
                    time.sleep(5)
            except Exception as e:
                pass

            
            try:
                x, y = pyautogui.locateCenterOnScreen('setting_browser.png', region=[165,205,730,545], confidence=0.7)
                if x and y:
                    time.sleep(2)
                    pyautogui.click(408,853)
                    time.sleep(1)
                    pyautogui.click(1750, 178)  #fingerprint
                    time.sleep(5)
                    pyautogui.click(1208, 267) #proxy
                    time.sleep(1)
                    pyautogui.click(340, 645)  #detect proxy
                    time.sleep(3)


                    for i in range(7):
                        pyautogui.moveTo(100, 100)
                        try:
                            x, y = pyautogui.locateCenterOnScreen('lang_eng.png', region=[244,335,645,637], confidence=0.7)
                            if x and y:
                                break
                        except Exception as e:
                            pyautogui.click(1218, 385) 
                            time.sleep(3)
                            pyautogui.click(401, 650)  #lang
                            time.sleep(3)

                    pyautogui.click(394, 984)  #emulation
                    time.sleep(8)
                    pyautogui.click(78, 295)  #emulation
                    time.sleep(3)
                    created = True
            except Exception as e:
                pass

            
            #pyautogui.click(750, 376)  #emulation
            #pyautogui.click(750, 225)  #emulation
            #time.sleep(5)
        except Exception as e:
            print(f"Error creating browser: {e}")
            return False

def always_active():
    open_link(link = 'chrome-extension://ehllkhjndgnlokhomdlhgbineffifcbj/data/options/index.html',newtab = False)
    time.sleep(3)
    pyautogui.click(850, 559)  # C
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')  # Select all text
    pyautogui.press('backspace')  # Clear the text
    pyautogui.typewrite('*')
    time.sleep(0.5)
    pyautogui.click(547, 916)  # C
    time.sleep(1)
    pyautogui.click(547, 874)  # C
    time.sleep(1)

def get_next_account(file_path= f"adspower_acc.txt"):
    accounts = []
    
    # Read accounts
    with open(file_path, "r") as f:
        accounts = [line.strip() for line in f if line.strip()]
    
    # Separate used/unused accounts
    unused = [acc for acc in accounts if not acc.endswith(" [USED]")]
    used = [acc for acc in accounts if acc.endswith(" [USED]")]
    
    # If all are used -> reset file
    if not unused:
        accounts = [acc.replace(" [USED]", "") for acc in accounts]
        with open(file_path, "w") as f:
            f.write("\n".join(accounts) + "\n")
        unused = accounts
    
    # Take first unused
    next_account = unused[0]
    email, password = next_account.replace(" [USED]", "").split(":", 1)
    
    # Mark it as used in file
    updated_accounts = []
    used_flag = False
    for acc in accounts:
        if acc.replace(" [USED]", "") == next_account and not used_flag:
            updated_accounts.append(acc.replace(" [USED]", "") + " [USED]")
            used_flag = True
        else:
            updated_accounts.append(acc)
    
    # Write back updated list
    with open(file_path, "w") as f:
        f.write("\n".join(updated_accounts) + "\n")
    
    return email, password

def myst_disconnect():
    focus_mysterium()
    time.sleep(2)
    try:
        x, y = pyautogui.locateCenterOnScreen('myst_disconnect.png', confidence=0.9)
        if x and y:
            pyautogui.click(x, y)
            time.sleep(2)
            
    except Exception as e:
        pass
def switch_adspower():
    #tuxler OFF
    
    if Mysterium_Mode:
        myst_disconnect()
        time.sleep(2)
    else:
        tuxler_switch = True
        while tuxler_switch == True:
            focus_tuxler()
            time.sleep(2)
            pyautogui.click(326,720)
            
            
            time.sleep(1)
            pyautogui.click(326,757)
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_on.png', confidence=0.9)
                if x and y:
                    pyautogui.click(x, y)
                    time.sleep(2)
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
                if x and y:
                    tuxler_switch = False
                    
            except Exception as e:
                print('tuxler off not found')
                print('tuxler off not found')
                pyautogui.hotkey('alt','tab')
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)
    focus_and_maximize_window('AdsPower')
    time.sleep(1)
    pyautogui.click(1227,141)
    time.sleep(1)
    pyautogui.click(1070,272)
    time.sleep(2)

    #Log out 
    print("Logging out AdsPower1")
    logoutadspower = False
    for i in range(50):
        if logoutadspower:
            print("Logged out AdsPower2")
            break
        try:
            x, y = pyautogui.locateCenterOnScreen('login_adspowr.png', confidence=0.9)
            if x and y:
                logoutadspower = True
                
        except Exception as e:
            print('Trying to Logout')
        pyautogui.click(1816,79)
        time.sleep(1)
        pyautogui.click(1805,335)
        time.sleep(3)
        pyautogui.click(1200,256)

    print("getting new account")
    mail, pw = get_next_account()
    print(mail, pw)
    print("Entering new account AdsPower")
    #Enter Mail /PAss
    pyautogui.click(1371,240) #e-mail
    time.sleep(0.4)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    clipboard.copy(mail)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pyautogui.click(1371,323) #pass
    time.sleep(0.4)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    clipboard.copy(pw)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pyautogui.click(1236,375) #Remember
    time.sleep(0.4)
    pyautogui.click(1396,421)
    time.sleep(5)
    return True

# Your Chrome executable path
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Your Chrome profile path
PROFILE_PATH = r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default"


def open_chrome():
    """Open Chrome with the given profile"""
    cmd = [CHROME_PATH, f'--user-data-dir={PROFILE_PATH}']
    process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Chrome is starting...")
    return process

def wait_for_chrome(timeout=10):
    """Wait until Chrome is running (or timeout)"""
    start = time.time()
    while time.time() - start < timeout:
        for proc in psutil.process_iter(attrs=['name']):
            if proc.info['name'] and 'chrome.exe' in proc.info['name'].lower():
                print("Chrome is running.")
                return True
        time.sleep(0.5)
    print("Timeout: Chrome did not start.")
    return False

def close_chrome():
    """Close all Chrome processes"""
    closed = False
    for proc in psutil.process_iter(attrs=['name']):
        if proc.info['name'] and 'chrome.exe' in proc.info['name'].lower():
            try:
                proc.terminate()
                closed = True
            except Exception as e:
                print("Error closing Chrome:", e)
    if closed:
        print("Chrome closed.")
    else:
        print("No Chrome process found.")


def is_sunbrowser_open():
    for process in psutil.process_iter(['name']):
        if process.info['name'] and 'sunbrowser' in process.info['name'].lower():
            return True
    return False

def create_browser():
    created = False
    focus_and_close_window('SunBrowser')
    focus_and_close_window('SunBrowser')
    focus_and_close_window('SunBrowser')
    focus_and_close_window('SunBrowser')
    tuxler_switch = True
    global ipqs_key
    global location_changes
    if Mysterium_Mode:
        myst_disconnect()
        time.sleep(2)
    else:
        while tuxler_switch == True:
            focus_tuxler()
            if location_changes >= 100:
                return None
            time.sleep(2)
            pyautogui.click(326,720)
            
            
            time.sleep(1)
            pyautogui.click(326,757)
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_on.png', confidence=0.9)
                if x and y:
                    pyautogui.click(x, y)
                    time.sleep(2)
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
                if x and y:
                    tuxler_switch = False
                    
            except Exception as e:
                print('tuxler off not found')
                print('tuxler off not found')
                pyautogui.hotkey('alt','tab')
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)
            
    for i in range(50):
        print('goin again',i)

        time.sleep(1)
        try:
            focus_and_maximize_window('AdsPower')
            time.sleep(1)  # Wait for the window to be focused

            try:
                x, y = pyautogui.locateCenterOnScreen('stop_browser_adspower.png', region=[1645,205,275,400], confidence=0.95)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
                    continue
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('closead_adspower3.png',  confidence=0.95)
                if x and y:
                    print('blackfri closea')
                    #pyautogui.click(x, y)
                    #time.sleep(1)
                    
                    pyautogui.click(1308, 260)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('closead_adspower4.png',  confidence=0.95)
                if x and y:
                    print('blackfri closea2')
                    #pyautogui.click(x, y)
                    #time.sleep(1)
                    
                    pyautogui.click(1323, 217)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('paywall_adpower.png',  confidence=0.9)
                if x and y:
                    pyautogui.click(98, 208)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('bindauthe_adpower2.png',  confidence=0.98)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('skip_adspower.png', region=[213,87,551,664], confidence=0.98)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('closeAdspowr.png', region=[1775,852,146,180], confidence=0.98)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(2)
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('close_privaymsg.png', region=[1611,100,309,228],confidence=0.9)
                if x and y:
                    print("adpoower Close X on Privacy")
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(5)
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('bind_autora.png',confidence=0.9)
                if x and y:
                    print("bind_autora Close X on Privacy")
                    pyautogui.click(x, y)
                    time.sleep(5)
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('close_adspowerg.png',  region=[922,202,528,265],confidence=0.99)
                if x and y:
                    print("close_adspowerg Close X on Privacy")
                    pyautogui.click(1187, 317)
                    time.sleep(5)
                    pyautogui.click(88,206)
                    time.sleep(1)
                    continue
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('bindaumsg.png', confidence=0.8)
                if x and y:
                    print("bindaumsg Close X on Privacy")
                    pyautogui.click(1325, 140)
                    time.sleep(5)
                    pyautogui.click(88,206)
                    time.sleep(1)
                    continue
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('settings_preferences.png', confidence=0.8)
                if x and y:
                    print("settings_preferences Close X on Privacy")
                    pyautogui.click(1325, 140)
                    time.sleep(5)
                    pyautogui.click(88,206)
                    time.sleep(1)
                    continue
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('limit_adpower.png', region=[927,173,480,260],confidence=0.9)
                if x and y:
                    print("adpower browser Limited")
                    switch_adspower()
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('login_adspowr.png', confidence=0.9)
                if x and y:
                    print("adpower browser Limited")
                    switch_adspower()
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('okk_adspowre.png', region=[950,154,430,230],confidence=0.9)
                if x and y:
                    print("OKKK")
                    pyautogui.click(x,y)
                    time.sleep(5)
                    if Mysterium_Mode:
                        myst_disconnect()
                        time.sleep(2)
                    else:
                        tuxler_switch = True
                        while tuxler_switch == True:
                            focus_tuxler()
                            time.sleep(2)
                            pyautogui.click(326,720)
                            
                            
                            time.sleep(1)
                            pyautogui.click(326,757)
                            try:
                                x, y = pyautogui.locateCenterOnScreen('tuxler_on.png', confidence=0.9)
                                if x and y:
                                    pyautogui.click(x, y)
                                    time.sleep(2)
                                    
                            except Exception as e:
                                pass
                            try:
                                x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
                                if x and y:
                                    tuxler_switch = False
                                    
                            except Exception as e:
                                print('tuxler off not found')
                                print('tuxler off not found')
                                pyautogui.hotkey('alt','tab')
                                time.sleep(1)
                                pyautogui.press('esc')
                                time.sleep(1)
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('del_confrim_adspower.png', confidence=0.95)
                if x and y:
                    pyautogui.click(689,296)
                    time.sleep(1)
                    pyautogui.click(1160,473)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(2)
                    continue
            except Exception as e:
                pass


            try:
                x, y = pyautogui.locateCenterOnScreen('start_browser_adspower.png', region=[1675,260,245,105], confidence=0.95)
                if x and y:
                    if created == True:
                        
                        tuxler_changer()
                        time.sleep(0.2)
                        focus_and_close_window('pythonanywhere')
                        focus_and_close_window('proxycheck')

                        focus_and_close_window('Google Chrome')
                        focus_and_close_window('New Tab')
                        focus_and_close_window('ipqualityscore')
                        close_chrome()
                        open_chrome()
                        wait_for_chrome(timeout=15)
                        focus_and_maximize_window("Google Chrome")
                        focus_and_maximize_window("New Tab")
                        time.sleep(5)
                        pyautogui.click(250, 64)
                        time.sleep(1)
                        open_link(link=f'https://api.ipify.org/', newtab=False)
                        time.sleep(5)
                        pyautogui.click(200, 219)
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl', 'a')
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl', 'c')
                        time.sleep(0.5)
                        ipaddress = clipboard.paste()
                        stringtg = """
Search Google or type a URL
"""
                        if stringtg in ipaddress or ipaddress in stringtg:
                            for i in range(8):
                                time.sleep(3)
                                pyautogui.click(200, 219)
                                time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'c')
                                time.sleep(0.5)
                                ipaddress = clipboard.paste()
                                if stringtg not in ipaddress and ipaddress not in stringtg:
                                    break
                        if ipaddress:
                            pass
                        else:
                            for i in range(5):
                                time.sleep(2)
                                pyautogui.click(200, 219)
                                time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'c')
                                time.sleep(0.5)
                                ipaddress = clipboard.paste()
                                if ipaddress:
                                    break

                        result = ipcheck_handle(ipaddress)

                        if result:
                            ip = result["ip"]
                            is_clean = result["is_clean"]
                            proxy_type = result["type"]
                            country = result["country"]
                            print(ip, is_clean, proxy_type, country)
                            if is_clean:
                                if Mysterium_Mode:

                                    ipqs_url = f"{ipqs_website}{ip}"
                                    open_link(link=ipqs_url, newtab=False)
                                    time.sleep(5)
                                    pyautogui.click(200, 219)
                                    time.sleep(0.5)
                                    pyautogui.hotkey('ctrl', 'a')
                                    time.sleep(0.5)
                                    pyautogui.hotkey('ctrl', 'c')
                                    time.sleep(0.5)
                                    data_copied = clipboard.paste()
                                    if data_copied:
                                        pass
                                    else:
                                        for i in range(5):
                                            pyautogui.click(200, 219)
                                            time.sleep(0.5)
                                            pyautogui.hotkey('ctrl', 'a')
                                            time.sleep(0.5)
                                            pyautogui.hotkey('ctrl', 'c')
                                            time.sleep(0.5)
                                            data_copied = clipboard.paste()
                                            if data_copied:
                                                break
                                    if '"success":false' in data_copied or data_copied in '"success":false' or data_copied in 'API issue':
                                        print("success false from ipqualityscore")

                                        valid_key = False
                                        if valid_key == False:
                                            # If no valid item found
                                            print("No valid items found.")
                                            time.sleep(7200)
                                            return False



                                    ip_data = json.loads(data_copied)
                                    print(ip_data)
                                    close_chrome()
                                    focus_and_close_window('Google Chrome')
                                    focus_and_close_window('New Tab')
                                    focus_and_close_window('ipqualityscore')
                                    focus_and_close_window('pythonanywhere')
                                    focus_and_close_window('proxycheck')
                                    
                                    time.sleep(0.5)
                                    #country = ip_data.get("country_code", "N/A")
                                    is_vpn = ip_data.get("vpn")
                                    is_proxy = ip_data.get("proxy")
                                    fraud_score = ip_data.get("fraud_score")
                                    print(f" VPN: {is_vpn}, Proxy: {is_proxy}, Fraud Score: {fraud_score}")

                                    if is_vpn == False and is_proxy == False and fraud_score < 30:
                                        print("Good IP")
                                        focus_and_maximize_window('AdsPower')
                                        time.sleep(2)
                                        pyautogui.click(x,y)
                                        time.sleep(0.2)
                                        pyautogui.click(x,y)
                                        time.sleep(5)
                                        return True
                                    else:
                                        print("Bad IP")
                                        continue
                                else:
                                    try:
                                        print("cHECKING iP  with IPQS")
                                        ip_data = metrics24_lookups(ip)
                                        #if 'no_key' == ipqs_key:
                                            # If no valid item found
                                        #    print("No valid items found.")
                                        #    time.sleep(7200)
                                        #    return False
                                        if ip_data:
                                            close_chrome()
                                            focus_and_close_window('Google Chrome')
                                            focus_and_close_window('New Tab')
                                            focus_and_close_window('ipqualityscore')
                                            focus_and_close_window('pythonanywhere')
                                            focus_and_close_window('proxycheck')
                                            
                                            print("Good IP")
                                            focus_and_maximize_window('AdsPower')
                                            time.sleep(2)
                                            pyautogui.click(x,y)
                                            time.sleep(7)
                                            pyautogui.click(x,y)
                                            time.sleep(5)
                                            return True
                                        else:
                                            print("Bad IP")
                                            continue

                                    except Exception as e:
                                        print("Error during IPQS lookup:", e)
                                        continue




                    pyautogui.click(1870,286)
                    time.sleep(1)

                    pyautogui.moveTo(1826,388) 
                    time.sleep(1)
                    pyautogui.click(1826,388)  # Hold the mouse button down
                    time.sleep(7)
                    continue
            except Exception as e:
                pass



            try:
                x, y = pyautogui.locateCenterOnScreen('empty_browser_adspower.png', region=[276,256,215,140], confidence=0.99)
                if x and y:
                    pyautogui.click(105,144)  # Click on the 'Create New Profile' button
                    time.sleep(5)
            except Exception as e:
                pass

            
            try:
                x, y = pyautogui.locateCenterOnScreen('setting_browser_adspower.png', confidence=0.9)
                if x and y:
                    time.sleep(1)
                    pyautogui.click(1784,208)
                    time.sleep(5)
                    try:
                        x, y = pyautogui.locateCenterOnScreen('ok_adspower.png',  confidence=0.9)
                        if x and y:
                            pyautogui.click(572,265)
                            time.sleep(3)
                            pyautogui.click(478,342)
                            time.sleep(1)
                            pyautogui.click(x,y , duration=1)
                            time.sleep(7)

                            created = True

                            
                    except Exception as e:
                        pass
            except Exception as e:
                pass

        except Exception as e:
            print(f"Error focusing window: {e}")
            


traffic_links2 = [
    'web.telegram.org/a/get',
    #'forums.animeuknews.net',
    #'novanon.net',
    'pinpaste.com',
    'reddit.com',
    'web.telegram.org/a/get',
    #'quora.com',
    #'site.trooporiginals.cloud',
    #'anime-planet.com',
    #'animekai.to/home',
    #'tiktok.com',
    #'blog.discoveruniversal.com',
    'web.telegram.org/a/get',
    'web.telegram.org/a/get',

    #'pinpaste.com',
    #'reddit.com',
    #'memoryhackers.org',
    'web.telegram.org/a/get',
    #'hey-gamer.com',
    #'joyfreak.com',
    #'hardforum.com',
    #'codepen.io',
    #'pinpaste.com',
    'pubnotepad.com',
    #'pubnotepad.com',
]
traffic_links = [
    'web.telegram.org/a/get',
    'pinpaste.com',
    'pubnotepad.com',
]

def random_link(link_type):
    # 90% chance for web.telegram.org/a/get
    if random.random() < 0.95:   # 0.9 = 90%
        site = 'web.telegram.org/a/get'
    else:
        site = random.choice([s for s in traffic_links if s != 'web.telegram.org/a/get'])
    
    return f"{site}#{link_type}"



#create_new_fingerprint_browser('timezone')
##################################################
########## Browser handling ## ######################
########################################################

def open_link(link = 'google.com',newtab = False):
    if newtab:
        pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)
    #pyautogui.typewrite(link)
    clipboard.copy(link)  # Copy the link to clipboard
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for the page to load
    return True

def configure_rektcaptcha():
    for i in range(30):
        time.sleep(2)
        print('waiting', i)
        try:
            x, y = pyautogui.locateCenterOnScreen('rek_off.png', region=[1524,146,396,77], confidence=0.9)
            if x and y:
                pyautogui.click(x, y)
                time.sleep(1)
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('rek_off.png', region=[1524,237,396,77], confidence=0.9)
            if x and y:
                pyautogui.click(x, y)
                time.sleep(1)
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('rek_onnn.png', region=[1636,112,284,242], confidence=0.9)
            if x and y:
                pyautogui.click(493,19, duration = 0.4)
                print("Rektcaptcha configured")
                return True
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('rektcaptcha_icon.png', region=[1653,31,261,61], confidence=0.9)
            if x and y:
                pyautogui.click(x, y)
                time.sleep(4)
                for i in range(8):
                    time.sleep(1)
                    try:
                        x, y = pyautogui.locateCenterOnScreen('rek_off.png', region=[1524,146,396,77], confidence=0.9)
                        if x and y:
                            pyautogui.click(x, y)
                            time.sleep(1)
                    except Exception as e:
                        pass
                    try:
                        x, y = pyautogui.locateCenterOnScreen('rek_off.png', region=[1524,237,396,77], confidence=0.9)
                        if x and y:
                            pyautogui.click(x, y)
                            time.sleep(1)
                    except Exception as e:
                        pass
                    try:
                        x, y = pyautogui.locateCenterOnScreen('rek_onnn.png', region=[1636,112,284,242], confidence=0.9)
                        if x and y:
                            pyautogui.click(493,19, duration = 0.4)
                            print("Rektcaptcha configured")
                            return True
                    except Exception as e:
                        pass
        except Exception as e:
            print("Rektcaptcha not found:", e)


def close_ads2():
    #pyautogui.click(493,19, duration = 0.4)
    close_window_by_name("Save As") 
    for i in range(5):
        try:
            x, y = pyautogui.locateCenterOnScreen('newcloseadas2.png', region=[1151,204,227,450] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=0.3)
                time.sleep(0.5)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(0.5)
                 
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('newcloseadas.png', region=[1151,204,227,350] ,confidence=0.95)
            if x and y:
                human_click(x, y, duration=0.3)
                time.sleep(0.5)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(0.5)
                 
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('cancelads2.png' ,confidence=0.95)
            if x and y:
                human_click(x, y, duration=0.3)
                time.sleep(0.5)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(0.5)
                 
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('cancelads1.png' ,confidence=0.95)
            if x and y:
                human_click(x, y, duration=0.3)
                time.sleep(0.5)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(0.5)
                 
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('js_ok.png', region=[930,130,342,165] ,confidence=0.95)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(2)
                pyautogui.click(95, 62)  # Click on the 'No Internet' button
                time.sleep(2)
                return 
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('reload_confrim.png', region=[930,130,342,165] ,confidence=0.95)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(2)
                pyautogui.click(95, 62)  # Click on the 'No Internet' button
                time.sleep(2)
                return 
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('mini_popup_close.png', region=[705,463,515,232] ,confidence=0.97)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('unloaded_adclose.png', region=[705,463,515,232] ,confidence=0.97)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad2.png', region=[1108,168,92,463] ,confidence=0.97)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad7.png', region=[1335,733,260,145] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('closeadgoogle511.png' ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=0.2)
                time.sleep(0.6)
                pyautogui.click(493,19, duration = 0.2)
                time.sleep(0.6)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad17.png', region=[1680,45,280,280] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('consent.png', region=[920,722,344,83] ,confidence=0.9)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ads19.png', region=[1194,256,192,167] ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.2)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad75.png', region=[1335,733,260,145] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('agreevalue.png', region=[908,586,1012,465] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('block_js.png', region=[186,80,320,165] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                return
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ads_gg.png', region=[1280,229,223,660] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad6.png', region=[1280,229,223,660] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad3.png', region=[1836,55,85,98] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad4.png', region=[1780,85,135,138] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad5.png', region=[876,527,484,413] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad8.png', region=[876,527,484,413] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('close_ad9.png', region=[1083,108,360,865] ,confidence=0.98)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen('closeadsgoogleg.png' ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.4)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass       
        try:
            x, y = pyautogui.locateCenterOnScreen('adclosegoogle2g.png' ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.4)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass            
        try:
            x, y = pyautogui.locateCenterOnScreen('closeadsgloogle2g.png' ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.4)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass  
        try:
            x, y = pyautogui.locateCenterOnScreen('closegoolge3.png' ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.4)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass  
        try:
            x, y = pyautogui.locateCenterOnScreen('closeadg23.png' ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.4)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass  

        try:
            x, y = pyautogui.locateCenterOnScreen('closeads321.png' ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.4)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass 


        try:
            x, y = pyautogui.locateCenterOnScreen('closeadsgootrans.png' ,confidence=0.98)
            if x and y:
                pyautogui.click(x, y, duration=0.4)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                continue
        except Exception as e:
            pass 
        try:
            x, y = pyautogui.locateCenterOnScreen('adremoved.png' ,confidence=0.98)
            if x and y:
                pyautogui.press('f5')
                time.sleep(2)
                continue
        except Exception as e:
            pass  
        return False






def close_ads():
    # 1. Configuration: Put your images and their specific regions in a list
    # Format: (image_name, region_or_None, confidence)
    close_window_by_name("Save As") 
    ad_resources = [
            ('newcloseadas2.png', [1151, 204, 227, 450], 0.98),
            ('newcloseadas.png', [1151, 204, 227, 350], 0.95),
            ('js_ok.png', [930, 130, 342, 165], 0.99),
            ('reload_confrim.png', [930, 130, 342, 165], 0.99),
            ('mini_popup_close.png', [705, 463, 515, 232], 0.97),
            ('unloaded_adclose.png', [705, 463, 515, 232], 0.97),
            ('close_ad2.png', [1108, 168, 92, 463], 0.97),
            ('close_ad7.png', [1335, 733, 260, 145], 0.98),
            ('close_ad17.png', [1680, 45, 280, 280], 0.98),
            ('consent.png', [920, 722, 344, 83], 0.9),
            ('close_ads19.png', [1194, 256, 192, 167], 0.98),
            ('close_ad75.png', [1335, 733, 260, 145], 0.98),
            ('agreevalue.png', [908, 586, 1012, 465], 0.98),
            ('block_js.png', [186, 80, 320, 165], 0.99),
            ('close_ads_gg.png', [1280, 229, 223, 660], 0.98),
            ('close_ad6.png', [1280, 229, 223, 660], 0.98),
            ('close_ad3.png', [1836, 55, 85, 98], 0.98),
            ('close_ad4.png', [1780, 85, 135, 138], 0.98),
            ('close_ad5.png', [876, 527, 484, 413], 0.98),
            ('close_ad8.png', [876, 527, 484, 413], 0.98),
            ('close_ad9.png', [1083, 108, 360, 865], 0.98),
            # Global searches (No region specified in your old code)
            ('cancelads2.png', None, 0.95),
            ('cancelads1.png', None, 0.95),
            ('closeadgoogle511.png', None, 0.98),
            ('closeadsgoogleg.png', None, 0.98),
            ('adclosegoogle2g.png', None, 0.98),
            ('closeadsgloogle2g.png', None, 0.98),
            ('closegoolge3.png', None, 0.98),
            ('closeadg23.png', None, 0.98),
            ('closeads321.png', None, 0.98),
            ('closeadsgootrans.png', None, 0.98),
            
        ]

    for i in range(5):
        print(f"Attempt {i+1} to close ads...")
        
        # 2. THE SECRET SAUCE: Take ONE screenshot for the whole loop
        # This prevents taking 30 separate screenshots
        full_screen = pyautogui.screenshot()

        for img_name, reg, conf in ad_resources:
            try:
                # 3. Search WITHIN the screenshot we already took
                # Use grayscale=True for 30% more speed
                match = pyautogui.locate(img_name, full_screen, region=reg, confidence=conf)
                
                if match:
                    print(f"Found {img_name} on attempt {i+1}")
                    x, y = pyautogui.center(match)
                    
                    # Logic for special buttons (JS/Reload/Block)
                    if img_name in ['js_ok.png', 'reload_confrim.png', 'block_js.png']:
                        pyautogui.click(x, y, duration=0.1)
                        time.sleep(2)
                        if img_name == 'block_js.png': 
                            pyautogui.click(x, y, duration=0.1) 
                            time.sleep(1)
                        #pyautogui.click(95, 62)
                        return True
                    
                    # Logic for Page Refresh


                    # Standard Ad Click Flow
                    if img_name in ['closeadgoogle511.png', 'close_ads19.png']:
                        # These had faster durations in your old code
                        pyautogui.click(x, y, duration=0.2)
                        time.sleep(0.6)
                        pyautogui.click(493, 19, duration=0.2)
                    else:
                        human_click(x, y, duration=0.3 if 'cancel' in img_name else 1)
                        time.sleep(0.5 if 'cancel' in img_name else 1)
                        pyautogui.click(493, 19, duration=0.4)
                    
                    time.sleep(1)
                    break # Found one, break to re-scan with fresh screenshot

            except Exception:
                continue
                
        return False




def facebook_leaving():
    title = get_focused_window_title()
    if 'Leaving Facebook' in title:
        pyautogui.scroll(500)
        time.sleep(1)
        pyautogui.click(1090, 820)  # Click on the 'Leave' button
        time.sleep(1)
        pyautogui.click(1117, 460)


def destined_reached(text):
    keywords = [
        '405 Not Allowed',
        '502 Bad Gateway',
        'This link is risky',
        'Database Error',
        'Privacy Error',
        '503 Service',
        '504: Gateway',
        '500 Internal',
        "A timeout occurred"






    ]
    return any(keyword.lower() in text.lower() for keyword in keywords)

    
def focus_tuxler():
    windows = gw.getWindowsWithTitle("Tuxler")
    if not windows:
        print("Tuxler window not found.")
        return

    win = windows[0]
    try:
        if win.isMinimized:
            win.restore()
        win.activate()

        # Move window to position (e.g., top-left corner)
        win.moveTo(100, 100)  # You can change this to any (x, y)

        print(f"Focused and moved: {win.title}")
    except Exception as e:
        print(f"Activation failed, trying manual click: {e}")
        try:
            win_x, win_y = win.topleft
            win_w, win_h = win.width, win.height
            pyautogui.click(win_x + win_w // 2, win_y + 10)  # Click title bar
            win.moveTo(100, 100)  # Try to move even after manual click
            print("Clicked and moved manually.")
        except Exception as e2:
            print(f"Manual click or move failed: {e2}")


def focus_mysterium():
    focus_and_maximize_window("Mysterium")



def get_random_country():
    # Country list with their probabilities
    countries = {
        "Germany": 90,
        "United Kingdom": 90,
        "Canada": 90,
        "Australia": 90,
        "United States": 70,
        "France": 70,
        "Argentina": 70,
        "Italy": 65,
        "Brazil": 60,
        "India": 60,
        "Indonesia": 60,
        "Philippines": 50,
        "Netherlands": 60,
        "Greece": 60,
        "Hungary": 60,
        #"Mexico": 50,
        "Spain": 50,
        "Denmark": 45,
        "Norway": 45,
        "Belgium": 45,
        "Nigeria": 40,
        #"Sweden": 40,
        "Ireland": 30,
        #"New Zealand": 50,
        "WorldWide": 20
    }



    countries_list = list(countries.keys())
    weights = [w / 100 for w in countries.values()]  
    return random.choices(countries_list, weights=weights, k=1)[0]

select_country = {

    
    "Germany": [552, 569],
    "United Kingdom": [660,565],
    "Canada": [524,590],
    "Australia": [505,558 ],
    "United States": [660,595],
    "France": [552, 508],
    "Argentina":  [497,620],
    "Italy": [570,600],
    "Brazil": [515,618],
    "India": [563,595],
    "Indonesia": [563,628],
    "Philippines":[624,570],
    "Netherlands": [612,535],
    "Greece": [552, 628],
    "Hungary": [563,563],
    #"Mexico": [603, 550],
    "Spain": [645, 512],
    "Denmark": [540, 518],
    "Norway": [615,605],
    "Belgium": [515,507],
    "Nigeria": [612,638],
    "South Africa": 40,
    #"Sweden": [645, 570],
    "Ireland": [570,537],
    #"New Zealand": [612,565],
    "WorldWide": [495,506],
}
def randomcountry():
    countries = [
        "Canada", "United States", "Mexico", "Brazil", "Argentina",
        "United Kingdom", "France", "Germany", "Italy", "Spain", "Portugal", "Netherlands", "Belgium",
        "Switzerland", "Austria", "Sweden", "Norway",
        "Greece", "Egypt", "South Africa", "Nigeria",
        "India", "Japan", "South Korea", "Vietnam",
        "Thailand",  "Philippines", "Australia", "New Zealand",
    ]
    return random.choice(countries)

prev_country = None
random_contry = None
def tuxler_changer(given_country="WorldWide"):
    global prev_country
    global random_contry
    global location_changes
    if Mysterium_Mode:
        try:
            for i in range(30):
                focus_mysterium()
                time.sleep(2)
                pyautogui.click(273,292)
                try:
                    x, y = pyautogui.locateCenterOnScreen('myst_disconnect.png',  region=[273,297,211,415],confidence=0.99)
                    if x and y:
                        break
                        
                except Exception as e:
                    print('tuxler off not found')
                    try:
                        x, y = pyautogui.locateCenterOnScreen('mysterium_connect.png',  region=[273,297,211,415],confidence=0.99)
                        if x and y:
                            break
                            
                    except Exception as e:
                        print('tuxler off not found')
                        pyautogui.hotkey('alt','tab')
                        time.sleep(1)
                        pyautogui.press('esc')
                        time.sleep(1)
            
            file_location = "traffic_flow.txt"
            gg_select_country = read_line_from_file(file_location, location_changes)
            if gg_select_country == 'WorldWide':
                gg_select_country = randomcountry()
            location_changes +=1

            pyautogui.click(273,292)
            time.sleep(1)
            pyautogui.click(420,104)
            time.sleep(1)
                
            pyautogui.click(227,105)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            pyautogui.press('delete')
            time.sleep(1)
            pyautogui.typewrite(gg_select_country)
            time.sleep(1)
            pyautogui.click(273,292)
            time.sleep(1)

            try:
                x, y = pyautogui.locateCenterOnScreen('mysterium_connect.png',  region=[273,297,211,415],confidence=0.99)
                if x and y:
                    pyautogui.click(x, y)
                    time.sleep(5)
            except Exception as e:
                pass
            return True
        except Exception as e:
            print(f"Error in Mysterium_Mode: {e}")
    else:

        try:

            for i in range(30):
                focus_tuxler()
                time.sleep(2)
                pyautogui.click(326,720)
                pyautogui.click(326,707)
                
                time.sleep(1)
                pyautogui.click(326,757)
                try:
                    x, y = pyautogui.locateCenterOnScreen('tuxler_on.png', confidence=0.9)
                    if x and y:
                        break
                        
                except Exception as e:
                    pass
                try:
                    x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
                    if x and y:
                        pyautogui.click(x, y)
                        time.sleep(3)
                        
                except Exception as e:
                    print('tuxler off not found')
                    pyautogui.hotkey('alt','tab')
                    time.sleep(1)
                    pyautogui.press('esc')
                    time.sleep(1)
            try:
                x, y = pyautogui.locateCenterOnScreen('butpremium_tuxler.png', confidence=0.8)
                if x and y:
                    tuxler_account_changer()
                    
                    
            except Exception as e:
                pass

            pyautogui.click(347,476)
            time.sleep(1)
            pyautogui.moveTo(345,566)
            pyautogui.scroll(15000)
            time.sleep(3)

            file_location = "traffic_flow.txt"
            gg_select_country = read_line_from_file(file_location, location_changes)
            location_changes +=1
            # Randomly choose a country
            prev_country = random_contry
            random_contry = gg_select_country #get_random_country()
            coords = select_country[random_contry]
            print(f"Initial country: {random_contry}")
            # Assign scroll and click coordinates
            scrollG, ClickG = coords

            print(f"Selected country: {country}")
            print(f"ScrollG: {scrollG}, ClickG: {ClickG}")

            pyautogui.moveTo(446, scrollG)
            pyautogui.click(446, scrollG)
            time.sleep(1)
            pyautogui.click(342, ClickG)

            #pyautogui.click(408, 618, duration=0.5)  
            time.sleep(8) 
            try:
                x, y = pyautogui.locateCenterOnScreen('minuteago.png', region=[182,674,278,140], confidence=0.98)
                if x and y:
                    pyautogui.click(409, 626)
                    time.sleep(5) 
                    
            except Exception as e:
                pass
            
        except Exception as e:
            print(f"Error in tuxler_changer: {e}")


def tuxler_account_changer():

    try:
        for i in range(30):
            focus_tuxler()
            time.sleep(2)
            pyautogui.click(326,720)
            
            pyautogui.click(326,707)
            time.sleep(1)
            pyautogui.click(326,757)
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_on.png', confidence=0.9)
                if x and y:
                    break
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
                if x and y:
                    break
                    
            except Exception as e:
                print('tuxler off not found')
                pyautogui.hotkey('alt','tab')
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)
        #time.sleep(10)
        print('Changing tuxler account')        
        #time.sleep(10)
        try:
            x, y = pyautogui.locateCenterOnScreen('butpremium_tuxler.png', confidence=0.9)
            if x and y:
                print('Premium button found, logging in with new account')
                pyautogui.click(148,116)
                time.sleep(2)
                pyautogui.click(211,146)
                time.sleep(2)
                trying_mail = tuxlermail1[0]
                mail, password = trying_mail.split(":", 1)  # split only at the first colon
                pyautogui.click(290,473)  
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')   
                pyautogui.typewrite(mail)
                time.sleep(1)
                pyautogui.click(290,511)    
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete') 
                pyautogui.typewrite(password)
                time.sleep(1)
                pyautogui.click(328,615)
                time.sleep(8)
                return True   
        except Exception as e:
            print('No premium button found',e)
            print(f'Erro:{e}')
            pass

        pyautogui.click(148,116)
        time.sleep(2)
        pyautogui.click(211,146)
        time.sleep(2)

        text = ocr_screen_region(119, 513, 382, 132)
        # Extract values
        expire, location_changes = extract_expire_and_location(text)
        print(f"\nExtracted -> Expiration date: {expire}, Location changes: {location_changes}")
        if location_changes == 100 or location_changes > 99:
            #text = ocr_screen_region(180, 432, 290, 40)
            #if text in tuxlermail1:
            for account in tuxlermail1:
                print('Current Mail ', account)
                pyautogui.click(315,688)
                time.sleep(5)
                pyautogui.click(148,116)
                time.sleep(2)
                pyautogui.click(207,154)
                time.sleep(2)
                ###################Log in
                mail, password = account.split(":", 1)  # split only at the first colon
                pyautogui.click(290,473)   
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete') 
                pyautogui.typewrite(mail)
                time.sleep(1)
                pyautogui.click(290,511)   
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')  
                pyautogui.typewrite(password)
                time.sleep(1)
                pyautogui.click(328,615)
                time.sleep(8)

                pyautogui.click(148,116)
                time.sleep(2)
                pyautogui.click(211,146)
                time.sleep(2)

                text = ocr_screen_region(119, 513, 382, 132)
                # Extract values
                expire, location_changes = extract_expire_and_location(text)
                print(f"\nExtracted -> Expiration date: {expire}, Location changes: {location_changes}")
                if location_changes == 100:
                    print('accounts exhausted')
                    continue
                elif location_changes == 0 or location_changes < 99:
                    return True
                
            while True:
                if is_between_12pm_and_6pm():
                    print("Yes, current time in Sri Lanka is between 12 PM and 6 PM. Both accounts exhausted")
                    time.sleep(100)
                else:
                    print("No, it's outside 12 PM - 6 PM in Sri Lanka. Both accounts exhausted")
                    break
            return True   
        
        time.sleep(1)
        pyautogui.click(326,757)
        return False

    except Exception as e:
        pass


def ipqs_lookup(ip, api_key, api_list):
    return api_key, True
    
    
    try:
        url = f"https://ipqualityscore.com/api/json/ip/{api_key}/{ip}"#?strictness=1&allow_public_access_points=true"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print('Data:',data)  # raw API response for debugging
        print(f"Using IPQS Key: {api_key}")

        # ✅ Safe if no VPN, no proxy, and fraud score < 75
        if data.get("success", False) is False:

            for key in api_list:
                try:
                    url = f"https://ipqualityscore.com/api/json/ip/{key}/{ip}"#?strictness=1&allow_public_access_points=true"
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()
                    data = response.json()
                    print(f"Checking IP {ip} with key {key}")
                    print("Data:", data)

                    if not data.get("success", False):
                        # invalid or rate limited key
                        print(f"Key {key} invalid or rate-limited. Trying next key...")
                        continue

                    # key worked, now check IP
                    if not data.get("vpn", True) and not data.get("proxy", True) and data.get("fraud_score", 100) < 29:
                        return True, key  # clean IP, working key
                    else:
                        # IP flagged
                        print(f"IP flagged: VPN={data.get('vpn')}, Proxy={data.get('proxy')}, Fraud Score={data.get('fraud_score')}")
                        return False, key  # working key but flagged IP

                except requests.RequestException as e:
                    print(f"Error with key {key}: {e}")
                    continue
            return False, "no_key"

        if (
            not data.get("vpn", True) and
            not data.get("proxy", True) and
            data.get("fraud_score", 100) < 29
        ):
            return True, api_key
        else:
            print(f"IPQS Check Failed: VPN={data.get('vpn')}, Proxy={data.get('proxy')}, Fraud Score={data.get('fraud_score')}")
            return False, api_key

    except requests.RequestException as e:
        print('Thers Issue in Function IPQS')
        return False, api_key  # error = treat as unsafe
    


def ipqs_browsercheck(ip, api_key, api_list):
    open_link(link=f'https://www.ipqualityscore.com/ip-lookup/search/{ip}', newtab=False)
    time.sleep(5)
    for i in range(53):
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
            pyautogui.click(x, y,duration=0.5)
            time.sleep(1)
            pyautogui.click(x, y,duration=0.5)
            time.sleep(5)
        except Exception as e:
            pass

        pyautogui.click(200, 219)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        data_str = clipboard.paste()
        if 'IP Address Lookup' in data_str:
            cond1 = "0% - Clean IP" in data_str
            cond2 = "Healthy IP — Not A Proxy or VPN Connection" in data_str

            if cond1 and cond2:
                print("PASS IP")
                return True
            else:
                print("NOT PASSED")
                return None


def update_fraud_report(text):
    # The new content to insert
    new_content = """
Device Fingerprinting
Real-Time Fraud Blocking
25+ Platform Integration
Custom Fraud Rules
Bot Traffic Filtering"""

    # Define the start and end anchors
    # We use re.escape to handle special characters and .*? (dotall) to match across lines
    pattern = re.compile(
        r"(Affiliate Fraud Detection Dashboard)(.*?)(Supported Platform Integrations)", 
        re.DOTALL
    )

    # Perform the replacement
    # \1 and \3 keep the original anchor headers intact
    updated_text = pattern.sub(f"\\1\n\n{new_content}\n\n\\3", text)
    
    return updated_text

def extract_ip_info24metric(text, ip):
    text = update_fraud_report(text)
    def find(label):
        pattern = rf"{label}\s*:?[\s]*([A-Za-z0-9 ._-]+)"
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else None

    Residential_proxy = find(r"Residential Proxy\?")
    Risk_Score = find(r"Risk Score")
    Recent_Abuse = find(r"Recent Abuse\?")
    is_vpn = find(r"VPN")
    is_proxy = find(r"Proxy")
    networkip = find(r"Network")
    print(is_vpn, is_proxy, networkip)
    if networkip and is_vpn:
        print(f"Extracted Network IP: {networkip} and {ip}")
        if networkip != '2003' and is_vpn != '- - -':
            print(f"Extracted Network IP: {networkip}")
            if Residential_proxy == 'No' and Risk_Score == 'No Risk' and Recent_Abuse == 'No' and is_vpn == 'False' and is_proxy == 'False':
                print("This IP is clean and safe to use.")
                return 'goodip'
            elif Residential_proxy == 'Yes' or Risk_Score == 'High Risk' or Risk_Score == 'Risk' or Recent_Abuse == 'Yes' or is_vpn == 'Yes' or is_proxy == 'Yes':
                print("Warning: This IP may be risky to use.")
                return 'badip'
    return 'noip'

def metrics24_lookups(ip):
    open_link(link=f'https://www.24metrics.com/#anchor-ip-scanner', newtab=False)
    time.sleep(2)
    for i in range(53):
        try:
            x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
            if x and y:
                break
        except Exception as e:
            pass
        time.sleep(1)

    met24_empty = ['24met_empty.png', '24met_empty2.png', '24met_empty3.png']
    lookup_metr = ['lookup_metr.png', 'lookup_metr2.png', 'lookup_metr3.png']
    for i in range(33):
        try:
            x, y = pyautogui.locateCenterOnScreen('24met_acceptcookie.png',  confidence=0.7)
            if x and y:
                pyautogui.click(x, y)
        except Exception as e:
            pass
        
        for img in met24_empty:
            print(f"Checking for image: {img}")
            try:
                x, y = pyautogui.locateCenterOnScreen(img,  confidence=0.7)
                if x and y:
                    for img in lookup_metr:
                        print(f"Checking for image: {img}")
                        try:
                            x, y = pyautogui.locateCenterOnScreen(img,  confidence=0.7)
                            if x and y:
                                print(f"Found lookup image at: {x}, {y}")
                                pyautogui.click(1444, y)
                                time.sleep(1)
                                pyautogui.hotkey('ctrl', 'a')
                                pyautogui.press('delete')   
                                pyautogui.typewrite(ip)
                                time.sleep(1)
                                pyautogui.click(x, y)
                                time.sleep(3)
                                break
                        except Exception as e:
                            pass
                    break
            except Exception as e:
                pass


        pyautogui.click(100, 300)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.click(100, 300)
        text = clipboard.paste()
        res_txt = extract_ip_info24metric(text, ip)
        if res_txt == 'goodip':
            return True
        if res_txt == 'badip':
            return False



    
def get_link():

    try:

        clipboard.copy('')
        pyautogui.click(228,63)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')  # Focus the address bar
        time.sleep(0.5)
        link = clipboard.paste()  # Get the copied link from clipboard
        if link == '' or link == None:
            pyautogui.press('esc')
        if link:
            print(f"Link copied: {link}")
            return link


    except Exception as e:
        print(f"Error in: {e}")


def newtab_validate(title):
    if 'New Tab' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
            if x and y:
                return True
        except Exception as e:
            pass
    return False

def linked_validate():


    valid_links = [
        'tpi',
        'shrinkme',
        'gplinks',
        'shortxlinks',
        'mtc',
        'procinehub',
        'tpi.li',
        'oii.la',
        'oii',
        'serverguidez',
        'cheaplann',
        'themezon',
        'shrinkme.top',
        'themezon.net',
        'mrproblogger',
        'en.mrproblogger.com',
        'en.mrproblogger',
        'cuty.io',
        'cuty',
        'cuttlinks.com',
        'cuttlinks',
        'cutlinks',
        'cuttlink'
    ]
    try:
        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
        if x and y: 
            text = ocr_screen_region(167, 45, 342, 35)
            title = get_focused_window_title()
            print(f"Screen OCR Text: {text}")

            text = text.lower().strip()

            # direct contains check
            for word in valid_links:
                if word in text or word in title.lower():
                    print(f'{word} found in {text} or {title}')
                    return True


            return False
    except Exception as e:
        pass
    return True



##############################################################
# Function to handle the Shortlinks statistics
#######################################################

def zyrox_handle():
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.4)
    pyautogui.click(493,19, duration = 0.4)
    title = get_focused_window_title()

    if destined_reached(title):
        return 5
    if newtab_validate(title):
        return 5

    try:
        x, y = pyautogui.locateCenterOnScreen('js_ok.png', region=[930,130,342,165] ,confidence=0.9)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(2)
            pyautogui.click(95, 62)  # Click on the 'No Internet' button
            time.sleep(2)
            return 5
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('getlink_zyrox.png',confidence=0.9)
        if x and y:
            human_click(x, y, duration=0.2)
            time.sleep(0.2)
            pyautogui.click(95, 62)  # Click on the 'No Internet' button
            return 5
    except Exception as e:
        pass
    close_ads()



def inidanxlinks(simple=False):
    
    pyautogui.click(493,19, duration = 0.4)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.4)
    title = get_focused_window_title()

    if destined_reached(title):
        return 5
    if newtab_validate(title):
        return 5

    try:
        x, y = pyautogui.locateCenterOnScreen('js_ok.png', region=[930,130,342,165] ,confidence=0.99)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(2)
            pyautogui.click(493,19, duration = 0.2)
            time.sleep(2)
            return 5
    except Exception as e:
        pass
    
    if simple:
        close_ads()
        
        buttons = ['wait_for_page.png','consent5.png','indiax_notrobo5.png','indiax_dualtap5.png','indiax_dualtap52.png','indiax_dualtap23.png','indiax_openc5.png','indiax_openc52.png','opencon53.png','opencon5.png','indiax_closead5.png', 'indiax_dualtap4.png','idiaad_open3.png','idiaad_dual3.png','indiadasclose.png','indiax_closead3.png','indiax_closead4.png','indiax_closead2.png', 'indiax_closead1.png','indiax_notrobo2.png','indiax_dualtap3.png','indiax_dualtap2.png','indiax_openc.png','indiax_notrobo1.png' ,'indiax_dualtap1.png','indiax_open_con.png','indiax_getlink.png']

        full_screen = pyautogui.screenshot()
        for img_name in buttons:
            try:

                match = pyautogui.locate(img_name, full_screen, confidence=0.99)
                if img_name == 'consent5.png':
                    match = pyautogui.locate(img_name, full_screen, confidence=0.99)
                if match:
                    x, y = pyautogui.center(match)
                    pyautogui.click(x,y)
                    time.sleep(0.5)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(0.5)
                    full_screen = pyautogui.screenshot()

            except Exception:
                pass

        adsclosebutton = [ 'closeadsgoogle1.png','closeadsgoole11.png','closeadsgoole10.png', 'closeadsgoole2.png', 'closeadsgoole3.png', 'closeadsgoole4.png', 'closeadsgoole5.png', 'closeadsgoole6.png', 'closeadsgoole7.png', 'closeadsgoole9.png','closeadsgoole8.png']
        full_screen = pyautogui.screenshot()
        for img_name in adsclosebutton:
            try:
                match = pyautogui.locate(img_name, full_screen,  region=[1,83,1914,956],confidence=0.99)
                if match:
                    x, y = pyautogui.center(match)
                    pyautogui.click(x,y)
                    time.sleep(0.5)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(0.5)
                    full_screen = pyautogui.screenshot()

            except Exception:
                pass

        try:
            x, y = pyautogui.locateCenterOnScreen( 'adremoved.png', confidence=0.98)
            if x and y:
                pyautogui.press('f5')
                return
        except Exception as e:
            pass
    try:
        x, y = pyautogui.locateCenterOnScreen( 'idiaad_rsum.png', confidence=0.99)
        if x and y:
            pyautogui.click(x, y, duration=0.1)
            time.sleep(1)
            pyautogui.click(494,19, duration = 0.2)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen( 'skipvidgp.png', confidence=0.99)
        if x and y:
            pyautogui.click(x, y, duration=0.1)
            time.sleep(1)
            pyautogui.click(494,19, duration = 0.2)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen( 'closevideoadgp.png', region=[900,212,714,522], confidence=0.99)
        if x and y:
            pyautogui.click(x, y, duration=0.1)
            time.sleep(1)
            pyautogui.click(970, 638, duration=0.1)
            time.sleep(1)
            pyautogui.click(494,19, duration = 0.2)
            return
            
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen( 'skipvidgp.png', confidence=0.99)
        if x and y:
            pyautogui.click(x, y, duration=0.1)
            time.sleep(2)
            pyautogui.click(494,19, duration = 0.2)
            return
            
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen( 'resumevidgp.png', region=[1,83,1914,956], confidence=0.99)
        if x and y:
            pyautogui.click(x, y, duration=0.1)
            time.sleep(2)
            pyautogui.click(494,19, duration = 0.2)
            return
            
    except Exception as e:
        pass





shrinkearn_continue= 1 

def shrinkearn_handle():
    global shrinkearn_continue
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=1)
    pyautogui.click(493,19, duration = 0.4)
    title = get_focused_window_title()
    print(f"Current Window Title: {title}")

    if destined_reached(title):
        return 5
    if newtab_validate(title):
        return 5
    if 'HealthShield - Review of Fitness, Weight Gain, Skin Care, Yoga & Weight Loss' in title:
        shorlink = random_link('link3')
        open_link(link = shorlink ,newtab = False)

    try:
        x, y = pyautogui.locateCenterOnScreen('js_ok.png', region=[930,130,342,165] ,confidence=0.9)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(2)
            pyautogui.click(95, 62)  # Click on the 'No Internet' button
            time.sleep(2)
            return 5
    except Exception as e:
        pass

    close_ads()
    try:
        x, y = pyautogui.locateCenterOnScreen('Getlink2.png', region=[680,110,557,909], confidence=0.8)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(5)
            return 1
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('recaptcha_fail2.png', region=[344,65,1208,977], confidence=0.98)
        if x and y:
            print('Failed Recaptcha')
            pyautogui.press('f5')
            time.sleep(3)
            pyautogui.press('enter')
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('recaptcha_valid.png', region=[699,156,530,870], confidence=0.9)
        if x and y:
            for i in range(6):
                close_ads()
                try:
                    x, y = pyautogui.locateCenterOnScreen('shrinkearn_continue1.png', region=[699,156,530,870], confidence=0.9)
                    if x and y:
                        human_click(x, y, duration=1)
                        time.sleep(1)
                        pyautogui.click(493,19, duration = 0.4)
                        time.sleep(3)
                        continue
                except Exception as e:
                    pass
                try:
                    x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                    if x and y:
                        pass
                except Exception as e:
                    
                    return 1 
            return 1
    except Exception as e:
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen('urlinkready.png', region=[680,110,557,909], confidence=0.8)
        if x and y:
            print("Link is ready")
            try:
                x, y = pyautogui.locateCenterOnScreen('zero.png', region=[680,110,557,909], confidence=0.9)
                if x and y:
                    print("Link is ready2")
                    for i in range(5):
                        close_ads()
                        try:
                            x, y = pyautogui.locateCenterOnScreen('Getlink2.png', region=[680,110,557,909], confidence=0.8)
                            if x and y:
                                human_click(x, y, duration=1)
                                time.sleep(1)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(5)
                                return 1
                        except Exception as e:
                            pyautogui.moveTo(400,409)
                            time.sleep(1)
                            pyautogui.scroll(-350)
                        try:
                            x, y = pyautogui.locateCenterOnScreen('getting_linkstuck2.png', region=[680,110,557,909], confidence=0.9)
                            if x and y:
                                
                                time.sleep(4)
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('getting_linkstuck2.png', region=[680,110,557,909], confidence=0.9)
                                    if x and y:
                                        pyautogui.press('f5')
                                        time.sleep(2)
                                        pyautogui.press('enter')
                                        return 1
                                except Exception as e:
                                    pass
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('shrime_getlink.png', region=[680,110,557,909], confidence=0.7)
                                    if x and y:
                                        human_click(x, y, duration=1)
                                        time.sleep(1)
                                        pyautogui.click(493,19, duration = 0.4)
                                        time.sleep(5)
                                        #return
                                except Exception as e:
                                    pass
                        except Exception as e:
                            pass
                else:
                    return 1
            except Exception as e:
                return 1
        pyautogui.scroll(5000)
    except Exception as e:
        pass
    if 'Health Shield' not in title or 'PolicyBuzz' not in title:
        if shrinkearn_continue > 4:
            pyautogui.press('f5')
            time.sleep(3)
            pyautogui.press('enter')
            shrinkearn_continue = 1
        
        try:
            x, y = pyautogui.locateCenterOnScreen('shrinkearn_continue2.png', region=[407,100,932,816], confidence=0.7)
            if x and y:
                human_click(x, y, duration=1)
                shrinkearn_continue += 1
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)

                  
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
            if x and y:
                try:
                    x, y = pyautogui.locateCenterOnScreen('continue_shrentop.png', region=[407,100,932,816], confidence=0.998)
                    if x and y:
                        shrinkearn_continue += 1
                        print("Top continue found", shrinkearn_continue)
                        y += 20
                        pyautogui.click(x, y, duration = 0.4)
                        #time.sleep(2)
                        #return  
                except Exception as e:
                    pass
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('continue_shren.png', region=[407,100,932,816], confidence=0.7)
            if x and y:
                human_click(x, y, duration=1)
                shrinkearn_continue += 1
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)

                  
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('shrinkearn_continue3.png', region=[407,100,932,816], confidence=0.7)
            if x and y:
                human_click(x, y, duration=1)
                shrinkearn_continue += 1
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(2)

                  
        except Exception as e:
            pass
    
    elif 'Health Shield' in title or 'PolicyBuzz' not in title:
        try:
            x, y = pyautogui.locateCenterOnScreen('close_shrinkearn_new.png', region=[1165,150,273,664], confidence=0.9)
            if x and y:
                pyautogui.click(x,y, duration=1)
                time.sleep(2)
        except Exception as e:
            pass
    #try:
    #    x, y = pyautogui.locateCenterOnScreen('Getlink1.png', region=[407,104,722,900], confidence=0.9)
    #    if x and y:
    #        human_click(x, y, duration=1)
    #        time.sleep(1)
    #        pyautogui.click(493,19, duration = 0.4)
    #        time.sleep(3)
    #        return 
    #except Exception as e:
    #    pass
    try:
        x, y = pyautogui.locateCenterOnScreen('getlink_shren.png',  confidence=0.7)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(3)
            shrinkearn_continue = 1
            return 1 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('Getlink1.png',  confidence=0.7)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(3)
            shrinkearn_continue = 1
            return 1 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('goup_shrinkearn.png',  confidence=0.9)
        if x and y: 
            pyautogui.click(x,y)
            time.sleep(2)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('post_comment2.png',  confidence=0.9)
        if x and y: 
            pyautogui.moveTo(300, 300)
            pyautogui.scroll(10000)
            time.sleep(1)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('adblockshrink.png',  confidence=0.9)
        if x and y: 
            return 5
    except Exception as e:
        pass
    


def fclink_handle():
    pyautogui.click(493,19, duration = 0.4)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.5)

    title = get_focused_window_title()
    if destined_reached(title):
        return True
    if 'Just' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
            pyautogui.click(x, y,duration=1)
            time.sleep(1)
            pyautogui.click(x, y,duration=1)
            time.sleep(5)

        except Exception as e:
            pass

    try:
        x, y = pyautogui.locateCenterOnScreen('fbg_lg.png', region=[394,83,303,123], confidence=0.95)
        if x and y:
            pyautogui.scroll(500)
            time.sleep(1)
            pyautogui.click(1090, 820)  # Click on the 'Leave' button
            time.sleep(1)
            pyautogui.click(1117, 550)
            pyautogui.click(1117, 540)
            pyautogui.click(1117, 530)
            pyautogui.click(1117, 520)
            pyautogui.click(1117, 510)
            pyautogui.click(1117, 500)
            pyautogui.click(1117, 490)
            pyautogui.click(1117, 480)
            pyautogui.click(1117, 470)
            pyautogui.click(1117, 460)
            pyautogui.click(1117, 450)
            pyautogui.click(1117, 430)
            pyautogui.click(1117, 420)
            pyautogui.click(1117, 410)
            pyautogui.click(1117, 400)
            return 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('yt_logo.png', region=[699,56,240,136], confidence=0.94)
        if x and y:
            pyautogui.click(885,394)
            time.sleep(1)
            return 
    except Exception as e:
        pass
    close_ads()
    button_found = False
    try:
        x, y = pyautogui.locateCenterOnScreen('fc_clickhere.png', region=[770,108,400,912], confidence=0.9)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(1)
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            button_found = True  
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('fc_clickverify.png', region=[493,98,930,935], confidence=0.9)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(1)  
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            button_found = True 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('fc_countinue.png', region=[493,98,930,935], confidence=0.9)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(1)  
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            button_found = True 
    except Exception as e:
        pass
    if button_found:
        for i in range(4):
            if button_found == False:
                break
            title = get_focused_window_title()
            if destined_reached(title):
                return True
            close_ads()
            try:
                x, y = pyautogui.locateCenterOnScreen('fc_clickhere.png', region=[770,108,400,912], confidence=0.9)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(1)
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    button_found = True  
            except Exception as e:
                button_found = False
            
            try:
                x, y = pyautogui.locateCenterOnScreen('fc_clickverify.png', region=[493,98,930,935], confidence=0.9)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(1)  
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    button_found = True 
            except Exception as e:
                button_found = False
            try:
                x, y = pyautogui.locateCenterOnScreen('fc_countinue.png', region=[493,98,930,935], confidence=0.9)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(1)  
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    button_found = True 
            except Exception as e:
                button_found = False
    try:
        x, y = pyautogui.locateCenterOnScreen('fc_scrolldown.png', region=[493,98,930,935], confidence=0.9)
        if x and y:
            pyautogui.moveTo(x, y, duration=1)
            time.sleep(1)
            pyautogui.scroll(-5000)
            time.sleep(2)  
    except Exception as e:
        pass

    try:
        x, y = pyautogui.locateCenterOnScreen('fc_getlink.png', region=[493,98,930,935], confidence=0.9)
        if x and y:
            for i in range(8):
                title = get_focused_window_title()
                if destined_reached(title):
                    return True
                close_ads()
                try:
                    x, y = pyautogui.locateCenterOnScreen('fc_getlink.png', region=[493,98,930,935], confidence=0.7)
                    if x and y:
                        human_click(x, y, duration=1)
                        time.sleep(1)
                        pyautogui.click(493,19, duration = 0.4)
                        time.sleep(1)
                        
                except Exception as e:
                    continue
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('fc_linkready.png', region=[493,98,930,935], confidence=0.8)
        if x and y:
            print("Link is ready2")
            x, y = pyautogui.locateCenterOnScreen('fczero.png', region=[493,98,930,935], confidence=0.9)
            if x and y:
                print("Link is ready2")
                for i in range(5):
                    title = get_focused_window_title()
                    if destined_reached(title):
                        return True
                    close_ads()
                    try:
                        x, y = pyautogui.locateCenterOnScreen('fc_getlink2.png', region=[493,98,930,935], confidence=0.7)
                        if x and y:
                            human_click(x, y, duration=1)
                            time.sleep(1)
                            pyautogui.click(493,19, duration = 0.4)
                            time.sleep(1)
                            
                    except Exception as e:
                        pyautogui.moveTo(400,409)
                        time.sleep(1)
                        pyautogui.scroll(-350)
        pyautogui.scroll(5000)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('fc_getlink2.png', region=[493,98,930,935], confidence=0.9)
        if x and y:
            for i in range(8):
                title = get_focused_window_title()
                if destined_reached(title):
                    return True
                close_ads()
                try:
                    x, y = pyautogui.locateCenterOnScreen('fc_getlink2.png', region=[493,98,930,935], confidence=0.7)
                    if x and y:
                        human_click(x, y, duration=1)
                        time.sleep(1)
                        pyautogui.click(493,19, duration = 0.4)
                        time.sleep(1)
                        
                except Exception as e:
                    pyautogui.moveTo(400,409)
                    time.sleep(1)
                    pyautogui.scroll(-350)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('fclc_title.png', region=[65, 6, 185, 35], confidence=0.98)
        if x and y:
            return
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('adblockfc2.png', region=[595,570,180,185], confidence=0.8)
        if x and y:
            print("Adblock found")
            pyautogui.press('f5')

    except Exception as e:
        pass
    if 'fc.lc' not in title or 'fclc' not in title or 'fc,lc' not in title or 'fle' not in title:
        #time.sleep(1)
        pyautogui.click(200,432, duration=1)
        time.sleep(1)
        pyautogui.click(1861,132, duration=1)
        time.sleep(1)
        pyautogui.click(493,19, duration = 0.4)
        time.sleep(1)
        pyautogui.click(200,432, duration=1)
        time.sleep(1)
        pyautogui.click(493,19, duration = 0.4)
    try:
        x, y = pyautogui.locateCenterOnScreen('clickhere_unload.png', region=[765,170,400,850], confidence=0.95)
        if x and y:
            pyautogui.press('f5')
            time.sleep(3)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
        if x and y:
            try:
                
                x, y = pyautogui.locateCenterOnScreen('fc_blur.png', confidence=0.98)
                if x and y:
                    print("Blur found")
                    pyautogui.press('f5')
                    time.sleep(3)
            except Exception as e:
                pass
    except Exception as e:
        pass

def cutty_handle():
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.3)
    pyautogui.click(493,19, duration=0.2)
    title = get_focused_window_title()

    if destined_reached(title):
        return True

    close_ads()
    try:
        x, y = pyautogui.locateCenterOnScreen('cssnotloadcutty.png',  confidence=0.95)
        if x and y:
            pyautogui.press('f5')
            time.sleep(3)
            return
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('cutty_continue.png', region=[541,146,812,895], confidence=0.9)
        if x and y:
            
            human_click(x, y, duration=0.2)
            time.sleep(0.2)
            pyautogui.click(493,19, duration = 0.2)
            time.sleep(0.4)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('cutty_notrobot.png', region=[541,146,812,895], confidence=0.9)
        if x and y:
            
            human_click(x, y, duration=0.2)
            time.sleep(0.2)
            pyautogui.click(493,19, duration = 0.2)
            time.sleep(0.2)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
        if x and y:
            pyautogui.moveTo(300,509)
            pyautogui.scroll(5000)
            button_found = False
            for i in range(4):
                if button_found:
                    break
                pyautogui.scroll(-300)
                time.sleep(1)
                try:
                    x, y = pyautogui.locateCenterOnScreen('cutty_notrobot.png', region=[541,146,812,895], confidence=0.8)
                    if x and y:
                        button_found = True
                except Exception as e:
                    pass
                try:
                    x, y = pyautogui.locateCenterOnScreen('cutty_go.png', region=[541,146,812,895], confidence=0.7)
                    if x and y:
                        button_found = True
                except Exception as e:
                    pass
            if button_found == False:
                return


            try:
                x, y = pyautogui.locateCenterOnScreen('cutty_notrobot.png', region=[541,146,812,895], confidence=0.9)
                if x and y:
                    for i in range(5):
                        try:
                            x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                            if x and y:
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('cutty_notrobot.png', region=[541,146,812,895], confidence=0.9)
                                    if x and y:
                                    
                                        human_click(x, y, duration=0.4)
                                        time.sleep(1)
                                        pyautogui.click(493,19, duration = 0.4)
                                        time.sleep(2)
                                        
                                except Exception as e:
                                    pass
                        except Exception as e:
                            pass
                    try:
                        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                        if x and y:
                            pyautogui.press('f5')
                            time.sleep(1)
                            return
                    except Exception as e:
                        pass
            except Exception as e:
                pass



            try:
                x, y = pyautogui.locateCenterOnScreen('cutty_go.png', region=[541,146,812,895], confidence=0.9)
                if x and y:
                    for i in range(6):
                        try:
                            x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                            if x and y:
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('cutty_go.png', region=[541,146,812,895], confidence=0.9)
                                    if x and y:
                                    
                                        human_click(x, y, duration=0.4)
                                        time.sleep(1)
                                        pyautogui.click(493,19, duration = 0.4)
                                        time.sleep(2)
                                        
                                except Exception as e:
                                    pass
                        except Exception as e:
                            pass
                    try:
                        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                        if x and y:
                            pyautogui.press('f5')
                            time.sleep(1)
                            return
                    except Exception as e:
                        pass
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('linkready_cutty.png', region=[680,110,557,909], confidence=0.8)
                if x and y:
                    print("Link is ready")
                    try:
                        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                        if x and y:
                            print("Link is ready2")
                            for i in range(6):
                                title = get_focused_window_title()
                                if 'Shorten Links' in title or 'cuty.io' in title:
                                    return True
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('cutty_go.png', region=[541,146,812,895], confidence=0.7)
                                    if x and y:
                                        human_click(x, y, duration=1)
                                        time.sleep(1)
                                        pyautogui.click(493,19, duration = 0.4)
                                        time.sleep(1)
                                        return
                                except Exception as e:
                                    pyautogui.moveTo(400,409)
                                    time.sleep(1)
                                    pyautogui.scroll(-350)
                        else:
                            return
                    except Exception as e:
                        return
                pyautogui.scroll(5000)
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('cutty_go.png', region=[541,146,812,895], confidence=0.9)
                if x and y:
                
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(1)
                    
            except Exception as e:
                pass
            for i in range(7):
                try:
                    x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                    if x and y:
                        try:
                            x, y = pyautogui.locateCenterOnScreen('cutty_continue.png', region=[541,146,812,895], confidence=0.9)
                            if x and y:
                                
                                human_click(x, y, duration=0.2)
                                time.sleep(0.2)
                                pyautogui.click(493,19, duration = 0.2)
                                time.sleep(0.4)
                                
                                continue  
                        except Exception as e:
                            pass
                        try:
                            x, y = pyautogui.locateCenterOnScreen('cutty_notrobot.png', region=[541,146,812,895], confidence=0.9)
                            if x and y:
                                
                                human_click(x, y, duration=0.2)
                                time.sleep(0.2)
                                pyautogui.click(493,19, duration = 0.2)
                                time.sleep(0.2)
                                
                                continue  
                        except Exception as e:
                            pass
                except Exception as e:
                    pass
                return
                print("Page loaded")  

    except Exception as e:
        pass




def shrtfly_handle():
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.2)
    pyautogui.click(493,19, duration=0.2)
    title = get_focused_window_title()
    if destined_reached(title):
        return True
    close_ads()


    try:
        x, y = pyautogui.locateCenterOnScreen('scrollshrt2.png',  confidence=0.8)
        if x and y:
            pyautogui.moveTo(300, 339, duration=0.2)
            pyautogui.scroll(-5000)
    except Exception as e:
        pass
    click_buttons = ['getnex_shrt.png', 'begin_shrt.png', 'clckhere_shrt.png', 'open_shrt.png', 'clickhere_shrt.png', 'vrify_shrt.png', 'gonex_shrt.png']
    try:
        x, y = pyautogui.locateCenterOnScreen('pleasecaptcha_shrt.png', confidence=0.9)
        if x and y:
            try:
                x, y = pyautogui.locateCenterOnScreen('recaptcha_valid.png', region=[699,156,530,870], confidence=0.9)
                if x and y:
                    for button in click_buttons:
                        try:
                            x, y = pyautogui.locateCenterOnScreen(button,  confidence=0.8)
                            if x and y:
                                human_click(x, y, duration=1)
                                time.sleep(0.2)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(0.2)
                        except Exception as e:
                            pass
            except Exception as e:
                pass

        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png",  confidence=0.7)
            if x and y:
                for i in range(3):
                    try:
                        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png",  confidence=0.7)
                        if x and y:
                            pyautogui.click(x, y,duration=0.2)
                    except Exception as e:
                        pass
                    time.sleep(1)
        except Exception as e:
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_success_win10.png",  confidence=0.7)
                if x and y:
                    for button in click_buttons:
                        try:
                            x, y = pyautogui.locateCenterOnScreen(button,  confidence=0.8)
                            if x and y:
                                human_click(x, y, duration=1)
                                time.sleep(0.2)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(0.2)
                        except Exception as e:
                            pass
            except Exception as e:
                pass
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('scrollshrt2.png',  confidence=0.8)
        if x and y:
            pyautogui.moveTo(300, 339, duration=0.2)
            pyautogui.scroll(-5000)
    except Exception as e:
        pass
    
    for button in click_buttons:
        try:
            x, y = pyautogui.locateCenterOnScreen(button,  confidence=0.8)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(0.2)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(0.2)
        except Exception as e:
            pass



shrinkme_nopage = 1    
def shrinkme_handle():
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=1)
    pyautogui.click(493,19, duration=1)
    title = get_focused_window_title()
    if destined_reached(title):
        return 5
    if newtab_validate(title):
        return 5
    try:
        x, y = pyautogui.locateCenterOnScreen('js_ok.png', region=[930,130,342,165] ,confidence=0.9)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(2)
            pyautogui.click(95, 62)  # Click on the 'No Internet' button
            time.sleep(2)
            return 5
    except Exception as e:
        pass
    if 'New Message!' in title:
        pyautogui.click(1887,108)
    close_ads()
    try:
        x, y = pyautogui.locateCenterOnScreen('conftransparent_ad.png', confidence=0.8)
        if x and y:
            print('Failed shrinkme_cssnotload')

            pyautogui.click(1179,333, duration = 0.4)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrinkme_cssnotload.png', confidence=0.95)
        if x and y:
            print('Failed shrinkme_cssnotload')
            pyautogui.press('f5')
            time.sleep(3)
            pyautogui.press('enter')
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrinkme_cssnotload2.png', confidence=0.95)
        if x and y:
            print('Failed shrinkme_cssnotload')
            pyautogui.press('f5')
            time.sleep(3)
            pyautogui.press('enter')
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrime_getlink.png', region=[680,110,557,909], confidence=0.7)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(1)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('recaptcha_fail2.png', region=[344,65,1208,977], confidence=0.98)
        if x and y:
            print('Failed Recaptcha')
            pyautogui.press('f5')
            time.sleep(3)
            pyautogui.press('enter')
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('recaptcha_valid.png', region=[699,156,530,870], confidence=0.9)
        if x and y:
            for i in range(6):
                close_ads()
                try:
                    x, y = pyautogui.locateCenterOnScreen('shrime_clickhere.png', region=[699,156,530,870], confidence=0.9)
                    if x and y:
                        human_click(x, y, duration=1)
                        time.sleep(1)
                        pyautogui.click(493,19, duration = 0.4)
                        time.sleep(3)
                        continue
                except Exception as e:
                    pass
                try:
                    x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                    if x and y:
                        pass
                except Exception as e:
                    
                    return 1  
            return 1
    except Exception as e:
        pass

    if color_exists_in_region((51, 51, 51), (15,200,100,350)):
        print("Blue pixel found in region!")
        pyautogui.click(22, 63)
        time.sleep(5)
        close_ads()
        time.sleep(3)

    region = (61, 181, 282, 743)
    target_color = (14, 14, 14)  # #0e0e0e

    if region_is_only_color_fast(target_color, region):
        print("Region is completely #0e0e0e")
        pyautogui.click(22, 63)
        time.sleep(5)

        
    try:
        x, y = pyautogui.locateCenterOnScreen('click2ver.png', region=[568,108,776,916], confidence=0.8)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(2)
            #return 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('srinkme_continue.png', region=[568,108,776,916], confidence=0.8)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(2)
            #return 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrink_generate.png', region=[568,108,776,916], confidence=0.8)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(1)
            return 1 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrime_getlink.png', region=[680,110,557,909], confidence=0.8)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(2)
            return 1
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrink_gourl.png', region=[680,110,557,909], confidence=0.8)
        if x and y:
            human_click(x, y, duration=1)
            time.sleep(1)
            pyautogui.click(493,19, duration = 0.4)
            time.sleep(2)
            return 1
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrink_urlink.png', region=[680,110,557,909], confidence=0.6)
        if x and y:
            title = get_focused_window_title()
            print("Link is ready")
            try:
                x, y = pyautogui.locateCenterOnScreen('shrink_ze.png', region=[680,110,557,909], confidence=0.8)
                if x and y:
                    print("Link is ready2")
                    for i in range(5):
                        title2 = get_focused_window_title()
                        if title2 != title:
                            return 
                        close_ads()
                        try:
                            x, y = pyautogui.locateCenterOnScreen('shrime_getlink.png', region=[680,110,557,909], confidence=0.7)
                            if x and y:
                                human_click(x, y, duration=1)
                                time.sleep(1)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(5)
                                #return
                        except Exception as e:
                            pyautogui.moveTo(400,409)
                            time.sleep(1)
                            pyautogui.scroll(-350)
                        try:
                            x, y = pyautogui.locateCenterOnScreen('getting_linkstuck.png', region=[680,110,557,909], confidence=0.9)
                            if x and y:
                                
                                time.sleep(4)
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('getting_linkstuck.png', region=[680,110,557,909], confidence=0.9)
                                    if x and y:
                                        pyautogui.press('f5')
                                        time.sleep(2)
                                        pyautogui.press('enter')
                                        return 1
                                except Exception as e:
                                    pass
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('shrime_getlink.png', region=[680,110,557,909], confidence=0.7)
                                    if x and y:
                                        human_click(x, y, duration=1)
                                        time.sleep(1)
                                        pyautogui.click(493,19, duration = 0.4)
                                        time.sleep(5)
                                        #return
                                except Exception as e:
                                    pass
                        except Exception as e:
                            pass
                else:
                    return 1
            except Exception as e:
                return
        title2 = get_focused_window_title()
        if title2 != title:
            return 
        pyautogui.scroll(5000)
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('shrime_socialg.png', region=[758,771,407,155], confidence=0.8)
        if x and y:
            try:
                x, y = pyautogui.locateCenterOnScreen('click2ver.png', region=[568,108,776,916], confidence=0.8)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(2)
                    #return 
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('srinkme_continue.png', region=[568,108,776,916], confidence=0.8)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(2)
                    #return 
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('shrink_generate.png', region=[568,108,776,916], confidence=0.8)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(1)
                    return 1 
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('shrime_getlink.png', region=[680,110,557,909], confidence=0.8)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(2)
                    return 1
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('shrink_gourl.png', region=[680,110,557,909], confidence=0.8)
                if x and y:
                    human_click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(493,19, duration = 0.4)
                    time.sleep(2)
                    return 1
            except Exception as e:
                pass
            pyautogui.moveTo(x, y)
            pyautogui.scroll(50000)
            return 1
    except Exception as e:
        pass

    if 'ShrinkMe.io' not in title or 'Shrink' not in title or 'Shrinkme' not in title or 'Shrinkme.io' not in title or 'fle' not in title:
        pyautogui.click(1885,107, duration=1)
        time.sleep(0.5)
        pyautogui.click(493,19, duration = 0.4)
        time.sleep(0.5)
    if 'ShrinkMe.io' not in title or 'Shrinkme' not in title or 'Shrinkme.io' not in title or 'ThemeZon' not in title or 'themezon' not in title or 'themezon.net' not in title: 
        shrinkme_nopage += 1
        if shrinkme_nopage >= 5:
            shrinkme_nopage = 1
            shorlink = random_link('link7')
            open_link(link = shorlink ,newtab = False)
            time.sleep(3)

clickads_gplink = True
clickads_gplink_attempts = 0



def gplink_handle():
    global clickads_gplink
    global clickads_gplink_attempts
    pyautogui.click(493,19, duration = 0.4)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.4)

    title = get_focused_window_title()
    #if destined_reached(title):
    #    return True
    if 'New Tab' in title:
        shorlink = random_link('link1')
        open_link(link = shorlink ,newtab = False)
        return 

    if 'Note from' in title:
        pyautogui.click(292,20)
        time.sleep(1)
        pyautogui.click(185,20)
        time.sleep(1)
        pyautogui.click(394,239, duration=1)
        time.sleep(1)
        pyautogui.click(394,239, duration=1)
        time.sleep(1)
        pyautogui.click(257,20)
        time.sleep(3)
        pyautogui.click(493,19, duration = 0.4)
        title = get_focused_window_title()
        if 'New Tab' in title:
            shorlink = random_link('link1')
            open_link(link = shorlink ,newtab = False)
            return 1
        

    if 'Just' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
            pyautogui.click(x, y,duration=1)
            time.sleep(1)
            pyautogui.click(x, y,duration=1)
            time.sleep(5)
            return

        except Exception as e:
            pass

    conbutfond_found = False
##########################################
    black_closeads_button = [

            ('blackcloseads_gp.png', None, 0.9),
            ('blackcloseads_gpskip.png', None, 0.9),
            ('noworkingpage.png', None, 0.95),
            ('rewrdingp.png', None, 0.9),
            ('continuenewgpg.png', None, 0.9),

            ('gp_verifynew.png', None, 0.9),
            ('gp_connew.png', None, 0.7),
            ('gp_connew3.png', None, 0.8),
            ('gp_verifynew3.png', None, 0.8),
            ('gp_verifynew2.png', None, 0.8),

        ]
        
    gpbuttons = ['gp_verifynew.png', 'gp_connew.png', 'gp_connew3.png', 'gp_verifynew2.png','gp_verifynew3.png']


    full_screen = pyautogui.screenshot()

    for img_name, reg, conf in black_closeads_button:
        try:
            # 3. Search WITHIN the screenshot we already took
            # Use grayscale=True for 30% more speed
            match = pyautogui.locate(img_name, full_screen, region=reg, confidence=conf)
            if match:
                if img_name == 'noworkingpage.png':
                    return 5
                if img_name == 'rewrdingp.png':
                    return 
                
                x, y = pyautogui.center(match)
                if img_name == 'continuenewgpg.png':
                    pyautogui.click(x, y, duration=0.1)
                    return 

                
                human_click(x, y, duration=0.2)
                time.sleep(0.5)
                pyautogui.click(493, 19, duration=0.3)

                if img_name in gpbuttons:
                    time.sleep(1)
                    conbutfond_found = True
                full_screen = pyautogui.screenshot()

        except Exception as e:
            pass

#################################################
    con_buttons = [
            
            ('cancel2.png', None, 0.9),
            ('close12new.png', None, 0.9),
            ('cancel3.png', None, 0.9),
            ('cancel1.png', None, 0.9),

    ]
    if conbutfond_found == True:
        combined_buttons = con_buttons + black_closeads_button
        for i in range(6):
            for img_name, reg, conf in combined_buttons:
                try:

                    match = pyautogui.locate(img_name, full_screen, region=reg, confidence=conf)
                    if match:
                        x, y = pyautogui.center(match)
                        human_click(x, y, duration=0.2)
                        time.sleep(0.5)
                        pyautogui.click(494,19, duration = 0.2)
                        time.sleep(0.5)
                        full_screen = pyautogui.screenshot()
                        
                        
                        
                except Exception as e:
                    pass
        return



    conbutfond_found = False
    for img_name, reg, conf in con_buttons:
        try:
            # 3. Search WITHIN the screenshot we already took
            # Use grayscale=True for 30% more speed
            match = pyautogui.locate(img_name, full_screen, region=reg, confidence=conf)
            if match:
                x, y = pyautogui.center(match)
                human_click(x, y, duration=0.2)
                time.sleep(0.5)
                pyautogui.click(494,19, duration = 0.2)
                time.sleep(0.5)
                conbutfond_found = True
                full_screen = pyautogui.screenshot()
                break
                
        except Exception as e:
            pass
    if conbutfond_found == True:
        for i in range(3):
            #pyautogui.click(494,19, duration = 0.2)
            for button in con_buttons:
                try:
                    x, y = pyautogui.locateCenterOnScreen(button,  confidence=0.9)
                    if x and y:
                        human_click(x, y, duration=0.2)
                        time.sleep(0.5)
                        pyautogui.click(494,19, duration = 0.2)
                        time.sleep(0.5)
                        clickads_gplink = False
                        
                except Exception as e:
                    pass

    close_ads()
    full_screen = pyautogui.screenshot()


    adsclosebutton = ['adremoved.png','resumevid_gp.png', 'skipvidgp.png', 'resumevidgp.png','closevideoadgp.png', 'consent5.png',  'closeadsgoogle1.png','closeadsgoole11.png','closeadsgoole10.png', 'closeadsgoole2.png', 'closeadsgoole3.png', 'closeadsgoole4.png', 'closeadsgoole5.png', 'closeadsgoole6.png', 'closeadsgoole7.png', 'closeadsgoole9.png','closeadsgoole8.png']
    for adbutton in adsclosebutton:
        try:
            if adbutton == 'closevideoadgp.png':
                match = pyautogui.locate(adbutton, full_screen, region=[900,212,714,522], confidence=0.9)
            elif adbutton == 'skipvidgp.png':
                match = pyautogui.locate(adbutton, full_screen,  confidence=0.9)
            else:
                match = pyautogui.locate(adbutton, full_screen,  region=[1,83,1914,956], confidence=0.9)
            if match:
                x, y = pyautogui.center(match)
                if adbutton == 'adremoved.png':
                    pyautogui.press('f5')
                    time.sleep(2)
                    return

                if adbutton == 'closevideoadgp.png':
                    pyautogui.click(x, y, duration=0.1)
                    time.sleep(0.5)
                    pyautogui.click(970, 638, duration=0.1)
                    time.sleep(0.5)
                    pyautogui.click(494,19, duration = 0.2)
                    return
                if adbutton == 'resumevidgp.png':
                    pyautogui.click(x, y, duration=0.1)
                    time.sleep(2)
                    pyautogui.click(494,19, duration = 0.2)
                    return
                
                pyautogui.click(x, y, duration=0.1)
                time.sleep(0.5)
                pyautogui.click(494,19, duration = 0.2)
                full_screen = pyautogui.screenshot()

        except Exception as e:
            pass


    
    pyautogui.click(1116,525, duration=0.5)


    
    if 'GPlinks' in title:
        pyautogui.moveTo(300,509)
        pyautogui.scroll(5000)
        time.sleep(0.5)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png",  confidence=0.7)
            if x and y:
                pyautogui.scroll(-40)
        except Exception as e:
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_success_win10.png",  confidence=0.7)
                if x and y:
                    pyautogui.scroll(-40)
            except Exception as e:
                pyautogui.scroll(-500)
            
        time.sleep(0.5)

        try:
            x, y = pyautogui.locateCenterOnScreen('gpverify.png', region=[610,55,670,989], confidence=0.75)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                pyautogui.moveTo(x, y, duration=1)
                pyautogui.scroll(-2000)
                time.sleep(1)
                
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('gpreload.png', region=[610,55,670,989], confidence=0.8)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(3)
                
        except Exception as e:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen('gpcontinue.png', confidence=0.8)
            if x and y:
                human_click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(493,19, duration = 0.4)
                pyautogui.click(100,300)
                time.sleep(1)
                for i in range(3):
                    time.sleep(1)
                    try:
                        x, y = pyautogui.locateCenterOnScreen('15sec.png', region=[610,55,670,989], confidence=0.95)
                        if x and y:
                            print("Page loaded but its 15sec",i)
                            pyautogui.click(100,300)
                            time.sleep(1)
                            pyautogui.click(493,19, duration = 0.4)
                            time.sleep(1)
                            continue
                    except Exception as e:
                        return 1
                
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('gpscroll.png', region=[610,55,670,989], confidence=0.9)
            if x and y:
                pyautogui.moveTo(x, y, duration=1)
                time.sleep(1)
                pyautogui.scroll(-2000)
                time.sleep(1)
                return 1
        except Exception as e:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
            if x and y:
                try:
                    x, y = pyautogui.locateCenterOnScreen('0zec_gp.png',  confidence=0.6)
                    if x and y:
                        print("Link is ready 000")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_success_win10.png",  confidence=0.7)
                            if x and y:
                                print("Link is ready 111")
                                for i in range(3):
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("gp_getlink.png", confidence=0.7)
                                        if x and y:
                                            print("Link is ready 222")
                                            pyautogui.click(x, y)
                                            time.sleep(1)
                                            pyautogui.click(493,19, duration = 0.4)
                                            time.sleep(2)
                                            return 1
                                    except Exception as e:
                                        pass
                                try:
                                    x, y = pyautogui.locateCenterOnScreen("gplinkload_stuck.png", confidence=0.8)
                                    if x and y:
                                        print("gplinkload_stuck found")
                                        for i in range(5):
                                            time.sleep(1)
                                            try:
                                                x, y = pyautogui.locateCenterOnScreen("gp_getlink.png",  confidence=0.7)
                                                if x and y:
                                                    print("Link is ready 222")
                                                    pyautogui.click(x, y)
                                                    time.sleep(1)
                                                    pyautogui.click(493,19, duration = 0.4)
                                                    time.sleep(2)
                                                    return 1
                                            except Exception as e:
                                                pass
                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("gplinkload_stuck.png", confidence=0.8)
                                            if x and y:
                                                print("gplinkload_stuck found2")
                                                pyautogui.press('f5')
                                                time.sleep(2)
                                                
                                                return 1
                                        except Exception as e:
                                            pass
                                        
                                except Exception as e:
                                    pass



                        except Exception as e:
                            pass
                        try:
                            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png",   confidence=0.7)
                            pyautogui.click(x, y,duration=1)
                            time.sleep(1)
                            pyautogui.click(x, y,duration=1)
                            time.sleep(3)

                        except Exception as e:
                            pass
                except Exception as e:
                    pass
                try:
                    x, y = pyautogui.locateCenterOnScreen("gplinkload_stuck2.png", confidence=0.8)
                    if x and y:
                        print("gplinkload_stuck2 found")
                        for i in range(6):
                            time.sleep(1)
                            try:
                                x, y = pyautogui.locateCenterOnScreen("gp_getlink.png",  confidence=0.7)
                                if x and y:
                                    print("Link is ready 222")
                                    pyautogui.click(x, y)
                                    time.sleep(1)
                                    pyautogui.click(493,19, duration = 0.4)
                                    time.sleep(2)
                                    return 1
                            except Exception as e:
                                pass
                        try:
                            x, y = pyautogui.locateCenterOnScreen("gplinkload_stuck2.png", confidence=0.8)
                            if x and y:
                                print("gplinkload_stuck2 found2")
                                pyautogui.press('f5')
                                time.sleep(2)
                                
                                return 1
                        except Exception as e:
                            pass
                        
                except Exception as e:
                    pass
        except Exception as e:
            pass

        try:
            x, y = pyautogui.locateCenterOnScreen('15sec.png', region=[610,55,670,989], confidence=0.95)
            if x and y:
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.5)
                pyautogui.click(103,300)
                time.sleep(0.5)
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(0.5)
                clip = clipboard.paste()
                if 'Please wait 15' in clip:
                    print("Page loaded but its 15secgggg")


                    try:
                        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                        if x and y:
                            for i in range(5):
                                time.sleep(1)
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(0.5)
                                pyautogui.hotkey('ctrl', 'c')
                                time.sleep(0.5)
                                pyautogui.click(103,300)
                                time.sleep(0.5)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(0.5)
                                clip = clipboard.paste()
                                if 'Please wait 15' in clip:
                                    print("Page loaded but its 15sec",i)
                                    
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                                        if x and y: 
                                            pyautogui.click(95,65, duration=1)
                                            time.sleep(1)
                                            pyautogui.click(493,19, duration = 0.4)
                                            time.sleep(5)   
                                            return 1
                                    except Exception as e:
                                        pass
                                        continue
                                else:
                                    return
                            pyautogui.click(95,65, duration=1)
                            time.sleep(1)
                            pyautogui.click(493,19, duration = 0.4)
                            time.sleep(5)   

                            return
                    except Exception as e:
                        pass
        except Exception as e:
            pass

        






def shortx_handle():
    pyautogui.click(493,19, duration = 0.4)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=1)

    title = get_focused_window_title()
    if destined_reached(title):
        return 5
    if newtab_validate(title):
        return 5
    if '522: Connection' in title:
        pyautogui.press('f5')
        time.sleep(1)
        return
    if 'Just' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
            pyautogui.click(x, y,duration=1)
            time.sleep(1)
            pyautogui.click(x, y,duration=1)
            time.sleep(5)

        except Exception as e:
            pass
    try:
        x, y = pyautogui.locateCenterOnScreen('acceptsxg.png', region=[572,68,762,960], confidence=0.7)
        if x and y:
            pyautogui.click(x,y, duration=0.4)
            time.sleep(0.5)
    except Exception as e:
        pass

    close_ads()

    button_clicked = False
    full_screen = pyautogui.screenshot()
    shortxbuttons = ['getlink_shotx.png', 'getlink_shotx2.png', 'imnorobo_shortx.png', 'gen_shotx.png', 'genlink2_shortx.png','shortxcss.png', 'linkdown_shotx.png', 'clickhere_shotx.png', 'gen_shotx.png']
    for img_name in shortxbuttons:
        try:
            match = pyautogui.locate(img_name, full_screen, region=[572,68,762,960], confidence=0.9)
            if match:
                x, y = pyautogui.center(match)
                pyautogui.click(x,y)
                #human_click(x, y, duration=0.1)
                time.sleep(0.5)
                if img_name == 'clickhere_shotx.png':
                    return
                pyautogui.click(493,19, duration = 0.4)
                time.sleep(1)
                full_screen = pyautogui.screenshot()
                button_clicked = True

        except Exception:
            pass
    
    if button_clicked:
        for i in range(3):
            for img_name in shortxbuttons:
                try:
                    match = pyautogui.locate(img_name, full_screen, region=[572,68,762,960], confidence=0.9)
                    match_reload = pyautogui.locate('loaded_page.png', full_screen, region=[60,33,77,58], confidence=0.95)
                    if match and match_reload:

                        x, y = pyautogui.center(match)
                        pyautogui.click(x,y)
                        #human_click(x, y, duration=0.1)
                        time.sleep(0.5)
                        if img_name == 'clickhere_shotx.png':
                            return
                        pyautogui.click(493,19, duration = 0.4)
                        time.sleep(1)
                        full_screen = pyautogui.screenshot()
                        button_clicked = True
                        if img_name == 'linkdown_shotx.png':
                            time.sleep(2)

                        continue
                except Exception:
                    pass



    try:
        x, y = pyautogui.locateCenterOnScreen('please_wait_get.png', region=[572,68,762,960], confidence=0.8)
        if x and y:
            try:
                x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                if x and y:
                    for i in range(7):
                        time.sleep(1)
                        try:
                            x, y = pyautogui.locateCenterOnScreen('getlink_shotx.png', region=[572,68,762,960], confidence=0.8)
                            if x and y:
                                pyautogui.click(x,y)
                                time.sleep(1)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(1)
                                pyautogui.click(x,y)
                                time.sleep(1)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(1)
                                return 1
                                
                        except Exception as e:
                            pass
                        try:
                            x, y = pyautogui.locateCenterOnScreen('getlink_shotx2.png', region=[572,68,762,960], confidence=0.8)
                            if x and y:
                                pyautogui.click(x,y)
                                time.sleep(1)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(1)
                                pyautogui.click(x,y)
                                time.sleep(1)
                                pyautogui.click(493,19, duration = 0.4)
                                time.sleep(1)
                                return 1
                                
                        except Exception as e:
                            pass
                    pyautogui.press('f5')
                    time.sleep(2)
                    pyautogui.press('enter')
            except Exception as e:
                pass
    except Exception as e:
        pass






def adding_extensions():
    open_link(link = 'chrome://extensions/', newtab = False)
    time.sleep(2)
    devon = True
    
    for i in range(63):
        time.sleep(1)
        print("Checking for extension installation...", i)
        if devon:
            try:
                x, y = pyautogui.locateCenterOnScreen('devmod_off.png', region=[1684,48,230,108], confidence=0.98)
                if x and y:
                    pyautogui.click(1894, 116)
                    time.sleep(1)
                    devon = False

            except Exception as e:
                pass
        try:
            x, y = pyautogui.locateCenterOnScreen('stealth_dom.png',  confidence=0.95)
            if x and y:
                #time.sleep(1)
                return True

        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('load_unpacked.png', confidence=0.9)
            if x and y:
                pyautogui.click(x, y)
                time.sleep(1)
                for i in range(20):
                    time.sleep(1)
                    try:
                        x, y = pyautogui.locateCenterOnScreen('directory_extension.png', confidence=0.8)
                        if x and y:
                            pyautogui.press('enter')
                            time.sleep(1)
                            break

                    except Exception as e:
                        pass
                    try:
                        x, y = pyautogui.locateCenterOnScreen('directory_extension3.png', confidence=0.8)
                        if x and y:
                            pyautogui.press('enter')
                            time.sleep(1)
                            break

                    except Exception as e:
                        pass
        except Exception as e:
            pass

def adurl_handle():
    pyautogui.click(493,19, duration = 0.2)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.2)

    title = get_focused_window_title()


    if 'Just' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
            pyautogui.click(x, y,duration=1)
            time.sleep(1)
            pyautogui.click(x, y,duration=1)
            time.sleep(5)

        except Exception as e:
            pass
    close_ads()
    buttonlist = ['nextadurl.png', 'continue_aduirl.png', 'continuelined_adurl.png']
    for buton in buttonlist:
        try:
            x, y = pyautogui.locateCenterOnScreen(buton, confidence=0.8)
            if x and y:
                human_click(x, y, duration=0.2)

        except Exception as e:
            pass
    if 'Adurl.io' in title:
        pyautogui.click(1889,135, duration=0.2)
        try:
            x, y = pyautogui.locateCenterOnScreen('get_linkadurl.png', confidence=0.8)
            if x and y:
                human_click(x, y, duration=0.2)

        except Exception as e:
            pass
        pyautogui.moveTo(300,309)
        pyautogui.scroll(-250)

adlink_ocr_answer = 'ng'
adlink_ocr_answerretry = "ng"
adlink_ocr_answerrewait = "ng"
def adlink_handle():
    global adlink_ocr_answer
    global adlink_ocr_answerretry
    global adlink_ocr_answerrewait
    print('adlink_ocr_answer:', adlink_ocr_answer)
    title_ocr = ocr_screen_region(38,1,230,36)
    print('title_ocr:', title_ocr)
    if 'seconds' in title_ocr:
        print('orc fond')
        title = get_focused_window_title()
        if 'seconds' in title:
            pyautogui.hotkey('ctrl', 't')
        return
    pyautogui.click(493,19, duration = 0.2)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.2)

    title = get_focused_window_title()
    if 'seconds' in title:
        pyautogui.hotkey('ctrl', 't')
        return

    if 'Just' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
            pyautogui.click(x, y,duration=1)
            time.sleep(1)
            pyautogui.click(x, y,duration=1)
            time.sleep(5)

        except Exception as e:
            pass


    close_ads()
    try:
        x, y = pyautogui.locateCenterOnScreen("getlink_adlink.png", confidence=0.9)
        if x and y:
            human_click(x, y, duration=0.2)

    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen("closedlinksg.png", confidence=0.95)
        if x and y:
            pyautogui.click(x, y, duration=0.2)

    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen("closeadsggadlink.png",region=[624,106,697,924], confidence=0.9)
        if x and y:
            human_click(x, y, duration=0.2)

    except Exception as e:
        pass
    print('checking adlink ocr')

    try:
        x, y = pyautogui.locateCenterOnScreen("check_adlink.png",confidence=0.6)
        if x and y:
            print('ocrtest detect adlinm')
            answer = ocrcaptchaadlink(826,454,252,69)
            print('answer:', answer)
            print('adlink_ocr_answer:', adlink_ocr_answer)
            if adlink_ocr_answer == answer:
                print('sameocrissue twice, refreshing')
                if adlink_ocr_answerrewait == answer:
                    print('sameocrissue thrice, opening new tab')
                    return
                try:
                    x, y = pyautogui.locateCenterOnScreen("refreshcodeadlin.png", confidence=0.7)
                    if x and y:
                        human_click(x, y, duration=0.2)

                except Exception as e:
                    pass
                time.sleep(8)
                adlink_ocr_answerrewait = answer
                return
            

                #pyautogui.press('f5')
            adlink_ocr_answer = answer
            pyautogui.click(1002,632, duration=0.2)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.5)
            pyautogui.press('delete')
            time.sleep(0.5)
            pyautogui.typewrite(adlink_ocr_answer)
            time.sleep(0.5)
            pyautogui.click(x, y, duration=0.2)
            time.sleep(10)


    except Exception as e:
        pass

    print('checking adlink ocr NOIO')
    try:
        x, y = pyautogui.locateCenterOnScreen("gonext_adlink.png" , confidence=0.7)
        if x and y:
            human_click(x, y, duration=0.2)

    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen("scrolldownadlinks.png", confidence=0.8)
        if x and y:
            print('10sec detected, simulating clicks to bypass')
            for i in range(6):
                pyautogui.rightClick(random.randint(700, 850), random.randint(225, 250), duration=0.2)
                pyautogui.rightClick(random.randint(700, 850), random.randint(790, 800), duration=0.2)
                time.sleep(1)
                try:
                    x, y = pyautogui.locateCenterOnScreen("opennwtablnk.png" , confidence=0.9)
                    if x and y:
                        human_click(x, y, duration=0.2)
                        return

                except Exception as e:
                    pass
                title_ocr = ocr_screen_region(38,1,230,36)
                if 'seconds' in title_ocr:
                    pyautogui.hotkey('ctrl', 't')
                    return
    except Exception as e:
        pass


mysite_count = 1
def mysite_handle():
    pyautogui.press('enter')
    global mysite_count
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=1)
    pyautogui.click(493,19, duration = 0.4)
    time.sleep(1)
    title = get_focused_window_title()
    #
    # if destined_reached(title):
    #    return True
    if 'Just' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
            pyautogui.click(x, y,duration=1)
            time.sleep(1)
            pyautogui.click(x, y,duration=1)
            time.sleep(5)

        except Exception as e:
            pass

    try:
        x, y = pyautogui.locateCenterOnScreen('fbg_lg.png', region=[394,83,303,123], confidence=0.95)
        if x and y:
            pyautogui.scroll(500)
            time.sleep(1)
            pyautogui.click(1090, 820)  # Click on the 'Leave' button
            time.sleep(1)
            pyautogui.click(1117, 550)
            pyautogui.click(1117, 540)
            pyautogui.click(1117, 530)
            pyautogui.click(1117, 520)
            pyautogui.click(1117, 510)
            pyautogui.click(1117, 500)
            pyautogui.click(1117, 490)
            pyautogui.click(1117, 480)
            pyautogui.click(1117, 470)
            pyautogui.click(1117, 460)
            pyautogui.click(1117, 450)
            pyautogui.click(1117, 430)
            pyautogui.click(1117, 420)
            pyautogui.click(1117, 410)
            pyautogui.click(1117, 400)
            return 
    except Exception as e:
        pass
    try:
        x, y = pyautogui.locateCenterOnScreen('yt_logo.png', region=[699,56,240,136], confidence=0.94)
        if x and y:
            pyautogui.click(885,394)
            time.sleep(1)
            return 
    except Exception as e:
        pass
    if 'Free Crypto' in title or 'New Message!' in title:
        print("Free Crypto or New Message found, skipping...",mysite_count)
        if mysite_count >= 25:
            mysite_count = 1
            shorlink = 'https://eloquent-banoffee-bb1d42.netlify.app' #random_link(mysite_handle)
            open_link(link = shorlink ,newtab = False)
            time.sleep(3)
        else:
            mysite_count +=1
        pyautogui.click(1885,107, duration=1)
        time.sleep(0.5)
        pyautogui.click(493,19, duration = 0.4)

        pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.5)
        pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.3)
        pyautogui.click(random.randint(50, 1500), random.randint(40, 700), duration=0.3)
        pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.5)
        #pyautogui.click(493,19, duration=1)
        time.sleep(1)   
    else:
        if 'Youtube' in title or 'Facebook'in title:
            pass
        else:
            shorlink = 'https://eloquent-banoffee-bb1d42.netlify.app' #random_link(mysite_handle)
            open_link(link = shorlink ,newtab = False)
            time.sleep(3)
            pyautogui.press('enter')
            mysite_count = 1
            pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.5)
            pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.3)
            pyautogui.click(random.randint(50, 1500), random.randint(40, 700), duration=0.3)
            pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.5)
            #pyautogui.click(493,19, duration=1)
            time.sleep(1) 
            

import json

def is_proxy_no(data_str):
    try:
        data = json.loads(data_str)
        # Skip the "status" key and look for the IP key
        for key in data:
            if ':' in key or '.' in key:  # Looks for an IP address (IPv6 or IPv4)
                ip_info = data[key]
                return ip_info.get('proxy', '') == 'no'
        return False  # No IP info found
    except json.JSONDecodeError:
        print("Invalid JSON")
        return False

def ipcheck_handle(ipaddress):
    open_link(link=f'https://proxycheck.io/v3/{ipaddress}', newtab=False)
    time.sleep(5)
    pyautogui.click(200, 219)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    data_str = clipboard.paste()
    if data_str:
        pass
    else:
        for i in range(5):
            time.sleep(2)
            pyautogui.click(200, 219)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.5)
            data_str = clipboard.paste()
            if data_str:
                break
    print("Data string:", data_str)
    try:
        data = json.loads(data_str)

        for key in data:
            if ':' in key or '.' in key:
                ip_info = data[key]
                
                # Extract needed fields
                detections = ip_info.get("detections", {})
                network = ip_info.get("network", {})
                location = ip_info.get("location", {})

                ip = key
                country = location.get("country_name", "Unknown")
                proxy = detections.get("proxy", True)
                vpn = detections.get("vpn", True)
                type_ = network.get("type", "Unknown")

                # Check both proxy and vpn
                is_clean = (proxy is False and vpn is False)

                return {
                    "ip": ip,
                    "country": country,
                    "type": type_,
                    "is_clean": is_clean
                }

        return None  # No IP info found

    except json.JSONDecodeError:
        print("Invalid JSON")
        return None
    


def tuxler_stat_check():
    try:
        for i in range(30):
            focus_tuxler()
            time.sleep(2)
            pyautogui.click(326,720)
            pyautogui.click(326,707)
            
            time.sleep(1)
            pyautogui.click(326,757)
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_on.png', confidence=0.9)
                if x and y:
                    break
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
                if x and y:
                    break
                    
            except Exception as e:
                print('tuxler off not found')
                pyautogui.hotkey('alt','tab')
                time.sleep(1)
                pyautogui.press('esc')
                time.sleep(1)

        try:
            x, y = pyautogui.locateCenterOnScreen('butpremium_tuxler.png', confidence=0.9)
            if x and y:
                print("Tuxler Logout detected, changing account...")
                tuxler_account_changer()
                
                
        except Exception as e:
            print("NOT Tuxler Logout detected")
        pyautogui.click(148,116)
        time.sleep(2)
        pyautogui.click(211,146)
        time.sleep(2)

        text = ocr_screen_region(119, 513, 382, 132)
        # Extract values
        expire, location_changes = extract_expire_and_location(text)
        print(f"\nExtracted -> Expiration date: {expire}, Location changes: {location_changes}")
        pyautogui.click(326,720)
        
        
        time.sleep(1)
        pyautogui.click(326,757)
        return expire, location_changes
    except Exception as e:
        print("Error during Tuxler status check:", e)
        return None, None
    
def read_line_from_file(file_path, line_number):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        if 1 <= line_number <= len(lines):
            item = lines[line_number - 1].strip()
            print(f"Line {line_number}: {item}")
            return item
        else:
            print(f"Line number {line_number} is out of range. File has {len(lines)} lines.")
            return "WorldWide"
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return "WorldWide"
    except Exception as e:
        print(f"Error reading file: {e}")
        return "WorldWide"

def export_farm_to_txt(farm_key: str, filename: str = None):
    """Fetch country list from MongoDB by farm key and save to txt file"""
    doc = maindb_collection.find_one({"type": "traffic_flow"}, {farm_key: 1, "_id": 0})
    
    if not doc or farm_key not in doc:
        print(f"⚠️ No data found for {farm_key}")
        return
    
    country_list = doc[farm_key]
    
    if not filename:
        filename = f"{farm_key}.txt"
    
    # Save each country on new line
    with open(filename, "w", encoding="utf-8") as f:
        for country in country_list:
            f.write(f"{country}\n")
    
    print(f"✅ Exported {len(country_list)} items from {farm_key} → {filename}")


def restart_tuxler():
    app_path = r"C:\Program Files (x86)\tuxlerVPN\tuxlerVPN.exe"
    process_name = "tuxler"

    # Kill all running tuxler processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                print(f"Killing {proc.info['name']} (PID {proc.info['pid']})")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Wait a bit before restarting
    time.sleep(2)

    # Start the app again
    print("Starting Tuxler...")
    launch_via_run_dialog(app_path)
    #process = subprocess.Popen([app_path], shell=False)

    # Wait for it to show up
    time.sleep(10)

    # Verify if running
    running = any("tuxler".lower() in (p.info['name'] or "").lower() 
                  for p in psutil.process_iter(['name']))
    if running:
        print("Tuxler started successfully ✅")
        return True
    else:
        print("Failed to start Tuxler ❌")
        launch_via_run_dialog(app_path)
    time.sleep(5)
    running = any("tuxler".lower() in (p.info['name'] or "").lower() 
                  for p in psutil.process_iter(['name']))
    if running:
        print("Tuxler started successfully ✅")
        return True
    else:
        print("Failed to start Tuxler ❌")
        launch_via_run_dialog(app_path)
    return process


def is_between_12pm_and_6pm():
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)

    current_time = sri_lanka_time.time()

    start = datetime.time(2, 0, 0)  # 12:00 PM
    end = datetime.time(18, 0, 0)    # 06:00 PM

    return start <= current_time <= end
# Example usage


true_count = 40
false_count = 60

# Generate a random order of True and False
bool_list = [True]*true_count + [False]*false_count
random.shuffle(bool_list)  # shuffle so True/False are randomly distributed

# Create a dictionary for quick lookup
premadelist = {i+1: bool_list[i] for i in range(100)}
print(premadelist)
# Function to check the value for a given number
def checkodd(premadelist, number):
    return premadelist.get(number, None)  # returns None if number not in list


def get_gplink_bug_status():
    doc = maindb_collection.find_one({"type": "main"})
    if doc and "gplink_bug" in doc:
        satt = doc["gplink_bug"]
        print("gplink_bug status from DB:", satt)
        if satt == "true":
            return True
    return False  # Default value if not found

def hyperhustlebrows():
    pyautogui.click(493,19, duration = 0.2)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.3)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.3)
    pyautogui.moveTo(random.randint(50, 1500), random.randint(40, 700), duration=0.3)

    title = get_focused_window_title()
    if 'Hyper Hustle' in title or 'hyperhustle.online' in title:
        print("Already on Hyper Hustle page.")
    else:

        if random.random() < 0.93:   # 0.9 = 90%
            shorlink = random_link('link3')
        else:
            shorlink = "https://hyperhustle.online/"
        switch_to_window(window3)
        pyautogui.click(493,19, duration = 0.4)
        shorlink = random_link('link3')
        open_link(link = shorlink ,newtab = False)
        time.sleep(2)
        pyautogui.click(1056,192, duration=0.6)



    close_ads()


    try:
        x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
        if x and y:
            if '– Hyper Hustle' in title:
                if random.random() < 0.6: 
                    pyautogui.moveTo(random.randint(300, 1600), random.randint(300, 900), duration=0.3)
                    pyautogui.moveTo(random.randint(300, 1600), random.randint(300, 900), duration=0.3)
                    if random.random() < 0.5: 
                        pyautogui.moveTo(random.randint(300, 1600), random.randint(300, 900), duration=0.4)
                    pyautogui.scroll(-random.randint(70, 300))
                    if random.random() < 0.5: 
                        pyautogui.scroll(-random.randint(70, 300))
                        if random.random() < 0.7: 
                            pyautogui.click(random.randint(950, 1050), random.randint(640, 900), duration=0.5)
                    if random.random() < 0.5: 
                        pyautogui.scroll(-random.randint(70, 300))
                        if random.random() < 0.7: 
                            pyautogui.click(random.randint(950, 1050), random.randint(640, 900), duration=0.5)
                    if random.random() < 0.5: 
                        pyautogui.scroll(-random.randint(70, 300))
                        if random.random() < 0.7: 
                            pyautogui.click(random.randint(950, 1050), random.randint(640, 900), duration=0.5)
                    if random.random() < 0.5: 
                        pyautogui.scroll(-random.randint(70, 300))
                        if random.random() < 0.7: 
                            pyautogui.click(random.randint(950, 1050), random.randint(640, 900), duration=0.5)
                    time.sleep(1)
                    return
                else:
                    if random.random() < 0.9:
                         pyautogui.scroll(random.randint(200, 900))
                    if random.random() < 0.5: 
                        pyautogui.click(random.randint(1460, 1550), random.randint(887, 868), duration=0.5)
                        time.sleep(0.5)
                        return
                    elif random.random() < 0.6: 
                        pyautogui.click(random.randint(1330, 1425), random.randint(130, 132), duration=0.5)
                        time.sleep(0.5)
                        return
                    elif random.random() < 0.5: 
                        pyautogui.click(random.randint(1460, 1550), random.randint(760, 800), duration=0.5)
                        time.sleep(0.5)
                        return
                    elif random.random() < 0.5: 
                        pyautogui.click(random.randint(1460, 1550), random.randint(650, 695), duration=0.5)
                        time.sleep(0.5)
                        return

            else:
                if random.random() < 0.5: 
                    pyautogui.click(random.randint(950, 1050), random.randint(640, 900), duration=0.5)
                if random.random() < 0.5: 
                    pyautogui.click(random.randint(950, 1050), random.randint(640, 900), duration=0.5)
                if random.random() < 0.5: 
                    pyautogui.click(random.randint(950, 1050), random.randint(640, 900), duration=0.5)
             
    except Exception as e:
        pass

###########################################################
update_content_extension()
export_farm_to_txt(f"farm{farm_id}","traffic_flow.txt")  # saves custom filename
gplink_bug = False
gplink_bug = get_gplink_bug_status()
print("gplink_bug status:", gplink_bug)
duration_time = time.time()
sites_done = 0
expire, location_changes = 29, 2 
tux_stat_check = 5 
timeoutforlink = 5000
testing = True
preip = ''
while True:
    window0 = None
    window1 = None
    window2 = None
    window3 = None
    window4 = None
    cutty_window = None
    browsero_Failed = True
    ip = None
    proxy = None
    proxy_type = None
    country = None
    fingerpintid= None
    adspowerfreeze = 1

    window1_lastclick = time.time()
    window2_lastclick = time.time()
    window3_lastclick = time.time()
    window4_lastclick = time.time()
    layout = 1
    print("Starting main loop...")
    if testing:
        location_changes += 1
        tux_stat_check += 1
        if tux_stat_check >= 5 and Mysterium_Mode == False or location_changes >= 96 and Mysterium_Mode == False:
            update_content_extension()
            gplink_bug = get_gplink_bug_status()
            print("gplink_bug status:", gplink_bug)
            focus_and_close_window('Software Update')
            running = any("tuxler".lower() in (p.info['name'] or "").lower() 
                        for p in psutil.process_iter(['name']))
            if running:
                print("Tuxler started successfully ✅")

            else:
                app_path = r"C:\Program Files (x86)\tuxlerVPN\tuxlerVPN.exe"
                process = subprocess.Popen([app_path], shell=False)
                print("Failed to start Tuxler ❌")
                tux_stat_check += 10 
                continue
            expire, location_changes = tuxler_stat_check()
            tux_stat_check = 1
            export_farm_to_txt(f"farm{farm_id}","traffic_flow.txt")  # saves custom filename


        if expire < 1 and Mysterium_Mode == False or location_changes >= 100 and Mysterium_Mode == False:
            print("Tuxler needs attention, exiting...")
            print("Tuxler Expire days:", expire, "Location changes used:", location_changes)
            if tuxler_account_changer():
                location_changes = 1
                continue
            for i in range(30):
                focus_tuxler()
                time.sleep(2)
                pyautogui.click(326,720)
                
                
                time.sleep(1)
                pyautogui.click(326,757)
                try:
                    x, y = pyautogui.locateCenterOnScreen('tuxler_on.png', confidence=0.9)
                    if x and y:
                        pyautogui.click(x, y)
                        time.sleep(3)
                        break
                        
                except Exception as e:
                    pass
                try:
                    x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
                    if x and y:
                        break
                        
                except Exception as e:
                    print('tuxler off not found')
                    pyautogui.hotkey('alt','tab')
                    time.sleep(1)
                    pyautogui.press('esc')
                    time.sleep(1)
            focus_and_close_window('SunBrowser')
            while True:
                if is_between_12pm_and_6pm():
                    print("Yes, current time in Sri Lanka is between 12 PM and 6 PM.")
                    time.sleep(100)
                else:
                    print("No, it's outside 12 PM - 6 PM in Sri Lanka.")
                    break
                    
        
        
        focus_and_maximize_window('SunBrowser')
        focus_and_maximize_window('SunBrowser')
        focus_and_maximize_window('SunBrowser')
        focus_and_maximize_window('SunBrowser')
        layout = 1


        browser_ready = create_browser()

        try:
            x, y = pyautogui.locateCenterOnScreen('limit_adpower.png', region=[927,173,480,260],confidence=0.9)
            if x and y:
                print("adpower browser Limited")
                continue
        except Exception as e:
            pass
        if not browser_ready:
            print("Browser not ready, retrying...")
            continue
        time.sleep(15)
        focus_and_maximize_window('Chromium')
        focus_and_maximize_window('P-')
        focus_and_maximize_window('SunBrowser')
        focus_and_maximize_window('New Tab')
        for i in range(40):
            clipboard.copy('')
            focus_and_maximize_window('Chromium')
            focus_and_maximize_window('SunBrowser')

            try:
                x, y = pyautogui.locateCenterOnScreen('bookmarksggg.png', confidence=0.7)
                if x and y:
                    pyautogui.rightClick(334,96)
                    time.sleep(1)
                    pyautogui.click(388,573)    
                    time.sleep(1)    
                    try:
                        x, y = pyautogui.locateCenterOnScreen('bookmarksggg.png', confidence=0.7)
                        if x and y:
                            pyautogui.rightClick(334,96)
                            time.sleep(1)
                            pyautogui.click(388,604)    
                            time.sleep(1)   
                    except Exception as e:   
                        print("Second bookmark close failed")    
                    try:
                        x, y = pyautogui.locateCenterOnScreen('bookmarksggg.png', confidence=0.7)
                        if x and y:
                            pyautogui.rightClick(334,96)
                            time.sleep(1)
                            pyautogui.click(388,543)    
                            time.sleep(1)   
                    except Exception as e:   
                        print("Second3  bookmark close failed")       
            except Exception as e:
                try:
                    x, y = pyautogui.locateCenterOnScreen('rektcaptcha_icon.png', region=[1653,31,261,61], confidence=0.9)
                    if x and y:
                        try:
                            x, y = pyautogui.locateCenterOnScreen('clip_adspower.png', region=[956,80,348,192], confidence=0.9)
                            if x and y:
                                human_click(x, y, duration=1)
                                time.sleep(1)
                                if clipboard.paste() != '':
                                    browsero_Failed = False
                                    break

                                    
                        except Exception as e:
                            print("Clipboard icon not found, retrying...", i)    
                            try:
                                x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[60,33,77,58], confidence=0.95)
                                if x and y:
                                    adspowerfreeze += 1
                                    if adspowerfreeze >= 6:
                                        pyautogui.press('f5')
                                        time.sleep(4)
                                        adspowerfreeze = 1
                                    print("Page loaded but adspowerfreeze not found, retrying...", adspowerfreeze)

                                        
                            except Exception as e:
                                pass
                except Exception as e:
                    print("Rektcaptcha icon not found, retrying...", i)
                    if i == 24:
                        
                        print("Rektcaptcha icon not found after 25 attempts, exiting...")
                    time.sleep(3)
        if browsero_Failed:
            continue

        result = ipcheck_handle(clipboard.paste())
        if result:
            ip = result["ip"]
            is_clean = result["is_clean"]
            proxy_type = result["type"]
            country = result["country"]
            if is_clean:
                print(ip, is_clean, proxy_type, country)
            else:
                continue

            print(ip, is_clean, proxy_type, country)
        else:
            print("IP check failed")
        if ip == preip:
            restart_tuxler()
            continue
        preip = ip

        adding_extensions()
        always_active()

        #pyautogui.hotkey('ctrl', 't')
        #time.sleep(2)
        #pyautogui.click(257,20)
        #time.sleep(1)
        #fingerpintid = fingerpint()
        #pyautogui.hotkey('ctrl', 'w')

        #rek_ready = configure_rektcaptcha()
        
        #if not rek_ready :
        #    print("Rektcaptcha not ready, retrying...")
        #    continue
    else:
        focus_and_maximize_window('SunBrowser')
    window1 = open_detatch_tab()
    window2 = open_detatch_tab()
    #cutty_window = open_detatch_tab()
    window3 = open_detatch_tab()
    #window4 = open_detatch_tab()
    print("Window IDs:", window1, window2)
    script_elapsed_time3 = time.time() - duration_time
    duration_time_sec = int(script_elapsed_time3)
    shrink_Timeout = False #checkodd(premadelist, location_changes)
    if testing and shrink_Timeout:
        add_farm_activity(farmid=f"Farm{farm_id}", country= country, ipaddress= ip , duration = proxy_type, sites = f'{sites_done}x | 4 ', fingerprints_id= fingerpintid, tuxler_left=location_changes, expiredate=expire)

    if testing and not shrink_Timeout:
        add_farm_activity(farmid=f"Farm{farm_id}", country= country, ipaddress= ip , duration = proxy_type, sites = f'{sites_done} | 4', fingerprints_id= fingerpintid, tuxler_left=location_changes, expiredate=expire)

    duration_time = time.time()
    layout = 1
    if layout == 1:
        switch_to_window(window1)
        pyautogui.click(493,19, duration = 0.4)
        shorlink = random_link('link1')
        open_link(link = shorlink ,newtab = False)
        time.sleep(2)
        switch_to_window(window2)
        pyautogui.click(493,19, duration = 0.4)
        shorlink = random_link('link2')
        open_link(link = shorlink ,newtab = False)
        time.sleep(2)

        switch_to_window(window3)
        pyautogui.click(493,19, duration = 0.4)
        shorlink = random_link('link4')
        open_link(link = shorlink ,newtab = False)
        time.sleep(2)
        
        hyperrefreshtime1 = random.randint(200, 500)
        hyperrefreshtime2 = random.randint(200, 800)
        hyperrefreshtime3 = random.randint(400, 1000)
        hyperrefreshtime4 = random.randint(600, 1000)

        hyperrefreshstat1 = False
        hyperrefreshstat2 = False
        hyperrefreshstat3 = False
        hyperrefreshstat4 = False


        #switch_to_window(cutty_window)
        #pyautogui.click(493,19, duration = 0.4)
        #shorlink = random_link('link5')
        #open_link(link = shorlink ,newtab = False)
        #time.sleep(2)

    ############################################################

    if layout != 0:

        tpi = None
        if gplink_bug:
            tpi = True
        adrin = None
        fc_lc = None
        cuty = None
        oii = None
        ggwin1_unvalid = 1
        ggwin2_unvalid = 1
        ggwin3_unvalid = 1
        ggwin4_unvalid = 1


        time.sleep(10)
        #focus_and_close_window('New Tab')
        gg = None
        started = time.time()
        sites_done = 0
        shrinkearn_continue = 1
        window1_lastclick = time.time()
        window2_lastclick = time.time()
        window3_lastclick = time.time()
        window4_lastclick = time.time()
        #layout = 1
        clickads_gplink = True
        clickads_gplink_attempts = 0

        check_indx = 1
        while gg == None:
            check_indx += 1
            try:



                script_elapsed_time = time.time() - started
                script_seconds_only = int(script_elapsed_time)
                print(f"Script has been running for {script_seconds_only} seconds")
                if script_seconds_only > 1000 and layout == 16:


                        print(cuty, tpi, 'Cuty and tpi is true')
                        focus_and_maximize_window('SunBrowser')
                        focus_and_maximize_window('New Tab')

                        open_link(link = 'chrome-extension://ehllkhjndgnlokhomdlhgbineffifcbj/data/options/index.html',newtab = False)
                        time.sleep(3)
                        pyautogui.click(850, 559)  # C
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl', 'a')  # Select all text
                        pyautogui.press('backspace')  # Clear the text
                        pyautogui.typewrite('mobiend.com, healthy4pepole.com, adurl.io')
                        time.sleep(0.5)
                        pyautogui.click(547, 916)  # C
                        time.sleep(1)
                        pyautogui.click(547, 874)  # C
                        time.sleep(1)
                        pyautogui.click(493,19, duration = 0.4)

                        extra_win = get_focused_window_id()
                        time.sleep(2)
                        window3 = open_detatch_tab()
                        window4 = open_detatch_tab()

                        
                        time.sleep(2)
                        switch_to_window(window3)
                        pyautogui.click(493,19, duration = 0.4)
                        shorlink = random_link('link5')
                        open_link(link = shorlink ,newtab = False)
                        time.sleep(2)
                        switch_to_window(window4)
                        pyautogui.click(493,19, duration = 0.4)
                        shorlink = random_link('link8')
                        open_link(link = shorlink ,newtab = False)
                        time.sleep(2)

                        time.sleep(10)
                        layout = 2

                        close_window(window1)
                        #close_window(cutty_window)
                        close_window(window2)


                if script_seconds_only >720:
                    gg = True
                #if script_seconds_only > 700:
                #    tpi = True

                try:
                    x, y = pyautogui.locateCenterOnScreen('leavebuttong.png',  confidence=0.98)
                    if x and y:
                        print('leave  working')
                        pyautogui.click(x,y)
                        time.sleep(3)
                        continue

                except Exception as e:
                    pass
                try:
                    x, y = pyautogui.locateCenterOnScreen('wait_for_page.png',  confidence=0.98)
                    if x and y:
                        print('wait_for_page working')
                        pyautogui.click(x,y)
                        time.sleep(3)
                        close_window(window3)
                        continue

                except Exception as e:
                    pass
                if layout == 1:
                    if layout == 1:
                        try:
                            
                            if win32gui.IsWindow(window1):
                                #focus_and_maximize_window('Task Manager')
                                switch = switch_to_window(window1)

                                if switch:

                                    ggwin1 = None
                                    ggwin1 = gplink_handle()
                                    if ggwin1 == 5:
                                        tpi = True
                                    elif ggwin1 == 1:
                                        tpi = False

                                    time.sleep(1)
        

                                try:
                                    x, y = pyautogui.locateCenterOnScreen('thissiteerror.png', region=[526,160,530,470], confidence=0.95)
                                    if x and y:
                                        print('site not working')
                                        pyautogui.click(24,64)
                                        time.sleep(3)
                                        tpi = True
                                except Exception as e:
                                    pass
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('cssnotload2.png', region=[1,66,230,190], confidence=0.8)
                                    if x and y:
                                        pyautogui.press('f5')
                                        time.sleep(3)
                                except Exception as e:
                                    pass

                                try:
                                    x, y = pyautogui.locateCenterOnScreen('resubmission.png', region=[585,210,585,290], confidence=0.8)
                                    if x and y:
                                        pyautogui.click(1027,235)
                                        time.sleep(3)
                                        #pyautogui.moveTo(500,300)
                                        #pyautogui.scroll(5000)
                                        #tpi = True
                                except Exception as e:
                                    pass

                            else:
                                print('tpi not exist')
                                if tpi:
                                    pass
                                else:
                                    sites_done += 1
                                tpi = True

                        except Exception as e:
                        #tpi = True
                            pass
                    
                #if tpi == True:
                #    close_window(window3)

                if layout == 1:
                    
                        try:
                            switch_to_window(window2)
                            if win32gui.IsWindow(window2):

                                switch = switch_to_window(window2)
                                pyautogui.click(150,200, duration = 0.4)

                                ggwin2 = None
                                ggwin2 = shortx_handle()
                                if ggwin2 == 5:
                                    cuty = True
                                elif ggwin2 == 1:
                                    cuty = False

                                                    

                                try:
                                    x, y = pyautogui.locateCenterOnScreen('resubmission.png', region=[585,210,585,290], confidence=0.8)
                                    if x and y:
                                        pyautogui.click(1027,235)
                                        time.sleep(3)
                                        #pyautogui.moveTo(500,300)
                                        #pyautogui.scroll(5000)
                                        #tpi = True
                                except Exception as e:
                                    pass
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('thissiteerror.png', region=[526,160,530,470], confidence=0.95)
                                    if x and y:
                                        print('site not working shortix')
                                        cuty = True
                                except Exception as e:
                                    pass
                            else:
                                print('cuty not exist')                               
                                
                                
                                if cuty:
                                    pass
                                else:
                                    sites_done += 1
                                cuty = True

                        except Exception as e:
                            #cuty = True
                            pass


                if layout == 1:

                        if check_indx % 10 == 0:
                            results = True
                        else:
                            results = False

                        # Print the results

                        try:
                            switch_to_window(window3)
                            if win32gui.IsWindow(window3):

                                switch = switch_to_window(window3)
                                pyautogui.click(150,200, duration = 0.4)

                                ggwin2 = None
                                ggwin2 = inidanxlinks(results)
                                if ggwin2 == 5:
                                    pass
                                    #tpi = True
                                elif ggwin2 == 1:
                                    pass
                                    #tpi = False

                                                    

                                try:
                                    x, y = pyautogui.locateCenterOnScreen('resubmission.png', region=[585,210,585,290], confidence=0.8)
                                    if x and y:
                                        pyautogui.click(1027,235)
                                        time.sleep(3)
                                        #pyautogui.moveTo(500,300)
                                        #pyautogui.scroll(5000)
                                        #tpi = True
                                except Exception as e:
                                    pass
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('thissiteerror.png', region=[526,160,530,470], confidence=0.95)
                                    if x and y:
                                        print('site not working shortix')
                                        tpi = True
                                except Exception as e:
                                    pass
                            else:
                                print('cuty not exist')                               
                                
                                
                                if tpi:
                                    pass
                                else:
                                    sites_done += 1
                                tpi = True
                        except Exception as e:
                            #cuty = True
                            pass





                if layout == 5:
                    if random.random() < 0.5: ##if cuty == None or cuty == False:
                        try:
                            switch_to_window(window3)
                            if win32gui.IsWindow(window3):

                                switch = switch_to_window(window3)
                                pyautogui.click(150,200, duration = 0.4)

                                ggwin2 = None
                                ggwin2 = hyperhustlebrows()

                                if hyperrefreshstat1 == False:
                                    if script_seconds_only > hyperrefreshtime1:
                                        hyperrefreshstat1 = True
                                        if random.random() < 0.93:   # 0.9 = 90%
                                            shorlink = random_link('link3')
                                        else:
                                            shorlink = "https://hyperhustle.online/"
                                        switch_to_window(window3)
                                        pyautogui.click(493,19, duration = 0.4)
                                        shorlink = random_link('link3')
                                        open_link(link = shorlink ,newtab = False)
                                        time.sleep(2)
                                        #pyautogui.click(1056,192, duration=0.6)



                                if hyperrefreshstat2 == False:
                                    if script_seconds_only > hyperrefreshtime2:
                                        hyperrefreshstat2 = True
                                        if random.random() < 0.93:   # 0.9 = 90%
                                            shorlink = random_link('link3')
                                        else:
                                            shorlink = "https://hyperhustle.online/"
                                        switch_to_window(window3)
                                        pyautogui.click(493,19, duration = 0.4)
                                        shorlink = random_link('link3')
                                        open_link(link = shorlink ,newtab = False)
                                        time.sleep(2)
                                        #pyautogui.click(1056,192, duration=0.6)

                                if hyperrefreshstat3 == False:
                                    if script_seconds_only > hyperrefreshtime3:
                                        hyperrefreshstat3 = True
                                        if random.random() < 0.93:   # 0.9 = 90%
                                            shorlink = random_link('link3')
                                        else:
                                            shorlink = "https://hyperhustle.online/"
                                        switch_to_window(window3)
                                        pyautogui.click(493,19, duration = 0.4)
                                        shorlink = random_link('link3')
                                        open_link(link = shorlink ,newtab = False)
                                        time.sleep(2)

                                        #pyautogui.click(1056,192, duration=0.6)




                                if hyperrefreshstat4 == False:
                                    if script_seconds_only > hyperrefreshtime4:
                                        hyperrefreshstat4 = True
                                        if random.random() < 0.93:   # 0.9 = 90%
                                            shorlink = random_link('link3')
                                        else:
                                            shorlink = "https://hyperhustle.online/"
                                        switch_to_window(window3)
                                        pyautogui.click(493,19, duration = 0.4)
                                        shorlink = random_link('link3')
                                        open_link(link = shorlink ,newtab = False)
                                        time.sleep(2)
                                        pyautogui.click(1056,192, duration=0.6)

                                    
                                try:
                                    x, y = pyautogui.locateCenterOnScreen('thissiteerror.png', region=[526,160,530,470], confidence=0.95)
                                    if x and y:
                                        print('site not working shortix')
                                        cuty = True
                                except Exception as e:
                                    pass
                            else:
                                print('cuty not exist')                               
                                


                        except Exception as e:
                            #cuty = True
                            pass






                if cuty and tpi and layout == 6:# and oii and fc_lc: #and cuty: #or oii:

                        print(cuty, tpi, 'Cuty and tpi is true')
                        focus_and_maximize_window('SunBrowser')
                        focus_and_maximize_window('New Tab')
                        open_link(link = 'chrome-extension://ehllkhjndgnlokhomdlhgbineffifcbj/data/options/index.html',newtab = False)
                        time.sleep(3)
                        pyautogui.click(850, 559)  # C
                        time.sleep(0.5)
                        pyautogui.hotkey('ctrl', 'a')  # Select all text
                        pyautogui.press('backspace')  # Clear the text
                        pyautogui.typewrite('mobiend.com, healthy4pepole.com, adurl.io')
                        time.sleep(0.5)
                        pyautogui.click(547, 916)  # C
                        time.sleep(1)
                        pyautogui.click(547, 874)  # C
                        time.sleep(1)
                        pyautogui.click(493,19, duration = 0.4)
                        extra_win = get_focused_window_id()
                        time.sleep(2)
                        window3 = open_detatch_tab()
                        window4 = open_detatch_tab()

                        
                        time.sleep(2)
                        switch_to_window(window3)
                        pyautogui.click(493,19, duration = 0.4)
                        shorlink = random_link('link5')
                        open_link(link = shorlink ,newtab = False)
                        time.sleep(2)
                        switch_to_window(window4)
                        pyautogui.click(493,19, duration = 0.4)
                        shorlink = random_link('link8')
                        open_link(link = shorlink ,newtab = False)
                        time.sleep(2)

                        time.sleep(10)
                        layout = 2

                        close_window(window1)
                        #close_window(cutty_window)
                        close_window(window2)
                        layout2_start = time.time()

                if oii and cuty and tpi and fc_lc:
                    gg = True
                    #time.sleep(90000)
                if cuty and tpi:
                    gg = True
                
                #switch_to_window(window3)
                #mysite_handle()

            except Exception as e:
                print("An error occurred:", e)
