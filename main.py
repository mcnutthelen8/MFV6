

print("Version 15.9 loaded.")
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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import json


Indianxorshrink = False
hybridmode_indianxshrink = False
#Tru = Shrink
#False = Indianxor

Mysterium_Mode = False

#time.sleep(99990)
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
    url = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/refs/heads/main/cookie/content.js"
    
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


def get_focused_window_title():
    hwnd = win32gui.GetForegroundWindow()
#    print(f"Focused window handle: {win32gui.GetWindowText(hwnd)}")
    return win32gui.GetWindowText(hwnd)
#get_focused_window_title()

    #text = get_ocr_from_screen_area(65, 6, 185, 35)
    #print("Detected Text:", text)
    #return text


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


def focus_and_maximize_window(partial_title):
    try:
        windows = Desktop(backend="uia").windows()
        for win in windows:
            title = win.window_text()
            if partial_title.lower() in title.lower():
                win.set_focus()
                #win.maximize()
                print(f"Activated and maximized: {title}")
                return True
        print(f"No matching window found for: {partial_title}")
    except Exception as e:
        print(f"Error: {e}")


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



def switch_adspower():
    #tuxler OFF
    

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

def reloginadspower():
    relogged = False
    focus_and_close_window('SunBrowser')
    focus_and_close_window('SunBrowser')
    focus_and_close_window('SunBrowser')
    focus_and_close_window('SunBrowser')
    tuxler_switch = True
    global ipqs_key
    global location_changes

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
        

    switch_adspower()
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
                x, y = pyautogui.locateCenterOnScreen('adspowerads2.png', region=[209,12,1470,840], confidence=0.95)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(3)
                    
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
                    
            except Exception as e:
                pass



            try:
                x, y = pyautogui.locateCenterOnScreen('api_btn_adspower.png',confidence=0.95)
                if x and y:
                    print("api_btn_adspower Found")
                    break
                    #switch_adspower()
                    
            except Exception as e:
                pass
            try:
                x, y = pyautogui.locateCenterOnScreen('adspower_rpa.png',confidence=0.95)
                if x and y:
                    print("adspower_rpa Found")
                    break
                    #switch_adspower()
                    
            except Exception as e:
                pass


        except Exception as e:
            print(f"Error focusing window: {e}")
            
    adspower_api_grabber()
    tuxler_switch = True
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
                tuxler_switch = False
                pyautogui.click(x, y)
                time.sleep(2)
                
        except Exception as e:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('tuxler_off.png', confidence=0.9)
            if x and y:
                pyautogui.click(x, y)
                time.sleep(2)
        except Exception as e:
            print('tuxler off not found')
            print('tuxler off not found')
            pyautogui.hotkey('alt','tab')
            time.sleep(1)
            pyautogui.press('esc')
            time.sleep(1)
        




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


def adspower_api_grabber():
    global API_KEY
    try:
        for i in range(50):
            time.sleep(2)
            focus_and_maximize_window('AdsPower')

            try:
                x, y = pyautogui.locateCenterOnScreen('login_adspowr.png', confidence=0.9)
                if x and y:
                    print("adpower browser Limited")
                    switch_adspower()
                    
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
                x, y = pyautogui.locateCenterOnScreen('adspowerads2.png', region=[209,12,1470,840], confidence=0.95)
                if x and y:
                    pyautogui.click(x, y)
                    pyautogui.moveTo(100, 100)  # Move mouse to a safe position
                    time.sleep(3)
                    
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
                x, y = pyautogui.locateCenterOnScreen('okk_adspowre.png', region=[950,154,430,230],confidence=0.9)
                if x and y:
                    print("OKKK")
                    pyautogui.click(x,y)
                    time.sleep(3)
            except Exception as e:
                pass
            

            try:
                x, y = pyautogui.locateCenterOnScreen('api_btn_adspower.png',confidence=0.9)
                if x and y:
                    print("api_btn_adspower Found")
                    pyautogui.click(x,y)
                    time.sleep(3)
                    #switch_adspower()
                    
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('api_switch.png',confidence=0.9)
                if x and y:
                    print("api_switch Found")
                    pyautogui.click(x,y)
                    time.sleep(3)
                    #switch_adspower()
                    
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('copyreset_adspower.png',confidence=0.9)
                if x and y:
                    print("copyreset_adspower Found")
                    try:
                        x2, y2 = pyautogui.locateCenterOnScreen('api_off_switch.png',confidence=0.9)
                        if x2 and y2:
                            print("api_off_switch Found")
                            clipboard.copy('1234')
                            x -= 38
                            pyautogui.click(x,y)
                            time.sleep(3)
                            clip = clipboard.paste()
                            print("clip is :",clip)
                            if '1234' == clip:
                                print('Clip is same....')
                                continue
                            else:
                                print('API Found')
                                API_KEY = clip
                                return clip

                            #switch_adspower()
                            
                    except Exception as e:
                        print('api_off_switch not found', e)

                    
            except Exception as e:
                pass

            try:
                x, y = pyautogui.locateCenterOnScreen('generate_adspowr.png',confidence=0.9)
                if x and y:
                    print("api_btn_adspower Found")
                    pyautogui.click(x,y)
                    time.sleep(3)
                    #switch_adspower()
                    
            except Exception as e:
                pass





    except Exception as e:
        print('ERR adspower_api_grabber:',e)
    return '1234'






def get_browser_region():
    """
    Returns the browser content area region for pyautogui image search.
    Excludes the browser chrome (nav bar) from the top.
    region = (left, top, width, height)
    """
    # browser_rect and nav_bar_height are your globals set at startup
    left   = browser_rect['x']
    top    = browser_rect['y'] + nav_bar_height
    width  = browser_rect['width']
    height = browser_rect['height'] - nav_bar_height

    print(f"🖥️ Browser region: left={left} top={top} width={width} height={height}")
    return (left, top, width, height)




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
    regiong = get_browser_region()
    for i in range(5):
        print(f"Attempt {i+1} to close ads...")
        
        # 2. THE SECRET SAUCE: Take ONE screenshot for the whole loop
        # This prevents taking 30 separate screenshots
        full_screen = pyautogui.screenshot()

        for img_name, reg, conf in ad_resources:
            try:
                # 3. Search WITHIN the screenshot we already took
                # Use grayscale=True for 30% more speed
                match = pyautogui.locate(img_name, full_screen, region=regiong, confidence=conf)
                
                if match:
                    print(f"Found {img_name} on attempt {i+1}")
                    x, y = pyautogui.center(match)
                    pyautogui.click(x, y, duration=0.2)
                    return True

            except Exception:
                continue
                
        return False



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

prev_country = None
random_contry = None
def tuxler_changer(given_country="WorldWide"):
    global prev_country
    global random_contry
    global location_changes
    if Mysterium_Mode:
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

            print(f"Selected country: {gg_select_country}")
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




# Your specific credentials
TOKEN = "8554666788:AAENrnKhyNeUDL93Q6oQPWiYpi0-5lRRWys"
USER_ID = "7670314322"


##############################################################
# Function to handle the Shortlinks statistics
#######################################################
       

import json

EMPTY_TIMEZONES = {
    "timezone": None,
    "longitude": None,
    "latitude": None,
    "country": None
}

def _make_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--log-level=3")
    options.page_load_strategy = 'eager'
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(options=options)


def _dismiss_popup(driver):
    try:
        overlay = driver.find_element(
            By.CSS_SELECTOR,
            "div.dialog-widget.dialog-lightbox-widget, "
            "div[id^='elementor-popup-modal']"
        )
        if overlay.is_displayed():
            try:
                close_btn = overlay.find_element(
                    By.CSS_SELECTOR,
                    "button.dialog-close-button, .elementor-popup-close, [aria-label='Close']"
                )
                close_btn.click()
                time.sleep(0.5)
                return
            except Exception:
                pass
            from selenium.webdriver.common.keys import Keys
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            time.sleep(0.5)
    except Exception:
        pass


def _js_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", element)

def _find_metric(result_items, pattern):
    """Find a value in 24metrics result items by key pattern."""
    for item in result_items:
        try:
            key_el = item.find_element(By.CLASS_NAME, "ip-scanner-result-key")
            if re.search(pattern, key_el.text, re.IGNORECASE):
                return item.find_element(
                    By.CLASS_NAME, "ip-scanner-result-value"
                ).text.strip()
        except Exception:
            continue
    return None


def _hdr(driver, elem_id):
    """Get header element text by ID."""
    try:
        return driver.find_element(By.ID, elem_id).text.strip()
    except Exception:
        return ""


def _scrape_verdict(driver):
    """Scrape 24metrics results. Returns (verdict_str, timezones_dict)."""
    result_items = driver.find_elements(
        By.CSS_SELECTOR, "#ipScannerResults .ip-scanner-result-item"
    )

    Residential_proxy = _find_metric(result_items, r"Residential Proxy\?")
    Risk_Score        = _find_metric(result_items, r"Risk Score")
    Recent_Abuse      = _find_metric(result_items, r"Recent Abuse\?")
    is_vpn            = _hdr(driver, "header-vpn-val")   or _find_metric(result_items, r"\bVPN\b")
    is_proxy          = _hdr(driver, "header-proxy-val") or _find_metric(result_items, r"\bProxy\b")
    networkip         = _find_metric(result_items, r"Network")

    list_timezones = {
        "timezone":  _find_metric(result_items, r"Timezone"),
        "longitude": _find_metric(result_items, r"Longitude"),
        "latitude":  _find_metric(result_items, r"Latitude"),
        "country":   _find_metric(result_items, r"Country"),
    }

    print(f"[24metrics] vpn={is_vpn!r} proxy={is_proxy!r} "
          f"network={networkip!r} risk={Risk_Score!r}")

    if not networkip or not is_vpn:
        return "noip", list_timezones
    if networkip == "2003" or is_vpn in ("- - -", ""):
        return "noip", list_timezones

    if (Residential_proxy == "No"
            and Risk_Score   == "No Risk"
            and Recent_Abuse == "No"
            and is_vpn       == "False"
            and is_proxy     == "False"):
        print("[24metrics] ✅ Clean IP")
        return "goodip", list_timezones

    if (Residential_proxy == "Yes"
            or Risk_Score in ("High Risk", "Risk", "Medium Risk")
            or Recent_Abuse == "Yes"
            or is_vpn       == "True"
            or is_proxy     == "True"):
        print("[24metrics] ❌ Risky IP")
        return "badip", list_timezones

    return "noip", list_timezones


def _check_24metrics_with_driver(driver, wait, ip, max_attempts=9, retry_delay=5):
    print(f"[24metrics] Starting scan for {ip} ...")
    ssl_fail_count = 0
    list_timezones = EMPTY_TIMEZONES.copy()

    for attempt in range(1, max_attempts + 1):
        print(f"[24metrics] Attempt {attempt}/{max_attempts} ...")
        verdict = "noip"

        try:
            driver.get("https://www.24metrics.com/#anchor-ip-scanner")
            ip_input = wait.until(
                EC.presence_of_element_located((By.ID, "ipScannerInputDesktop"))
            )
            _dismiss_popup(driver)
            driver.execute_script("""
                arguments[0].scrollIntoView(true);
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', {bubbles:true}));
            """, ip_input, ip)
            btn = driver.find_element(By.ID, "ipScannerButtonDesktop")
            _js_click(driver, btn)
            ssl_fail_count = 0

            poll_deadline = time.time() + 60
            while time.time() < poll_deadline:
                time.sleep(3)
                verdict, list_timezones = _scrape_verdict(driver)
                if verdict in ("goodip", "badip"):
                    break
                print("[24metrics] ⏳ Waiting...")

        except Exception as e:
            err = str(e)
            print(f"[24metrics] ⚠️ Attempt {attempt}: {err[:80]}")
            if "ERR_SSL_PROTOCOL_ERROR" in err:
                ssl_fail_count += 1
                if ssl_fail_count >= 2:
                    print("[24metrics] SSL blocked, skipping.")
                    return "noip", EMPTY_TIMEZONES.copy()
            verdict = "noip"

        if verdict in ("goodip", "badip"):
            return verdict, list_timezones

        if attempt < max_attempts:
            print(f"[24metrics] 🔄 Retry in {retry_delay}s ...")
            time.sleep(retry_delay)

    print("[24metrics] ❌ Failed all attempts.")
    return "noip", EMPTY_TIMEZONES.copy()




def checkip_selenium(sameip='123'):
    driver = _make_driver()
    wait   = WebDriverWait(driver, 30)
    list_timezones = EMPTY_TIMEZONES.copy()

    try:
        # STEP 1 — Get public IP
        print("=" * 55)
        print("STEP 1 – Getting public IP ...")
        driver.get("https://api.ipify.org/")
        ip = driver.find_element(By.TAG_NAME, "body").text.strip()
        print(f"  Public IP: {ip}")

        # Same IP shortcut — skip all checks
        if sameip == ip:
            print("  Same IP detected, skipping checks.")
            return ip, True, True, list_timezones

        # STEP 2 — ProxyCheck via plain requests (no browser needed)
        print("\nSTEP 2 – ProxyCheck.io ...")
        pc_good = False
        try:
            resp = requests.get(
                f"https://proxycheck.io/v3/{ip}",
                timeout=15
            )
            data = resp.json()
            if data.get("status") == "ok":
                ip_data    = data.get(ip, {})
                detections = ip_data.get("detections", {})
                network    = ip_data.get("network", {})
                is_hosting = detections.get("hosting", True)
                is_vpn_pc  = detections.get("vpn",     True)
                is_proxy_pc= detections.get("proxy",   True)
                print(f"[ProxyCheck] provider={network.get('provider')} "
                      f"hosting={is_hosting} vpn={is_vpn_pc} proxy={is_proxy_pc}")
                pc_good = not is_hosting and not is_vpn_pc and not is_proxy_pc
            else:
                print(f"[ProxyCheck] ERROR: {data.get('status')}")
        except Exception as e:
            print(f"[ProxyCheck] Request failed: {e}")

        print(f"[ProxyCheck] {'✅ PASS' if pc_good else '❌ FAIL'}")

        # STEP 3 — 24metrics (only if ProxyCheck passed)
        tm_good = False
        verdict = "skipped"
        if pc_good:
            print("\nSTEP 3 – 24metrics.com ...")
            verdict, list_timezones = _check_24metrics_with_driver(driver, wait, ip)
            tm_good = (verdict == "goodip")
        else:
            print("\nSTEP 3 – Skipped (ProxyCheck failed)")

        # Final verdict
        print("=" * 55)
        print(f"  IP         : {ip}")
        print(f"  ProxyCheck : {'✅' if pc_good else '❌'}")
        print(f"  24metrics  : {'✅' if tm_good else '❌'}")
        print(f"  Result     : {'GOOD ✅' if pc_good and tm_good else 'BAD ❌'}")

        return ip, pc_good, tm_good, list_timezones

    except Exception as e:
        print(f"ERR checkip_selenium: {e}")
        return None, False, False, EMPTY_TIMEZONES.copy()

    finally:
        driver.quit()



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




def get_gplink_bug_status():
    doc = maindb_collection.find_one({"type": "main"})
    if doc and "gplink_bug" in doc:
        satt = doc["gplink_bug"]
        print("gplink_bug status from DB:", satt)
        if satt == "true":
            return True
    return False  # Default value if not found



