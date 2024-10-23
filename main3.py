

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support import expected_conditions as EC
import random
import requests
from requests.exceptions import RequestException
from seleniumbase import Driver
import subprocess
import pyautogui
from datetime import datetime
import pytz
import datetime
import cv2
import numpy as np
from PIL import Image
from pymongo import MongoClient
from paddleocr import PaddleOCR
import Levenshtein
import json
import argparse
import clipboard


# Initialize the argument parser
parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument('--farm', type=int, help="Farm")
parser.add_argument('--fresh', type=int, help="Fresh")
args = parser.parse_args()
farm_id = args.farm
fresh = args.fresh
facebook_cookies = '0'



CSB1_farms = [1, 2, 3, 4]
fb_pass = 'ashen1997'
yt_api_key = 'AIzaSyCoAMmJOYzKhFdLO5oEmwI2Ne7C329jJtg'
mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"

if farm_id == 1:
    facebook_cookies = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/Facebook_Logins/alisabro.json'
    mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
    yt_api_key = 'AIzaSyCoAMmJOYzKhFdLO5oEmwI2Ne7C329jJtg'
    fb_pass = 'ashen1997'
    server_name1 = 'thailand'
    CSB1_farms = [1, 2, 3, 4]
elif farm_id == 2:
    facebook_cookies = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/Facebook_Logins/diludilakshi.json'
    mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
    yt_api_key = 'AIzaSyCoAMmJOYzKhFdLO5oEmwI2Ne7C329jJtg'
    fb_pass = 'ashen1997'
    server_name1 = 'romania'
    CSB1_farms = [1, 2, 3, 4]
elif farm_id == 3:
    facebook_cookies = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/Facebook_Logins/williesmith.json'
    mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
    yt_api_key = 'AIzaSyCoAMmJOYzKhFdLO5oEmwI2Ne7C329jJtg'
    fb_pass = 'ashen1997'
    server_name1 = 'poland'
    CSB1_farms = [1, 2, 3, 4]
elif farm_id == 4:
    facebook_cookies = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/Facebook_Logins/metroboom.json'
    mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
    yt_api_key = 'AIzaSyCoAMmJOYzKhFdLO5oEmwI2Ne7C329jJtg'
    fb_pass = 'ashen1997'
    server_name1 = 'hungary'
    CSB1_farms = [1, 2, 3, 4]

else:
    while True:
        print('SOmething Wrong Did u use --farm')

debug_mode = False

ip_required = 0
#farm_id = 1

run_sb1 = True
with_baymack = True


chrome_binary_path = '/opt/google/chrome/google-chrome'
chrome_user_data_dir = '/root/.config/google-chrome/'


mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"

client = MongoClient(mongo_uri)
db = client['MoneyFarmV6'] 
collection = db[f'Farm{farm_id}']
ocr = PaddleOCR(use_angle_cls=True, lang='en',  drop_score=0)

bitmoon = True
earnpp = True
claimcoin = True
feyorra = True


def add_messages(type_value, new_messages):
    try:
        query = {"type": type_value}
        existing_doc = collection.find_one(query)
        print("Existing document before update")
        new_message = new_messages # {'2024-09-06 03:47:14': 220}  # Use a new timestamp
        messages = existing_doc['messages']
        messages.update(new_message)
        update = {"$set": {"messages": messages}}
        result = collection.update_one(query, update)
        print("Updated document")
        if result.matched_count > 0:
            print(f"Added new messages to existing document. Updated {result.modified_count} document(s).")
        else:
            print("No document found with the specified type.")
    except Exception as e:
        print(e)

def insert_data(ip, amount1, amount2):
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')

    query = {"type": "main"}
    sample_document = {
        "Skylom": amount1,
        "Baymack": amount2,
        "Status": now,
        "Ip": ip,
        "response": 'Running'
        
    }
    update = {"$set": sample_document}
    result = collection.update_one(query, update)      
    if result.modified_count > 0:
        print(f"Updated {result.modified_count} document(s).")
    else:
        print("No document was updated.")
    add_messages('skylom', {now: amount1})
    add_messages('baymack', {now: amount2})
    return