###################AdsPower-Chrome################################

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys


API_KEY = "84497762bcd3f3cfb5203c044df6d2a000620e0171e1e1b3"
#API_KEY = "de27de41a1baf17d8ffebac045f4e2660064bb6652d4f79a"

BASE_URL = "http://local.adspower.net:50325"



# resolutions per OS
RESOLUTIONS = {
    "windows": [        
        "1920_1080",
        "1920_1080",  # most common ~30%
        "1366_768",   # budget laptops ~20%
        "1536_864",   # common Windows scaling default
        "1440_900",   # mid laptops
        "1600_900",
        "1600_900",   # widescreen laptops
        "1280_720",   # budget
        "1280_1024",  # older office monitors
        ],
    "mac":     ["1920_1080", "1440_900", "2560_1600", "1680_1050", "1280_800"],
    "linux":   ["1920_1080", "1366_768", "1280_1024", "1440_900"],
    "android": ["360_800",   "390_844",  "412_915",   "414_896"],
    "iphone":  ["390_844",   "375_812",  "414_896",   "428_926"],
}

# ─────────────────────────────────────────────────────────
#  BASE REQUESTS
# ─────────────────────────────────────────────────────────

def get(endpoint, **params):
    resp = requests.get(
        f"{BASE_URL}{endpoint}",
        params={"serial_number": API_KEY, **params}
    )
    data = resp.json()
    print(f"[GET {endpoint}] {json.dumps(data, indent=2)}")
    return data

def post(endpoint, payload):
    resp = requests.post(
        f"{BASE_URL}{endpoint}",
        params={"serial_number": API_KEY},
        json=payload
    )
    data = resp.json()
    print(f"[POST {endpoint}] {json.dumps(data, indent=2)}")
    return data

# ─────────────────────────────────────────────────────────
#  PROFILES
# ─────────────────────────────────────────────────────────
def get_all_profiles():
    resp = requests.post(
        f"{BASE_URL}/api/v2/browser-profile/list",
        params={"serial_number": API_KEY},
        json={"page": 1, "limit": 100}
    ).json()
    print("Profiles V2:", json.dumps(resp, indent=2))
    return resp.get("data", {}).get("list", [])


def delete_all_profiles():
    profiles = get_all_profiles()
    if not profiles:
        print("✅ No profiles to delete")
        return True

    profile_ids = [p["profile_id"] for p in profiles]
    print(f"\n🗑️  Deleting {len(profile_ids)} profiles: {profile_ids}")

    # try lowercase profile_id
    resp = requests.post(
        f"{BASE_URL}/api/v2/browser-profile/delete",
        params={"serial_number": API_KEY},
        json={"profile_id": profile_ids}   # lowercase
    ).json()
    print(json.dumps(resp, indent=2))

    if resp.get("code") == 0:
        print(f"✅ Deleted {len(profile_ids)} profiles")
        return True

    # fallback — try V1 delete with profile_ids as user_ids
    print("V2 failed, trying V1 fallback...")
    resp = requests.post(
        f"{BASE_URL}/api/v1/user/delete",
        params={"serial_number": API_KEY},
        json={
            "user_ids":     profile_ids,
            "delete_cache": "true"
        }
    ).json()
    print(json.dumps(resp, indent=2))

    if resp.get("code") == 0:
        print(f"✅ Deleted via V1 fallback")
        return True

    print(f"❌ Delete failed: {resp.get('msg')}")
    return False
# Most common fonts real users have per OS



OS_RANDOM_UA = {
    "windows": {
        "ua_browser":        ["chrome", "firefox"],
        "ua_system_version": ["Windows 10","Windows 11"],
    },
    "mac": {
        "ua_browser":        ["chrome", "firefox"],
        "ua_system_version": ["Mac OS X 10", "Mac OS X 11", "Mac OS X 12", "Mac OS X 13"],
    },
    "linux": {
        "ua_browser":        ["chrome", "firefox"],
        "ua_system_version": ["Linux"],
    },
    "android": {
        "ua_browser":        ["chrome"],
        "ua_system_version": ["Android 15", "Android 14", "Android 13"],
    },
    "iphone": {
        "ua_browser":        ["chrome"],
        "ua_system_version": ["iOS 15", "iOS 16", "iOS 17"],  # wait actually iOS uses safari
    },
}



def create_profile(timezone_list=None, name=None, os_type="windows", os_version="Windows 10", chrome_ver='latest', resolution=None):
    profile_name = name or f"profile_{random.randint(10000, 99999)}"
    res = resolution or random.choice(RESOLUTIONS[os_type])
    
    # AdsPower API expects strings for these numerical values
    cpu = str(random.choice([4, 6, 8, 10]))
    ram = str(random.choice([8, 16, 32, 64])) # 64 is rare, 8-32 is more organic
    if ram < cpu:
        for i in range(5):
            cpu = str(random.choice([4, 6, 8]))
            ram = str(random.choice([8, 16, 32, 64])) # 64 is rare, 8-32 is more organic
            if ram > cpu:
                break
    
    ua_config = OS_RANDOM_UA[os_type]

    # Pulling data from your provided timezone_list
    timezone = timezone_list.get("timezone")
    lat = timezone_list.get("latitude")
    lon = timezone_list.get("longitude")

    # Spoofing the location slightly so not every bot is at the exact same GPS coordinate
    spoofed_lat = str(round(float(lat) + random.uniform(-0.005, 0.005), 6))
    spoofed_lon = str(round(float(lon) + random.uniform(-0.005, 0.005), 6))

    payload = {
        "name": profile_name,
        "group_id": "0",
        "user_proxy_config": {
            "proxy_soft": "other",
            "proxy_type": "socks5",
            "proxy_host": "127.0.0.1",
            "proxy_port": "23321"
        },
        "fingerprint_config": {
            "automatic_timezone": "1",
            "language_switch": "1",
            "location_switch": "1", # Set to 0 to use our custom spoofed lat/lon
            "location": "ask",
            "page_language_switch": "1",
            #"longitude": spoofed_lon,
            #"latitude": spoofed_lat,
            #"accuracy": str(random.randint(10, 1000)),
            
            "webrtc": "proxy", 
            "canvas": "1",
            "media_devices": "1",
            "webgl_image": "1",
            "webgl": "3",
            "webgl_config": {
                "unmasked_vendor": "",
                "unmasked_renderer": "",
                "webgpu": {"webgpu_switch": "1"}
            },
            "audio": "1",
            "client_rects": "1",
            "speech_switch": "1",
            "device_name_switch": "1",
            "mac_address_config": {"model": "1", "address": ""},
            
            "hardware_concurrency": cpu, # Fixed: Must be string
            "device_memory": ram,        # Fixed: Must be string
            "gpu": "1",
            "scan_port_type": "1",
            
            "browser_kernel_config": {
                "version": chrome_ver,
                "type": "chrome"
            },
            "screen_resolution": res,
            "do_not_track": "default",
            "flash": "block",
            
            "random_ua": {
                "ua_browser": ["chrome"],
                "ua_system_version":[os_version] #ua_config['ua_system_version']
            }
        }
    }

    # IMPORTANT: Use headers for API key and catch the response correctly
    headers = {"api-key": API_KEY}
    response = requests.post(
        f"{BASE_URL}/api/v2/browser-profile/create",
        json=payload,
        headers=headers
    )
    
    # Fixed: data = response.json(), not resp.get()
    data = response.json()
    
    if data.get("code") == 0:
        profile_id = data["data"]["profile_id"]
        print(f"✅ Profile created | ID: {profile_id}")
        return profile_id
    else:
        print(f"❌ Create failed: {data.get('msg')}")
        if 'daily limit' in data.get('msg'):
            return 'daily limit'


DEVICE_ADSPOWER ="notest" #"windows"
# ─────────────────────────────────────────────────────────
#  BROWSER
# ─────────────────────────────────────────────────────────

def start_browser(profile_id):
    headers = {
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }

    # Simplified payload to ensure compatibility
    payload = {
        "user_id": profile_id, # V2 often expects user_id inside the body
        "headless": "0",
        "last_opened_tabs": "0",
        "proxy_detection": "0", # Setting to 0 is safer to avoid extra tabs
        "cdp_mask": "1",
        "user_proxy_config": {
            "proxy_soft": "other",
            "proxy_type": "socks5",
            "proxy_host": "127.0.0.1",
            "proxy_port": "23321"
        }
    }

    try:
        # ⚠️ FIX: Try v1 endpoint first if v2 fails, as it's more stable for starting
        # Some AdsPower setups use /api/v1/browser/start even with V2 keys
        url = f"{BASE_URL}/api/v1/browser/start"
        
        # Use params for v1/start, but headers for the key
        resp = requests.get(url, params={"user_id": profile_id}, headers=headers)
        
        if resp.status_code != 200:
            print(f"❌ Server returned status {resp.status_code}: {resp.text}")
            return None, None

        data = resp.json()
        
        if data.get("code") == 0:
            # Handle different return structures between versions
            debug_data = data.get("data", {})
            port = debug_data.get("debug_port") or debug_data.get("ws", {}).get("selenium", "").split(":")[-1]
            chromedriver = debug_data.get("webdriver")
            
            print(f"✅ Profile {profile_id} is LIVE (Port: {port})")
            return port, chromedriver
        else:
            print(f"❌ Launch failed: {data.get('msg')}")
            if 'Exceeding open daily limit' in data.get('msg'):
                print('Limit Hit on Adspower..')
                return '555512', 'daily limit'
            
            return None, None

    except Exception as e:
        print(f"❌ API Error: {e}")
        # If it's a JSON error, print the raw response to see what's wrong
        if 'resp' in locals():
            print(f"Raw Response: {resp.text}")
        return None, None

def stop_browser(user_id):
    data = get("/api/v1/browser/stop", user_id=user_id)
    if data.get("code") == 0:
        print(f"✅ Browser stopped")
    return data


def connect_selenium(port, chromedriver):
    service = Service(executable_path=chromedriver)
    options = Options()
    options.page_load_strategy = 'none'
    options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
    driver = webdriver.Chrome(service=service, options=options)
    print(f"✅ Selenium connected")
    return driver


################################################################################################
port_selenium = ''
chromedriver_selenium =''
def wait_for_load_state2(driver, state="interactive", timeout=10, wait= False):
    try:
        """
        state can be:
        - "interactive": Half load (DOM ready, good for JS injection)
        - "complete": Full load (Everything done)
        """
        if wait:
            start_time = time.time()

            while time.time() - start_time < timeout:
                # Check the readyState via JavaScript
                current_state = driver.execute_script("return document.readyState")
                
                if state == "interactive":
                    if current_state in ["interactive", "complete"]:
                        return True
                elif state == "complete":
                    if current_state == "complete":
                        return True
                
                time.sleep(0.2) # Small poll interval to save CPU
        else:
            current_state = driver.execute_script("return document.readyState")
            
            if state == "interactive":
                if current_state in ["interactive", "complete"]:
                    return True
            elif state == "complete":
                if current_state == "complete":
                    return True
            else:
                return False
    except Exception as e:
        print('Error at wait_for_load state:',e)
    return False


def wait_for_load_state(driver, state="interactive", timeout=10, wait=False):
    """
    state: "interactive" (DOM ready) | "complete" (fully loaded)
    pass port + chromedriver to enable auto-reconnect on disconnect.
    """
    global port_selenium
    global chromedriver_selenium
    try:
        if wait:
            start_time = time.time()
            while time.time() - start_time < timeout:
                try:
                    driver.set_script_timeout(3)
                    current_state = driver.execute_script("return document.readyState")
                    if state == "interactive" and current_state in ("interactive", "complete"):
                        return True, driver
                    if state == "complete" and current_state == "complete":
                        return True, driver
                    time.sleep(0.5)

                except Exception as e:
                    err = str(e)
                    if "HTTPConnectionPool" in err or "timed out" in err:
                        print(f"⚠️ Selenium disconnected during wait: {err[:60]}")
                        if port_selenium and chromedriver_selenium:
                            new_driver = connect_selenium(port_selenium, chromedriver_selenium)
                            if new_driver:
                                driver = new_driver   # swap to new connection
                                continue              # retry the readyState check
                        return False, driver
                    print(f"⚠️ wait_for_load inner error: {err[:60]}")
                    return False, driver
        else:
            try:
                driver.set_script_timeout(3)
                current_state = driver.execute_script("return document.readyState")
                if state == "interactive":
                    return current_state in ("interactive", "complete"), driver
                if state == "complete":
                    return current_state == "complete", driver
                return False, driver

            except Exception as e:
                err = str(e)
                if "HTTPConnectionPool" in err or "timed out" in err:
                    print(f"⚠️ Selenium disconnected (non-wait): {err[:60]}")
                    if port_selenium and chromedriver_selenium:
                        new_driver = connect_selenium(port_selenium, chromedriver_selenium)
                        if new_driver:
                            return False, new_driver   # return fresh driver
                                                       # caller retries next tick
                return False, driver

    except Exception as e:
        print(f"Error at wait_for_load_state: {e}")
    return False, driver



traffic_links = [
    'web.telegram.org/a/get',
    'pinpaste.com',
    'pubnotepad.com',

]


def random_spoofing_reffer():
    odd = random.random()
    print('ODD:',odd)
    if odd < 0.90: # 0.9 = 90%
        site = 'web.telegram.org/a/get'
    elif odd < 0.93:
        site = 'https://corelinks.site/'
    else:
        site = 'noreffer'

    print('REffer:',site)
    return site


def spoof_referrer_and_redirect(driver, referer_site, target_site, new_page = True):
    """
    1. Opens referer_site
    2. Injects a hidden anchor tag pointing to target_site
    3. Clicks it to spoof the 'Referer' header
    """
    print(f"🔗 Spoofing Referer via: {referer_site}")
    
    try:
        # 1. Go to the high-authority 'Referer' site
        if new_page:
            driver.switch_to.new_window('tab')
        if referer_site == "random":
            print('random spoofing detect...')
            referer_site = random_spoofing_reffer()
        if referer_site == 'noreffer':    
            print('direct visit')
            driver.get(target_site)
            time.sleep(2)
            print("✅ Redirect Successful!")
            return driver.current_window_handle
        driver.get(referer_site)
        
        waitforpage, driver = wait_for_load_state(driver, state="interactive", timeout=30, wait= True)
        if waitforpage == False:
            print(f'Page Loading Failed... {referer_site}')
            return False

        # Wait for body to be ready to inject the link
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # 2. Inject the hidden dummy button/link via JavaScript
        # We use a.click() directly in JS to ensure the 'Referer' is passed
        script = f"""
            const a = document.createElement('a');
            a.href = '{target_site}';
            a.id = 'spoof_link';
            a.style.position = 'fixed';
            a.style.left = '-9999px';
            a.style.top = '-9999px';
            a.style.opacity = '0';
            a.target = '_self'; 
            document.body.appendChild(a);
            
            // Trigger the click immediately
            a.click();
        """
        
        print(f"🚀 Redirecting to: {target_site}")
        driver.execute_script(script)
        
        # 3. Wait for the URL to change to the target site
        # This ensures we don't return until the redirect has started
        #WebDriverWait(driver, 15).until(lambda d: target_site in d.current_url)
        time.sleep(2)
        
        print("✅ Redirect Successful!")
        return driver.current_window_handle

    except Exception as e:
        print(f"❌ Referer Spoof Failed: {e}")
        return False