def get_ip(driver):
    while True:
        original_window = driver.current_window_handle
        driver.open_new_window()
        try:
            #driver.switch_to.newest_window()
            driver.get('https://api.ipify.org/')
            ip_address = driver.get_text('body')
            print('IP =', ip_address)
            driver.close()
            driver.switch_to.window(original_window)
            return ip_address
        
        except Exception as e:
            print(e)
        driver.close()
        driver.switch_to.window(original_window)


def get_current_window_id():
    # Run the command to get the current window ID
    result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE)
    window_id = result.stdout.decode('utf-8').strip()
    print(f"Current Window ID: {window_id}")
    return window_id

def activate_window_by_id(window_id):
    # Run the command to activate the window by its ID
    print(f"Activate Window ID: {window_id}")
    subprocess.run(['xdotool', 'windowactivate', window_id])


def get_proxycheck_inbrowser(sb1, ip, server_name):   
    url = f'https://proxycheck.io/v2/{ip}?vpn=1&asn=1'
    val = None
    try:
        original_window = sb1.current_window_handle
        sb1.open_new_window()
        sb1.get(url)
        ip_address_raw = sb1.get_text('body')
        #print("Raw Response:", ip_address_raw)
        ip_address = json.loads(ip_address_raw)
        proxy_status = ip_address[str(ip)]["proxy"]
        country = ip_address[str(ip)]["country"]

        print(f"IP Address: {ip} \nProxy Status: {proxy_status} \nCountry: {country}")
        if country.lower() in server_name.lower():
            if proxy_status == 'no':
                val = 200
            else:
                print(f'{country} is valid with not proxy status.')
                val = 50
        sb1.close()
        sb1.switch_to.window(original_window)
        
        return val
    
    except Exception as e:
        print(f'ibbrowser ProxyCheck Error: {e}')
        return val


def get_proxycheck(driver, ip, server_name):
    url = f'https://proxycheck.io/v2/{ip}?vpn=1&asn=1'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
        #print(result)
        # Extract IP address and proxy status
        status = result.get('status')
        if status == 'ok':
            ip_address = ip
            ip_info = result.get(f'{ip_address}', {})
            proxy_status = ip_info.get('proxy', 'Unknown')
            country = ip_info.get('country', 'Unknown')
            print(f"IP Address: {ip_address} \nProxy Status: {proxy_status} \country Status: {country}")
            if country.lower() in server_name.lower():
                if proxy_status =='no':
                    return 200
                else:
                    print(f'{country} is not {200}')
                    return 50
        else:
            print("Error: Status not OK : Trying Inbrowser Way")
            val = get_proxycheck_inbrowser(driver, ip, server_name)
            return val
    except requests.RequestException as e:
        print(f"Error retrieving IP address and proxy status: {e}")
        return None

def get_ipscore(ip):
    url = f'https://ipqualityscore.com/api/json/ip/Bfg1dzryVqbpSwtbxgWb1uVkXLrr1Nzr/{ip}?strictness=3&allow_public_access_points=false'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
        # print(result)  # Print the raw response for debugging

        # Assign specific data fields to variables
        fraud_score = result.get('fraud_score', None)
        if fraud_score is None or not isinstance(fraud_score, int):
            fraud_score = 89  # Assign a default integer value if fraud_score is not valid

        proxy = result.get('proxy', False)
        vpn = result.get('vpn', False)
        tor = result.get('tor', False)
        active_vpn = result.get('active_vpn', False)
        active_tor = result.get('active_tor', False)
        recent_abuse = result.get('recent_abuse', False)
        bot_status = result.get('bot_status', False)

        # Print the assigned variables
        print(f"Fraud Score: {fraud_score}")
        print(f"Proxy: {proxy}")
        print(f"VPN: {vpn}")
        print(f"TOR: {tor}")
        print(f"Active VPN: {active_vpn}")
        print(f"Active TOR: {active_tor}")
        print(f"Recent Abuse: {recent_abuse}")
        print(f"Bot Status: {bot_status}")

        # Ensure fraud_score is an integer for comparison
        if fraud_score:
            if vpn == False and tor == False:# and active_vpn == False and active_tor == False and fraud_score < 90:
                return True
            else:
                return None
    except requests.RequestException as e:
        print(f"Error retrieving IP data: {e}")
        return None