def destined_reached(text):
    keywords = [
        '405 Not Allowed',
        '502 Bad Gateway',
        'This link is risky',
        'Database Error',
        'Privacy Error',
        'Google',
        '503 Service',
        '504: Gateway',
        '500 Internal',
        "A timeout occurred",
        "dynamicslab",
        "demo.dynamicslab.ai",






    ]
    return any(keyword.lower() in text.lower() for keyword in keywords)



def human_click(driver, element):
    # 1. Get the exact position relative to the screen WITHOUT scrolling
    # This replaces location_once_scrolled_into_view

    rect = driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        return {
            x: rect.left,
            y: rect.top,
            w: rect.width,
            h: rect.height
        };
    """, element)

    # 2. Get Browser Window Position & Header Height

    # 3. Calculate safe random offsets (30% to 70% of button)
    # This keeps us in the "meat" of the button so we don't miss small ones
    offset_x = random.uniform(rect['w'] * 0.3, rect['w'] * 0.7)
    offset_y = random.uniform(rect['h'] * 0.3, rect['h'] * 0.7)

    # 4. Final Math
    # Browser X + Button X (inside window) + Random Offset
    click_x = browser_rect['x'] + rect['x'] + offset_x
    click_y = browser_rect['y'] + nav_bar_height + rect['y'] + offset_y

    # 5. Move and Click
    pyautogui.moveTo(click_x, click_y, duration=0.1, tween=pyautogui.easeOutQuad)
    pyautogui.click()
    
    print(f"🎯 Human Click at: ({int(click_x)}, {int(click_y)}) | No Jump!")



def move_human_os(target_x, target_y):
    if DEVICE_ADSPOWER == "android":
        return
    """
    Moves the mouse from current position to (target_x, target_y)
    using a curved Bezier path.
    """
    # 1. Get current position
    start_x, start_y = pyautogui.position()
    
    # 2. Create control points for the Bezier curve
    # We pick two random points 'in between' to create a natural arc
    control1_x = start_x + (target_x - start_x) * random.uniform(0.1, 0.4)
    control1_y = start_y + (target_y - start_y) * random.uniform(0.1, 0.4) + random.randint(-100, 100)
    
    control2_x = start_x + (target_x - start_x) * random.uniform(0.6, 0.9)
    control2_y = start_y + (target_y - start_y) * random.uniform(0.6, 0.9) + random.randint(-100, 100)
    
    # 3. Generate the curve points (the 'steps' of the move)
    steps = random.randint(15, 35) # How many segments in the move
    for i in range(1, steps + 1):
        t = i / steps
        # Cubic Bezier Formula
        x = (1-t)**3 * start_x + 3*(1-t)**2 * t * control1_x + 3*(1-t) * t**2 * control2_x + t**3 * target_x
        y = (1-t)**3 * start_y + 3*(1-t)**2 * t * control1_y + 3*(1-t) * t**2 * control2_y + t**3 * target_y
        
        # Add a tiny 'jitter' to simulate human hand shaking (0.5 pixel)
        x += random.uniform(-0.5, 0.5)
        y += random.uniform(-0.5, 0.5)
        
        # Move the physical mouse
        pyautogui.moveTo(x, y)
        
        # Human speed variation (Faster in middle, slower at ends)
        # This mimics 'Fitts Law'
        sleep_time = 0.001 * (1 + (0.5 - abs(t - 0.5)) * 10)
        time.sleep(sleep_time)






#######################Shortlinks Handle##########################################

def accept_consent_popups(driver):

    # 2. JS to find the first VISIBLE consent button
    find_consent_script = """

    // replace your consent detection block with this
    const consent_selectors = [
        
        '#accept-btn',                                      // ← direct ID fallback
        'button[id="accept-btn"]',
        'button[mode="primary"]',
        '.fc-agreement-dialog .fc-primary-button',
        'button[aria-label="Consent"]',
        '#save .tp-button',
        '.sd-cmp-2V7v7 .sd-button-primary',
        '.fc-primary-button',
        '.qc-cmp2-summary-buttons button[mode="primary"]',
    ];

    // consent uses looser visibility — overlay animation can hide it temporarily
    const isVisConsent = (el) => {
        if (!el) return false;
        const s = window.getComputedStyle(el);
        const r = el.getBoundingClientRect();
        // looser check — just needs to exist in DOM with size
        // skips opacity/visibility since overlay animates in
        return s.display !== 'none' && r.width > 0 && r.height > 0;
    };

    for (const sel of consent_selectors) {
        const btn = document.querySelector(sel);
        if (btn && isVisConsent(btn)) {
            consent_btn = sel;
            return consent_btn;
            break;
        }
    }

    return null;




    """

    found_selector = driver.execute_script(find_consent_script)

    if found_selector:
        print(f"🛡️ Consent Popup Detected: {found_selector}")
        
        try:
            # 3. Get Element & calculate "No-Jump" Screen Coords
            btn_el = driver.find_element(By.CSS_SELECTOR, found_selector)
            human_click(driver, btn_el)
            return True
            
        except Exception as e:
            print(f"⚠️ Failed to click consent: {e}")
    
    return False


def close_google_ads(driver):
    found = driver.execute_script("""
        const isVignette = window.location.href.includes('#google_vignette');

        const isVis = (el) => {
            if (!el) return false;
            const s = window.getComputedStyle(el);
            const r = el.getBoundingClientRect();
            return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0;
        };

        const isAdClose = (el) => {
            const label = (el.getAttribute('aria-label') || '').toLowerCase();
            const text  = (el.innerText || '').toLowerCase().trim();
            const id    = (el.id || '').toLowerCase();
            const cls   = (el.className || '').toLowerCase();
            return (
                label.includes('close ad')   ||
                label.includes('close')      ||
                text  === 'close'            ||
                text  === 'x'               ||
                id.includes('dismiss')       ||
                cls.includes('close-button') ||
                cls.includes('dismiss-button')
            );
        };

        const selectors_gads = [
            '#dismiss-button',
            '[aria-label="Close ad"]',
            '[aria-label="Close Ad"]',
            '[id*="dismiss"]',
            '[id*="close-button"]',
            '[class*="close-button"]',
            '[class*="dismiss-button"]',
            'button[class*="close"]',
        ];

        // ── collect ALL visible matching buttons ──────────────────────
        let candidates = [];
        for (const sel of selectors_gads) {
            const els = document.querySelectorAll(sel);
            for (const el of els) {
                if (isVis(el) && isAdClose(el)) {
                    const r = el.getBoundingClientRect();
                    const z = parseInt(window.getComputedStyle(el).zIndex) || 0;

                    // ── visibility score ─────────────────────────────
                    // how much of the element is inside the viewport
                    const vpW = window.innerWidth  || document.documentElement.clientWidth;
                    const vpH = window.innerHeight || document.documentElement.clientHeight;
                    const visW = Math.max(0, Math.min(r.right,  vpW) - Math.max(r.left, 0));
                    const visH = Math.max(0, Math.min(r.bottom, vpH) - Math.max(r.top,  0));
                    const visibleArea = visW * visH;
                    const totalArea   = r.width * r.height;
                    const visRatio    = totalArea > 0 ? visibleArea / totalArea : 0;

                    candidates.push({
                        sel:       sel,
                        zIndex:    z,
                        visRatio:  visRatio,
                        area:      totalArea,
                    });
                }
            }
        }

        if (candidates.length === 0) {
            return { found: null, isVignette: isVignette };
        }

        // ── pick best candidate: highest z-index, then highest vis ratio ─
        candidates.sort((a, b) => {
            if (b.zIndex !== a.zIndex) return b.zIndex - a.zIndex;   // z-index first
            return b.visRatio - a.visRatio;                           // then visibility
        });

        const best = candidates[0];
        const bestEl = document.querySelector(best.sel);
        bestEl.setAttribute('data-gadclose', 'true');
        bestEl.scrollIntoView({ behavior: 'smooth', block: 'center' });

        console.log(`Best candidate: ${best.sel} | z:${best.zIndex} | vis:${best.visRatio.toFixed(2)}`);

        return { found: best.sel, isVignette: isVignette };
    """)   # 1 call

    is_vignette = found['isVignette']
    found_sel   = found['found']
    print('Found ',found_sel)

    if is_vignette:
        print("🔍 Google Vignette detected via #google_vignette")

    if found_sel:
        print(f"🧹 Best close btn: {found_sel}")
        try:
            btn = driver.find_element(By.CSS_SELECTOR, "[data-gadclose='true']")   # 1 call
            time.sleep(0.2)
            human_click(driver, btn)
            print("✅ Ad closed")
            return True
        except Exception as e:
            print(f"⚠️ Main doc click failed, trying iframes: {e}")

    # ── vignette fallback: dismiss-button inside google iframe ───────────
    if is_vignette:
        try:
            iframes = driver.find_elements(By.TAG_NAME, "iframe")   # 1 call
            for iframe in iframes:
                try:
                    driver.switch_to.frame(iframe)
                    btn = driver.find_element(By.CSS_SELECTOR, "#dismiss-button")
                    if btn.is_displayed():
                        print("🎯 Vignette dismiss-button in iframe")
                        time.sleep(0.2)
                        human_click(driver, btn)
                        driver.switch_to.default_content()
                        print("✅ Vignette closed")
                        return True
                    driver.switch_to.default_content()
                except:
                    driver.switch_to.default_content()
                    continue
        except Exception as e:
            print(f"⚠️ Iframe search failed: {e}")
            driver.switch_to.default_content()

    return False



def check_powergram_btns_covered(driver):

    result = driver.execute_script("""
        const btnSelectors = ["#VerifyBtn", "#NextBtn"];
        let anyCovered    = false;
        let anyVisible    = false;
        let isFullscreen  = false;
        let details       = [];

        const vpW = window.innerWidth  || document.documentElement.clientWidth;
        const vpH = window.innerHeight || document.documentElement.clientHeight;

        for (const sel of btnSelectors) {
            const el = document.querySelector(sel);
            if (!el) {
                details.push({sel: sel, status: 'not_found'});
                continue;
            }

            const r = el.getBoundingClientRect();
            const s = window.getComputedStyle(el);

            if (s.display === 'none' || r.width === 0) {
                details.push({sel: sel, status: 'hidden'});
                continue;
            }

            el.scrollIntoView({ behavior: 'instant', block: 'center' });

            const r2 = el.getBoundingClientRect();
            const cx = r2.left + r2.width  / 2;
            const cy = r2.top  + r2.height / 2;

            if (cy < 0 || cy > vpH) {
                details.push({sel: sel, status: 'offscreen', cy: Math.round(cy)});
                continue;
            }

            const topEl = document.elementFromPoint(cx, cy);
            if (!topEl) {
                details.push({sel: sel, status: 'offscreen'});
                continue;
            }

            const isOwn = topEl === el || el.contains(topEl);
            if (isOwn) {
                anyVisible = true;
                details.push({sel: sel, status: 'visible'});
                continue;
            }

            // ── coverage calculation ──────────────────────────────
            anyCovered = true;
            const ts       = window.getComputedStyle(topEl);
            const tr       = topEl.getBoundingClientRect();
            const coverPct = Math.round((tr.width * tr.height) / (vpW * vpH) * 100);
            const isFull   = coverPct >= 60;
            if (isFull) isFullscreen = true;

            details.push({
                sel:    sel,
                status: 'covered',
                isFullscreen: isFull,
                coverPct: coverPct,
                by: {
                    tag:    topEl.tagName,
                    id:     topEl.id     || '',
                    cls:    (topEl.className || '').substring(0, 60),
                    z:      parseInt(ts.zIndex) || 0,
                    pos:    ts.position,
                    width:  Math.round(tr.width),
                    height: Math.round(tr.height),
                }
            });
        }

        return {
            anyCovered:   anyCovered,
            anyVisible:   anyVisible,
            isFullscreen: isFullscreen,
            details:      details
        };
    """)   # 1 call

    anyCovered   = result['anyCovered']
    anyVisible   = result['anyVisible']
    isFullscreen = result['isFullscreen']

    # ── log details ───────────────────────────────────────────────
    for d in result['details']:
        status = d['status']
        if status == 'covered':
            b = d['by']
            kind = '🖥️ FULLSCREEN' if d['isFullscreen'] else '🔲 PARTIAL'
            print(f"🚫 {d['sel']} covered by {kind} overlay ({d['coverPct']}% of viewport)")
            print(f"   by: <{b['tag']}> id='{b['id']}' size={b['width']}x{b['height']}")

    if anyCovered and not anyVisible:
        if isFullscreen:
            print('🖥️ Fullscreen ad overlay detected')
        else:
            print('🔲 Partial element covering btn')
        return True, isFullscreen
    else:
        return False, False



def find_button_multi_scale(template_path, region=None, threshold=0.7):
    """
    region: (x, y, width, height) - same format as pyautogui
    """
    # 1. Load your template image
    template = cv2.imread(template_path, 0)
    (tH, tW) = template.shape[:2]

    # 2. Take a screenshot of ONLY the region (saves CPU/Time)
    # If no region is provided, it takes the full screen
    screenshot = pyautogui.screenshot(region=region)
    screen_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

    found = None

    # 3. Multi-scale loop (checks from 120% down to 20% size)
    for scale in np.linspace(0.2, 1.2, 20)[::-1]:
        resized = cv2.resize(screen_gray, (int(screen_gray.shape[1] * scale), int(screen_gray.shape[0] * scale)))
        r = screen_gray.shape[1] / float(resized.shape[1])

        if resized.shape[0] < tH or resized.shape[1] < tW:
            continue

        result = cv2.matchTemplate(resized, template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)

    # 4. Convert local region coordinates back to screen coordinates
    if found and found[0] >= threshold:
        (maxVal, maxLoc, r) = found
        
        # Calculate center within the cropped screenshot
        local_x = int((maxLoc[0] + tW/2) * r)
        local_y = int((maxLoc[1] + tH/2) * r)
        
        # Add the region's offset to get the real screen position
        offset_x = region[0] if region else 0
        offset_y = region[1] if region else 0
        
        return (local_x + offset_x, local_y + offset_y)

    return None




emptygppgae = time.time()
gplink_page_loaded = False
gplink_page_notfound = 1
gplink_adclose_failed = 1

def gplinks_main(driver, window):
    btn1_clicked = False
    global emptygppgae
    global gplink_page_notfound
    global gplink_page_loaded
    global gplink_adclose_failed
    try:
        if random.randint(1, 10) >= 8:
            print('random Move')
            move_human_os(random.randint(100, 800), random.randint(100, 500))

        wait, driver = wait_for_load_state(driver, state="interactive", timeout=10, wait=False)
        if wait:
            print('starting GP automation')

            # ── SINGLE execute_script: gets title, url, site type, AND runs rescue ──
            result = driver.execute_script("""
                const title = document.title;
                const url   = window.location.href;

                const isPowergram  = url.includes('powergram') || url.includes('powergam.online') || url.includes('collegedekho') || url.includes('collegedekho.online');
                const isGPlinks    = url.includes('gplinks.co');
                const isCloudflare = isGPlinks && !title.includes('GPlinks');
                const isGetLink    = title.includes('GPlinks');
                let isVignette   = null;                                            
                let rescueSelector = null;
                let consent_btn    = null;
                let adblock_warn  = null;                
                let google_close_btn = null;
                let google_ad_url      = url.includes('#goog_rewarded') || url.includes('#google_vignette') || url.includes('#google_') || url.includes('#goog_') 

                if (isPowergram) {

                                           
                    const consent_selectors = [
                        '.qc-cmp2-summary-buttons button[mode="primary"]',
                        '#accept-btn',                                      // ← direct ID fallback
                        'button[id="accept-btn"]',
                        'button[mode="primary"]',
                        '.fc-agreement-dialog .fc-primary-button',
                        'button[aria-label="Consent"]',
                        '#save .tp-button',
                        '.sd-cmp-2V7v7 .sd-button-primary',
                        '.fc-primary-button',
                    ];

                    // consent uses looser visibility — overlay animation can hide it temporarily
                    const isVisConsent = (el) => {
                        if (!el) return false;
                        const s = window.getComputedStyle(el);
                        const r = el.getBoundingClientRect();
                        // looser check — just needs to exist in DOM with size
                        // skips opacity/visibility since overlay animates in
                        return s.display !== 'none' && r.width > 0 && r.height > 0;
                    };

                    for (const sel of consent_selectors) {
                        const btn = document.querySelector(sel);
                        if (btn && isVisConsent(btn)) {
                            consent_btn = sel;

                            break;
                        }
                    }


                    const selectors = ["#VerifyBtn", "#NextBtn", "#captchaForm button", "#skip-btn"];

                    const btnSelectors = ["#VerifyBtn", "#NextBtn"];
                    let anyCovered    = false;
                    let anyVisible    = false;
                    let isFullscreen  = false;
                    let details       = [];

                    const vpW = window.innerWidth  || document.documentElement.clientWidth;
                    const vpH = window.innerHeight || document.documentElement.clientHeight;

                    for (const sel of btnSelectors) {
                        const el = document.querySelector(sel);
                        if (!el) {
                            continue;
                        }

                        const r = el.getBoundingClientRect();
                        const s = window.getComputedStyle(el);

                        if (s.display === 'none' || r.width === 0) {
                            continue;
                        }

                        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                        el.scrollIntoView({ behavior: 'instant', block: 'center' });

                        const r2 = el.getBoundingClientRect();
                        const cx = r2.left + r2.width  / 2;
                        const cy = r2.top  + r2.height / 2;

                        if (cy < 0 || cy > vpH) {
                            continue;
                        }

                        const topEl = document.elementFromPoint(cx, cy);
                        if (!topEl) {
                            continue;
                        }

                        const isOwn = topEl === el || el.contains(topEl);
                        if (isOwn) {
                            anyVisible = true;
                            continue;
                        }

                        // ── coverage calculation ──────────────────────────────
                        anyCovered = true;
                        const ts       = window.getComputedStyle(topEl);
                        const tr       = topEl.getBoundingClientRect();
                        const coverPct = Math.round((tr.width * tr.height) / (vpW * vpH) * 100);
                        const isFull   = coverPct >= 98;
                        if (isFull) isFullscreen = true;


                    }


                    if (anyCovered){
                        if (isFullscreen){
                                isVignette = true;
                                
                            }
                       }
                                           
                    const btn = document.querySelector('button.button-adb-refresh');
                    if (btn) {
                        const s = window.getComputedStyle(btn);
                        const r = btn.getBoundingClientRect();
                        if (s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0) {
                            const btnText = (btn.innerText || '').toLowerCase();
                            if (btnText.includes('reload page')){
                                    adblock_warn = true;
                                    isVignette = false;
                                           
                                }
                                           
                            }
                    }
                    if (isVignette){
                        if (!google_ad_url){
                            isVignette = false;
                        }
                    }



                    if (!isVignette){
                        const styleId = 'ui-helper-styles';
                        if (!document.getElementById(styleId)) {
                            const style = document.createElement('style');
                            style.id = styleId;
                            style.innerHTML = `
                                .btn-rescue-active { z-index: 2147483647 !important; position: relative !important; outline: 3px solid #00FF00 !important; }
                                .obstacle-ghost    { pointer-events: none !important; opacity: 0 !important; visibility: hidden !important; }
                            `;
                            document.head.appendChild(style);
                        }
                        for (const selector of selectors) {
                            const btn = document.querySelector(selector);
                            if (btn) {
                                const s = window.getComputedStyle(btn);
                                const r = btn.getBoundingClientRect();
                                if (s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0) {
                                    const btnText = (btn.innerText || '').toLowerCase();
                                    if (btnText.includes('wait') || btnText.includes('...')) continue;
                                    const cx = r.left + r.width  / 2;
                                    const cy = r.top  + r.height / 2;
                                    let topEl = document.elementFromPoint(cx, cy);
                                    let lim = 0;
                                    while (topEl && topEl !== btn && !btn.contains(topEl) &&
                                        topEl !== document.documentElement && lim < 15) {
                                        topEl.classList.add('obstacle-ghost');
                                        topEl = document.elementFromPoint(cx, cy);
                                        lim++;
                                    }
                                    if (!isVignette){
                                        btn.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                        btn.classList.add('btn-rescue-active');
                                        }

                                    rescueSelector = selector;
                                    break;
                                }
                            }
                        }
                    }
                                           
                }    // ← closes if (isPowergram)

                return {
                    title:          title,
                    url:            url,
                    isPowergram:    isPowergram,
                    isCloudflare:   isCloudflare,
                    isGetLink:      isGetLink,
                    consent_btn:    consent_btn,
                    rescueSelector: rescueSelector,
                    google_close_btn: google_close_btn,
                    isVignette:     isVignette,
                };
            """)   # ← ONE call does everything

            title       = result['title']
            stealth_url = result['url']
            isVignette = result['isVignette']
            rescueSelector = result['rescueSelector']
            print(stealth_url)
            print(title)
            print('isVignette:',isVignette)

            # ── Direct resource check (pure Python, zero extra calls) ────────
            if is_direct_resource_link(stealth_url):
                print('link is detect')
                driver.close()
                return

            #accept_consent_popups(driver)   # 1 call
            if 'chrome-error://chromewebdata/' in stealth_url:
                print('chrome-error is detect')
                #driver.close()
                return "chrome-error"
            # ── Cloudflare on gplinks.co ─────────────────────────────────────
            if result['isCloudflare']:
                print('Cloudflare turnstile Detected')
                gplink_page_loaded = True
                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png",confidence=0.6)
                    pyautogui.click(x, y, duration=1)
                    time.sleep(1)
                    pyautogui.click(x, y, duration=1)
                    time.sleep(5)
                except Exception as e:
                    pass

            # ── Powergram ────────────────────────────────────────────────────
            if result['isPowergram']:
                gplink_page_loaded = True
                print('Powergram site')
                #if '#google_' in stealth_url or  '#goog_rewarded' in stealth_url or '#goog_' in stealth_url or'#google_vignette' in stealth_url:
                if isVignette:
                    if '#google_' in stealth_url or  '#goog_rewarded' in stealth_url or '#goog_' in stealth_url or'#google_vignette' in stealth_url:
                        print('GOOGLE ADS blocking — clearing first')
                        regiong = get_browser_region()
                        jk = close_ads()
                        try:
                            # 1. Get the full box instead of just the center
                            # Box = (left, top, width, height)
                            box = find_button_multi_scale("resume_shapedbtn.png", region=regiong, threshold=0.8)
                            #box = pyautogui.locateOnScreen("resume_shapedbtn.png", region=regiong,confidence=0.995)
                            pyautogui.click(box)
                            
                        except Exception as e:
                            print("No Close Ad video Found1")
                        try:
                            # 1. Get the full box instead of just the center
                            # Box = (left, top, width, height)
                            box = find_button_multi_scale("closevideogoogle.png", region=regiong,threshold=0.8)
                            #box = pyautogui.locateOnScreen("resume_shapedbtn.png", region=regiong,confidence=0.995)
                            pyautogui.click(box)
                            
                        except Exception as e:
                            print("No Close Ad video Found2")
                        try:
                            # 1. Get the full box instead of just the center
                            # Box = (left, top, width, height)
                            box = find_button_multi_scale("blackbtn_close.png", region=regiong,threshold=0.8)
                            #box = pyautogui.locateOnScreen("resume_shapedbtn.png", region=regiong,confidence=0.995)
                            pyautogui.click(box)
                            
                        except Exception as e:
                            print("No Close Ad video Found3")

                        try:
                            x, y = pyautogui.locateCenterOnScreen("gvideo_ads.png", region=regiong, confidence=0.9)
                            if x and y:
                                print('Yes Google Video Ads')
                                    


                                jk = True
                            else:
                                jk = close_ads()
                                
                        except Exception as e:
                            print('No Google Video Ads')
                        
                        time.sleep(1)
                        try:
                            # 1. Get the full box instead of just the center
                            # Box = (left, top, width, height)
                            box = pyautogui.locateOnScreen("resume_shapedbtn.png", region=regiong,confidence=0.97)
                            
                            if box:
                                target_x = (box.left + (box.width // 2)) - 120
                                target_y = box.top + box.height
                                
                                print(f"🎯 Target Acquired: X={target_x}, Y={target_y}")
                                
                                # 3. Perform the click
                                pyautogui.click(target_x, target_y, duration=0.2)
                                if jk == False:
                                    jk = True
                            else:
                                print("No Close Ad video Found")
                        except Exception as e:
                            print("No Close Ad video Found")
                        try:
                            # 1. Get the full box instead of just the center
                            # Box = (left, top, width, height)
                            box = pyautogui.locateOnScreen("skipres.png", region=regiong,confidence=0.97)
                            
                            if box:
                                target_x = (box.left + (box.width // 2)) - 38
                                target_y = box.top + box.height
                                
                                print(f"🎯 Target Acquired: X={target_x}, Y={target_y}")
                                
                                # 3. Perform the click
                                pyautogui.click(target_x, target_y, duration=0.2)
                                if jk == False:
                                    jk = True
                            else:
                                print("No Close Ad video Found")
                        except Exception as e:
                            print("No Close Ad video Found")
                            #pass
                        if jk == False:
                            try:
                                x, y = pyautogui.locateCenterOnScreen('loaded_page.png', region=[1,1,1917,95], confidence=0.98)
                                if x and y: 
                                    print('Page Fully Loaded and There no Ads found so refreshing')
                                    if gplink_adclose_failed > 5:
                                        current_url = driver.current_url
                                        if "#google_vignette" in current_url or "#google_" in current_url or "#goog_rewarded" in current_url or "#google_" in current_url:
                                            # Remove the fragment (split at # and take the first part)
                                            clean_url = current_url.split('#')[0]
                                            print(f"🔄 Vignette detected. Reloading to: {clean_url}")
                                            # 3. Reload the page without the fragment
                                            driver.get(clean_url)
                                            return
                                        else:
                                            print("✅ No vignette fragment found in URL.")

                                        gplink_adclose_failed = 1
                                    else:
                                        gplink_adclose_failed += 1


                            except Exception as e:
                                pass


                if result['consent_btn']:
                    
                    gg = accept_consent_popups(driver)
                    if gg:
                        driver.switch_to.window(window)

                                

                # Reusable rescue — now a single execute_script per attempt
                rescue_script = """
                const selectors = arguments[0];
                const styleId = 'ui-helper-styles';
                const url   = window.location.href;
                let isVignette   = false;
                const btnSelectors = ["#VerifyBtn", "#NextBtn"];
                let anyCovered    = false;
                let anyVisible    = false;
                let isFullscreen  = false;
                let details       = [];
                let google_ad_url      = url.includes('#goog_rewarded') || url.includes('#google_vignette') || url.includes('#google_') || url.includes('#goog_') 

                const vpW = window.innerWidth  || document.documentElement.clientWidth;
                const vpH = window.innerHeight || document.documentElement.clientHeight;

                for (const sel of btnSelectors) {
                    const el = document.querySelector(sel);
                    if (!el) {
                        continue;
                    }

                    const r = el.getBoundingClientRect();
                    const s = window.getComputedStyle(el);

                    if (s.display === 'none' || r.width === 0) {
                        continue;
                    }

                    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    el.scrollIntoView({ behavior: 'instant', block: 'center' });

                    const r2 = el.getBoundingClientRect();
                    const cx = r2.left + r2.width  / 2;
                    const cy = r2.top  + r2.height / 2;

                    if (cy < 0 || cy > vpH) {
                        continue;
                    }

                    const topEl = document.elementFromPoint(cx, cy);
                    if (!topEl) {
                        continue;
                    }

                    const isOwn = topEl === el || el.contains(topEl);
                    if (isOwn) {
                        anyVisible = true;
                        continue;
                    }

                    // ── coverage calculation ──────────────────────────────
                    anyCovered = true;
                    const ts       = window.getComputedStyle(topEl);
                    const tr       = topEl.getBoundingClientRect();
                    const coverPct = Math.round((tr.width * tr.height) / (vpW * vpH) * 100);
                    const isFull   = coverPct >= 98;
                    if (isFull) isFullscreen = true;


                }


                if (anyCovered){
                    if (isFullscreen){
                            isVignette = true;
                            
                        }
                    }
                if (isVignette){
                    if (!google_ad_url){
                        isVignette = false;
                    }
                }
                if (isVignette){
                    return null;
                }
                if (!document.getElementById(styleId)) {
                    const style = document.createElement('style');
                    style.id = styleId;
                    style.innerHTML = `
                        .btn-rescue-active { z-index: 2147483647 !important; position: relative !important; outline: 3px solid #00FF00 !important; }
                        .obstacle-ghost    { pointer-events: none !important; opacity: 0 !important; visibility: hidden !important; }
                    `;
                    document.head.appendChild(style);
                }
                for (const selector of selectors) {
                    const btn = document.querySelector(selector);
                    if (btn) {
                        const s = window.getComputedStyle(btn);
                        const r = btn.getBoundingClientRect();
                        if (s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0) {
                            const btnText = (btn.innerText || '').toLowerCase();
                            if (btnText.includes('wait') || btnText.includes('...')) continue;
                            const cx = r.left + r.width  / 2;
                            const cy = r.top  + r.height / 2;
                            let topEl = document.elementFromPoint(cx, cy), lim = 0;
                            while (topEl && topEl !== btn && !btn.contains(topEl) &&
                                   topEl !== document.documentElement && lim < 15) {
                                topEl.classList.add('obstacle-ghost');
                                topEl = document.elementFromPoint(cx, cy);
                                lim++;
                            }
                            btn.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            btn.classList.add('btn-rescue-active');
                            return selector;
                        }
                    }
                }
                return null;
                """

                selectors = ["#VerifyBtn", "#NextBtn", "#captchaForm button", "#skip-btn"]

                # First click — use the selector already found in the big script above
                found_selector = result['rescueSelector']

                if found_selector:
                    gplink_adclose_failed = 1
                    found_selector = driver.execute_script(rescue_script, selectors)
                    emptygppgae = time.time()
                    print(f"✅ Found and Rescued: {found_selector}")
                    btn_element = driver.find_element(By.CSS_SELECTOR, found_selector)
                    human_click(driver, btn_element)
                    print(f"🎯 OS Click Success on {found_selector}")
                    btn1_clicked = True
                else:
                    print("❌ No valid buttons found (or they are in 'Wait' state).")
                    btn1_clicked = False

                # Second click attempt
                if btn1_clicked:
                    time.sleep(1)
                    driver.switch_to.window(window)
                    found_selector = driver.execute_script(rescue_script, selectors)   # 1 call
                    if found_selector:
                        print(f"✅ Found and Rescued: {found_selector}")
                        btn_element = driver.find_element(By.CSS_SELECTOR, found_selector)
                        human_click(driver, btn_element)
                        print(f"🎯 OS Click Success on {found_selector}")
                        btn1_clicked = True
                        selectors.remove(found_selector)
                    else:
                        print("❌ No valid buttons found.")
                        btn1_clicked = False

                # Third click attempt
                if btn1_clicked:
                    time.sleep(1)
                    driver.switch_to.window(window)
                    found_selector = driver.execute_script(rescue_script, selectors)   # 1 call
                    if found_selector:
                        print(f"✅ Found and Rescued: {found_selector}")
                        btn_element = driver.find_element(By.CSS_SELECTOR, found_selector)
                        human_click(driver, btn_element)
                        print(f"🎯 OS Click Success on {found_selector}")
                        btn1_clicked = True
                    else:
                        print("❌ No valid buttons found.")
                        btn1_clicked = False

                script_elapsed_time = time.time() - emptygppgae
                script_seconds_only = int(script_elapsed_time)
                print('Powergram Time:', script_seconds_only)

                if script_seconds_only > 40:
                    btn_elements = driver.find_elements(By.CSS_SELECTOR, "#myTimerDiv")
                    if btn_elements:
                        print("⏳ Timer found, resetting start time.")
                        emptygppgae = time.time()
                        return
                    else:
                        print("🔄 No Timer found after 50s. Forcing Redirect...")
                        link = get_item_from_list("gplink_urls", "random")
                        window1 =  spoof_referrer_and_redirect(driver, "random", link, new_page=False)

            # ── GPlinks Get Link page ────────────────────────────────────────
            if result['isGetLink']:
                gplink_page_loaded = True
                try:
                    get_link_btn = driver.find_element(By.ID, "captchaButton")
                    btn_text = get_link_btn.text.strip()

                    if btn_text == "Get Link":
                        print("🎯 'Get Link' detected. Preparing human click...")
                        driver.execute_script(
                            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                            get_link_btn)
                        human_click(driver, get_link_btn)
                        return True

                    if btn_text == "Please wait...":
                        print('please wait btn cloudflare checking')
                        try:
                            x, y = pyautogui.locateCenterOnScreen(
                                "C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png",
                                confidence=0.6)
                            pyautogui.click(x, y, duration=1)
                            time.sleep(1)
                            pyautogui.click(x, y, duration=1)
                            time.sleep(5)
                        except Exception as e:
                            pass
                        return

                except Exception as e:
                    print('GPbtn', e)

            if 'powergram' in stealth_url or 'collegedekho' in stealth_url or 'powergam.online' in stealth_url or 'collegedekho.online' in stealth_url or 'gplinks.co' in stealth_url or 'gplinks' in stealth_url: 
                print('we are on page')
                gplink_page_loaded = True
            else:
                if gplink_page_loaded:
                    if gplink_page_notfound > 3:
                        print('Page Broken trying backwarding')
                        driver.back()
                        wait, driver = wait_for_load_state(driver, state="interactive", timeout=10, wait=True)
                        if wait:
                            print('Page loading')
                            current_url = driver.current_url

                            print(f"Current Page URL: {current_url}")
                            if 'powergram' in stealth_url or 'collegedekho' in stealth_url or 'powergam.online' in stealth_url or 'collegedekho.online' in stealth_url or 'gplinks.co' in stealth_url or 'gplinks' in stealth_url: 
                                print('we are on page')
                                gplink_page_notfound = 1
                                gplink_page_loaded = True
                            else:
                                link = get_item_from_list("gplink_urls", "random")
                                window1 =  spoof_referrer_and_redirect(driver, "random", link, new_page=False)

                    gplink_page_notfound += 1

        else:
            print('waiting for page to fully load gp')

    except Exception as e:
        print('Error at Gplinks:', e)



def shortxlinks_main(driver):
    if random.randint(1, 10) >= 8:
        print('random Move')
        move_human_os(random.randint(100, 800), random.randint(100, 500))

    try:
        wait, driver = wait_for_load_state(driver, state="interactive", timeout=10, wait=False)
        if not wait:
            return

        # ── SINGLE execute_script: classify + shortxlinks btn check in one shot ──
        result = driver.execute_script("""
            const title = document.title;
            const url   = window.location.href;

            const isShortxlinks = url.includes('shortxlinks');
            const isMtc         = url.includes('mtc');
            let consent_btn     = null;
            let bottomBtn       = null;    // ← top level
            let waitingBtnReady = false;   // ← top level

            if (isShortxlinks) {
                const btn = document.querySelector('#waiting-btn');
                if (btn) {
                    const s = window.getComputedStyle(btn);
                    const r = btn.getBoundingClientRect();
                    waitingBtnReady = (
                        s.display       !== 'none'   &&
                        s.visibility    !== 'hidden' &&
                        s.pointerEvents !== 'none'   &&
                        r.width > 0                  &&
                        !btn.disabled
                    );
                }
            }

            if (isMtc) {
                const consent_selectors =     [
                        '.qc-cmp2-summary-buttons button[mode="primary"]',
                        'button[mode="primary"]',
                        '.fc-agreement-dialog .fc-primary-button',         
                        'button[aria-label="Consent"]',                    
                        '#save .tp-button',                                
                        '.sd-cmp-2V7v7 .sd-button-primary',       
                        '.fc-primary-button',
                    ]

                for (const consen of consent_selectors) {
                    const btn = document.querySelector(consen);
                    if (btn) {
                        const style = window.getComputedStyle(btn);
                        const rect  = btn.getBoundingClientRect();
                        if (style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0) {
                            consent_btn = consen;
                            break;
                        }
                    }
                }

                const selectors = ["img[alt='DOWNLOAD LINK']", "img[alt='human verification']", "img[alt='CLICK 2X FOR GENERATE LINK']"];
                let maxTop = -1;
                for (const selector of selectors) {
                    const el = document.querySelector(selector);
                    if (el) {
                        const style = window.getComputedStyle(el);
                        const rect  = el.getBoundingClientRect();
                        const isVisibleCSS  = style.display !== 'none' && style.visibility !== 'hidden' && rect.height > 0;
                        const isInsideViewport = (
                            rect.top    >= 0 &&
                            rect.left   >= 0 &&
                            rect.bottom <= (window.innerHeight  || document.documentElement.clientHeight) &&
                            rect.right  <= (window.innerWidth   || document.documentElement.clientWidth)
                        );
                        if (isVisibleCSS && isInsideViewport && rect.top > maxTop) {
                            maxTop    = rect.top;
                            bottomBtn = selector;    // ← writes to top-level var
                        }
                    }
                }
            }

            return {
                title:           title,
                url:             url,
                isShortxlinks:   isShortxlinks,
                isMtc:           isMtc,
                waitingBtnReady: waitingBtnReady,
                bottomBtn:       bottomBtn,    // ← always defined now
                consent_btn:     consent_btn,
            };
        """)   # ← ONE call replaces title + url + verify_script (was 3 calls)

        title       = result['title']
        stealth_url = result['url']
        print(stealth_url)
        print(title)
        if 'chrome-error://chromewebdata/' in stealth_url:
            print('chrome-error is detect')
            #driver.close()
            return "chrome-error"
        if is_direct_resource_link(stealth_url):
            print('link is detect')
            driver.close()
            return

        if destined_reached(title):
            print('destined_reached is detect')
            driver.close()
            return
        # ── shortxlinks path ─────────────────────────────────────────────────
        if result['isShortxlinks']:
            print('shortxlinks page load')
            if result['waitingBtnReady']:
                print('btn is ready')
                btn_element = driver.find_element(By.CSS_SELECTOR, "#waiting-btn")   # 1 call
                human_click(driver, btn_element)
            else:
                print('btn is not ready')
            return

        # ── mtc path ─────────────────────────────────────────────────────────
        if result['isMtc']:
            print('we are on mtc1')
            selectors = [

                "img[alt='DOWNLOAD LINK']", # CSS selector for the image alt
                "img[alt='human verification']",
                "img[alt='CLICK 2X FOR GENERATE LINK']",
            ]
            if result['consent_btn']:
                accept_consent_popups(driver)
                
            if result['bottomBtn']:
                already_clicked = False
                for i in range(4):
                    clickf, selectors = wpsafe_human_handler(driver, selectors)
                    if clickf == "noclicks":
                        if already_clicked:
                            time.sleep(2)
                            already_clicked = False
                            continue
                        return
                    if clickf == "clicked":
                        time.sleep(1)
                        already_clicked = True
                        continue
                    if clickf == "clicked_last":
                        return

    except Exception as e:
        print('Shortxlinks Error:', e)


def wpsafe_human_handler(driver, selectors):
    # ── Single JS call: finds lowest visible button in viewport ──────────────
    found_selector = driver.execute_script("""
        const selectors = arguments[0];
        let bottomBtn = null, maxTop = -1;
        for (const s of selectors) {
            const el = document.querySelector(s);
            if (el) {
                const st = window.getComputedStyle(el);
                const r  = el.getBoundingClientRect();
                const visibleCSS = st.display !== 'none' && st.visibility !== 'hidden' && r.height > 0;
                const inViewport = (
                    r.top    >= 0 &&
                    r.left   >= 0 &&
                    r.bottom <= (window.innerHeight  || document.documentElement.clientHeight) &&
                    r.right  <= (window.innerWidth   || document.documentElement.clientWidth)
                );
                if (visibleCSS && inViewport && r.top > maxTop) {
                    maxTop = r.top;
                    bottomBtn = s;
                }
            }
        }
        return bottomBtn;
    """, selectors)   # 1 call — unchanged logic, just cleaned up

    if found_selector:
        print(f"✅ Safelink Button Ready: {found_selector}")
        btn_element = driver.find_element(By.CSS_SELECTOR, found_selector)   # 1 call
        human_click(driver, btn_element)
        selectors.remove(found_selector)
        if found_selector == "img[alt='DOWNLOAD LINK']":
            return "clicked_last", selectors
        return "clicked", selectors

    print("⏳ Safelink button not visible yet (still counting down...)")
    return "noclicks", selectors






def indianxshort_main(driver):
    if random.randint(1, 10) >= 8:
        print('random Move')
        move_human_os(random.randint(100, 800), random.randint(100, 500))
    wait, driver = wait_for_load_state(driver, state="interactive", timeout=10, wait=False)
    if not wait:
        return
    # ── SINGLE execute_script: title + url + consent + sticky + first btn scan ──
    result = driver.execute_script("""
        const title = document.title;
        const url   = window.location.href;
        let bottomBtn = null;
        let maxTop    = -1;
        let sticky_btn = null;
        const sticky_selectors = ["#closeStickyTop", "#closeStickyBottom"];
        let consent_btn = null;              
        // ── consent check ────────────────────────────────────────────────
        
        const consent_selectors =     [
                '.qc-cmp2-summary-buttons button[mode="primary"]',
                'button[mode="primary"]',
                '.fc-agreement-dialog .fc-primary-button',         
                'button[aria-label="Consent"]',                    
                '#save .tp-button',                                
                '.sd-cmp-2V7v7 .sd-button-primary',       
                '.fc-primary-button',
            ]
        for (const sel of consent_selectors) {
            const btn = document.querySelector(sel);
            if (btn) {
                const s = window.getComputedStyle(btn);
                const r = btn.getBoundingClientRect();
                if (s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0) {
                    consent_btn = sel;
                    break;
                }
            }
        }

        // ── sticky ad check ──────────────────────────────────────────────

        for (const sel of sticky_selectors) {
            const el = document.querySelector(sel);
            if (el) {
                const s = window.getComputedStyle(el);
                const r = el.getBoundingClientRect();
                if (s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0) {
                    sticky_btn = sel;
                    break;
                }
            }
        }

        // ── first robot btn scan (lowest visible) + scrollIntoView merged ─

        const robot_selectors = [
            "#robotButton", "#robot", "#robot2", "#rtgli1",
            "#rtg-generate", "#robotContinueButton",
            "#open-continue-btn", "#rtg-snp2"
        ];
        for (const sel of robot_selectors) {
            const el = document.querySelector(sel);
            if (el) {
                const s = window.getComputedStyle(el);
                const r = el.getBoundingClientRect();
                if (s.display !== 'none' && s.visibility !== 'hidden' && r.height > 0) {
                    if (r.top > maxTop) { maxTop = r.top; bottomBtn = sel; }
                }
            }
        }
        // scroll to it now so PyAutoGUI coords are ready when Python runs
        if (bottomBtn) {
            document.querySelector(bottomBtn).scrollIntoView({behavior: 'smooth', block: 'center'});
        }

        return {
            title:      title,
            url:        url,
            consent_btn: consent_btn,
            sticky_btn:  sticky_btn,
            bottomBtn:   bottomBtn,
        };
    """)   # ← replaces: title call + url call + accept_consent_popups JS
           #             + clear_sticky_ads JS + first rescue_script call
           #             + first scrollIntoView call  =  6 calls → 1

    title       = result['title']
    stealth_url = result['url']
    print(stealth_url)
    print(title)
    if 'chrome-error://chromewebdata/' in stealth_url:
        print('chrome-error is detect')
        #driver.close()
        return "chrome-error"
    if is_direct_resource_link(stealth_url):
        print('link is detect')
        driver.close()
        return
    if destined_reached(title):
        print('destined_reached is detect')
        driver.close()
        return
    # ── consent — only call if pre-scan found one ────────────────────────────
    if result['consent_btn']:
        accept_consent_popups(driver)   # 1 call only when needed

    # ── sticky ad — direct JS click, no find_element needed ─────────────────
    if result['sticky_btn']:
        try:
            #time.sleep(random.uniform(0.1, 0.3))
            driver.execute_script(
                f"document.querySelector('{result['sticky_btn']}').click();"
            )   # 1 call, skips find_element entirely
            print(f"🧹 Sticky Ad dismissed: {result['sticky_btn']}")
        except Exception as e:
            print(f"⚠️ Sticky click failed: {e}")

    # ── no buttons found on first scan — nothing to do ──────────────────────
    if not result['bottomBtn']:
        print("⏳ No robot buttons visible yet.")
        return False

    selectors = [
        "#robotButton", "#robot", "#robot2", "#rtgli1",
        "#rtg-generate", "#robotContinueButton",
        "#open-continue-btn", "#rtg-snp2"
    ]

    # rescue_script for loop iterations 2-4
    # scrollIntoView merged in so no separate execute_script per iteration
    rescue_script = """
        const selectors = arguments[0];
        let bottomBtn = null, maxTop = -1;
        for (const sel of selectors) {
            const el = document.querySelector(sel);
            if (el) {
                const s = window.getComputedStyle(el);
                const r = el.getBoundingClientRect();
                if (s.display !== 'none' && s.visibility !== 'hidden' && r.height > 0) {
                    if (r.top > maxTop) { maxTop = r.top; bottomBtn = sel; }
                }
            }
        }
        if (bottomBtn) {
            document.querySelector(bottomBtn).scrollIntoView({behavior: 'smooth', block: 'center'});
        }
        return bottomBtn;
    """

    # ── first iteration uses pre-scanned bottomBtn (0 JS calls) ─────────────
    target_selector = result['bottomBtn']

    for i in range(4):
        if target_selector:
            print(f"✅ Target found (Lowest): {target_selector}")
            try:
                element = driver.find_element(By.CSS_SELECTOR, target_selector)   # 1 call
                try:
                    element.click()
                except Exception as e:
                    print('click failed, JS fallback...')
                    driver.execute_script("arguments[0].click();", element)   # 1 call fallback
                time.sleep(random.uniform(0.1, 0.4))
                selectors.remove(target_selector)
                print(f"🎯 Click on {target_selector}")
            except Exception as e:
                print(f"⚠️ Click failed: {e}")
        else:
            print("⏳ No robot buttons visible yet.")
            return False

        # next iteration scan (scroll already merged inside rescue_script)
        target_selector = driver.execute_script(rescue_script, selectors)   # 1 call per iter


def close_unauthorized_tabs(driver, whitelist_handles):
    try:
        # Get a fresh list of handles every time
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle not in whitelist_handles:
                print('found some pages outside and try closing')
                try:
                    # 1. Switch focus
                    driver.switch_to.window(handle)
                    
                    # 2. Grab metadata safely
                    current_url = driver.current_url
                    current_title = driver.title
                    
                    # 3. Decision Logic: Only close real web pages (http)
                    if current_url.startswith('http'):
                        print(f"🧹 Closing unauthorized popup: {current_title} ({current_url})")
                        driver.close()
                        # IMPORTANT: After closing, move to the NEXT handle immediately
                        continue 
                    
                    # 4. Skip internal browser UI (like the Omnibox popup)
                    elif not current_title.strip() or 'Omnibox' in current_title or not current_url.startswith('http'):
                        print(f"⏩ Skipping Ghost/Internal Handle: {handle}")
                        continue
                        
                except Exception as e:
                    # If the window was already closed by an ad-blocker or it's a dead handle
                    print(f"⚠️ Handle {handle} was inaccessible, moving on...")
                    continue

        # 5. ALWAYS return focus to the main work tab
        if whitelist_handles:
            driver.switch_to.window(whitelist_handles[0])
            
    except Exception as e:
        print(f"⚠️ Master cleanup error: {e}")

    finally:
        # 3. RESTORE ORIGINAL TIMEOUT so the rest of your bot works normally

        print('all done closed..')



def close_shrink_ad_span(driver):
    result = driver.execute_script("""
        // ── main document check ──────────────────────────────────────
        const allSpans = document.querySelectorAll('span');
        const target = Array.from(allSpans).find(el => {
            const s = el.getAttribute('style') || '';
            return s.includes('width: 35%') && s.includes('left: 0px');
        });
        if (target) {
            target.setAttribute('data-adclose', 'true');
            target.scrollIntoView({ behavior: 'smooth', block: 'center' });
            return { found: true, inIframe: false, iframeIndex: null };
        }

        // ── iframe check (same-origin only) ──────────────────────────
        const iframes = document.querySelectorAll('iframe');
        for (let i = 0; i < iframes.length; i++) {
            try {
                const frameDoc = iframes[i].contentDocument || iframes[i].contentWindow.document;
                const frameSpan = Array.from(frameDoc.querySelectorAll('span')).find(el => {
                    const s = el.getAttribute('style') || '';
                    return s.includes('width: 35%') && s.includes('left: 0px');
                });
                if (frameSpan) {
                    frameSpan.setAttribute('data-adclose', 'true');
                    frameSpan.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    return { found: true, inIframe: true, iframeIndex: i };
                }
            } catch (e) {
                // cross-origin, skip
            }
        }
        return { found: false, inIframe: false, iframeIndex: null };
    """)   # 1 call

    if not result['found']:
        print("∅ No ad close span found")
        return False

    print("🎯 Ad close span found, clicking...")
    try:
        time.sleep(0.2)

        if result['inIframe']:
            # switch into the correct iframe first
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            driver.switch_to.frame(iframes[result['iframeIndex']])
            el = driver.find_element(By.CSS_SELECTOR, "[data-adclose='true']")
            human_click(driver, el)
            driver.switch_to.default_content()   # always switch back
        else:
            el = driver.find_element(By.CSS_SELECTOR, "[data-adclose='true']")
            human_click(driver, el)

        print("✅ Ad span closed")
        return True

    except Exception as e:
        print(f"⚠️ Click failed: {e}")
        driver.switch_to.default_content()   # safety restore on failure
    return False


midpageshrinkearn = False

def shrinkearn_main(driver, page_shrinkearn_close):
    if random.randint(1, 10) >= 8:
        print('random Move')
        move_human_os(random.randint(100, 800), random.randint(100, 500))
    global midpageshrinkearn
    try:
        wait, driver = wait_for_load_state(driver, state="interactive", timeout=10, wait=False)
        if not wait:
            return

        # ── SINGLE execute_script: title + url + consent + both branch logic ──
        script_code = """