def mysterium_vpn_connect(server_name, driver):
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.95)
        pyautogui.click(x, y)
        print("mysterium_icon_empty Found")
        time.sleep(5)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/myserium_disconnect.png", region=(1325, 190, 800, 400), confidence=0.95)
            pyautogui.click(x, y)
            print("myserium_disconnect Found")
        except pyautogui.ImageNotFoundException:
            print("No myserium_disconnect .")
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_login.png", region=(1375, 543, 600, 300), confidence=0.99)
            #pyautogui.click(x, y)
            print("mysterium_login Found")
            mysterium_login(driver)
            #return 0
        except Exception as e:
            print("mysterium_logged")
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/quick_connect.png", region=(1325, 190, 800, 400), confidence=0.95)
        
            print("quick_connect Found")
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/search_mysterium.png", region=(1325, 494, 800, 400), confidence=0.95)
                pyautogui.click(x, y)
                print("search_mysterium Found")
                time.sleep(2)
                pyautogui.typewrite(server_name)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.scroll(-500)
                time.sleep(2)
                pyautogui.click(1627, 568)
                return True
            except pyautogui.ImageNotFoundException:
                print("No search_mysterium .")
        except pyautogui.ImageNotFoundException:
            print("No quick_connect .")


    except pyautogui.ImageNotFoundException:
        print("No mysterium_icon_empty .")
    return None


def fix_ip(drive, name):
    ipscore = None
    proxycheck = None
    ip_address = 0
    while not (ipscore and proxycheck):
        ip_address = get_ip(drive)
        ipscore = get_ipscore(ip_address)
        proxycheck = get_proxycheck(drive, ip_address, server_name= name)
        if ipscore and proxycheck == 200:
            print(f'Good IP found: {ip_address}')
            return ip_address
        else:
            print(f'Bad IP detected: {ip_address}. Changing IP...')
            query = {"type": "main"}
            update = {"$set": {"response": f'Changed IP🔴: {ip_address}'}}
            result = collection.update_one(query, update)
            mysterium_vpn_connect(name, drive)
            print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
            time.sleep(5)


def mysterium_web_login(driver):
    driver.open('https://app.mysteriumvpn.com/')
    time.sleep(5)
    for i in range(1,100):
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cookie_icon.png", region=(1625, 43, 400, 300), confidence=0.99)
            pyautogui.click(x, y)
            print("cookie_icon Found")
            time.sleep(3)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/all_site.png", region=(1300, 212, 600, 300), confidence=0.99)
                pyautogui.click(x, y)
                print("all_site Found")
            except pyautogui.ImageNotFoundException:
                print("No all_site .")
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.99)
                pyautogui.click(x, y)
                print("import_icon Found")
                time.sleep(3)
                for i in range(1,50):
                    url = mysterium_raw #"https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie.json"
                    response = requests.get(url)
                    if response.status_code == 200:
                        text_content = response.text
                    else:
                        print(f"Failed to retrieve the content. Status code: {response.status_code}")
                        text_content = None
                    if text_content:
                        pyautogui.click(1385, 310)
                        time.sleep(1)
                        
                        pyautogui.typewrite(text_content)
                        time.sleep(5)
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.99)
                            pyautogui.click(x, y)
                            print("import_icon Found")
                            
                            time.sleep(5)
                            pyautogui.click(113, 100)
                            pyautogui.press('f5')
                            time.sleep(5)
                            #driver.close()
                            return True
                        
                        except pyautogui.ImageNotFoundException:
                            print(f"No import_icon .{i}")
                    time.sleep(1)


            except pyautogui.ImageNotFoundException:
                print("No import_icon .")

        except pyautogui.ImageNotFoundException:
            print("No cookie_icon .")

        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/allow_button.png", region=(1080, 247, 400, 300), confidence=0.99)
            pyautogui.click(x, y)
            print("allow_button Found")
                    
        except pyautogui.ImageNotFoundException:
            print("No allow_button .")
        #driver.close()

def mysterium_login(driver):
    while True:
        titile = sb1.get_title()
        pyautogui.click(113, 100)
        time.sleep(1)
        if 'Home' in titile:

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.99)
                pyautogui.click(x, y)
                print("mysterium_icon_empty Found")
                i = 1
                for i in range(1, 10):
                    time.sleep(1)
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_login.png", region=(1375, 543, 600, 300), confidence=0.99)
                        pyautogui.click(x, y)
                        print("mysterium_login Found")
                        for i in range(1, 10):
                            time.sleep(2)
                            try:
                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_allow.png", region=(842, 750, 400, 300), confidence=0.99)
                                pyautogui.click(x, y)
                                print("mysterium_allow Found")
                                time.sleep(3)
                                try:
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.99)
                                    pyautogui.click(x, y)
                                    print("mysterium_icon_empty 2 Found")
                                    time.sleep(3)
                                    for i in range(1,100):
                                        time.sleep(1)
                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/settings_mysterium.png", region=(1445, 630, 400, 300), confidence=0.99)
                                            pyautogui.click(x, y)
                                            print("settings_mysterium 2 Found")
                                            time.sleep(1)
                                        except pyautogui.ImageNotFoundException:
                                            print("No settings_mysterium 2.")

                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/connection_mysterium_option.png", region=(1325, 109, 800, 900), confidence=0.99)
                                            pyautogui.click(x, y)
                                            print("connection_mysterium_option Found")
                                            time.sleep(1)
                                        except pyautogui.ImageNotFoundException:
                                            print("No connection_mysterium_option.")

                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/refresh_ip_off.png", region=(1325, 109, 800, 900), confidence=0.99)
                                            pyautogui.click(1640, 300)
                                            pyautogui.click(1668, 300)
                                            print("refresh_ip_off Found")
                                            time.sleep(1)
                                        except pyautogui.ImageNotFoundException:
                                            print("No refresh_ip_off.")

                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/refresh_ip_on.png", region=(1325, 109, 800, 900), confidence=0.99)
                                            pyautogui.click(300, 300)
                                            print("refresh_ip_on Found")
                                            return True
                                        except pyautogui.ImageNotFoundException:
                                            print("No refresh_ip_on.")

                                                        #return True
                                except pyautogui.ImageNotFoundException:
                                    print("No mysterium_icon_empty 2.")

                            except pyautogui.ImageNotFoundException:
                                print("No mysterium_allow .")

                    except pyautogui.ImageNotFoundException:
                        print("No mysterium_login .")

                                        
            except pyautogui.ImageNotFoundException:
                print("No mysterium_icon_empty .")
                            #return True
        mysterium_web_login(driver)



def pin_extensions():
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/extension_icon.png", region=(1700, 30, 300, 300), confidence=0.9)
        pyautogui.click(x, y)
        print("extension_icon Button Found")

        for i in range(1,400):
            time.sleep(1)
            pyautogui.moveTo(1700, 30)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/pin.png", region=(1588, 170, 400, 600), confidence=0.9)
                pyautogui.click(x, y)
                pyautogui.moveTo(1700, 30)
                print("pin Button Found")
                time.sleep(1)    
            except pyautogui.ImageNotFoundException:
                print("No pin Button.")
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/all_pinned.png", region=(1588, 170, 400, 600), confidence=0.99)
                pyautogui.moveTo(1700, 40)
                print("all_pinned Button Found")
                return True   
            except pyautogui.ImageNotFoundException:
                print("No all_pinned Button.")
    except pyautogui.ImageNotFoundException:
        print("No extension_icon Button.")
        return False