const title = document.title;
const url   = window.location.href;
const isHealthShield = title.includes('Health Shield');

let consent_btn      = null;
let action           = null;
let value            = null;
let close_span       = null;
let adblockdetect       = null;

const isVis = (el) => {
    if (!el) return false;
    const s = window.getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0;
};

const inView = (r) => {
    return r.top >= 0 && r.bottom <= (window.innerHeight || document.documentElement.clientHeight);
};

const isVisConsent = (el) => {
    if (!el) return false;
    const s = window.getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return s.display !== 'none' && r.width > 0 && r.height > 0;
};

const consent_selectors = [
    
    '#accept-btn',
    'button[id="accept-btn"]',
    'button[mode="primary"]',
    '.fc-agreement-dialog .fc-primary-button',
    'button[aria-label="Consent"]',
    '#save .tp-button',
    '.sd-cmp-2V7v7 .sd-button-primary',
    '.fc-primary-button',
    '.qc-cmp2-summary-buttons button[mode="primary"]',
];

if (isHealthShield) {
    const getLinkBtn  = document.querySelector('a.btn.btn-success.btn-lg.get-link');
    const continueBtn = document.querySelector('button.btn.btn-primary.btn-captcha#continue');
    const adblock_btn = document.querySelector('div.alert.alert-danger');

    let click_btn_exist = false;
    if (isVis(getLinkBtn) && getLinkBtn.innerText.toLowerCase().includes('get link')) {
        action = 'scroll_click';
        value  = 'a.btn.btn-success.btn-lg.get-link';
        click_btn_exist = true;
    } else if (isVis(continueBtn) && !continueBtn.disabled && continueBtn.innerText.toLowerCase().includes('continue')) {
        action = 'scroll_click';
        value  = 'button.btn.btn-primary.btn-captcha#continue';
        click_btn_exist = true;
    }else if (isVis(adblock_btn) && continueBtn.innerText.toLowerCase().includes('disable adblock')) {
        adblockdetect = true;
    }

    if (click_btn_exist) {
        const spans = document.querySelectorAll('span');
        for (const el of spans) {
            const s = el.getAttribute('style') || '';
            if (
                s.includes('width: 35%')        &&
                s.includes('position: absolute') &&
                s.includes('left: 0px')          &&
                s.includes('bottom: 0px')
            ) {
                const innerText = (el.innerText || '').trim().toLowerCase();
                if (innerText.includes('close')) {
                    el.setAttribute('data-adclose', 'true');
                    close_span = true;
                    break;
                }
            }
        }
    }

} else {
    // ── shrinkearn normal branch ─────────────────────────────────
    const targets = ["#getnewlink", "#startButton", "#message .wp2continuelink"];
    for (const sel of targets) {
        const el = document.querySelector(sel);
        if (isVis(el) && inView(el.getBoundingClientRect())) {
            action = 'click'; value = sel; break;
        }
    }
    if (!value) {
        let closest = null, minD = Infinity;
        for (const sel of targets) {
            const el = document.querySelector(sel);
            if (isVis(el)) {
                const d = Math.abs(el.getBoundingClientRect().top);
                if (d < minD) { minD = d; closest = sel; }
            }
        }
        if (closest) { action = 'scroll_click'; value = closest; }
    }


}   // ← closes if/else — only ONE closing brace here, was TWO before
for (const sel of consent_selectors) {
    const btn = document.querySelector(sel);
    if (btn && isVisConsent(btn)) {
        consent_btn = true;
        break;
    }
}
return {
    title:          title,
    url:            url,
    isHealthShield: isHealthShield,
    consent_btn:    consent_btn,
    action:         action,
    value:          value,
    close_span:     close_span,
    adblockdetect: adblockdetect
};



        """   # ← replaces: title + url + accept_consent_popups JS
               #             + master_logic_js (either branch) = 4 calls → 1
        result = driver.execute_script(script_code)
        title       = result['title']
        stealth_url = result['url']
        close_spang =result['close_span']
        adblockdetect = result['adblockdetect']
        print(stealth_url)
        print(title)
        print(close_spang)
        if 'chrome-error://chromewebdata/' in stealth_url:
            print('chrome-error is detect')
            #driver.close()
            return "chrome-error"
        
        if is_direct_resource_link(stealth_url):
            print('link is detect')
            driver.close()
            return
        if adblockdetect:
            print('Adblock Detect...')
            driver.close()
            return
        # ── consent ──────────────────────────────────────────────────────
        if result['consent_btn']:
            print('found consents on shrinkearn')
            accept_consent_popups(driver)   # 1 call only when needed
        else:
            print('no consents on shrinkearn')
        if close_spang:
            try:
                print("🎯 Close span found, clicking...")
                # find_element works because we stamped data-adclose on it in JS
                el_close = driver.find_element(By.CSS_SELECTOR, "[data-adclose='true']")   # 1 call
                human_click(driver, el_close)
                time.sleep(0.2)
            except Exception as e:
                print("Failed to click close span:", e)
        try:
            x, y = pyautogui.locateCenterOnScreen(
                "shrinkearnadsblock",
                confidence=0.9)
            if x and y:
                print('adblock found shrinkearn')
                return 'adblock'
        except:
            pass
        # ── Health Shield cloudflare check (pyautogui only, 0 API calls) ─
        if result['isHealthShield']:
            print('Health shield found')
            close_shrink_ad_span(driver)
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    "C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png",
                    confidence=0.6)
                pyautogui.click(x, y, duration=1)
                time.sleep(1)
                pyautogui.click(x, y, duration=1)
                time.sleep(5)
            except:
                pass
            regiong = get_browser_region()
            try:
                # 1. Get the full box instead of just the center
                # Box = (left, top, width, height)
                box = pyautogui.locateOnScreen("closeadbts.png",region=regiong, confidence=0.99)
                
                if box:
                    target_x = (box.left + (box.width // 2)) - 50
                    target_y = (box.top + (box.height // 2))
                    
                    print(f"🎯 Target Acquired: X={target_x}, Y={target_y}")
                    
                    # 3. Perform the click
                    pyautogui.click(target_x, target_y, duration=0.2)

                else:
                    print("No Close Ad video Found")
            except Exception as e:
                print("No Close Ad video Found")
                #pass
        else:
            print('at shrinkearn pages')

        # ── click the pre-found button ────────────────────────────────────
        if result['value']:
            if result['isHealthShield']:
                if page_shrinkearn_close == 1:
                    driver.close()
                    return 'close'
            else:
                if midpageshrinkearn:
                    if page_shrinkearn_close == 3:
                        driver.close()
                        return 'close'
                if page_shrinkearn_close == 2:
                    driver.close()
                    return 'close'
                
            el = driver.find_element(By.CSS_SELECTOR, result['value'])   # 1 call
            if result['action'] == 'scroll_click':

                driver.execute_script(
                    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", el)   # 1 call
                time.sleep(0.2)
            human_click(driver, el)
            print(f"✅ Fast Action: {result['action']} on {result['value']}")
            if result['isHealthShield']:
                pass
            else:
                
                time.sleep(1)
                result = driver.execute_script(script_code)
                if result['value']:
                    el = driver.find_element(By.CSS_SELECTOR, result['value'])
                    if result['action'] == 'scroll_click':
                        driver.execute_script(
                            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", el)   # 1 call
                        time.sleep(0.2)
                    human_click(driver, el)
                    print(f"✅ Fast Action: {result['action']} on {result['value']}")
                    midpageshrinkearn = True
                else:
                    print('No more btns Srinkearn')
        else:
            print("∅ No target buttons found.")
            return None

    except Exception as e:
        print('ERR Shrinkearn:', e)


def cuttyio_main(driver):
    if random.randint(1,10) >= 8:
        print('random Move')
        move_human_os(random.randint(100,800), random.randint(100,500))

    try:
        wait, driver = wait_for_load_state(driver, state="interactive", timeout=10, wait= False)
        if wait:
            title = driver.execute_script("return document.title;")
            stealth_url = driver.execute_script("return window.location.href;")
            print(stealth_url)
            print(title)
            if 'github' in stealth_url:
                print('link is detect')
                driver.close()
            accept_consent_popups(driver)
            print('Cutty page load')
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.6)
                pyautogui.click(x, y,duration=1)
                time.sleep(1)
                pyautogui.click(x, y,duration=1)
                time.sleep(5)
                

            except Exception as e:
                pass
            # The JS script above (stored as a string)
            find_btn_script = """