def install_extensions(extension_name):
    #on chrome://extensions/

    for i in range(1,4):
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/dev_off.png", region=(1700, 95, 300, 300), confidence=0.9)
            pyautogui.click(x, y)
            print("Developer Button Found")
        except pyautogui.ImageNotFoundException:
            print("No Developer Button.")
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/load_unpack.png", region=(2, 100, 400, 400), confidence=0.90)
            pyautogui.click(x, y)
            print("load_unpack Button Found")
            time.sleep(2)
            for i in range(1,100):
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mfv6_unselect.png", region=(388, 260, 300, 300), confidence=0.60)
                    pyautogui.click(x, y)
                    print("mfv6_unselect Button Found")
                        
                except pyautogui.ImageNotFoundException:
                    print("No mfv6_unselect Button.")
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mfv6_select.png", region=(388, 260, 300, 300), confidence=0.90)
                    pyautogui.click(x, y)
                    print("mfv6_select Button Found")
                    #####Select Your Extension
                    extension_path = f"/root/Desktop/MFV6/images/{extension_name}.png" 
                    try:
                        x, y = pyautogui.locateCenterOnScreen(extension_path, region=(545, 200, 500, 500), confidence=0.9)
                        pyautogui.click(x, y)
                        print(f"{extension_path} folder Found")
                        time.sleep(2)
                        pyautogui.click(1467, 123)
                        print(f"{extension_path} folder Installed Complete")
                        return True
                    
                    except pyautogui.ImageNotFoundException:
                        print(f"No {extension_path} folder.")
                except pyautogui.ImageNotFoundException:
                    print("No mfv6_select Button.")
                time.sleep(1)
                print(f'Waiting Seconds:{i}')

        except pyautogui.ImageNotFoundException:
            print("No load_unpack Button.")
    return None





baymack_coins = 0
vnc_url = 0
vnc_window = 0
start_vnc = 0

earnpp_cookie = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/earnpp.json'
feyorra_cookie = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/feyorra.json'
claimcoin_cookie = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/claimcoins.json'


if run_sb1:
    sb1 = Driver(uc=True, headed= True, undetectable= True, undetected=True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
    sb1.maximize_window()
    id1 = get_current_window_id()
    url = "chrome://extensions/"
    sb1.open(url)
    print(sb1.get_title())
    sb1.maximize_window()
    query = {"type": "main"}
    update = {"$set": {"response": 'Browser Configuring...'}}
    result = collection.update_one(query, update)
    update = {"$set": {"request": 'ipfixer'}}
    result = collection.update_one(query, update)
    if result.matched_count > 0:
        print(f"Added new messages to existing document. Updated {result.modified_count} document(s).")
    else:
        print("No document found with the specified type.")
    sb1.maximize_window()

    if fresh >= 3:
        mysterium = install_extensions('mysterium')
        nopecha = install_extensions('nopecha')
        cookie = install_extensions('cookie')
        fingerprint = install_extensions('fingerprint')
        mfhelper = install_extensions('mfhelper')
        if fingerprint and mysterium and nopecha and cookie and mfhelper:
            print('All Extensions are installed..')
            query = {"type": "main"}
            update = {"$set": {"response": 'All Extensions are installed..'}}
            result = collection.update_one(query, update)

    if fresh >= 2:
        if pin_extensions():
            print('All Extensions are pinned')
            query = {"type": "main"}
            update = {"$set": {"response": 'All Extensions are pinned'}}
            result = collection.update_one(query, update)

            if mysterium_login(sb1):
                print('Mysterium Login Done...')
                query = {"type": "main"}
                update = {"$set": {"response": 'Mysterium Login Done...'}}
                result = collection.update_one(query, update)

    if fresh >= 1:            
        #facebook_login()
        sb1.maximize_window()
        query = {"type": "main"}
        update = {"$set": {"response": 'Setup Done...'}}
        result = collection.update_one(query, update)
    
    current_window = sb1.current_window_handle
    all_windows = sb1.window_handles
    for window in all_windows:
        if window != current_window:
            sb1.switch_to.window(window)
            sb1.close()  # Close the tab
    sb1.switch_to.window(current_window)
    #time.sleep(1)
    #ipfixer()
    ip_required = fix_ip(sb1, server_name1)
    ip_address = get_ip(sb1)

def verify_and_claim(sb1):
    # Check if the "Verified!" message exists
    if sb1.is_element_visible('div.hp-bg-success-3'):
        print("Verified! message found.")
        
        # Click the "Claim" button
        if sb1.is_element_visible('button#claimBtn'):
            sb1.click('button#claimBtn')
            print("Claim button clicked.")
        else:
            print("Claim button not found.")
    else:
        print("Verified! message not found.")

def solve_icon_captcha(sb1):
    # Extract the class name of the captcha icon (e.g., "fa-arrow-alt-circle-left")
    captcha_icon_class = sb1.get_attribute('div.captcha-icon', 'class')
    captcha_icon_class = captcha_icon_class.split(' ')[-1]  # Extract only the icon class part

    # Get the available icon options
    icon_options = sb1.find_elements('div#icon-options i.icon-option')

    # Iterate through the options to find the matching icon and click it
    for option in icon_options:
        icon_class = option.get_attribute('class')
        if captcha_icon_class in icon_class:
            option.click()
            print(f"Clicked on the matching icon: {icon_class}")
    time.sleep(1)

    print("No matching icon found.")

def cloudflare(sb):
    try:
        gg = False
        while gg == False:
            try:

                page_title = sb.get_title()
                
                if page_title == 'Just a moment...':
                    sb.disconnect() 
                    try:
                        time.sleep(1)
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.9)
                        print("verify_cloudflare git Found")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.9)
                            pyautogui.click(x, y)
                            time.sleep(5)

                        except Exception as e:
                            print(e)

                    except Exception as e:
                            print(e)
                            time.sleep(2)
                            try:
                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.9)
                                print("verify_cloudflare git Found")
                            except Exception as e:
                                print(e)
                                time.sleep(2)
                                try:
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.9)
                                    print("verify_cloudflare git Found")
                                except Exception as e:
                                    print(e)
                                    time.sleep(2)
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.9)
                                        print("verify_cloudflare git Found")
                                    except Exception as e:
                                        print(e)
                                        pyautogui.press('f5')

                    sb.connect()
                else:
                    gg = True
            except Exception as e:
                print(e)
                gg = True
            
    except Exception as e:
        print(e)


def find_and_click_collect_button(sb1):
    # Selector for the button

    button_selector = 'button.btn.btn-primary.btn-lg.claim-button'
    #hide_ads(sb1)
    # Check if the "Collect your reward" button exists and contains the correct text
    if sb1.is_element_visible(button_selector):
        sb1.execute_script("window.scrollTo(0, 1000);")
        button_text = sb1.get_text(button_selector)
        
        if "Collect your reward" in button_text:
            print("Button with 'Collect your reward' text found.")
            original_window = sb1.current_window_handle
            all_windows_before_click = sb1.window_handles.copy()
            pyautogui.click(350, 200)

            all_windows = sb1.window_handles
            for window in all_windows:
                if window not in all_windows_before_click:
                    print(f"Closing new tab: {window}")
                    sb1.switch_to.window(window)
                    sb1.close()
            sb1.switch_to.window(original_window)
            
            sb1.click(button_selector)
            print("Collect button clicked.")
            return True
        else:
            print("Button found, but it doesn't contain 'Collect your reward' text.")
            return None
    else:
        print("Collect your reward button not found.")
        return None


def add_cookies_with(driver, cookies):
    for i in range(1,100):
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cookie_icon.png", region=(1625, 43, 400, 300), confidence=0.99)
            pyautogui.click(x, y)
            print("cookie_icon Found")
            time.sleep(13)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/all_site.png", region=(1300, 212, 600, 300), confidence=0.99)
                pyautogui.click(x, y)
                print("all_site Found")
            except pyautogui.ImageNotFoundException:
                print("No all_site .")
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.99)
                pyautogui.click(x, y)
                print("import_icon Found")
                time.sleep(3)
                for i in range(1,50):
                    print(url)
                    url = cookies
                    response = requests.get(url)
                    if response.status_code == 200:
                        text_content = response.text
                    else:
                        print(f"Failed to retrieve the content. Status code: {response.status_code}")
                        text_content = None
                    if text_content:
                        pyautogui.click(1385, 310)
                        time.sleep(1)
                        pyautogui.typewrite(text_content)
                        time.sleep(5)
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.99)
                            pyautogui.click(x, y)
                            print("import_icon Found")
                            
                            time.sleep(3)
                            pyautogui.click(113, 100)
                            pyautogui.press('f5')
                            time.sleep(3)
                            #driver.close()
                            return True
                        
                        except pyautogui.ImageNotFoundException:
                            print(f"No import_icon .{i}")
                    time.sleep(1)


            except pyautogui.ImageNotFoundException:
                print("No import_icon .")

        except pyautogui.ImageNotFoundException:
            print("No cookie_icon .")

        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/allow_button.png", region=(1080, 247, 400, 300), confidence=0.99)
            pyautogui.click(x, y)
            print("allow_button Found")
                    
        except pyautogui.ImageNotFoundException:
            print("No allow_button .")