const findAndPrepareButton = () => {
// Select all buttons with the ID or Class provided
const buttons = document.querySelectorAll('button#submit-button, button.vhit');

for (let btn of buttons) {
    const text = (btn.innerText || btn.value || "").trim().toLowerCase();
    const style = window.getComputedStyle(btn);
    const rect = btn.getBoundingClientRect();

    // 1. Basic Filters: Skip if "please wait", hidden, or disabled
    if (text.includes("please wait") || text.includes("...") ) continue;
    if (btn.disabled || style.display === 'none' || style.visibility === 'hidden' || style.opacity < 0.1) continue;

    // 2. Check if it's actually in the DOM with size
    if (rect.width === 0 || rect.height === 0) continue;

    // 3. Viewport & Scrolling Logic
    const isVisibleInViewport = (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );

    if (!isVisibleInViewport) {
        console.log("DEBUG: Button found but off-screen. Scrolling...");
        btn.scrollIntoView({ behavior: 'smooth', block: 'center' });
        // Return 'scrolled' so Python knows to wait a split second for the animation
        return { status: "scrolled", ref: btn.getAttribute('data-ref') };
    }

    // 4. Obstruction check (Clearing invisible overlays)
    const x = rect.left + rect.width / 2;
    const y = rect.top + rect.height / 2;
    const topEl = document.elementFromPoint(x, y);
    if (topEl && topEl !== btn && !btn.contains(topEl)) {
        // If it's a typical transparent ad overlay, hide it
        if (window.getComputedStyle(topEl).opacity < 0.5) {
            topEl.style.setProperty('display', 'none', 'important');
        }
    }

    return { status: "ready", ref: btn.getAttribute('data-ref'), text: text };
}
return { status: "not_found" };
};