bitmoon_window = None
earnpp_window = None
claimcoin_window = None
feyorra_window = None




    
current_window = sb1.current_window_handle
all_windows = sb1.window_handles
for window in all_windows:
    if window != current_window:
        sb1.switch_to.window(window)
        sb1.close()  # Close the tab
sb1.switch_to.window(current_window)

if earnpp:
    #sb1.open_new_window()
    sb1.uc_open_with_reconnect("https://earn-pepe.com/member/faucet", 5)
    sb1.uc_gui_click_captcha()
    sb1.uc_gui_handle_captcha()
    
    time.sleep(1)
    ggt = sb1.get_title()
    ready = True
    while ready == True:
        time.sleep(1)
        ggt = sb1.get_title()
        if 'Home' in ggt:
            add_cookies_with(sb1, earnpp_cookie)
        elif 'Just' in ggt:
            sb1.uc_gui_click_captcha()
            sb1.uc_gui_handle_captcha()
            cloudflare(sb1)
        elif 'Faucet' in ggt:
            ready = False
        else:
            print(f'{ggt} is wrong')
            sb1.uc_open_with_reconnect("https://earn-pepe.com/member/faucet", 5)
            sb1.uc_gui_click_captcha()
            sb1.uc_gui_handle_captcha()
            

    earnpp_window = sb1.current_window_handle
    print(f"earnpp_window handle: {earnpp_window}")

if feyorra:
    sb1.open_new_window()
    sb1.uc_open_with_reconnect("https://feyorra.site/member/faucet", 5)
    sb1.uc_gui_click_captcha()
    sb1.uc_gui_handle_captcha()

    all_windows = sb1.window_handles
    print(f"All windows: {all_windows}")
    for window in all_windows:
        if window != earnpp_window:
            feyorra_window = window
            break
        
    print(f"feyorra_window window handle: {feyorra_window}")
    sb1.switch_to.window(feyorra_window)

    time.sleep(1)
    ggt = sb1.get_title()

    ready = True
    while ready == True:
        sb1.switch_to.window(feyorra_window)
        time.sleep(1)
        ggt = sb1.get_title()
        if 'Home' in ggt:
            add_cookies_with(sb1, feyorra_cookie)
        elif 'Just' in ggt:
            sb1.uc_gui_click_captcha()
            sb1.uc_gui_handle_captcha()
            cloudflare(sb1)
        elif 'Faucet | Feyorra' in ggt:
            ready = False
        else:
            print(f'{ggt} is wrong')
            sb1.uc_open_with_reconnect("https://feyorra.site/member/faucet", 5)
            sb1.uc_gui_click_captcha()
            sb1.uc_gui_handle_captcha()
            all_windows = sb1.window_handles
            print(f"All windows: {all_windows}")
            for window in all_windows:
                if window != earnpp_window:
                    feyorra_window = window
                    break
                
            print(f"feyorra_window window handle: {feyorra_window}")
            sb1.switch_to.window(feyorra_window)

    all_windows = sb1.window_handles
    print(f"All windows: {all_windows}")

        # Find and assign Baymack window (not matching Popmack window)
    for window in all_windows:
        if window != earnpp_window:
            feyorra_window = window
            break
        
    print(f"feyorra_window window handle: {feyorra_window}")

    sb1.switch_to.window(feyorra_window)
    ggt = sb1.get_title()
    print(f"Title of Baymack window: {ggt}")

if claimcoin:
    sb1.open_new_window()
    sb1.uc_open_with_reconnect("https://claimcoin.in/faucet", 5)
    sb1.uc_gui_click_captcha()
    sb1.uc_gui_handle_captcha()

    all_windows = sb1.window_handles
    print(f"All windows: {all_windows}")
    for window in all_windows:
        if window != earnpp_window or window != feyorra_window:
            claimcoin_window = window
            break
    sb1.switch_to.window(claimcoin_window)
    print(f"claimcoin_window window handle: {claimcoin_window}")
    time.sleep(1)
    ggt = sb1.get_title()

    ready = True
    while ready == True:
        sb1.switch_to.window(claimcoin_window)
        time.sleep(1)
        ggt = sb1.get_title()
        if 'ClaimCoin - MultiCurrency Crypto Earning Platform' in ggt:
            add_cookies_with(sb1, claimcoin_cookie)
        elif 'Just' in ggt:
            sb1.uc_gui_click_captcha()
            sb1.uc_gui_handle_captcha()
            cloudflare(sb1)
        elif 'Faucet | ClaimCoin' in ggt:
            ready = False
        else:
            print(f'{ggt} is wrong')
            sb1.uc_open_with_reconnect("https://claimcoin.in/faucet", 5)
            sb1.uc_gui_click_captcha()
            sb1.uc_gui_handle_captcha()
            all_windows = sb1.window_handles
            print(f"All windows: {all_windows}")
            for window in all_windows:
                if window != earnpp_window or window != feyorra_window:
                    claimcoin_window = window
                    break
            sb1.switch_to.window(claimcoin_window)
            print(f"claimcoin_window window handle: {claimcoin_window}")

    print(f"Title after opening Zaptaps: {ggt}")
        

    all_windows = sb1.window_handles
    print(f"All windows: {all_windows}")

        # Find and assign Baymack window (not matching Popmack window)
    for window in all_windows:
        if window != earnpp_window or window != feyorra_window:
            claimcoin_window = window
            break
        
    print(f"claimcoin_window window handle: {claimcoin_window}")

    sb1.switch_to.window(claimcoin_window)
    ggt = sb1.get_title()
    print(f"Title of Baymack window: {ggt}")

print(f'{earnpp_window} |{feyorra_window}| {claimcoin_window}')



time.sleep(2)
start_time = time.time()
while True:
    try:
        ip_address = get_ip(sb1)
        if ip_address == ip_required:
            if earnpp:
                try:
                    sb1.switch_to.window(earnpp_window)
                    title =sb1.get_title()
                    if 'Faucet' in title:
                        solve_icon_captcha(sb1)
                    elif 'Just' in title:
                        sb1.uc_gui_click_captcha()
                        sb1.uc_gui_handle_captcha()
                        cloudflare(sb1)
                    else:
                        sb1.uc_open_with_reconnect("https://earn-pepe.com/member/faucet", 9)
                        sb1.uc_gui_click_captcha()
                        sb1.uc_gui_handle_captcha()
                        
                        earnpp_window = sb1.current_window_handle
                except Exception as e:
                    print(e)
            if feyorra:
                try:
                    sb1.switch_to.window(feyorra_window)
                    title =sb1.get_title()
                    if 'Faucet' in title:
                        solve_icon_captcha(sb1)
                    elif 'Just' in title:
                        sb1.uc_gui_click_captcha()
                        sb1.uc_gui_handle_captcha()
                        cloudflare(sb1)
                    else:
                        sb1.uc_open_with_reconnect("https://feyorra.site/member/faucet", 9)
                        sb1.uc_gui_click_captcha()
                        sb1.uc_gui_handle_captcha()
                        
                        feyorra_window = sb1.current_window_handle
                except Exception as e:
                    print(e)

            if claimcoin:
                try:
                    elapsed_time = time.time() - start_time
                    seconds_only = int(elapsed_time)
                    if seconds_only > 12:
                        sb1.switch_to.window(claimcoin_window)
                        title =sb1.get_title()
                        if 'Faucet' in title:
                            cc_faucet =  find_and_click_collect_button(sb1)
                            if cc_faucet:
                                start_time = time.time()
                            sb1.switch_to.window(claimcoin_window)
                        elif 'Just' in title:
                            sb1.uc_gui_click_captcha()
                            sb1.uc_gui_handle_captcha()
                            cloudflare(sb1)
                        else:
                            sb1.uc_open_with_reconnect("https://earn-pepe.com/member/faucet", 9)
                            sb1.uc_gui_click_captcha()
                            sb1.uc_gui_handle_captcha()
                            
                            claimcoin_window = sb1.current_window_handle
                        
                except Exception as e:
                    print(e)

        else:
            print('Ip fucked')
            break
            #ip_required = fix_ip(sb1, server_name1)
            #ip_address = get_ip(sb1)
    except Exception as e:
        print(f'Oh Hell No{e}')