return findAndPrepareButton();
"""

            result = driver.execute_script(find_btn_script)
            
            if result['status'] == "scrolled":
                print(f"Scrolling to button: {result['ref']}")
                time.sleep(1.5) # Wait for smooth scroll to finish
                # Re-run once to confirm it's now in view
                result = driver.execute_script(find_btn_script)

            if result['status'] == "ready":
                data_ref = result['ref']
                print(f"Button {data_ref} ('{result['text']}') is ready for human click")
                
                # Target the specific button found by JS using its data-ref and text
                # This is safer than just ID since ID is duplicated in your HTML
                try:
                    xpath = f"//button[@data-ref='{data_ref}' and not(@disabled)]"
                    btn_element = driver.find_element(By.XPATH, xpath)
                    
                    # Execute human click
                    human_click(driver, btn_element)
                    print(f"Successfully clicked {data_ref}")
                    return
                except Exception as e:
                    print(f"Error locating button after JS check: {e}")
            else:
                print('No valid clickable button found yet.')
                return
            
    except Exception as e:
        pass

def close_ad_overlay_fast(driver):
    # This script targets the container first, then the specific button.
    # It avoids searching the entire DOM.
    fast_find_js = """
    // 1. Target the overlay container by its unique centered-flex style
    // Usually these overlays are high-level children of <body> or a main wrapper
    const containers = document.querySelectorAll('div[style*="position: absolute"][style*="left: 50%"][style*="top: 50%"]');
    
    for (const div of containers) {
        // 2. Check for the 'Ad' marker or the specific Image source 
        // This confirms it's the specific overlay we're looking for
        if (div.innerText.includes('Ad') || div.querySelector('img[src*="bobapsoabauns.com"]')) {
            
            // 3. Narrow search only WITHIN this div for the 'Close' button
            const closeBtn = Array.from(div.querySelectorAll('span')).find(s => 
                s.innerText.trim().toLowerCase() === 'close' || 
                window.getComputedStyle(s).animationName.includes('showButtonTimerText')
            );

            if (closeBtn) {
                // If the span is the inner one, we want the clickable parent span
                const target = closeBtn.tagName === 'SPAN' && closeBtn.parentElement.tagName === 'SPAN' 
                               ? closeBtn.parentElement : closeBtn;
                
                target.setAttribute('data-target-overlay', 'true');
                return true;
            }
        }
    }
    return false;
    """

    try:
        # Execute the targeted search
        if driver.execute_script(fast_find_js):
            btn = driver.find_element(By.CSS_SELECTOR, "[data-target-overlay='true']")
            
            # Use your human_click logic
            human_click(driver, btn)
            print("🎯 Snipped the 'Close' overlay.")
            return True
    except:
        pass
    return False



def shrinkme_main(driver):
    btn1_clicked = False
    try:
        if random.randint(1,10) >= 8:
            print('random Move')
            move_human_os(random.randint(100,800), random.randint(100,500))

        wait, driver = wait_for_load_state(driver, state="interactive", timeout=10, wait= False)
        if wait:
            title = driver.execute_script("return document.title;")
            stealth_url = driver.execute_script("return window.location.href;")
            print(stealth_url)
            print(title)
            if 'workout' in stealth_url:
                print('link is detect')
                driver.close()
            accept_consent_popups(driver)
            close_ad_overlay_fast(driver)
            if 'ShrinkMe.io' in title:
                master_logic_js = """
                        const selectors = {
                           
                            getLink: ".btn.btn-success.btn-lg.get-link",
                            continueBtn: "button.btn.btn-primary",
                            
                        };

                        const isVis = (el) => {
                            if (!el) return false;
                            const style = window.getComputedStyle(el);
                            const rect = el.getBoundingClientRect();
                            return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0;
                        };

                        const inView = (rect) => {
                            return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);
                        };

                        // Priority 2: Check Get Link / Continue
                        const gl = document.querySelector(selectors.getLink);
                        if (isVis(gl) && gl.innerText.toLowerCase().includes('get link')) return { action: 'scroll_click', type: 'css', value: selectors.getLink };

                        const cb = document.querySelector(selectors.continueBtn);
                        if (isVis(cb) && !cb.disabled && cb.innerText.toLowerCase().includes('click here to continue')) return { action: 'scroll_click', type: 'css', value: selectors.continueBtn };

                        return null;
                        """

                result = driver.execute_script(master_logic_js)

                if result:
                    action = result['action']
                    val = result['value']
                    

                    el = driver.find_element(By.CSS_SELECTOR, val)

                    if action == 'scroll_click':
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",  el)
                        time.sleep(0.2) # Shortest possible wait
                    
                    human_click(driver, el)
                    print(f"✅ Fast Action: {action} on {val}")
                
            else:
                print('SHrin site')
                # 1. Define target selectors
                selectors = [".center-link-items #btn1", '#nextPage #btn2', ".center-link-items .tp-btn.tp-blue", ".center-link-items #btn2", "#tp-snp2" ];
                
                # The no-nonsense rescue script for Powergram
                rescue_script = """
                const selectors = arguments[0];
                const styleId = 'ui-helper-styles';

                // 1. Inject Styles
                if (!document.getElementById(styleId)) {
                    const style = document.createElement('style');
                    style.id = styleId;
                    style.innerHTML = `
                        .btn-rescue-active { z-index: 2147483647 !important; position: relative !important; outline: 3px solid #00FF00 !important; }
                        .obstacle-ghost { pointer-events: none !important; opacity: 0 !important; visibility: hidden !important; }
                    `;
                    document.head.appendChild(style);
                }


                const isVis = (el) => {
                    if (!el) return false;
                    const style = window.getComputedStyle(el);
                    const rect = el.getBoundingClientRect();
                    return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0;
                };

                const inView = (rect) => {
                    return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);
                };


                // Priority 3: Check Viewport Targets
                for (const sel of selectors) {
                    const el = document.querySelector(sel);
                    if (isVis(el) && inView( el.getBoundingClientRect())){

                            const rect = el.getBoundingClientRect();
                            const x = rect.left + rect.width / 2;
                            const y = rect.top + rect.height / 2;

                            let topEl = document.elementFromPoint(x, y);
                            let loopLimit = 0;
                            while (topEl && topEl !== el && !el.contains(topEl) && topEl !== document.documentElement && loopLimit < 15) {
                                topEl.classList.add('obstacle-ghost');
                                topEl = document.elementFromPoint(x, y);
                                loopLimit++; 
                            }
                            
                            // 3. Pop to top
                            el.scrollIntoView({ behavior: "smooth", block: "center" });
                            el.classList.add('el-rescue-active');
                            return sel;
                            
                            
                            }
                }

                // Priority 4: Find Closest
                let closest = null; let minD = Infinity;
                for (const sel of selectors) {
                    const el = document.querySelector(sel);
                    if (isVis(el)) {
                        const d = Math.abs(el.getBoundingClientRect().top);
                        if (d < minD) { minD = d; closest = sel; }
                    }
                }
                if (closest){
                            const el = document.querySelector(closest);
                            const rect = el.getBoundingClientRect();
                            const x = rect.left + rect.width / 2;
                            const y = rect.top + rect.height / 2;

                            let topEl = document.elementFromPoint(x, y);
                            let loopLimit = 0;
                            while (topEl && topEl !== el && !el.contains(topEl) && topEl !== document.documentElement && loopLimit < 15) {
                                topEl.classList.add('obstacle-ghost');
                                topEl = document.elementFromPoint(x, y);
                                loopLimit++; 
                            }
                            
                            // 3. Pop to top
                            el.scrollIntoView({ behavior: "smooth", block: "center" });
                            el.classList.add('el-rescue-active');
                            return closest;
                            
                            
                            }

                return null;


                """
                found_selector = driver.execute_script(rescue_script,selectors)

                if found_selector:
                    print(f"✅ Found and Rescued: {found_selector}")

                    # 4. Get the physical element object in Python
                    btn_element = driver.find_element(By.CSS_SELECTOR, found_selector)
                    
                    # 5. Execute your Adaptive PyAutoGUI Click (The "Human" part)
                    # We reuse the logic that worked perfectly for you
                    human_click(driver, btn_element)

                    
                    print(f"🎯 OS Click Success on {found_selector}")
                    btn1_clicked =  True
                    
                
                else:
                    print("❌ No valid buttons found (or they are in 'Wait' state).")
                    btn1_clicked =  False




                if btn1_clicked:
                    time.sleep(1)
                    found_selector = driver.execute_script(rescue_script, selectors)
                    if found_selector:
                        print(f"✅ Found and Rescued: {found_selector}")
                        # 4. Get the physical element object in Python
                        btn_element = driver.find_element(By.CSS_SELECTOR, found_selector)
                        # 5. Execute your Adaptive PyAutoGUI Click (The "Human" part)
                        # We reuse the logic that worked perfectly for you
                        human_click(driver, btn_element)
                        print(f"🎯 OS Click Success on {found_selector}")
                        btn1_clicked =  True
                        selectors.remove(found_selector)
                    else:
                        print("❌ No valid buttons found (or they are in 'Wait' state).")
                        btn1_clicked =  False

                if btn1_clicked:
                    time.sleep(1)
                    found_selector = driver.execute_script(rescue_script, selectors)
                    if found_selector:
                        print(f"✅ Found and Rescued: {found_selector}")
                        # 4. Get the physical element object in Python
                        btn_element = driver.find_element(By.CSS_SELECTOR, found_selector)
                        # 5. Execute your Adaptive PyAutoGUI Click (The "Human" part)
                        # We reuse the logic that worked perfectly for you
                        human_click(driver, btn_element)
                        print(f"🎯 OS Click Success on {found_selector}")
                        btn1_clicked =  True
                    else:
                        print("❌ No valid buttons found (or they are in 'Wait' state).")
                        btn1_clicked =  False
                
                





        else:
            print('waiting for page to fully load gp')

    except Exception as e:
        print('Error at Gplinks:',e)



def is_direct_resource_link(url):
    """
    Checks if a URL contains any of the blocked/resource keywords.
    Returns True if a match is found, False otherwise.
    """
    if not url:
        return False
        
    # Your specific list of keywords
    resource_keywords = [

        "huggingface.co",
        "huggingface",
        "mediafire.com",
        "gamemodding.com",
        "gamemodding",
        "gta5-mods.com",
        "gta5-mods",
        "aether.mom",
"limewire",
"dogegamer",
        "hianime.to",
        "hianime",
        "4anime.gg",
        "4anime",
        "simkl.com",
        "simkl",
        "aliexpress",
        "animekai.me",
        "animekai.to",
        "animekai",
        "animetosho.org",
        "codepen.io",
        "github.com",
        "megaup.site",
        "pastebin.com",
        "simkl.com",
        "vikingf1le.us.to",
        "vikingfile.com",

        "explore.org",
        "demo.",
        "demo.dynamicslab.ai",
        "learn-anything",
        "hacksplaining",
        "ifixit.com",
        "human.biodigital",
        "photoskop.com",
        "typingclub",
        "myemulator",
        "remove.photos",
        "secretflixcodes",
        "3dtuning",
        "workout.cool",
        "x-minus",
        "buildcores",
        "yoprintables",
        "remusic.ai",
        "chronas",
        "faceonlive",

        "pointerpointer.com",
        "neal.fun",
        "onemillioncheckboxes.com",
        "staggeringbeauty.com",
        "eelslap.com",
        "shademap.co",
        "homicide.watch",
        "worldometers.info",
        "webwithoutwords.com",
        "cookingforengineers.com",
        "notalwaysright.com",
        "artofmanliness.com",
        "cracked.com",
        "quickdraw.withgoogle.com",
        "play2048.co",
        "9gag.com",
        "iwastesomuchtime.com",
        "stellarium-web.org",
        "fallingfalling.com",
        "zoomquilt.org",
        'mediafire',
        'filebin',
        "patreon.com",
        "getintopc.com",
        "mega.nz",
        "drive.google.com",
        "vidu.com",
        "drive.usercontent.google.com",
        "gtaxscripting.blogspot.com",

        "moewalls.com",
        "cursify.vercel.app",
        "cursify",
        "dynamicslab",
        'contentcore.xyz',
        'pixelmotion.art',
        'catbox.moe',
        'litterbox.catbox.moe',
        'napkin.ai',
        'wolframalpha.com',
        'spline.design',
        'freesewing.eu',
        'chefgpt.xyz',
        'asciiart.eu',

        "docs.google.com",
        "thenewscasts.com"
    ]

    # Convert URL to lowercase once for comparison
    url_lower = url.lower()

    for keyword in resource_keywords:
        if keyword.lower() in url_lower:
            print(f"🚫 Match Found: URL contains '{keyword}'")
            return True
            
    return False


#############Random item Selections####################################





def get_item_from_list(list_name, item_number, filename=r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\shortlink_urls.txt"):
    try:
        if not os.path.exists(filename):
            print("❌ Error: Database file not found.")
            return None

        with open(filename, "r") as f:
            data = json.load(f)

        if list_name in data:
            target_list = data[list_name]
            
            # --- NEW RANDOM LOGIC ---
            if str(item_number).lower() == "random":
                result = random.choice(target_list)
                print(f"🎲 Randomly picked from '{list_name}': {result}")
                return result
            
            # --- ORIGINAL NUMBER LOGIC ---
            index = int(item_number) - 1
            if 0 <= index < len(target_list):
                result = target_list[index]
                print(f"🔍 Found in '{list_name}' at position {item_number}: {result}")
                return result
            else:
                print(f"❌ Error: Position {item_number} is out of range for list '{list_name}'.")
                time.sleep(999999)
        else:
            print(f"❌ Error: List name '{list_name}' does not exist.")
            time.sleep(999999)
            
    except Exception as e:
        print(f"⚠️ Error reading file: {e}")
        time.sleep(999999)
    time.sleep(999999)



def get_profile_by_line(line_number,filename=r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\fingerprint_os.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            
            # Adjust for 0-based indexing (Line 64 is index 63)
            target_index = int(line_number) - 1
            
            if 0 <= target_index < len(lines):
                data = lines[target_index].strip().split("|")
                
                # Assign to your variables
                _current_id = data[0]
                _device_os = data[1]
                _chrome_version = data[2]
                
                print(f"Loaded Profile {line_number}: OS={_device_os}, Chrome={_chrome_version}")
                return _device_os, _chrome_version
            else:
                print("Error: Line number out of range (1-100 only).")
                print(line_number)
                #return "Windows 11", "145"
                time.sleep(9999)
                
    except FileNotFoundError:
        print("Error: profiles.txt not found. Run generate_profile_list() first.")
        time.sleep(9999)



def update_Url_shortners():
    # URL to the raw GitHub file
    url = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/refs/heads/main/claimcoins.json"
    
    # Path to your local content.js
    file_path = r"C:\Users\Administrator\Downloads\MFV6-main\MFV6-main\shortlink_urls.txt"

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



def get_city_slug(tz_string):
    if not tz_string: return ""
    # Replace underscores with slashes to handle all formats, then split
    parts = tz_string.replace('_', '/').split('/')
    # Return the last part, lowercased and stripped
    return parts[-1].strip().lower()
import zoneinfo
def get_utc_offset(tz_name):
    try:
        # Normalize common naming issues (like Calcutta)
        # zoneinfo usually handles aliases, but we need a valid TZ string
        now = datetime.datetime.now(zoneinfo.ZoneInfo(tz_name))
        return now.utcoffset().total_seconds()
    except Exception:
        return None
    

update_content_extension()
update_Url_shortners()
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
nochange_ip = False
sameip = ''
same_timezones = ''


testrun = True


_device_os = "Windows 11" # Windows 10 , Windows 11, Linux, Mac OS X 15 , Mac OS X 26 , Mac OS X 14
_device_type = "windows"
_chrome_version = "144"


API_KEY = adspower_api_grabber()




while testrun:
        start_time = time.time()
        focus_and_close_window('SunBrowser')
        close_chrome()
        time.sleep(1)
        location_changes += 1
        tux_stat_check += 1
        if testing:
            if tux_stat_check >= 5 and Mysterium_Mode == False or location_changes >= 97 and Mysterium_Mode == False:
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
                        
            if nochange_ip:
                print('use same ip')
                

                ip, pc_good, tm_good , list_timezones =  checkip_selenium(sameip) #"151.73.1.91", True, True, list_timezones
                if ip == sameip:
                    
                    list_timezones = same_timezones
                nochange_ip = False
            else:
                tuxler_changer()
                ip, pc_good, tm_good , list_timezones =  checkip_selenium()

            if not pc_good or not tm_good:
                print("\n❌ Current IP is not suitable for testing. Please check your network settings or try again later.")
                continue
            if preip == ip:
                restart_tuxler()
                continue
            script_elapsed_time = time.time() - start_time
            script_seconds_only = int(script_elapsed_time)
            print('Ip checked Time:', script_seconds_only)
            delete_all_profiles()

            time.sleep(1)
            print('create profile')
            _device_os, _chrome_version = get_profile_by_line(location_changes)
            print(_device_os, _chrome_version)
            user_id = create_profile(timezone_list =list_timezones, os_type=_device_type,os_version= _device_os, chrome_ver=_chrome_version)  # ← returns string directly now

            if 'daily limit' == user_id:
                nochange_ip = True
                sameip = ip
                same_timezones = list_timezones
                reloginadspower()
                continue

            if not user_id:
                exit()
            port_selenium, chromedriver_selenium = start_browser(user_id)
            if 'daily limit' == chromedriver_selenium:
                print('ADspowerLimit')
                #time.sleep(88888)
                nochange_ip = True
                sameip = ip
                same_timezones = list_timezones
                reloginadspower()
                continue
        else:
            port_selenium, chromedriver_selenium = start_browser("k1alt6kr")
            if 'daily limit' == chromedriver_selenium:
                print('ADspowerLimit')
                #time.sleep(88888)
                reloginadspower()
                continue
        if not port_selenium:
            exit()
        

        
        time.sleep(5)

        # 4. connect selenium
        driver = connect_selenium(port_selenium, chromedriver_selenium)
        driver.set_page_load_timeout(10)
        script_elapsed_time = time.time() - start_time
        script_seconds_only = int(script_elapsed_time)
        print('Selenium Time:', script_seconds_only)
        print("\n── IP check ────────────────────────────────────")

        focus_and_maximize_window('Sunbrowser')




        driver.get("https://api.ipify.org/")
        
        waitforpage, driver = wait_for_load_state(driver, state="complete", timeout=30, wait= True)
        if waitforpage == False:
            print('Page Loading Failed... ipifly')
            continue
            

        ipaddress = driver.find_element(By.TAG_NAME, "body").text.strip()
        print(f"✅ IP: {ipaddress}")

        if testing:
            if ipaddress != ip :
                print('IP missmatched',ipaddress, ip)
                continue

        
        browser_tz_raw = driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone;")
        ip_tz_raw = list_timezones.get("timezone", "")

        # 2. Normalize and extract the last part (e.g., 'cordoba')


        browser_city = get_utc_offset(browser_tz_raw)
        ip_city = get_utc_offset(ip_tz_raw)

        print(f"Browser City: {browser_city} | IP City: {ip_city}")

        # 3. Compare the "City" level instead of the full path
        if browser_city == ip_city and browser_city != "":
            print("✅ Timezone Match: Success")
        else:
            print(f"⚠️ Timezone Mismatch ({browser_city} vs {ip_city}): Potential Bot Flag")
            #time.sleep(99999)
            focus_and_close_window('SunBrowser')
            close_chrome()
            time.sleep(4)
            port_selenium, chromedriver_selenium = start_browser(user_id)
            driver = connect_selenium(port_selenium, chromedriver_selenium)

        
        script_elapsed_time = time.time() - start_time
        script_seconds_only = int(script_elapsed_time)
        print('Selenium Time:', script_seconds_only)
        print("\n── IP check ────────────────────────────────────")

        focus_and_maximize_window('Sunbrowser')
        driver.get("https://api.ipify.org/")
        
        waitforpage, driver = wait_for_load_state(driver, state="complete", timeout=30, wait= True)
        if waitforpage == False:
            print('Page Loading Failed... ipifly')
            continue
            

        ipaddress = driver.find_element(By.TAG_NAME, "body").text.strip()
        print(f"✅ IP: {ipaddress}")

        if testing:
            if ipaddress != ip :
                print('IP missmatched',ipaddress, ip)
                continue



        browser_rect = None
        for attempt in range(5):
            try:
                # Ensure we are switched to the active tab
                if len(driver.window_handles) > 0:
                    driver.switch_to.window(driver.window_handles[0])
                
                browser_rect = driver.get_window_rect()
                if browser_rect:
                    break
            except Exception as e:
                print(f"⏳ Window not ready (Attempt {attempt+1}/5)...")
                time.sleep(2)
        
        if not browser_rect:
            print("❌ Critical Error: Could not grab browser geometry.")
            continue

        browser_rect = driver.get_window_rect()
        nav_bar_height = driver.execute_script('return window.outerHeight - window.innerHeight;')
        print(browser_rect, nav_bar_height)


        
        browser_tz_raw = driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone;")
        ip_tz_raw = list_timezones.get("timezone", "")

        # 2. Normalize and extract the last part (e.g., 'cordoba')


        #browser_city = get_city_slug(browser_tz_raw)
        #ip_city = get_city_slug(ip_tz_raw)
        browser_city = get_utc_offset(browser_tz_raw)
        ip_city = get_utc_offset(ip_tz_raw)

        print(f"Browser City: {browser_city} | IP City: {ip_city}")

        # 3. Compare the "City" level instead of the full path
        if browser_city == ip_city and browser_city != "":
            print("✅ Timezone Match: Success")
        else:
            print(f"⚠️ Timezone Mismatch ({browser_city} vs {ip_city}): Potential Bot Flag")
            continue


        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        preip = ip
        print("\n── Extension Configure ────────────────────────────────────")
        print("\n── Always on Configure ────────────────────────────────────")
        driver.get("chrome-extension://ehllkhjndgnlokhomdlhgbineffifcbj/data/options/index.html")
        waitforpage, driver = wait_for_load_state(driver, state="complete", timeout=30, wait= True)
        if waitforpage == False:
            print('Page Loading Failed... extension1')
            continue
            
        wait = WebDriverWait(driver,20)
        textarea = wait.until(EC.visibility_of_element_located((By.ID, "hosts")))
        
        # 3. Clear existing content and type '*'
        # textarea.clear() sometimes fails on extension pages, 
        # so we use CTRL+A + Backspace to be safe.
        if DEVICE_ADSPOWER == "android":
            # Mobile: skip ALL selenium interactions, pure JS only
            driver.execute_script("""
                var ta = document.getElementById('hosts');
                ta.value = '*';
                ta.dispatchEvent(new Event('input', { bubbles: true }));
                ta.dispatchEvent(new Event('change', { bubbles: true }));
                
                var btn = document.getElementById('save');
                btn.click();
            """)
            print("Extension settings updated successfully (mobile JS mode).")
        else:
            # Desktop: original keyboard flow
            textarea.click()
            textarea.send_keys(Keys.CONTROL + "a")
            textarea.send_keys(Keys.BACKSPACE)
            textarea.send_keys("*")
            time.sleep(1)
            save_button = driver.find_element(By.ID, "save")
            save_button.click()
            print("Extension settings updated successfully.")





        print("\n── Rekt Configure ────────────────────────────────────")
        driver.get("chrome-extension://bbdhfoclddncoaomddgkaaphcnddbpdh/popup.html")
        waitforpage, driver = wait_for_load_state(driver, state="complete", timeout=30, wait= True)
        if waitforpage == False:
            print('Page Loading Failed... extension2')
            continue
        wait = WebDriverWait(driver,20)
        settings_to_enable = ["recaptcha_auto_open", "recaptcha_auto_solve"]
        for i in range(4):
            for setting in settings_to_enable:
                # Locate the specific toggle div by its data-settings attribute
                xpath = f"//div[@data-settings='{setting}']"
                toggle_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                
                # Get the current class to see if it's already 'on'
                current_class = toggle_element.get_attribute("class")
                
                if "off" in current_class:
                    print(f"[+] Toggling {setting} to ON...")
                    toggle_element.click()
                else:
                    print(f"[-] {setting} is already ON. Skipping.")
                
        print("✅ Recaptcha automation settings are ready.")

        print("\n──All Extensions are configured ────────────────────────────────────")
        print("\n──Openning Shortlinks ────────────────────────────────────")
        try:
            add_farm_activity(farmid=f"Farm{farm_id}", country= list_timezones.get("country"), ipaddress= ip , duration = f"B: {browser_tz_raw} |IP: {ip_tz_raw}", sites = f'{sites_done}x | 3 ', fingerprints_id= f"{browser_rect['width']} x {browser_rect['height']}", tuxler_left=location_changes, expiredate=expire)
        except Exception as e:
            print('ERR at Pymong:',e)

        new_tab_handle = driver.current_window_handle

        
        link = get_item_from_list("gplink_urls", "random")
        window1 =  spoof_referrer_and_redirect(driver, "random", link)
        if window1 == False:
            continue
        if DEVICE_ADSPOWER == "notest":
            link = get_item_from_list("shortxlink_urls", "random")
            window2 = spoof_referrer_and_redirect(driver,"random", link)
            if window2 == False:
                continue

            link = get_item_from_list("indianxlink_urls", "random")
            window3 = spoof_referrer_and_redirect(driver, "random", link)
            if window3 == False:
                continue


            window4 = 'g3t3tg'# spoof_referrer_and_redirect(driver, "https://web.telegram.org/a/get/", "https://tpi.li/PojXEQ9") #spoof_referrer_and_redirect(driver, "https://web.telegram.org/a/get/", "https://gplinks.co/fp7jnWT")
            if window4 == False:
                continue
        if DEVICE_ADSPOWER == "notest":
            print(window1,window2,window3,window4)
        driver.switch_to.window(new_tab_handle)
        driver.close()
        driver.switch_to.window(window1)
        shortxlink_done = False


        win1_done = False
        win2_done = False
        win3_done = False
        
        start_loop = True
        last_closetab = time.time()
        last_ipcheck = time.time()
        gplink_page_loaded = False
        gplink_page_notfound = 1
        gplink_adclose_failed = 1
        gg = random.random()
        if gg < 0.7:
            print("hel",gg)
            close_shrinkearn = False
        else:
            close_shrinkearn = True
        page_shrinkearn_close = random.choice([1, 2, 3])
        midpageshrinkearn = False

        while start_loop:
            try:
                script_elapsed_time = time.time() - start_time
                script_seconds_only = int(script_elapsed_time)
                print('Time:', script_seconds_only)
                if script_seconds_only > 600:
                    print("TimeOut All pages are Closed and Failed... 600")
                    start_loop = False
                    continue

                if win1_done and win2_done and win3_done:
                    print("All pages are Closed and Success")
                    start_loop = False
                    continue

                if DEVICE_ADSPOWER == "notest":
                    script_elapsed_time = time.time() - last_closetab
                    script_seconds_only = int(script_elapsed_time)
                    print('Last Close:', script_seconds_only)
                    main_handlers = [window1,window2,window3,window4]
                    if script_seconds_only > 40:
                        close_unauthorized_tabs(driver, main_handlers)
                        last_closetab = time.time()
                        
                    ################    
                    script_elapsed_time = time.time() - last_ipcheck
                    script_seconds_only = int(script_elapsed_time)
                    print('last_ipcheck :', script_seconds_only)
                    if script_seconds_only > 100:
                        last_ipcheck = time.time()

                        driver.switch_to.new_window('tab')
                        driver.get("https://api.ipify.org/")
                        
                        waitforpage, driver = wait_for_load_state(driver, state="interactive", timeout=30, wait= True)
                        if waitforpage == False:
                            print(f'Page Loading Failed... api ipfly')
                            continue

                        ipaddress = driver.find_element(By.TAG_NAME, "body").text.strip()
                        print(f"✅ IP: {ipaddress}")
                        if ipaddress != ip :
                            print('IP missmatched',ipaddress, ip)
                            start_loop = False
                            continue
                sites_done = 0
                try:

                    driver.switch_to.window(window1)
                    time.sleep(1)
                    result = False
                    result = gplinks_main(driver, window1)
                    if result == "chrome-error":
                        print('gplinks_main is broken 1')
                        win1_done = True
                except Exception as e:
                    win1_done = True
                    sites_done += 1
                    #print('Win1 ERR automation:', e)

                if DEVICE_ADSPOWER == "notest":
                    if shortxlink_done == False:
                        try:
                            driver.switch_to.window(window2)
                            time.sleep(1)
                            result = False
                            result = shortxlinks_main(driver)
                            if result == "chrome-error":
                                print('shortxlinks_main is broken 1')
                                win2_done = True

                        except Exception as e:
                            win2_done = True
                            #sites_done += 1
                            #print('Win2 ERR automation:', e)
                            if shortxlink_done == False:
                                link = get_item_from_list("shrinkearn_urls", "random")
                                window4 = spoof_referrer_and_redirect(driver, "random", link) #spoof_referrer_and_redirect(driver, "https://web.telegram.org/a/get/", "https://gplinks.co/fp7jnWT")
                                if window4 == False:
                                    continue
                                shortxlink_done = True
                                win2_done = False
                    try:
                        driver.switch_to.window(window3)
                        time.sleep(1)
                        result = False
                        result = indianxshort_main(driver)
                        if result == "chrome-error":
                            print('indianxshort_main is broken 1')
                            win3_done = True
                    except Exception as e:
                        win3_done = True
                        sites_done += 1

                        #print('Win3 ERR automation:', e)
                    if shortxlink_done == True:

                        try:
                            driver.switch_to.window(window4)
                            time.sleep(1)
                            result = False
                            if close_shrinkearn:
                                result = shrinkearn_main(driver, page_shrinkearn_close)
                            result = shrinkearn_main(driver, '5')
                            if result == "close":
                                print('shrinkearn_main is close 1')
                                win2_done = True
                            if result == "chrome-error":
                                print('shrinkearn_main is broken 1')
                                win2_done = True
                            if result == "adblock":
                                print('shrinkearn_main is adblock 2')
                                win2_done = True
                        except Exception as e:
                            win2_done = True
            except Exception as e:
                print("ERR at loop: ",e)












