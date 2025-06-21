
print('Version 9.9.9.9.9.8')
import ipaddress
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import requests
import time
from selenium.webdriver.support import expected_conditions as EC
import random
import requests
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
import json
import argparse
import clipboard
import os
import subprocess
import socket
import psutil


query = {"type": "main"}
# Example usage
pyautogui.moveTo(100, 100)
vps_ip = '172.238.101.178'
farm_id =5
print('Farm',farm_id)
fresh = 1 # args.fresh
pyautogui.FAILSAFE = False
from ctypes import wintypes


from pywinauto import Desktop
def focus_and_maximize_window(partial_title):
    try:
        windows = Desktop(backend="uia").windows()
        for win in windows:
            title = win.window_text()
            if partial_title.lower() in title.lower():
                win.set_focus()
                win.maximize()
                print(f"Activated and maximized: {title}")
                return
        print(f"No matching window found for: {partial_title}")
    except Exception as e:
        print(f"Error: {e}")
def get_ip_OS(timeout=10):
    try:
        # Check if DNS and basic connectivity works
        socket.setdefaulttimeout(timeout)
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), timeout)
        s.close()

        # Get public IP from AWS IP check service
        response = requests.get("https://checkip.amazonaws.com/", timeout=timeout)
        ip = response.text.strip()
        print(f"Internet is working. Public IP: {ip}")
        return ip

    except Exception:
        print("No internet connection.")
    return None

ip_address = get_ip_OS()
if ip_address == None:
    for i in range(5):
        ip_address = get_ip_OS()
        if vps_ip == ip_address:
            break

        else:
            focus_and_maximize_window("Mysterium")
            time.sleep(2)
            pyautogui.click(1319, 878)
            time.sleep(4)

CSB1_farms = []
sb1 = None

fb_pass = 'ashen1997'
yt_api_key = 'AIzaSyCoAMmJOYzKhFdLO5oEmwI2Ne7C329jJtg'
mysterium_raw = ""

earnpp_email = 'Nooo'
earnpp_pass = 'Nooo'
feyorra_email = 'Nooo'
feyorra_pass = 'Nooo'
claimc_email = 'yvonne12463@gmail.com'
claimc_pass = 'Uwuinsta@2005'


mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"

client = MongoClient(mongo_uri)
db = client['MoneyFarmV6'] 
collection = db[f'Farm{farm_id}']

collectionbip = db[f'LocalCSB']
quer2y = {"type": "main"}
dochh = collectionbip.find_one(quer2y)
blacklistedIP = dochh["blacklistedIP"]
print(blacklistedIP)


server_name1 = ''
CSB1_farms  = ''
earnpp_email = ''
earnpp_pass = ''
feyorra_email = ''
feyorra_pass = ''
layout = ''

Farm_list = [1, 2, 3]
Farm_list2 = [4, 5]
Farm_list3 = [ 6, 7, 8]
def get_mails_passowrds(farm_id):
    global server_name1
    global CSB1_farms
    global earnpp_email
    global earnpp_pass
    global feyorra_email
    global feyorra_pass
    global layout
    global mysterium_raw
    global Farm_list
    global Farm_list2

    collection = db[f'Farm{farm_id}']
    quer2y = {"type": "main"}
    dochh2 = collection.find_one(quer2y)
    layout = dochh2["withdraw_mail"]
    print(f'Farm ID:{farm_id} | Layout: {layout}')

    if farm_id <= 4:
        mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
    else:

        mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"



    if farm_id == 1:

        if '1' in layout:
            server_name1 = 'thailand'
            CSB1_farms = Farm_list
            earnpp_email = 'mackbinb23@gmail.com'
            earnpp_pass = 'mackbinb23'
            feyorra_email = 'mackbinb23@gmail.com'
            feyorra_pass = 'mackbinb23'

        elif '2' in layout:
            server_name1 = 'thailand' # 'morocco' #'bulgaria'
            CSB1_farms = Farm_list #[6, 7, 8, 9, 10]
            earnpp_email = 'bommetro5@gmail.com'
            earnpp_pass = 'bommetro5'
            feyorra_email = 'bommetro5@gmail.com'
            feyorra_pass = 'bommetro5'
        elif '3' in layout:
            server_name1 = 'thailand' # 'morocco' #'bulgaria'
            CSB1_farms =Farm_list#[6, 7, 8, 9, 10]
            earnpp_email = 'grandkolla19972@gmail.com'
            earnpp_pass = 'grandkolla19972'
            feyorra_email = 'jjona323h123@gmail.com'
            feyorra_pass = 'jjona323h123'

        elif '4' in layout:
            server_name1 = 'thailand'
            CSB1_farms =Farm_list
            earnpp_email = 'gihanfer9076@gmail.com'
            earnpp_pass = 'gihanfer9076'
            feyorra_email = 'gihanfer9076@gmail.com'
            feyorra_pass = 'gihanfer9076'

        elif '5' in layout:
            server_name1 = 'thailand'
            CSB1_farms = Farm_list
            earnpp_email = 'ddilakshi23@gmail.com'
            earnpp_pass = 'ddilakshi23'
            feyorra_email = 'ddilakshi23@gmail.com'
            feyorra_pass = 'ddilakshi23' 
            
        elif '6' in layout:
            server_name1 = 'thailand'
            CSB1_farms = Farm_list
            earnpp_email = 'shemprer@gmail.com'
            earnpp_pass = 'shemprer'
            feyorra_email = 'shemprer@gmail.com'
            feyorra_pass = 'shemprer'

        
        else:
            print('Layout issue', layout)

    elif farm_id == 2:

        if '1' in layout:
            server_name1 = 'poland'
            CSB1_farms = Farm_list
            earnpp_email = 'helenmcnutt6@gmail.com'
            earnpp_pass = 'helenmcnutt6'
            feyorra_email = 'helenmcnutt6@gmail.com'
            feyorra_pass = 'helenmcnutt6'

        elif '2' in layout:
            server_name1 = 'poland' #'portugal'
            CSB1_farms = Farm_list
            earnpp_email = 'gtared666@gmail.com'
            earnpp_pass = 'gtared666'
            feyorra_email = 'gtared666@gmail.com'
            feyorra_pass = 'gtared666'

        elif '3' in layout:
            server_name1 = 'poland' #'portugal'
            CSB1_farms = Farm_list
            earnpp_email = 'grncaptain6@gmail.com'
            earnpp_pass = 'grncaptain6'
            feyorra_email = 'grncaptain6@gmail.com'
            feyorra_pass = 'grncaptain6'
        elif '4' in layout:
            server_name1 = 'poland'
            CSB1_farms = Farm_list
            earnpp_email = 'roxashen97@gmail.com'
            earnpp_pass = 'roxashen97'
            feyorra_email = 'roxashen97@gmail.com'
            feyorra_pass = 'roxashen97'
        elif '5' in layout:
            server_name1 = 'austria'
            CSB1_farms = Farm_list
            earnpp_email = 'oronchu23@gmail.com'
            earnpp_pass = 'oronchu23'
            feyorra_email = 'oronchu23@gmail.com'
            feyorra_pass = 'oronchu23' 
            
        elif '6' in layout:
            server_name1 = 'austria'
            CSB1_farms = Farm_list
            earnpp_email = 'drameson3@gmail.com'
            earnpp_pass = 'drameson3'
            feyorra_email = 'drameson3@gmail.com'
            feyorra_pass = 'drameson3'
        else:
            print('Layout issue', layout)

    elif farm_id == 3:

        if '1' in layout:
            server_name1 = 'france'
            CSB1_farms =Farm_list
            earnpp_email = 'shldmky53@gmail.com'
            earnpp_pass = 'shldmky53'
            feyorra_email = 'shldmky53@gmail.com'
            feyorra_pass = 'shldmky53'

        elif '2' in layout:
            server_name1 = 'france' #'belgium'
            CSB1_farms =Farm_list
            earnpp_email = 'merlelcn666@gmail.com'
            earnpp_pass = 'merlelcn666'
            feyorra_email = 'merlelcn666@gmail.com'
            feyorra_pass = 'merlelcn666'

        elif '3' in layout:
            server_name1 = 'france' #'belgium'
            CSB1_farms = Farm_list
            earnpp_email = 'tanishaamy2500@gmail.com'
            earnpp_pass = 'tanishaamy2500'
            feyorra_email = 'tanishaamy2500@gmail.com'
            feyorra_pass = 'tanishaamy2500'
        elif '4' in layout:
            server_name1 = 'france' #'belgium'
            CSB1_farms =Farm_list
            earnpp_email = 'hayzgonzle5@gmail.com'
            earnpp_pass = 'hayzgonzle5'
            feyorra_email = 'hayzgonzle5@gmail.com'
            feyorra_pass = 'hayzgonzle5'
        elif '5' in layout:
            server_name1 = 'france' #'belgium'
            CSB1_farms =Farm_list
            earnpp_email = 'henndaneys5@gmail.com'
            earnpp_pass = 'henndaneys5'
            feyorra_email = 'henndaneys5@gmail.com'
            feyorra_pass = 'henndaneys5' 
            
        elif '6' in layout:
            server_name1 = 'france'
            CSB1_farms = Farm_list
            earnpp_email = 'sumithrohan2@gmail.com'
            earnpp_pass = 'sumithrohan2'
            feyorra_email = 'sumithrohan2@gmail.com'
            feyorra_pass = 'sumithrohan2'

        else:
            print('Layout issue', layout)

    elif farm_id == 4:

        if '1' in layout:
            server_name1 = 'canada'
            CSB1_farms = Farm_list2
            earnpp_email = 'berendkalpana55@gmail.com'
            earnpp_pass = 'berendkalpana55'
            feyorra_email = 'berendkalpana55@gmail.com'
            feyorra_pass = 'berendkalpana55'
        elif '2' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list2
            earnpp_email = 'neyvon432@gmail.com'
            earnpp_pass = 'neyvon432'
            feyorra_email = 'neyvon432@gmail.com'
            feyorra_pass = 'neyvon432'


        elif '3' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list2
            earnpp_email = 'sheldnkumr86@gmail.com'
            earnpp_pass = 'sheldnkumr86'
            feyorra_email = 'sheldnkumr86@gmail.com'
            feyorra_pass = 'sheldnkumr86'

        elif '4' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list2
            earnpp_email = 'drewaperea@gmail.com' #'andrewperera8@gmail.com'
            earnpp_pass = 'drewaperea'#'andrewperera8'
            feyorra_email = 'drewaperea@gmail.com'#'andrewperera8@gmail.com'
            feyorra_pass = 'drewaperea'#'andrewperera8'
        elif '5' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list2
            earnpp_email = 'howard998@gmail.com'
            earnpp_pass = 'howard998'
            feyorra_email = 'howard998@gmail.com'
            feyorra_pass = 'howard998' 
            
        elif '6' in layout:
            server_name1 = 'canada'
            CSB1_farms = Farm_list2
            earnpp_email = 'amberodum7@gmail.com'
            earnpp_pass = 'amberodum7'
            feyorra_email = 'amberodum7@gmail.com'
            feyorra_pass = 'amberodum7'


        else:
            print('Layout issue', layout)

######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################

    elif farm_id == 5:

        if '1' in layout:
            server_name1 = 'germany'
            CSB1_farms =Farm_list2
            earnpp_email = 'ernestost5@gmail.com' 
            earnpp_pass = 'ernestost5'
            feyorra_email = 'ernestost5@gmail.com'
            feyorra_pass = 'ernestost5'

        elif '2' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms =Farm_list2
            earnpp_email = 'taptioronl8@gmail.com'
            earnpp_pass = 'taptioronl8'
            feyorra_email = 'taptioronl8@gmail.com'
            feyorra_pass = 'taptioronl8'
        elif '3' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms = Farm_list2
            earnpp_email = 'kevincharl3@gmail.com'
            earnpp_pass = 'kevincharl3'
            feyorra_email = 'kevincharl3@gmail.com'
            feyorra_pass = 'kevincharl3'

        elif '4' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms = Farm_list2
            earnpp_email = 'kendleo4@gmail.com'
            earnpp_pass = 'kendleo4'
            feyorra_email = 'kendleo4@gmail.com'
            feyorra_pass = 'kendleo4'

        elif '5' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms =Farm_list2
            earnpp_email = 'llwimisle53@gmail.com'
            earnpp_pass = 'llwimisle53'
            feyorra_email = 'llwimisle53@gmail.com'
            feyorra_pass = 'llwimisle53' 
            
        elif '6' in layout:
            server_name1 = 'germany'
            CSB1_farms = Farm_list2
            earnpp_email = 'adaavery5@gmail.com'
            earnpp_pass = 'adaavery5'
            feyorra_email = 'adaavery5@gmail.com'
            feyorra_pass = 'adaavery5'



    elif farm_id == 6:

        if '1' in layout:
            server_name1 = 'sweden'
            CSB1_farms =Farm_list3
            earnpp_email = 'helmstarr80@gmail.com' 
            earnpp_pass = 'helmstarr80'
            feyorra_email = 'helmstarr80@gmail.com'
            feyorra_pass = 'helmstarr80'

        elif '2' in layout:
            server_name1 = 'sweden' #'chile'
            CSB1_farms =Farm_list3
            earnpp_email = 'debbyemerson@gmail.com'
            earnpp_pass = 'debbyemerson'
            feyorra_email = 'debbyemerson@gmail.com'
            feyorra_pass = 'debbyemerson'
        elif '3' in layout:
            server_name1 = 'sweden' #'chile'
            CSB1_farms = Farm_list3
            earnpp_email = 'marcfink18@gmail.com'
            earnpp_pass = 'marcfink18'
            feyorra_email = 'marcfink18@gmail.com'
            feyorra_pass = 'marcfink18'

        elif '4' in layout:
            server_name1 = 'sweden' #'chile'
            CSB1_farms = Farm_list3
            earnpp_email = 'solanohazel7@gmail.com'
            earnpp_pass = 'solanohazel7'
            feyorra_email = 'solanohazel7@gmail.com'
            feyorra_pass = 'solanohazel7'

        elif '5' in layout:
            server_name1 = 'sweden' #'chile'
            CSB1_farms =Farm_list3
            earnpp_email = 'vadabecerra75@gmail.com'
            earnpp_pass = 'vadabecerra75'
            feyorra_email = 'vadabecerra75@gmail.com'
            feyorra_pass = 'vadabecerra75' 
            
        elif '6' in layout:
            server_name1 = 'sweden'
            CSB1_farms = Farm_list3
            earnpp_email = 'ervinmeyer29@gmail.com'
            earnpp_pass = 'ervinmeyer29'
            feyorra_email = 'ervinmeyer29@gmail.com'
            feyorra_pass = 'ervinmeyer29'



    elif farm_id == 7:

        if '1' in layout:
            server_name1 = 'new zealand'
            CSB1_farms =Farm_list3
            earnpp_email = 'hickssarah4@gmail.com' 
            earnpp_pass = 'hickssarah4'
            feyorra_email = 'hickssarah4@gmail.com'
            feyorra_pass = 'hickssarah4'

        elif '2' in layout:
            server_name1 = 'new zealand' #'chile'
            CSB1_farms =Farm_list3
            earnpp_email = 'ervinleanne8@gmail.com'
            earnpp_pass = 'ervinleanne8'
            feyorra_email = 'ervinleanne8@gmail.com'
            feyorra_pass = 'ervinleanne8'
        elif '3' in layout:
            server_name1 = 'new zealand' #'chile'
            CSB1_farms = Farm_list3
            earnpp_email = 'aidenjarett2@gmail.com'
            earnpp_pass = 'aidenjarett2'
            feyorra_email = 'aidenjarett2@gmail.com'
            feyorra_pass = 'aidenjarett2'

        elif '4' in layout:
            server_name1 = 'new zealand' #'chile'
            CSB1_farms = Farm_list3
            earnpp_email = 'cashspencer2@gmail.com'
            earnpp_pass = 'cashspencer2'
            feyorra_email = 'cashspencer2@gmail.com'
            feyorra_pass = 'cashspencer2'

        elif '5' in layout:
            server_name1 = 'new zealand' #'chile'
            CSB1_farms =Farm_list3
            earnpp_email = 'snowbasil33@gmail.com'
            earnpp_pass = 'snowbasil33'
            feyorra_email = 'snowbasil33@gmail.com'
            feyorra_pass = 'snowbasil33' 
            
        elif '6' in layout:
            server_name1 = 'new zealand'
            CSB1_farms = Farm_list3
            earnpp_email = 'jettweller92@gmail.com'
            earnpp_pass = 'jettweller92'
            feyorra_email = 'jettweller92@gmail.com'
            feyorra_pass = 'jettweller92'


    elif farm_id == 8:

        if '1' in layout:
            server_name1 = 'malaysia'
            CSB1_farms =Farm_list3
            earnpp_email = 'erenyeger688@gmail.com' 
            earnpp_pass = 'erenyeger688'
            feyorra_email = 'erenyeger688@gmail.com'
            feyorra_pass = 'erenyeger688'

        elif '2' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms =Farm_list3
            earnpp_email = 'mcwilliams88@gmail.com'
            earnpp_pass = 'mcwilliams88'
            feyorra_email = 'mcwilliams88@gmail.com'
            feyorra_pass = 'mcwilliams88'
        elif '3' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms = Farm_list3
            earnpp_email = 'aspen769@gmail.com'
            earnpp_pass = 'aspen769'
            feyorra_email = 'aspen769@gmail.com'
            feyorra_pass = 'aspen769'

        elif '4' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms = Farm_list3
            earnpp_email = 'esquivel681@gmail.com'
            earnpp_pass = 'esquivel681'
            feyorra_email = 'esquivel681@gmail.com'
            feyorra_pass = 'esquivel681'

        elif '5' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms =Farm_list3
            earnpp_email = 'marcello184@gmail.com'
            earnpp_pass = 'marcello184'
            feyorra_email = 'marcello184@gmail.com'
            feyorra_pass = 'marcello184' 
            
        elif '6' in layout:
            server_name1 = 'malaysia'
            CSB1_farms = Farm_list3
            earnpp_email = 'whitman34@gmail.com'
            earnpp_pass = 'whitman34'
            feyorra_email = 'whitman34@gmail.com'
            feyorra_pass = 'whitman34'


        else:
            print('Layout issue', layout)
##################################################


    else:
        while True:
            print('SOmething Wrong Did u use --farm')
    print(server_name1)
    print(CSB1_farms)
    print(earnpp_email)
    print(earnpp_pass)
    print(feyorra_email)
    print(feyorra_pass)
    print(layout)
    print(mysterium_raw)


debug_mode = False
get_mails_passowrds(farm_id)
ip_required = 0
#farm_id = 1

run_sb1 = True

chrome_binary_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
chrome_user_data_dir = '/root/.config/google-chrome/'



earnpp = True
claimcoin = False
feyorra = True
earntrump = True
earnbonk = True



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

def insert_data(ip, amount1, amount2, amount3, amount4,accuracy,emailg):
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')

    query = {"type": "main"}
    sample_document = {
        "Email": emailg,
        "pepelom": amount1,
        "feyorramack": amount2,
        "trump": amount3,
        "bonk": amount4,
        "Status": now,
        "Ip": ip,
        "mainfaucet":accuracy,
        "response": 'Running'

        
    }
    update = {"$set": sample_document}
    result = collection.update_one(query, update)      
    if result.modified_count > 0:
        print(f"Updated {result.modified_count} document(s).")
    else:
        print("No document was updated.")
    add_messages('pepelom', {now: amount1})
    add_messages('feyorramack', {now: amount2})
    add_messages('claimcoins', {now: amount3})
    add_messages('bonkmgs', {now: amount4})

    return

def extract_valid_ipv4(text):
    # Remove leading/trailing spaces
    text = text.strip()

    # Regex match for an IPv4 address
    match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)
    if match:
        ip_candidate = match.group()
        try:
            # Validate IP format (ensures each octet is 0–255)
            ipaddress.IPv4Address(ip_candidate)
            return ip_candidate
        except ipaddress.AddressValueError:
            return None
    return None


def get_ip(driver):
    for i in range(5):
        try:
            original_window = driver.current_window_handle
            driver.open_new_window()
            try:
                #driver.switch_to.newest_window()
                #driver.get('https://api.ipify.org/')
                driver.get('https://checkip.amazonaws.com/')
                
                ip_address = driver.get_text('body')
                print('IP =', ip_address)
                ip_address = ip_address.replace(' ', '')
                driver.close()
                driver.connect()
                driver.switch_to.window(original_window)
                if 'This site' in ip_address:
                    time.sleep(1)
                    print('THIS no sign', i)
                    if i == 3:
                        return '27.145.186.4'
                    continue
                ip_address = extract_valid_ipv4(ip_address)
                if ip_address:
                    return ip_address
            
            except Exception as e:
                print(e)
            driver.close() 
            driver.connect()
            driver.switch_to.window(original_window)
        except Exception as e:
            print(e)
    return None



def Full_blacklist_Check(sb1, ip_to_check, current_layout):
    ip_to_check = ip_to_check.replace(' ','')
    ip_address = ip_to_check
    if  vps_ip == ip_address:
        return False
    collectionbip = db[f'LocalCSB']
    #BlackLIST
    quer2y = {"type": "main"}
    dochh = collectionbip.find_one(quer2y)
    black_list = dochh["blacklistedIP"]
    if ip_to_check in black_list:
        response_messege(f'Changed IP : found on blacklist...{ip_to_check}')
        print(f'IP found on blacklist...{ip_to_check}')
        return False


    ipscore = get_ipscore(ip_to_check)
    proxycheck = get_proxycheck(sb1, ip_to_check, server_name= server_name1)
    if ipscore and proxycheck == 200:

        #FxLx List
        quer2y = {"type": "main"}
        dochh = collectionbip.find_one(quer2y)
        fxlx_list = dochh["blacklistedIP2"]

        # Track where the IP is used
        used_in = []

        for layout, ips in fxlx_list.items():
            if ip_to_check in ips:
                used_in.append(layout)
        print(used_in)

        # Output result

        print(f"IP {ip_to_check} is also used in: {', '.join(used_in)}")
        if len(used_in) == 1:
            if current_layout in used_in:
                print('Already Using this')
                response_messege(f'Ready IP :Already Using this {ip_address}')
                print('Good IP')
                return True
            else:
                print('Already USing on another layout...',used_in)
                response_messege(f'Changed IP :Already Using this {used_in}')
                return False
        elif len(used_in) == 0:
            print('Unique IP Found')
            response_messege(f'Ready IP :Unique {ip_address}')
            return True
        else:
            response_messege(f'Changed IP : Duplicate Use...{ip_to_check} | Farms: {len(used_in)}')
            print('Duplicate Use',len(used_in))
        return False
    else:
        response_messege(f'Changed IP : IP Score:{ipscore} | proxycheck:{proxycheck} | IP: {ip_to_check}')
        return False

def get_timezone(ip):
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
            timezone = ip_info.get('timezone')
            print(f"IP Address: {ip_address} \nProxy Status: {proxy_status} \country Status: {country} \nTimezone: {timezone}")
            return timezone
    except requests.RequestException as e:
        print(f"Error retrieving IP address and proxy status: {e}")
 
def get_proxycheck_inbrowser(sb1, ip, server_name):   
    for i in range(9):
        url = f'https://proxycheck.io/v2/{ip}?vpn=1&asn=1'
        val = False
        try:
            original_window = sb1.current_window_handle
            sb1.open_new_window()
            sb1.get(url)
            ip_address_raw = sb1.get_text('body')
            #print("Raw Response:", ip_address_raw)
            ip_address = json.loads(ip_address_raw)
            proxy_status = ip_address[str(ip)]["proxy"]
            country = ip_address[str(ip)]["country"]
            #timezone = ip_address[str(ip)]["timezone"]
    
            print(f"IP Address: {ip} \nProxy Status: {proxy_status} \nCountry: {country}")
            if country.lower() in server_name.lower():
                if proxy_status in 'no' or 'no' in proxy_status:
                    print(f'{country} is valid with proxy status.')
                    val = 200
                else:
                    print(f'{country} is valid with not proxy status.')
                    val = 50
            else:
                print(f'{country} is not {server_name}')
                return 301

            sb1.close()
            sb1.connect()
            sb1.switch_to.window(original_window)
    
            return val
    
        except Exception as e:
            print(f'ibbrowser ProxyCheck Error: {e}')
        time.sleep(2)  # Wait before retrying
 
def get_proxycheck_with_api(driver, ip, server_name):
    for i in range(9):
        url = f'https://proxycheck.io/v2/{ip}?key=434489-84608j-v97020-20y548?vpn=1&asn=1'
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
                    return 301
            elif 'error' in status:
                continue
            else:
                print("Error: Status not OK : Trying Inbrowser Way")
                val = get_proxycheck_inbrowser(driver, ip, server_name)
                if val:
                    return val
        except requests.RequestException as e:
            print(f"Error retrieving IP address and proxy status: {e}")
        time.sleep(2)  # Wait before retrying

def get_proxycheck(driver, ip, server_name):
    for i in range(9):
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
                    return 301
            elif 'error' in status:
                continue
            else:
                print("Error: Status not OK : Trying Inbrowser Way")
                val = get_proxycheck_with_api(driver, ip, server_name)
                if val:
                    return val
        except requests.RequestException as e:
            print(f"Error retrieving IP address and proxy status: {e}")
        time.sleep(2)  # Wait before retrying

 
def get_ipscore(ip):
    url = f'https://ipqualityscore.com/api/json/ip/Bfg1dzryVqbpSwtbxgWb1uVkXLrr1Nzr/{ip}?strictness=3&allow_public_access_points=true&lighter_penalties=true&mobile=true'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
 
        # Debug: Print the full API response
        print("Raw API Response:", result)
 
        # Assign specific data fields to variables with default values
        fraud_score = result.get('fraud_score', 89)  # Default to 89 if missing
        proxy = result.get('proxy', False)
        vpn = result.get('vpn', False)
        tor = result.get('tor', False)
        active_vpn = result.get('active_vpn', False)
        active_tor = result.get('active_tor', False)
 
        # Debug: Print all extracted variables
        print(f"Fraud Score: {fraud_score}")
        print(f"Proxy: {proxy}")
        print(f"VPN: {vpn}")
        print(f"TOR: {tor}")
        print(f"Active VPN: {active_vpn}")
        print(f"Active TOR: {active_tor}")
 
        # Adjusted condition to match expected behavior
        if (
 
            not vpn
            and not tor
        ):
            print("Conditions met: Returning True")
            return True
        else:
            print("Conditions not met: Returning None")
            return None
 
    except requests.RequestException as e:
        print(f"Error retrieving IP data: {e}")
        return None

def fix_ip(drive, name):
    ipscore = None
    proxycheck = None
    ip_address = 0
    
    while True:

        get_mails_passowrds(farm_id)
        ip_address = get_ip_OS()
        if ip_address:
            collection_csb = db[f'Farm{farm_id}']
            query = {"type": "main"}
            doc = collection_csb.find_one(query)
            layout_test = doc["withdraw_mail"]
            if layout_test != layout:
                return
            
            quer2y = {"type": "main"}
            dochh2 = collection.find_one(quer2y)
            layout2 = dochh2["withdraw_mail"]
            lay = re.search(r'\d+', layout2).group()
            other_blacklists = Full_blacklist_Check(drive, ip_address, f'F{farm_id}L{lay}')
            if other_blacklists:
                print(f'Good IP found: {ip_address}')
                return ip_address
            else:
                print(f'Bad IP detected: {ip_address}. Changing IP...1')
                query = {"type": "main"}
                update = {"$set": {"response": f'Changed IP Blacklisted IP🔴: {ip_address}'}}
                result = collection.update_one(query, update)
                for i in CSB1_farms:
                    collection_csb = db[f'Farm{i}']
                    update = {"$set": {"request": 'ipfixer'}}
                    result = collection_csb.update_one(query, update)
                    print('Update Farm', i)
                #mysterium_vpn_connect(name, drive)
                mysteryum_changer(name)
                print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
                time.sleep(5)
        else:
            mysteryum_changer(name)
            print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
            time.sleep(5)
    
 
####################################Control Panel Shit##########################################################
def mysterium_web_login(driver):
    driver.uc_open('https://app.mysteriumvpn.com/')
    time.sleep(5)
    for i in range(1,100):
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cookie_icon.png", region=(1525, 43, 600, 300), confidence=0.99)
            pyautogui.click(x, y)
            print("cookie_icon Found")
            time.sleep(3)
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/all_site.png", region=(1300, 212, 600, 300), confidence=0.99)
                pyautogui.click(x, y)
                print("all_site Found")
            except pyautogui.ImageNotFoundException:
                print("No all_site .")
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.99)
                time.sleep(3)
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.99)
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
                        clipboard.copy(text_content)
                        pyautogui.click(1385, 310)
                        time.sleep(1)
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                        #pyautogui.typewrite(text_content)
                        time.sleep(5)
                        try:
                            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.99)
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
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/allow_button.png", region=(1080, 247, 400, 300), confidence=0.7)
            pyautogui.click(x, y)
            print("allow_button Found")
 
        except pyautogui.ImageNotFoundException:
            print("No allow_button .")
        #driver.close()
 
def ipfixer():
    ip = 0
    preip = 0
    respo = 0
    gg2344 = 0
    query = {"type": "main"}
    update = {"$set": {"request": 'ipfixer'}}
    result = collection.update_one(query, update)
    ready_count = 0
    global layout
    global sb1
    while True:

        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        doc = collection.find_one(query)
        request = doc["request"]
        layout_test = doc["withdraw_mail"]
        if layout_test != layout:
            print(f'Wrong Farm ID | {layout_test} / {layout} ')
            response_messege(f'Wrong Farm ID | {layout_test} / {layout} ')
            try:
                sb1.quit()
                time.sleep(2)
            except Exception as e:
                print(f"sb1.quit() failed: {e}")

            # Fallback kill
            for proc_name in ['chrome', 'chromium']:
                try:
                    subprocess.run(['pkill', '-f', proc_name], check=False, stderr=subprocess.DEVNULL)
                    print(f"All {proc_name} script_seconds_only killed (if any).")
                except Exception as e:
                    print(f"Failed to kill {proc_name} script_seconds_only: {e}")
                    
            time.sleep(2)
            sb1 = open_browsers()
            time.sleep(2)
        if request == 'ipfixer':
            preip = get_ip_OS()
            if preip:
                if ip == preip:
                        sri_lanka_tz = pytz.timezone('Asia/Colombo')
                        utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                        sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                        now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                        print(f'Good IP found: {ip} |{now}')
                        query = {"type": "main"}
                        update = {"$set": {"response": f'Ready IP 🟢: {ip} | {now} | {ready_count} / {len(CSB1_farms)} | {gg2344}/6'}}
                        result = collection.update_one(query, update)
                        print('Result:',result)
                        print(f"repo {respo}")
                        res_farms = []
                        for frm in CSB1_farms:
                            collection_csb = db[f'Farm{frm}']
                            query = {"type": "main"}
                            doc = collection_csb.find_one(query)
                            res = doc["response"]
                            req = doc["request"]
                            if req == 'ipfixer' and 'Ready' in res:
                                res_farms.append(res)
                            elif req == 'ipfixer' and 'Loging' in res:
                                res_farms.append(res)
                            elif req == 'mainscript': #and 'Running' in res:
                                res_farms.append(res)
                            else:
                                print('aiyo', req)
                        ready_count = len(res_farms)
                        print('Ready Count:', ready_count)
                        if len(res_farms) == len(CSB1_farms):
                            time.sleep(5)
                            if gg2344 > 4:
                                return
                            else:
                                gg2344 += 1
                        else:
                            gg2344 = 1
                        time.sleep(5)
                            

                    
                else:
                    respo = 0
                    gg2344 = 0
                    sri_lanka_tz = pytz.timezone('Asia/Colombo')
                    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                    print(now)
                    ip = fix_ip(sb1, server_name1)
                    gg2344 = 0
        else:
            return True

                         
def control_panel():
    try:
        query = {"type": "main"}
        doc = collection.find_one(query)
        request = doc["request"]
        print(request)
        if request == 'ipfixer':
            return 2
        elif request == 'mainscript':
            print(request)
            return 1
        elif request == 'reset':
            print(request)
            return 3
        elif request == 'withdrawpepe':
            print(request)
            return 4
        elif request == 'pause':
            print(request)
            return 5
        elif request == 'withdrawfeyorra':
            print(request)
            return 6
        
        elif request == 'withdrawclaimc':
            print(request)
            return 7
        elif request == 'kill':
            print(request)
            return 8
        
        else:
            print('No function Found to Run')
    except Exception as e:
        print(f"Control Panel Function Exception:{e}")
        ip_address = get_ip_OS()
        if ip_address == None:
            for i in range(5):
                ip_address = get_ip_OS()
                if vps_ip == ip_address:
                    return 10

                else:
                    focus_and_maximize_window("Mysterium")
                    time.sleep(2)
                    pyautogui.click(1319, 878)
                    time.sleep(4)
    return None






#####################################Control Panel Shit##########################################################

# Main function
# Example usage
def mouse_moveclick(cropped_path="element_screenshot.png"):
    try:
        x, y = pyautogui.locateCenterOnScreen(cropped_path, region=(625,183,933,895) ,confidence=0.99)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        return True
    except Exception as e:
        print(f"Error moving and clicking: {e}")

import base64
def save_base64_image(base64_string, filename='output.png'):
    # If the base64 string contains the data URL prefix, strip it
    if base64_string.startswith('data:image'):
        base64_string = base64_string.split(',')[1]

    # Decode and write to file
    image_data = base64.b64decode(base64_string)
    with open(filename, 'wb') as f:
        f.write(image_data)
    print(f"Image saved as {filename}")



import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model('captcha_model_v17.keras')
category_classes_list  =  ['award-solid', 'bell-solid', 'broom-solid', 'bug-solid', 'bullhorn-solid', 'camera-solid', 'cannabis-solid', 'capsules-solid', 'car-burst-solid', 'car-solid', 'carrot-solid', 'cat-solid', 'certificate-solid', 'charging-station-solid', 'chart-line-solid', 'check-solid', 'chess-knight-solid', 'circle-xmark-solid', 'clock-rotate-left-solid', 'couch-solid', 'crow-solid', 'democrat-solid', 'dice-solid', 'dog-solid', 'dove-solid', 'dragon-solid', 'droplet-solid', 'envelope-solid', 'face-surprise-solid', 'face-tired-solid', 'feather-pointed-solid', 'gear-solid', 'gem-solid', 'gift-solid', 'gopuram-solid', 'graduation-cap-solid', 'guitar-solid', 'hammer-solid', 'hat-wizard-solid', 'heart-solid', 'helicopter-solid', 'house-solid', 'image-solid', 'key-solid', 'kiwi-bird-solid', 'laptop-solid', 'leaf-solid', 'lightbulb-solid', 'link-solid', 'lock-solid', 'marker-solid', 'microchip-solid', 'microphone-solid', 'money-bill-wave-solid', 'moon-solid', 'mug-hot-solid', 'mug-saucer-solid', 'music-solid', 'oil-can-solid', 'paw-solid', 'piggy-bank-solid', 'pizza-slice-solid', 'plug-solid', 'puzzle-piece-solid', 'republican-solid', 'ribbon-solid', 'robot-solid', 'rocket-solid', 'rotate-solid', 'satellite-solid', 'scissors-solid', 'screwdriver-wrench-solid', 'ship-solid', 'shuttle-space-solid', 'signal-solid', 'sim-card-solid', 'sitemap-solid', 'skull-crossbones-solid', 'smoking-solid', 'snowman-solid', 'spa-solid', 'spider-solid', 'spoon-solid', 'star-of-david-solid', 'star-solid', 'sun-solid', 'syringe-solid', 'tablets-solid', 'tag-solid', 'temperature-half-solid', 'thermometer-solid', 'thumbs-up-solid', 'thumbtack-solid', 'tooth-solid', 'tractor-solid', 'traffic-light-solid', 'train-subway-solid', 'tree-solid', 'truck-monster-solid', 'truck-pickup-solid', 'umbrella-solid', 'user-solid', 'utensils-solid', 'van-shuttle-solid', 'vector-square-solid', 'vial-solid', 'vials-solid', 'video-solid', 'volleyball-solid', 'xmark-solid', 'yin-yang-solid']

def predict_image_from_list(image_path, category_options):
    #print(f"Predicting image: {image_path}")
    img_size = (50, 45)
    class_names = category_classes_list
    
            # Load and preprocess the image
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Run prediction
    prediction = model.predict(img_array, verbose=0)[0]

    # Map class names to probabilities
    class_probs = {class_names[i]: prediction[i] for i in range(len(class_names))}

    # Filter only the given category options
    filtered = {cat: class_probs.get(cat, 0) for cat in category_options}

    # Sort by confidence
    best_match = max(filtered.items(), key=lambda x: x[1])

    print(f"\n<¯ Predicted Best Match: {best_match[0]} with confidence {best_match[1]:.4f}\n")
    return best_match[0] , best_match[1]

def predict_image(image_path):
    #print(f"Predicting image: {image_path}")
    img_size = (50, 45)

    img = image.load_img(image_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict the class
    prediction = model.predict(img_array)

    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(prediction)

    # Get the predicted class name and confidence score
    predicted_class_name = category_classes_list[predicted_class_index]
    confidence_score = prediction[0][predicted_class_index]  # Confidence score for the predicted class
    print(f"Predicted class: {predicted_class_name} with confidence: {confidence_score:.4f}")
    return predicted_class_name

def save_with_random_number(image_path):
    # Split the filename and extension
    base_name, ext = os.path.splitext(image_path)
    
    # Load the image
    img = Image.open(image_path)
    
    while True:
        # Generate random 3-digit number
        random_number = random.randint(100, 999)
        new_filename = f"element_icons/{base_name}{random_number}{ext}"
        
        # Check if file exists
        if not os.path.exists(new_filename):
            img.save(new_filename)
            print(f"Saved as {new_filename}")
            break
def is_image_width_greater_than_200(image_path):
    try:
        with Image.open(image_path) as img:
            width, _ = img.size
            return width > 200
    except Exception as e:
        print(f"Error checking image width: {e}")
        return False

def click_element_with_mouse(driver, element, duration=0.1):
    """
    Moves the real mouse to the center of a Selenium element and clicks it.
    Automatically adjusts for browser window borders and title bar.

    Args:
        driver: Selenium WebDriver instance.
        element: WebElement to click.
        duration: Duration of mouse movement (default: 0.3s).
    """
    # Get element position and size inside browser viewport

    # Get element position and size
    location = element.location
    size = element.size

    # Calculate the center of the element based on its position and size
    x_center = location['x'] + size['width'] / 2
    y_center = location['y'] + size['height'] / 2

    # Get the browser window offset (title bar, borders)
    offset_x = driver.execute_script("return window.outerWidth - window.innerWidth;")
    offset_y = driver.execute_script("return window.outerHeight - window.innerHeight;")

    # Adjust for the window offset to calculate screen position
    x_center += offset_x / 2
    y_center += offset_y #+ 15

    # Move the mouse to the exact center and click
    pyautogui.moveTo(x_center , y_center, duration=duration)
    pyautogui.click()

captcha_basetring = ''
#V3
#Steps to solve the captcha:
#1. Get the captcha 
def solve_icon_captcha_v3(sb1):
    try:
        print("solve_icon_captcha_v3")

        global captcha_basetring
        script = """
        let xpathExpression = `//form[@method="POST"]//*[contains(@class, "bxs-") or 
            contains(@class, "bx-") or contains(@class, "la-") or 
            contains(@class, "fa-") or contains(@class, "fas fa-") or 
            contains(@class, "far fa-") or contains(@class, "ri-") or 
            contains(@class, "ti ti-") or contains(@class, "bi bi-") or 
            self::img]`;

        // Evaluate XPath expression
        let matchingElements = document.evaluate(xpathExpression, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);

        let filteredElements = [];
        console.log("All matching elements with computed styles:");

        for (let i = 0; i < matchingElements.snapshotLength; i++) {
            let element = matchingElements.snapshotItem(i);
            let style = window.getComputedStyle(element);

            let opacity = parseFloat(style.opacity); // Convert opacity to a number
            let filter = style.filter.trim(); // Trim spaces

            console.log(`Element ${i}:`, element);
            console.log(`  Opacity: ${opacity}`);
            console.log(`  Filter: ${filter}`);

            // Extract opacity from filter if it exists
            let filterOpacityMatch = filter.match(/opacity\(([\d.]+)\)/);
            let filterOpacity = filterOpacityMatch ? parseFloat(filterOpacityMatch[1]) : null;

            // Keep elements where opacity is > 0.5 AND filter opacity (if present) is also > 0.5
            if (opacity > 0.5 && (filterOpacity === null || filterOpacity > 0.5)) {
                filteredElements.push(element);
            }
        }

        console.log("Filtered elements (opacity > 0.5):", filteredElements);

        // Map elements to id/class or src if first element is an img with a src
        let result = filteredElements.map((el, index) => {
            if (index === 0 && el.tagName.toLowerCase() === 'img' && el.src) {
                return el.src;
            }
            return el.id ? `#${el.id}.${el.className}` : `.${el.className}`;
        });

        console.log("Final Result:", result);
        return result;
        """

        # Execute JavaScript and get the filtered elements
        filtered_elements = sb1.execute_script(script)

        # Print each element
        #print("Filtered elements:")
        # Assign the first element to captchaElement
        if len(filtered_elements) < 5:
            captchaElement = filtered_elements[0]
            base64_images2 = [
                "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAToAAAAXCAIAAAAUZRRXAAAACXBI",
                "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV0AAAAXCAIAAAAnXgteAAAACXBI",
            ]


            for base64_image in base64_images2:
                if base64_image in captchaElement:
                    print("Opps Error found in the first list.")
                    pyautogui.press('f5')
                    return False

            return False

        if filtered_elements:
            captchaElement = filtered_elements[0]
            if captcha_basetring != captchaElement:
                #print("\nCaptcha Element:", captchaElement)
                save_base64_image(captchaElement, 'captchaElement.png')
                captcha_basetring = captchaElement
                #save_with_random_number('captchaElement.png')


        to_remove = [
            filtered_elements[0],  # First element
            filtered_elements[1],  # Second element
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none"
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none me-6"  # Specific element"
            "#loginBtnSpinner.fas.fa-spinner.fa-spin.d-none.me-6"
            "#loginBtnSpinner.fas.fa-spinner.fa-spin.d-none.me-1"
        ]

        filtered_elements = [el for el in filtered_elements if el not in to_remove]
        filtered_elements = [el for el in filtered_elements if '#loginBtnSpinner' not in el]
        # Print the final list after removal
        #print("\nFiltered elements after removal:", filtered_elements)
        category_elementss = []
        for item in filtered_elements:
            item = item.replace(' ','.')
            if 'fas.fa' not in item:
                print('no fa fas in ',item)
                continue
            #capture_element_screenshot(sb1, item, screenshot_path="full_screenshot.png", cropped_path=f"cropped_icons/captchaimg{item}.png")
            item_css = item.replace(' ', '.')
            item_filtered = item_css.replace('.fas.fa-', '')
            #item_filtered = item_filtered.replace('-alt', ' ')  
            if item_filtered not in category_classes_list:
                print('new category',item)
                capture_element_screenshot(sb1, item, screenshot_path="full_screenshot.png", cropped_path=f"cropped_icons/captchaimg{item}.png")
                save_with_random_number('captchaElement.png')

            category_elementss.append(item_filtered)
        if is_image_width_greater_than_200('captchaElement.png'):
            print('image is more than 200 width lol')
            #pyautogui.press('f5')
            return False 
        best_match, score = predict_image("captchaElement.png", category_elementss) #captcha_image_filter("captchaElement.png", "cropped_icons")
        print("Best match:", best_match, "score:", score)
        if score < 0.3:
            print("Score is too low, retrying...")
            #save_with_random_number('captchaElement.png')
                #save_with_random_number('captchaElement.png')
        #    return False
        
        for item in filtered_elements:
            item_css = item.replace(' ', '.')
            item_filtered = item_css.replace('.fas.fa-', '')
            #item_filtered = item_filtered.replace('-alt', ' ')  
   
            #item_filtered = item_filtered.replace('shuttle-space', 'rocket')   
            best_match = best_match.replace('shuttle-space', 'rocket')
            if item_filtered in best_match or best_match in item_filtered:
                print(f'Match Valid: {item_css}')
                #capture_element_screenshot(sb1, item_css, screenshot_path="full_screenshot.png", cropped_path=f"cropped_icons/aaaacaptcha.png")
                #mouse_moveclick(cropped_path=f"cropped_icons/aaaacaptcha.png")

                element = sb1.find_element(By.CSS_SELECTOR, item_css)
                click_element_with_mouse(sb1, element, duration=0.1)

                #actions = ActionChains(sb1)
                #actions.move_to_element(element).click().perform()
                return True

        return True

    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False


#V4
#1. Get the captcha 

#V4
#1. Get the captcha 
def solve_icon_captcha(sb1):
    try:
        print("solve_icon_captcha_v4")
        #time.sleep(1)
        global captcha_basetring
        title = sb1.get_title()
        form_selector = 'form[method="POST"]'
        if 'Earn-pepe' in title:
            form_selector = 'form#Claimformx'
        elif 'Feyorra' in title:
            form_selector = 'form#Claimform'
        elif 'Earn-Trump' in title:
            form_selector = 'form#ClaimForm'
        elif 'Earn-Bonk' in title:
            form_selector = 'form#dataform'

        script = f'''
            const form = document.querySelector('{form_selector}');
            if (!form) return [];

            const imgs = form.querySelectorAll('img');
            const base64s = [];

            imgs.forEach(img => {{
                const src = img.src;
                if (src.startsWith("data:image/") && src.includes("base64,")) {{
                    base64s.push(src.split("base64,")[1]);
                }}
            }});

            return base64s;
        '''

        filtered_elements = sb1.execute_script(script)
        #print("Script result:", filtered_elements)

        # Print each element
        #print("Filtered elements:")
        # Assign the first element to captchaElement
        if len(filtered_elements) < 3:
            print('Less Item on list :', len(filtered_elements))
            captchaElement = filtered_elements[0]
            base64_images2 = [
                "iVBORw0KGgoAAAANSUhEUgAAAToAAAAXCAIAAAAUZRRXAAAACXBI",
                "iVBORw0KGgoAAAANSUhEUgAAAV0AAAAXCAIAAAAnXgteAAAACXBI",
                
            ]

            if 'iVBORw0KGgoAAAANSUhEUgAAAV0AAAAXCAIAAAAnXgteAAAACXBI' in captchaElement:
                print("Opps Error found in the first list.")
                pyautogui.press('f5')
                return 201
            

            if "iVBORw0KGgoAAAANSUhEUgAAAToAAAAXCAIAAAAUZRRXAAAACXBI" in captchaElement:
                print("Select Timeout")
                pyautogui.press('f5')
                return 101
            return False

        if filtered_elements:
            captchaElement = filtered_elements[0]
            if captcha_basetring != captchaElement:
                #print("\nCaptcha Element:", captchaElement)
                save_base64_image(captchaElement, 'captchaElement.png')
                captcha_basetring = captchaElement
                #save_with_random_number('captchaElement.png')


        to_remove = [
            filtered_elements[0],  # First element
            filtered_elements[1],  # Second element
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none"
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none me-6"  # Specific element"
            "#loginBtnSpinner.fas.fa-spinner.fa-spin.d-none.me-6"
            "#loginBtnSpinner.fas.fa-spinner.fa-spin.d-none.me-1"
        ]

        filtered_elements = [el for el in filtered_elements if el not in to_remove]
        filtered_elements = [el for el in filtered_elements if '#loginBtnSpinner' not in el]


        category_dic = {}
        category_elementss =[]
        for index, base64_paths in enumerate(filtered_elements):
            #print(f"Index: {index}, Item: {item}")
            save_base64_image(base64_paths, f'Answer_{index}.png')
            best_match = predict_image(f'Answer_{index}.png')
            category_dic[best_match] = base64_paths
            category_elementss.append(best_match)


        if is_image_width_greater_than_200('captchaElement.png'):
            print('image is more than 200 width lol')
            #pyautogui.press('f5')
            return False 
        best_match = ''
        best_match, score = predict_image_from_list("captchaElement.png", category_elementss) #
        print("Best match:", best_match, "score:", score)

        if score < 0.1:
            print("Score is too low")
            #save_with_random_number('captchaElement.png')
            #save_with_random_number('captchaElement.png')
            #return False
            #using it later...for debugging
        
        for item, base64_path in category_dic.items():
            #print(f"{item} Checking")
            if best_match in item or item in best_match:
                #preview = base64_path[:100]
                element = sb1.find_element(By.CSS_SELECTOR, f'img[src*="{base64_path}"]')
                click_element_with_mouse(sb1, element, duration=0.1)
                #capture_element_screenshot(sb1, f'img[src*="{base64_path}"]', screenshot_path="full_screenshot.png", cropped_path=f"aaaacaptcha.png")
                #mouse_moveclick(cropped_path=f"aaaacaptcha.png")
                print('Solved',item )
                return True
            
        print('Something went wrong')
        return False


    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False







import ctypes
import ctypes.wintypes

def get_active_window_title():
    try:
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32
        hwnd = user32.GetForegroundWindow()

        length = user32.GetWindowTextLengthW(hwnd)
        buffer = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buffer, length + 1)

        return buffer.value if buffer.value else None
    except Exception:
        return None


def cloudflare(sb, login = True):
    try:
        page_title = sb.get_title()
        gg = False
        while gg == False:
            if 'Just' in page_title:
                sb.disconnect() 
                for i in range(50):
                    time.sleep(1)
                    gtitle = get_active_window_title()
                    if 'Just' in gtitle:
                                try:
                                    time.sleep(1)
                                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_win10.png", confidence=0.55)
                                    print("verify_cloudflare git Found Just")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.55)
                                        pyautogui.click(x, y)
                                        time.sleep(5)
    
                                    except Exception as e:
                                        print(e)
                                except Exception as e:
                                    print(e)
                    else:
                        sb.connect()
                        gg = True
                        return
                sb.connect()
                return

            else:

                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_win10.png", confidence=0.55)
                    print("verify_cloudflare git Found")
                    if x and y:
                        sb.disconnect() 
                        for i in range(1, 300):
                            page_title = get_active_window_title()
    
                            if 'Login' in page_title or 'Faucetpay' in page_title:
                                try:
                                    time.sleep(1)
                                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_win10.png", confidence=0.55)
                                    print("verify_cloudflare git Found")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.55)
                                        pyautogui.click(x, y)
                                        time.sleep(5)
    
                                    except Exception as e:
                                        print(e)
    
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_success_win10.png", confidence=0.55)
                                        pyautogui.click(x, y)
                                        time.sleep(1)
                                        sb.connect()
                                        return True
    
                                    except Exception as e:
                                        print(e)
                                except Exception as e:
                                    print('cloudflare not found keep trying')
                            else:
                                sb.connect()
                                return
    
                        sb.connect()
                    else:
                        if login == False: 
                            gg = True
                        else:
                            gg = False
                except Exception as e:
                    print(e)
                    gg = True
 
    except Exception as e:
        print(e)
 


def cloudflare_dark(sb, login = True):
    try:
        page_title = sb.get_title()
        gg = False
        while gg == False:
            if 'Just' in page_title:
                sb.disconnect() 
                for i in range(50):
                    time.sleep(1)
                    gtitle = get_active_window_title()
                    if 'Just' in gtitle:
                                try:
                                    time.sleep(1)
                                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_dark.png", confidence=0.7)
                                    print("verify_cloudflare git Found Just")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_dark.png", confidence=0.7)
                                        pyautogui.click(x, y)
                                        time.sleep(5)
    
                                    except Exception as e:
                                        print(e)
                                except Exception as e:
                                    print(e)
                    else:
                        sb.connect()
                        gg = True
                        return
                sb.connect()
                return

            else:

                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_dark.png", confidence=0.7)
                    print("verify_cloudflare git Found")
                    if x and y:
                        sb.disconnect() 
                        for i in range(1, 300):
                            #pyautogui.moveTo(100, 200)
    
                            if 'Login' in page_title or 'Faucet' in page_title:
                                try:
                                    time.sleep(1)
                                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_dark.png", confidence=0.7)
                                    print("verify_cloudflare git Found")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_dark.png", confidence=0.7)
                                        pyautogui.click(x, y)
                                        time.sleep(5)
    
                                    except Exception as e:
                                        print(e)
    
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_success_dark.png", confidence=0.7)
                                        pyautogui.click(x, y)
                                        time.sleep(1)
                                        sb.connect()
                                        return True
    
                                    except Exception as e:
                                        print(e)
                                except Exception as e:
                                    print('cloudflare not found keep trying')
                            else:
                                sb.connect()
                                return
    
                        sb.connect()
                    else:
                        if login == False: 
                            gg = True
                        else:
                            gg = False
                except Exception as e:
                    print(e)
                    gg = True
 
    except Exception as e:
        print(e)

def previous_script_seconds_cal(pre_g,gg):
    total_str, added_str = pre_g.split(' | ')
    total = int(total_str)
    added = int(added_str)

    # Add the new seconds
    new_total = total + gg

    # Format the result
    result = f'{new_total} | {gg}'
    return result


#Driver Method
def login_to_faucet_old(url, driver, email, password, captcha_image, restrict_pages, submit_button, ip_required):

    driver.uc_open(url)
    time.sleep(2)

    all_windows = driver.window_handles
    for window in all_windows:
        if window not in restrict_pages:
            driver.switch_to.window(window)
            
    print("WebDriver Check")
    current_title = driver.get_title()
    print(f"Current g title: {current_title}")
    if 'Login' in current_title:
        # Wait for the email input by type attribute
        email_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        email_input.send_keys(email)

        # Locate the password input by type attribute
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        password_input.send_keys(password)

        # Step 3: Wait for the CAPTCHA checkbox to be validated
        print("CAPTCHA Check")
        if captcha_image:
                for i in range(1, 10):
                    time.sleep(1)
                    #pyautogui.moveTo(100, 200)

                    sb1.execute_script("window.scrollTo(0, 1000);")
                    cloudflare(driver, True)
                    ip_address = get_ip_OS()
                    if ip_required != ip_address:
                        print("IP address mismatch, login")
                        return False
                    all_windows = driver.window_handles
                    for window in all_windows:
                        if window not in restrict_pages:
                            driver.switch_to.window(window)
                    try:
                        x, y = pyautogui.locateCenterOnScreen(f"C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/{captcha_image}.png", confidence=0.85)
                        if x and y: 
                            if 'Feyorra' in current_title:

                                mouse_moveclick(cropped_path="C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/feyorra_loginbt.png")
                                time.sleep(1)
                                #pyautogui.click(943 ,788)
                                #x:943 y:788
                                time.sleep(5)
     
                            #if driver.is_element_visible(submit_button):
                            #    sb1.uc_click(submit_button)
                            #element = sb1.find_element(By.CSS_SELECTOR, submit_button)
                            #click_element_with_mouse(sb1, element, duration=0.2)
                            capture_element_screenshot(sb1, submit_button, screenshot_path="full_screenshot.png", cropped_path=f"login_buttong.png")
                            mouse_moveclick(cropped_path=f"login_buttong.png")
                            time.sleep(5)
                            return
                    except Exception as e:
                        print(f'ERR:{e}') 


        print("✅ CAPTCHA validated")
        #click_element_with_pyautogui(sb1, 'button[type="submit"]')
        #pyautogui.press('enter')
        if driver.is_element_visible(submit_button):
            sb1.uc_click(submit_button)
        
        time.sleep(3)
        print("🚀 Login attempt made!")
    

def cloudflare_without_driver():
    for i in range(100):
        gtitle = get_active_window_title()
        if 'Login' in gtitle:
            try:
                time.sleep(1)
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_win10.png", confidence=0.55)
                print("verify_cloudflare git Found")
                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_box_win10.png", confidence=0.55)
                    pyautogui.click(x, y)
                    time.sleep(5)

                except Exception as e:
                    print(e)

                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cloudflare_success_win10.png", confidence=0.55)
                    pyautogui.click(x, y)
                    time.sleep(1)
                    return True

                except Exception as e:
                    print(e)
            except Exception as e:
                print('cloudflare not found keep trying')
        else:
            return

#OS Level Method
def Fill_mailpass_faucets(sitekey, email, password):
    if 'Earn-pepe' in sitekey:
        pyautogui.click(852, 430)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(email)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.click(812, 516)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(password)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/pepe_login.png",confidence=0.5)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            return True
        except Exception as e:
            print(f"Error moving and clicking: {e}")
        pyautogui.press('enter')
        
    if 'Feyorra' in sitekey:
        pyautogui.click(883, 316)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(email)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.click(810, 397)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(password)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/feyorra_loginbt.png",confidence=0.5)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            return True
        except Exception as e:
            print(f"Error moving and clicking: {e}")
        pyautogui.press('enter')

    if 'Earn-Trump' in sitekey:
        pyautogui.click(883, 385)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(email)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.click(810, 473)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(password)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/trump_login.png",confidence=0.5)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            return True
        except Exception as e:
            print(f"Error moving and clicking: {e}")
        pyautogui.press('enter')

    if 'Earn-Bonk' in sitekey:
        pyautogui.click(883, 418)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(email)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.click(810, 534)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        time.sleep(1)
        clipboard.copy(password)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/bonk_login.png",confidence=0.5)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            return True
        except Exception as e:
            print(f"Error moving and clicking: {e}")
        pyautogui.press('enter')

#OS level
def login_to_faucet(url, driver, email, password, captcha_image, restrict_pages, submit_button, ip_required):
    ##new tab open
    pyautogui.hotkey('ctrl','t')
    time.sleep(2)
    #Paste Link
    pyautogui.hotkey('ctrl','l')
    time.sleep(2)
    pyautogui.typewrite(url)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    for i in range(5):
        time.sleep(1)
        current_title =get_active_window_title()
        print(f"Current login title: {current_title}")
        if 'Login' in current_title:
            #Login Found
            cloudflare_without_driver()
            time.sleep(1)
            for frm in CSB1_farms:
                collection_csb = db[f'Farm{frm}']
                query = {"type": "main"}
                doc = collection_csb.find_one(query)
                res = doc["response"]
                req = doc["request"]
                if req == 'ipfixer':
                    if 'Changed' in res:
                        print('IP is BAD HANLDE SITE')
                        return 404
            Fill_mailpass_faucets(current_title, email, password)
            time.sleep(3)
        if 'Dashboard' in current_title:
            pyautogui.hotkey('ctrl','w')
            return True





earnpp_window = None
claimcoin_window = None
feyorra_window = None
baymack_window = None
feyorratop_window = None
earntrump_window = None
earnbonk_window = None

def close_extra_windows(driver, keep_window_handles):
    closed_any = False
    #print('Closing Tabs')
    # Always re-query handles, in case they shift when you close one:
    for handle in list(driver.window_handles):
        # If this handle should be kept, skip it:
        if handle in keep_window_handles:
            continue
        # If closing this would leave zero windows, bail out:
        if len(driver.window_handles) <= 1:
            break
        driver.switch_to.window(handle)
        driver.close()
        closed_any = True

    # Switch back to your original “main” window at the end
    # (but only if it still exists):
    if keep_window_handles and keep_window_handles[0] in driver.window_handles:
        driver.switch_to.window(keep_window_handles[0])
    #print('Closed Stats:', closed_any)
    return closed_any

def handle_captcha_and_cloudflare(driver):
    cloudflare(driver, login = False)

def handle_site(driver, url, expected_title, not_expected_title , function, window_list ,ip_required, ip_check = False):
    driver.uc_open(url)
    ready = False
    while not ready:
        print('Handle Site....')
        time.sleep(1)
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        
        for frm in CSB1_farms:
            collection_csb = db[f'Farm{frm}']
            query = {"type": "main"}
            doc = collection_csb.find_one(query)
            res = doc["response"]
            req = doc["request"]
            if req == 'ipfixer':
                if 'Changed' in res:
                    print('IP is BAD HANLDE SITE')
                    return 404
        quer2y = {"type": "main"}
        dochh2 = collection.find_one(quer2y)
        layout_test = dochh2["withdraw_mail"]
        if layout_test != layout:
            return 404
        
        all_windows = driver.window_handles
        for window in all_windows:
            if window not in window_list:
                driver.switch_to.window(window)
                time.sleep(1)
        print("WINDOW LIST:", window_list)
        print("CURRENT LIST:", all_windows)
        print('Switch:',window)
        if ip_check:
            driver.uc_open(url)
        time.sleep(1)
        current_title = driver.get_title()
        print(f"Current title: {current_title}")
        if "Google" in current_title:
            return 404
        

        get_mails_passowrds(farm_id)


        if not_expected_title in current_title:
            print(f"{current_title} is not the expected title. Reconnecting...")
            if window_list:
                print('error 405')
                login_faucet_detect = True
                return 405

            if function == 1:
                sb1.disconnect()
                time.sleep(2)
                login_to_faucet('https://earn-pepe.com/login', sb1, earnpp_email, earnpp_pass, 'cloudflare_success', window_list, 'button#ClaimBtn', ip_required = ip_required)
                sb1.connect()
                time.sleep(3)
            elif function == 2:
                sb1.disconnect()
                time.sleep(2)
                login_to_faucet('https://feyorra.site/login', sb1, feyorra_email, feyorra_pass, 'cloudflare_success', window_list, 'button#ClaimBtn',ip_required = ip_required)
                sb1.connect()

                time.sleep(3)
            elif function == 3:
                sb1.disconnect()
                time.sleep(2)
                login_to_faucet('https://earn-trump.com/login', sb1, earnpp_email, earnpp_pass,  'cloudflare_success', window_list, 'button#ClaimBtn', ip_required = ip_required)
                sb1.connect()

                time.sleep(3)
            elif function == 4:
                sb1.disconnect()
                time.sleep(2)
                login_to_faucet('https://earn-bonk.com/login', sb1, feyorra_email, feyorra_pass,  'cloudflare_success', window_list, 'button#ClaimBtn', ip_required = ip_required)
                sb1.connect()

                time.sleep(3)
            time.sleep(1)
            continue
        elif expected_title in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Lock' in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Maintenance' in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Just a moment' in current_title:
            print('Just a fff')
            handle_captcha_and_cloudflare(driver)
        
        else:
            print(f"{current_title} is not the expected title. Reconnecting...")
            all_windows = driver.window_handles
            for window in all_windows:
                if window not in window_list:
                    driver.switch_to.window(window)
            driver.uc_open(url)
            print("WINDOW LIST2:", window_list)
            print("CURRENT LIST2:", all_windows)
            print('Switch2:',window)
    print('Site fine Return to Function')
    return driver.current_window_handle


def pin_extensions():
    try:
        x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/extension_icon.png", region=(1234, 30, 683, 522), confidence=0.9)
        pyautogui.click(x, y)
        print("extension_icon Button Found")

        for i in range(1,50):
            time.sleep(1)
            pyautogui.moveTo(1700, 30)
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/pin.png", region=(1234, 30, 683, 522), confidence=0.9)
                pyautogui.click(x, y)
                pyautogui.moveTo(1700, 30)
                print("pin Button Found")
                time.sleep(1)    
            except pyautogui.ImageNotFoundException:
                print("No pin Button.")
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/all_pinned.png", region=(1234, 30, 683, 522), confidence=0.99)
                pyautogui.moveTo(1700, 40)
                print("all_pinned Button Found")
                return True   
            except pyautogui.ImageNotFoundException:
                print("No all_pinned Button.")
        return False
    except pyautogui.ImageNotFoundException:
        print("No extension_icon Button.")
        return False


def install_extensions(extension_name):
    #on chrome://extensions/

    for i in range(1,4):
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/dev_off.png", region=(1700, 95, 300, 300), confidence=0.9)
            pyautogui.click(x, y)
            print("Developer Button Found")
        except pyautogui.ImageNotFoundException:
            print("No Developer Button.")
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/load_unpack.png", region=(2, 100, 400, 400), confidence=0.90)
            pyautogui.click(x, y)
            print("load_unpack Button Found")
            time.sleep(2)
            for i in range(1,100):
                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/mfv6_unselect_nomachine_paths.png", region=(388, 260, 300, 300), confidence=0.70)
                    pyautogui.click(x, y)
                    print("mfv6_unselect Button Found")
                    time.sleep(1)
                        
                except pyautogui.ImageNotFoundException:
                    print("No mfv6_unselect Button.")
                #####Select Your Extension
                extension_path = f"C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/{extension_name}_nomachine_paths.png" 
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

                time.sleep(1)
                print(f'Waiting Seconds:{i}')

        except pyautogui.ImageNotFoundException:
            print("No load_unpack Button.")
    return None


def remove_border(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Define the border size to be removed
    border_size = 2
    
    # Calculate new dimensions
    width, height = image.size
    new_width = width - 2 * border_size
    new_height = height - 2 * border_size
    
    # Crop the image to remove the border
    cropped_image = image.crop((border_size, border_size, width - border_size, height - border_size))
    
    # Save the cropped image
    cropped_image.save(output_path)
    print(f"Image saved without border at: {output_path}")

def response_messege(response):
    query = {"type": "main"}
    update = {"$set": {"response": response}}
    result = collection.update_one(query, update)


def get_coins(driver, sitekey):
    coins = None
    title =sb1.get_title()
    try:
        driver.execute_script("window.scrollTo(0, 0);")
        if sitekey == 1 and 'Earn-pepe' in title:
            if driver.is_element_present('small span span'):
                select_element = driver.find_element('css selector', 'small span span')
                selected_text = select_element.text.strip()  # Extract and clean the text
                coins = selected_text
            else:
                print(f'Sitekey:{sitekey} not found')

        if sitekey == 1 and 'Earn-Trump' in title:
            if driver.is_element_present('li a span span span'):
                select_element = driver.find_element('css selector', 'li a span span span')
                selected_text = select_element.text.strip()  # Extract and clean the text
                coins = selected_text
            else:
                print(f'Sitekey:{sitekey} not found')
            #coins = float(coins.split()[0]) 
        if sitekey == 2:
            if driver.is_element_present('li a span span'):
                select_element = driver.find_element('css selector', 'li a span span')
                selected_text = select_element.text.strip()  # Extract and clean the text
                coins = selected_text

            #if driver.is_element_present('select'):
            #    select_element = driver.find_element('css selector', 'select.form-select option[selected]')  # Locate the selected option
            #    selected_text = select_element.text.strip()  # Extract and clean the text
            #    print(f"Selected option text: {selected_text}")
            #    coins = selected_text
            else:
                print(f'Sitekey:{sitekey} not found')
        if sitekey == 3:
            if driver.is_element_present('div.col-md-6.col-xl-3:nth-child(4) p.lh-1.mb-1.font-weight-bold'):
                coins = driver.get_text('div.col-md-6.col-xl-3:nth-child(4) p.lh-1.mb-1.font-weight-bold', timeout= 1)
            else:
                print(f'Sitekey:{sitekey} not found')

        debug_messages(f'SiteKey{sitekey}{coins}')
        if '/' in coins and sitekey == 3:
            numerator = coins.split('/')[0]
            return numerator

        numeric_value = re.search(r"\d+\.\d+", coins)
        if numeric_value:
            debug_messages(f'SiteKey{sitekey}{coins}')
            return float(numeric_value.group())
        return False
    except Exception as e:
        print(f"ERR on Getcoin:{sitekey} | {e}")
        pyautogui.press('enter')
    return False



def capture_element_screenshot(driver, selector, screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png"):
    try:
        # Step 1: Find the element using SeleniumBase
        element = driver.find_element(selector)
    
        # Step 3: Capture the full-page screenshot
        driver.save_screenshot(screenshot_path)
    
        # Step 4: Re-fetch the element after scrolling
        element = driver.find_element(selector)
        location = element.location
        size = element.size
    
        # Step 5: Load the full screenshot with Pillow
        screenshot = Image.open(screenshot_path)
        scroll_y = driver.execute_script("return window.scrollY;")
    
        # Step 6: Calculate the crop area
        left = int(location['x'])
        top = int(location['y'] - scroll_y)
        right = int(left + size['width'])
        bottom = int(top + size['height'])
    
        print(f"Crop area: left={left}, top={top}, right={right}, bottom={bottom}")
    
        # Step 7: Crop the image to the element's size
        cropped_image = screenshot.crop((left, top, right, bottom))
    
        # Step 8: Save the cropped image
        cropped_image.save(cropped_path)
        print(f"Cropped screenshot saved at {cropped_path}")
    except Exception as e:
        print(f"Error capturing element screenshot: {e}")

    
#V2 Withdraw Function
def withdraw_faucet(driver, sitekey):
    try:
        global faucetlayout
        collectionbip = db[f'LocalCSB']
        quer2y = {"type": "main"}
        dochh = collectionbip.find_one(quer2y)
        currency = dochh["currency"]
        driver.open_new_window()
        current_window = driver.current_window_handle

        close_extra_windows(sb1, [current_window])
        driver.switch_to.window(current_window)
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        time.sleep(5)
        #Earn PePe
        driver.open('https://earn-pepe.com/member/faucetpay')
        time.sleep(8)
        title = driver.get_title()
        print(title)
        if 'Just' in title:
            cloudflare(driver, login = False)
        elif 'Faucetpay' in title:
            driver.execute_script("""const element = document.querySelector('button#ClaimBtn'); 
                const rect = element.getBoundingClientRect();
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const offset = rect.bottom + scrollTop + 20 - window.innerHeight;
                window.scrollTo({
                top: offset > 0 ? offset : 0,
                behavior: 'smooth'
                });
                """)
            time.sleep(1)
            driver.execute_script("""(function() {
                    const priorityCoins = ["SOL", "LTC", "DOGE", "TRX", "PEPE"];
                    const cards = document.querySelectorAll("form#wdform .card");
                    let selected = false;

                    for (let coin of priorityCoins) {
                        for (let card of cards) {
                            try {
                                const input = card.querySelector("input[type='radio']");
                                const coinCode = input.getAttribute("data-coincode");
                                if (coinCode !== coin) continue;

                                const percentText = card.querySelector("small.fw-bold").textContent.trim().replace('%', '');
                                const percent = parseFloat(percentText);

                                console.log(`${coinCode}: ${percent}%`);

                                if (percent > 15) {
                                    input.click();
                                    console.log(` Clicked ${coinCode} radio button`);
                                    selected = true;
                                    break;
                                }
                            } catch (e) {
                                console.warn(`L Error processing ${coin}:`, e);
                            }
                        }
                        if (selected) break;
                    }

                    if (!selected) {
                        console.log("W None of the priority coins have availability above 9%");
                    }
                })();
                """)
            time.sleep(1)
            cloudflare(driver, login = True)
            time.sleep(2)
            driver.uc_click('button#ClaimBtn')
            time.sleep(10)
            response_messege(f'EarnPP FaucetPay Withdrawed')
###########################################################################
        #Feyorra
        driver.open('https://feyorra.site/member/faucetpay')
        time.sleep(8)
        title = driver.get_title()
        print(title)
        if 'Just' in title:
            cloudflare(driver, login = False)
        elif 'Faucetpay' in title:
            driver.execute_script("""const element = document.querySelector('button#ClaimBtn'); 
                const rect = element.getBoundingClientRect();
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const offset = rect.bottom + scrollTop + 20 - window.innerHeight;
                window.scrollTo({
                top: offset > 0 ? offset : 0,
                behavior: 'smooth'
                });
                """)
            time.sleep(1)
            driver.execute_script("""(function () {
                    const priorityCoins = ["SOL", "LTC", "DOGE", "TRX", "PEPE"];
                    const coinCards = document.querySelectorAll("form#FPwithdraw .card-body");
                    let selected = false;

                    for (let coin of priorityCoins) {
                        for (let card of coinCards) {
                            try {
                                const input = card.querySelector("input[type='radio']");
                                const coinCode = input.getAttribute("data-coincode");
                                if (coinCode !== coin) continue;

                                const percentSpan = card.querySelector("span.fw-bold");
                                const percentText = percentSpan?.textContent.trim().replace('%', '') || "0";
                                const percent = parseFloat(percentText);

                                console.log(`${coinCode}: ${percent}%`);

                                if (percent > 15) {
                                    input.click();
                                    console.log(` Clicked ${coinCode} radio button`);
                                    selected = true;
                                    break;
                                }
                            } catch (err) {
                                console.warn(`L Error processing ${coin}:`, err);
                            }
                        }
                        if (selected) break;
                    }

                    if (!selected) {
                        console.log("W None of the priority coins have availability above 9%");
                    }
                })();

                """)
            time.sleep(1)
            cloudflare(driver, login = True)
            time.sleep(2)
            driver.uc_click('button#ClaimBtn')
            time.sleep(10)
            response_messege(f'Fey FaucetPay Withdrawed')

###########################################################################
        #Earn Trump
        driver.open('https://earn-trump.com/member/faucetpay')
        time.sleep(8)
        title = driver.get_title()
        print(title)
        if 'Just' in title:
            cloudflare(driver, login = False)
        elif 'Faucetpay' in title:
            driver.execute_script("""const element = document.querySelector('button#ClaimBtn'); 
                const rect = element.getBoundingClientRect();
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const offset = rect.bottom + scrollTop + 20 - window.innerHeight;
                window.scrollTo({
                top: offset > 0 ? offset : 0,
                behavior: 'smooth'
                });
                """)
            time.sleep(1)
            driver.execute_script("""(function () {
                const priorityCoins = ["SOL", "LTC", "DOGE", "TRX"];
                const cards = document.querySelectorAll("#wdform .card");
                let selected = false;

                for (let coin of priorityCoins) {
                    for (let card of cards) {
                        try {
                            const input = card.querySelector("input[type='radio']");
                            const coinCode = input?.getAttribute("data-coincode");
                            if (coinCode !== coin) continue;

                            const progress = card.querySelector(".progress-bar");
                            const percent = parseFloat(progress.getAttribute("aria-valuenow"));

                            console.log(`${coinCode}: ${percent}%`);

                            if (percent > 15) {
                                input.click();
                                console.log(` Clicked ${coinCode} radio button`);
                                selected = true;
                                break;
                            }
                        } catch (e) {
                            console.warn(`L Error processing ${coin}:`, e);
                        }
                    }
                    if (selected) break;
                }

                if (!selected) {
                    console.log("W None of the priority coins have availability above 9%");
                }
            })();


                """)
            time.sleep(1)
            cloudflare(driver, login = True)
            time.sleep(2)
            driver.uc_click('button#ClaimBtn')
            time.sleep(10)
            response_messege(f'Trump FaucetPay Withdrawed')
###########################################################################
        #Earn bonk
        driver.open('https://earn-bonk.com/member/faucetpay')
        time.sleep(8)
        title = driver.get_title()
        print(title)
        if 'Just' in title:
            cloudflare(driver, login = False)
        elif 'Faucetpay' in title:
            driver.execute_script("""const element = document.querySelector('button#ClaimBtn'); 
                const rect = element.getBoundingClientRect();
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
                const offset = rect.bottom + scrollTop + 20 - window.innerHeight;
                window.scrollTo({
                top: offset > 0 ? offset : 0,
                behavior: 'smooth'
                });
                """)
            time.sleep(1)
            driver.execute_script("""(function() {
                const priorityCoins = ["SOL", "LTC", "DOGE", "TRX"];
                const cards = document.querySelectorAll("form#wdform .card");
                let selected = false;

                for (let coin of priorityCoins) {
                    for (let card of cards) {
                        try {
                            const input = card.querySelector("input[type='radio']");
                            const coinCode = input.getAttribute("data-coincode");
                            if (coinCode !== coin) continue;

                            const percentText = card.querySelector("span.fw-bold.ms-5").textContent.trim().replace('%', '');
                            const percent = parseFloat(percentText);

                            console.log(`${coinCode}: ${percent}%`);

                            if (percent > 15) {
                                input.click();
                                console.log(` Clicked ${coinCode} radio button`);
                                selected = true;
                                break;
                            }
                        } catch (e) {
                            console.warn(`L Error processing ${coin}:`, e);
                        }
                    }
                    if (selected) break;
                }

                if (!selected) {
                    console.log("W None of the priority coins have availability above 9%");
                }
            })();



                """)
            time.sleep(1)
            cloudflare(driver, login = True)
            time.sleep(2)
            driver.uc_click('button#ClaimBtn')
            time.sleep(10)
            response_messege(f'BONK FaucetPay Withdrawed')
        query = {"type": "main"}
        update = {"$set": {"request": 'mainscript'}}
        result = collection.update_one(query, update)
    except Exception as e:
        print(f'ERR on withdraw{e}')
        response_messege(f'FaucetPay ERR on withdraw{e}')


 


def faucet_limit_check(driver, sitekey):
    try:
        if driver.is_text_visible('Limit Reached, Comeback Again Tomorrow!'):
            pass
    except Exception as e:
        print(f'LIMITG:ERR{e}')
# Main logic

reset_count = 0
reset_count_isacc = 0
previous_reset_count = 0

start_time = 0
start_time3 = 0
earnpp_coins = None
feyorra_coins = None
claimc_coins = None
earntrump_coins = None
earnbonk_coins = None

earnpp_coins_pre = None
feyorra_coins_pre = None
earnbonk_coins_pre = None
earntrump_coins_pre = None
claimc_coins_pre = None
earnpp_limit_reached = None
feyorra_limit_reached = None
earntrump_limit_reached = None
earnbonk_limit_reached = None
#if run_sb1:

def are_extensions_exist():
    all_extensions_not = True
    for i in range(3):
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/cookie_icon.png", region=(1225, 33, 755, 400), confidence=0.9)
            #pyautogui.click(x, y)
            print("extension_icon Button Found")
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/mysterium_icon_empty.png", region=(1225, 33, 755, 400), confidence=0.95)
                #pyautogui.click(x, y)
                print("mysterium_icon_emptyf Button Found")
                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_dis_icon.png", region=(1225, 33, 755, 400), confidence=0.95)
                    #pyautogui.click(x, y)
                    print("sweet_dis_icon Button Found")
                    all_extensions_not = False

                except pyautogui.ImageNotFoundException:
                    print("No sweet_dis_icon Button.")
                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_nl_icon.png", region=(1225, 33, 755, 400), confidence=0.95)
                    #pyautogui.click(x, y)
                    print("sweet_nl_icon Button Found")
                    all_extensions_not = False

                except pyautogui.ImageNotFoundException:
                    print("No sweet_nl_icon Button.")
            except pyautogui.ImageNotFoundException:
                print("No mysterium_icon_emptyf Button.")
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/mysterium_icon_connected.png", region=(1225, 33, 755, 400), confidence=0.95)
                #pyautogui.click(x, y)
                print("mysterium_icon_emptyf Button Found")
                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_dis_icon.png", region=(1225, 33, 755, 400), confidence=0.95)
                    #pyautogui.click(x, y)
                    print("sweet_dis_icon Button Found")
                    all_extensions_not = False

                except pyautogui.ImageNotFoundException:
                    print("No sweet_dis_icon Button.")
                try:
                    x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_nl_icon.png", region=(1225, 33, 755, 400), confidence=0.95)
                    #pyautogui.click(x, y)
                    print("sweet_nl_icon Button Found")
                    all_extensions_not = False

                except pyautogui.ImageNotFoundException:
                    print("No sweet_nl_icon Button.")

            except pyautogui.ImageNotFoundException:
                print("No mysterium_icon_emptyf Button.")

        except pyautogui.ImageNotFoundException:
            print("No extension_icon Button.")
    return all_extensions_not
        







def get_browser_proxy():
    collectionbip = db[f'LocalCSB']
    quer2y = {"type": "main"}
    dochh = collectionbip.find_one(quer2y)
    proxy = dochh["browser_proxy"]
    print('BRowser PRoxy :', proxy)
    global browser_proxy
    browser_proxy = proxy
    return browser_proxy

 


def sweet_enable():
    for x in range(5):
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_nl_icon.png",  region=(1625, 43, 700, 300), confidence=0.98)
            return
            
        except pyautogui.ImageNotFoundException:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_dis_icon.png",  region=(1625, 43, 700, 300), confidence=0.98)
            pyautogui.click(x, y)
            for i in range(5):
                time.sleep(3)
                try:
                    a, b = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_connect.png", confidence=0.8)
                    pyautogui.click(1518, 438)
                    time.sleep(2)

                    pyautogui.click(a, b)
                    time.sleep(8)
                    return
                except pyautogui.ImageNotFoundException:
                    print("Waiting for Sweet to pop")

        except pyautogui.ImageNotFoundException:
            print("No icon_image_loaded Human.")
            try:
                x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/sweet_us.png", region=(1625, 43, 700, 300), confidence=0.98)
                pyautogui.click(x, y)
                time.sleep(3)
                pyautogui.click(1518, 438)
                time.sleep(2)
                return
                
            except pyautogui.ImageNotFoundException:
                print("Waiting for Sweet to pop")


def mysterium_reinstaller():
    response_messege('Changed IP🔴 :Mys Reinstaller')
    global sb1
    global chrome_user_data_dir
    global layout
    global browser_proxy
    for i in range(4):
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/mysterium_icon_connected.png", region=(1625, 43, 400, 300), confidence=0.99)
            if x and y:

                pyautogui.moveTo(100, 100)
                pyautogui.click(100, 200, duration=0.5)
                browser_proxy  =get_browser_proxy()

                quer2y = {"type": "main"}
                dochh2 = collection.find_one(quer2y)
                layout = dochh2["withdraw_mail"]
                print(f'Farm ID:{farm_id} | Layout: {layout}')
                chrome_user_data_dir = f'/root/.config/google-chrome/{browser_proxy}{layout}'
                try:
                    sb1.quit()
                    time.sleep(2)
                except Exception as e:
                    print(f"sb1.quit() failed: {e}")

                # Fallback kill
                for proc_name in ['chrome', 'chromium']:
                    try:
                        subprocess.run(['pkill', '-f', proc_name], check=False, stderr=subprocess.DEVNULL)
                        print(f"All {proc_name} processes killed (if any).")
                    except Exception as e:
                        print(f"Failed to kill {proc_name} processes: {e}")
                time.sleep(3)
                delete_folder(chrome_user_data_dir)
                sb1 = open_browsers()
                return
 
        except pyautogui.ImageNotFoundException:
            print("No icon_image_loaded Human.")


import shutil
def delete_folder(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"Deleted: {folder_path}")
        except Exception as e:
            print(f"Error deleting {folder_path}: {e}")
    else:
        print(f"Folder not found or not a directory: {folder_path}")

def add_blacklistedip2(input, ip):
    collectionbip = db[f'LocalCSB']
    query = {"type": "main"}
    update = {
        "$addToSet": {  # Ensures the IP is added only if it doesn't already exist
            f"blacklistedIP2.{input}": ip
        }
    }
    result = collectionbip.update_one(query, update)
    if result.modified_count > 0:
        print(f"Successfully added IP '{ip}' to {input}.")
    else:
        print(f"No update occurred. IP '{ip}' might already exist.")
    try:
        sri_lanka_tz = pytz.timezone('Asia/Colombo')
        utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
        sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
        now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')

        query = {"type": 'ip_log'}
        existing_doc = collectionbip.find_one(query)
        print("Existing document before update")
        new_message = {now:f'{input} | {ip}'} # {'2024-09-06 03:47:14': 220}  # Use a new timestamp
        messages = existing_doc['messages']
        messages.update(new_message)
        update = {"$set": {"messages": messages}}
        result = collectionbip.update_one(query, update)
        print("Updated document")
        if result.matched_count > 0:
            print(f"Added new messages to existing document. Updated {result.modified_count} document(s).")
        else:
            print("No document found with the specified type.")
    except Exception as e:
        print(e)



 
 
 


browser_proxy = ''
query = {"type": "main"}
refresh_count = 0
get_mails_passowrds(farm_id)
#for frm in CSB1_farms:
#    collection_csb = db[f'Farm{frm}']
#    update = {"$set": {"response": f'Changed IP🔴: Starting Farm:{farm_id}'}}
#    result = collection_csb.update_one(query, update)
#    update = {"$set": {"request": 'ipfixer'}}
#    result = collection_csb.update_one(query, update)

def Limit_Checked():
    title = sb1.get_title()
    if 'Earn-pepe1' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/pepe_limit.png", confidence=0.9)
            print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Earn-Trump12' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/trump_limit.png", confidence=0.9)
            print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Feyorra' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/feyorra_limit_win10.png", confidence=0.9)
            print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Earn-Bonk' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/bonk_limit_win10.png", confidence=0.9)
            print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    return False

def Click_Understand():
    print('Trying CLicks')
    #time.sleep(1)
    title = sb1.get_title()
    if 'Feyorra' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/feyorra_understand.png", confidence=0.8)
            pyautogui.click(x, y, duration = 0.2)
            #print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Earn-Bonk' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/images/bonk_understand.png", confidence=0.8)
            #print('Limit Reached')
            pyautogui.click(x, y, duration = 0.2)
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    return False

def update_ip(new_ip, config_path="mfhelper/config.json"):
    try:
        # Load existing config.json
        with open(config_path, "r") as file:
            config = json.load(file)
        
        # Update the targetIP
        config["targetIP"] = new_ip

        # Save the updated config.json
        with open(config_path, "w") as file:
            json.dump(config, file, indent=4)

        print(f"Updated targetIP to: {new_ip}")
    except Exception as e:
        print(f"Error updating config.json: {e}")



def calculate_accuracy_captchas(total_tests, failed_tests):
    if total_tests == 0:
        return 0
    accuracy = ((total_tests - failed_tests) / total_tests) * 100
    return round(accuracy, 2)


def fix_all_cloudflare(sb1):
    cloud = False
    all_window_handles = sb1.window_handles
    for handle in all_window_handles:
        sb1.switch_to.window(handle)
        if 'Just' in sb1.get_title():
            cloudflare(sb1, login = False)
            time.sleep(2)
            cloud = True

def quick_open_faucet(sb1):
    sb1.open_new_window()
    current_window = sb1.current_window_handle
    close_extra_windows(sb1, [current_window])
    earnpp_window = None
    feyorra_window = None
    trump_window = None
    bonk_window = None


    ##Open All Faucets
    sb1.uc_open('https://earn-pepe.com/member/faucet')

    sb1.open_new_window()
    sb1.uc_open('https://feyorra.site/member/faucet')

    sb1.open_new_window()
    sb1.uc_open('https://earn-trump.com/member/faucet')


    sb1.open_new_window()
    sb1.uc_open('https://earn-bonk.com/member/faucet')

    
    #time.sleep(2)

    cloudg = fix_all_cloudflare(sb1)
    if cloudg:
        cloudg = fix_all_cloudflare(sb1)


    print('Length of all windows:', len(sb1.window_handles))

    all_window_handles = sb1.window_handles
    for handle in all_window_handles:
        sb1.switch_to.window(handle)
        print('Current Window Title:', sb1.get_title())

        if "Faucet | Earn-pepe" in sb1.get_title():
            earnpp_window = sb1.current_window_handle
            print('EarnPP Window Found')

        elif "Faucet | Feyorra" in sb1.get_title():
            feyorra_window = sb1.current_window_handle
            print('Feyorra Window Found')

        elif "Faucet | Earn-Trump" in sb1.get_title():
            trump_window = sb1.current_window_handle
            print('Trump Window Found')

        elif "Faucet | Earn-Bonk" in sb1.get_title():
            bonk_window = sb1.current_window_handle
            print('Bonk Window Found')
    if earnpp_window and feyorra_window and trump_window and bonk_window:
        print('All Faucet Windows Found')
    else:
        print('Not all Faucet Windows Found, trying again')
        all_window_handles = sb1.window_handles
        for handle in all_window_handles:
            sb1.switch_to.window(handle)

            if "Faucet | Earn-pepe" in sb1.get_title():
                earnpp_window = sb1.current_window_handle
                print('EarnPP Window Found')

            elif "Faucet | Feyorra" in sb1.get_title():
                feyorra_window = sb1.current_window_handle
                print('Feyorra Window Found')

            elif "Faucet | Earn-Trump" in sb1.get_title():
                trump_window = sb1.current_window_handle
                print('Trump Window Found')

            elif "Faucet | Earn-Bonk" in sb1.get_title():
                bonk_window = sb1.current_window_handle
                print('Bonk Window Found')

    return earnpp_window, feyorra_window, trump_window, bonk_window


def ensure_mysterium_window_running():
    mysterium_path = r"C:\Users\Administrator\Downloads\myst_win\myst_win\mysterium_vpn.exe"
    keyword = "mysterium"

    try:
        windows = Desktop(backend="uia").windows()
        for win in windows:
            title = win.window_text()
            if keyword.lower() in title.lower():
                print(f"Mysterium is already running (Window: {title})")
                return

        # If no window found, launch it
        if os.path.exists(mysterium_path):
            print("Mysterium not found. Launching...")
            subprocess.Popen([mysterium_path], shell=False)
            time.sleep(5)  # Wait for the application to launch
        else:
            print("Error: Mysterium path does not exist.")

    except Exception as e:
        print(f"Window detection failed: {e}")
def mysteryum_changer(server):
    ref = True
    for i in range(10):
        if ref:
            try:
                ensure_mysterium_window_running()
                focus_and_maximize_window("Mysterium")
                time.sleep(2)
                pyautogui.click(301, 321)  # Click on the Mysterium icon in the system tray
                time.sleep(2)

                pyautogui.click(112, 104)  # Click on the Mysterium icon in the system tray
                time.sleep(2)
                pyautogui.click(415, 103)
                time.sleep(2)
                pyautogui.click(112, 104)  # Press the Delete key to remove the current server
                time.sleep(2)
                pyautogui.typewrite(server)  # Type the server name
                time.sleep(3)
                pyautogui.click(145, 482, duration=0.5)  # Click on the "Change Server" button
                time.sleep(5)  # Wait for the server change to take effect
                pyautogui.hotkey('alt', 'tab') 
            except Exception as e:
                print(f"Error changing Mysterium server: {e}")
        ip_address = get_ip_OS()
        if ip_address == vps_ip:
            ref = True
            continue
        elif ip_address == None:
            focus_and_maximize_window("Mysterium")
            time.sleep(2)
            pyautogui.click(1150, 916, duration=0.5)  # Click on the Mysterium icon in the system tray
            time.sleep(5)
            ref = False
        else:
            break
    focus_and_maximize_window("Chrome")

iana_to_windows = {
    "Asia/Bangkok": "SE Asia Standard Time",
    "Asia/Kolkata": "India Standard Time",
    "Europe/London": "GMT Standard Time",
    "America/New_York": "Eastern Standard Time",
    "America/Los_Angeles": "Pacific Standard Time",
    "UTC": "UTC",

    # Added timezones
    "Europe/Warsaw": "Central European Standard Time",       # Poland
    "Europe/Paris": "Romance Standard Time",                 # France
    "Europe/Berlin": "W. Europe Standard Time",              # Germany
    "Europe/Vienna": "W. Europe Standard Time",              # Austria
    "America/Toronto": "Eastern Standard Time",              # Canada (Ontario/Quebec)
    "America/Vancouver": "Pacific Standard Time",            # Canada (British Columbia)
    "America/Edmonton": "Mountain Standard Time",            # Canada (Alberta)
    "America/Winnipeg": "Central Standard Time",             # Canada (Manitoba)
}

def timezone_changer(timezone_str):
    """
    Sets Windows timezone using an IANA timezone name by converting it to the corresponding Windows name.
    """
    windows_tz = iana_to_windows.get(timezone_str)
    
    if not windows_tz:
        print(f"Unknown IANA timezone: {timezone_str}")
        return

    try:
        cmd = f'powershell -Command "tzutil /s \'{windows_tz}\'"'
        subprocess.run(cmd, shell=True, check=True)
        print(f"Timezone successfully set to: {timezone_str} ({windows_tz})")
    except subprocess.CalledProcessError:
        print(f"Failed to set timezone to: {timezone_str} ({windows_tz})")


def close_mysterium_and_wireguard():
    # List of processes to kill
    targets = ["mysterium_vpn.exe", "wireguard_svc.exe"]

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in targets:
                print(f"Killing {proc.info['name']} (PID: {proc.info['pid']})")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    # Try to gracefully close Mysterium VPN if it's open via taskkill (just in case)
    subprocess.call('taskkill /f /im mysterium_vpn.exe >nul 2>&1', shell=True)
    subprocess.call('taskkill /f /im wireguard_svc.exe >nul 2>&1', shell=True)

def kill_all_python_processes():
    current_pid = os.getpid()
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'python' in proc.info['name'].lower():
                if proc.info['pid'] != current_pid:
                    print(f"Killing other Python process: PID {proc.info['pid']}")
                    proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    print(f"Killing current Python process: PID {current_pid}")
    psutil.Process(current_pid).kill()
def Kill_Script():
    try:
        sb1.quit()
        time.sleep(2)
    except Exception as e:
        print(f"sb1.quit() failed: {e}")
    for i in range(5):
        ip_address = get_ip_OS()
        if vps_ip == ip_address:
            close_mysterium_and_wireguard()
            kill_all_python_processes()
            return

        else:
            focus_and_maximize_window("Mysterium")
            time.sleep(2)
            pyautogui.click(1319, 878)
            time.sleep(2)


ip_memory_cache = '' 

already_ready = False
fresh_start_faucet = True
login_faucet_detect = True
def open_browsers():
    global sb1
    global chrome_user_data_dir
    global layout
    global browser_proxy
    global already_ready
    global ip_memory_cache

    pyautogui.moveTo(100, 100)
    #pyautogui.click(100, 200, duration=0.5)
    browser_proxy  =get_browser_proxy()

    quer2y = {"type": "main"}
    dochh2 = collection.find_one(quer2y)
    layout = dochh2["withdraw_mail"]
    if layout == 'Layout7':
        Kill_Script()
        raise ValueError("Layout cannot be 7, please check the database configuration.")
    print(f'Farm ID:{farm_id} | Layout: {layout}')
    chrome_user_data_dir = f'C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/{browser_proxy}{layout}'
    try:
        for l in range(1,7):
            if chrome_user_data_dir == f'C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/{browser_proxy}Layout{l}':
                print(f'No Del Layout{l}')
            else:
                delete_folder(f'C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/{browser_proxy}Layout{l}')
    except Exception as e:
        pass
    sb1 = Driver(
        uc=True,
        headed=True,
        undetectable=True,
        undetected=True,
        disable_gpu=True,
        no_sandbox=True,

        user_data_dir=chrome_user_data_dir,  # e.g., "C:/Users/YourName/AppData/Local/Google/Chrome/User Data/Profile 1"
        binary_location=chrome_binary_path,  # e.g., "C:/Program Files/Google/Chrome/Application/chrome.exe"
        page_load_strategy="none",
        extension_dir="C:/Users/Administrator/Downloads/MFV6-main/MFV6-main/mfhelper", 
        chromium_arg=[
            # Windows-specific and stealth-friendly arguments
            "--disable-blink-features=AutomationControlled",
            "--disable-background-timer-throttling",
            "--disable-backgrounding-occluded-windows",
            "--disable-renderer-backgrounding",

        ]
    )
    sb1.maximize_window()
    sb1.uc_open("chrome://extensions/")
    current_window = sb1.current_window_handle
    sb1.open_new_window()
    current_window2 = sb1.current_window_handle
    sb1.switch_to.window(current_window)
    sb1.close()  # Close the tab
    sb1.connect()
    sb1.switch_to.window(current_window2)
    sb1.uc_open("chrome://extensions/")
    focus_and_maximize_window("Chrome")
    #time.sleep(5000000000)
    #sb1.execute_script("window.scrollTo(0, 300);")
    print(sb1.get_title())
    #fix_tab_search_icon()
    #gggv = are_extensions_exist()
    get_mails_passowrds(farm_id)
    ip_address = get_ip_OS()
    lay = re.search(r'\d+', layout).group()

    if ip_memory_cache == ip_address:
        print(f'IP Already Using and Ready: {ip_address}')
        query = {"type": "main"}
        update = {"$set": {"response": f'Ready IP for Reuse Session:{ip_address}'}}
        result = collection.update_one(query, update)
        already_ready = True
        return sb1 #, True


    Not_Black_Listed_Stt = Full_blacklist_Check(sb1, ip_address,f'F{farm_id}L{lay}')
    if Not_Black_Listed_Stt:
        print(f'Good IP Ready IP at Start: {ip_address}')
        update_ip(ip_address, config_path="mfhelper/config.json")
        query = {"type": "main"}
        update = {"$set": {"response": f'Ready IP at Start:{ip_address}'}}
        result = collection.update_one(query, update)
        already_ready = True
        return sb1 #, True


    #sb1.disconnect()
    #time.sleep(99999)
    return sb1 #, False

faucetlayout = None
def open_faucets():
    global sb1
    while True:
        try:
            pyautogui.moveTo(100, 200)
            pyautogui.moveTo(200, 400)
            global faucetlayout
            global fresh_start_faucet
            global login_faucet_detect
            global already_ready
            global ip_memory_cache
            focus_and_maximize_window("Chrome")
            ip_required = None
            quer2y = {"type": "main"}
            dochh2 = collection.find_one(quer2y)
            layout2 = dochh2["withdraw_mail"]
            print(f'Farm ID:{farm_id} | Layout: {layout2}')
            browser_proxy2  =get_browser_proxy()
            chrome_user_data_dir2 = f'C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/{browser_proxy2}{layout2}'
            if chrome_user_data_dir == chrome_user_data_dir2 and layout == layout2 and browser_proxy2 == browser_proxy:
                print(f'Same Browser | L {layout2}')
            else:
                #@response_messege(f'Resetting Browser')
                try:
                    sb1.quit()
                    time.sleep(2)
                except Exception as e:
                    print(f"sb1.quit() failed: {e}")

                sb1 = open_browsers()
                continue
            pyautogui.moveTo(100, 200)
            pyautogui.moveTo(200, 400)
            print('ff already_ready',already_ready)
            focus_and_maximize_window("Chrome")

            if already_ready:
                for frm in CSB1_farms:
                    collection_csb = db[f'Farm{frm}']
                    query = {"type": "main"}
                    doc = collection_csb.find_one(query)
                    res = doc["response"]
                    req = doc["request"]
                    if req == 'ipfixer':
                        if 'Ready' in res or 'Loging' in res:
                            print(f'IP is ready Farm{frm}')

                        else:
            
                            ipfixer()
                            already_ready = False
                            raise Exception("Ready IP ipfixer Done earnbonk == 404")
                        
                if already_ready:    
                    earnpp_window, feyorra_window, earntrump_window, earnbonk_window =quick_open_faucet(sb1)
                    ip_address = get_ip_OS()
                    lay = re.search(r'\d+', layout2).group()
                    Not_Black_Listed_Stt = True
                    if ip_memory_cache != ip_address:
                        Not_Black_Listed_Stt = Full_blacklist_Check(sb1,ip_address,f'F{farm_id}L{lay}')
                        if Not_Black_Listed_Stt:
                            tizon = get_timezone(ip_address)
                            timezone_changer(tizon)
                            add_blacklistedip2(f'F{farm_id}L{lay}', ip_address)
                            ip_memory_cache = ip_address

                    print(f'Not_Black_Listed_Stt: {Not_Black_Listed_Stt} | IP: {ip_address} | earnpp_window: {earnpp_window} | feyorra_window: {feyorra_window} | earntrump_window: {earntrump_window} | earnbonk_window: {earnbonk_window}')
                    if Not_Black_Listed_Stt and earnpp_window and feyorra_window and earntrump_window and earnbonk_window:
                        print('All Faucets are opened')
                        query = {"type": "main"}
                        update = {"$set": {"request": 'mainscript'}}
                        result = collection.update_one(query, update)
                        
                        return earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_address
                    else:
                        already_ready = False


            current_window = sb1.current_window_handle
            close_extra_windows(sb1, [current_window])
            sb1.switch_to.window(current_window)
            sb1.uc_open("chrome://extensions/")
            time.sleep(1)
            global blacklistedIP
            lay = re.search(r'\d+', layout2).group()
            ip_address = get_ip_OS()
            Not_Black_Listed_Stt = Full_blacklist_Check(sb1,ip_address,f'F{farm_id}L{lay}')
            if Not_Black_Listed_Stt:
                focus_and_maximize_window("Chrome")
                print(f'Good IP found: {ip_address}')
                for frm in CSB1_farms:
                    collection_csb = db[f'Farm{frm}']
                    query = {"type": "main"}
                    doc = collection_csb.find_one(query)
                    res = doc["response"]
                    req = doc["request"]
                    if req == 'ipfixer':
                        if 'Ready' in res or 'Loging' in res:
                            print('IP is ready')
                            ip_required = ip_address
                            update_ip(ip_address, config_path="mfhelper/config.json")

                        else:
            
                            ipfixer()
                            raise Exception("Ready IP ipfixer Done")
                    else:
                        ip_required = ip_address
                        update_ip(ip_address, config_path="mfhelper/config.json")
            else:
                ipfixer()
                raise Exception("Ready IP ipfixer Done")

            pyautogui.moveTo(100, 200)
            pyautogui.moveTo(200, 400)
            if ip_address:
                add_blacklistedip2(f'F{farm_id}L{lay}', ip_address)
                current_window = sb1.current_window_handle
                close_extra_windows(sb1, [current_window])
                sb1.switch_to.window(current_window)
                sb1.uc_open("chrome://extensions/")
                get_mails_passowrds(farm_id)
                faucetlayout = 1 #dochh2["mainfaucet"]
                print(f'Farm ID:{farm_id} | Faucet Layout: {faucetlayout}')
                fresh_start_faucet = True
                pyautogui.moveTo(100, 200)
                pyautogui.moveTo(200, 400)
                tizon = get_timezone(ip_address)
                timezone_changer(tizon)
                #time.sleep(99999)
                if fresh_start_faucet == True:
                    ip_address = get_ip_OS()
                    if ip_required == ip_address:
                        response_messege('EarnPP Loging Fresh')
                        if earnpp:
                            if faucetlayout == 1:
                                earnpp_window = handle_site(sb1, "https://earn-pepe.com/member/faucet","Faucet | Earn-pepe" , "Home | Earn-pepe", 1, [], ip_required, ip_check = True)
                                close_extra_windows(sb1, [earnpp_window])
                                if earnpp_window == 404:
                                    print('404 Errore')
                                    raise Exception(" earnpp_window == 404")
                                print(f"EarnPP window handle: {earnpp_window}")

                        else:
                            earnpp_window = None
                    else:
                        raise Exception("Ip changed")

                    
                    ip_address = get_ip_OS()
                    if ip_required == ip_address:
                        response_messege('Feyorra Loging Fresh')
                        if feyorra:
                            #sb1.open_new_window()
                            if faucetlayout == 1:
                                feyorra_window = handle_site(sb1, "https://feyorra.site/member/faucet", "Faucet | Feyorra" , "Best - Meme Coins Faucet", 2, [], ip_required, ip_check = True)
                                close_extra_windows(sb1, [feyorra_window])
                                if feyorra_window == 404:
                                    print('404 Errore')
                                    raise Exception(" feyorra_window == 404")
                                print(f"Feyorra window handle: {feyorra_window}")
                                time.sleep(2)
                                Click_Understand()



                        else:
                            feyorra_window = None
                    else:
                        raise Exception("Ip changed")
                    
                    ip_address = get_ip_OS()
                    if ip_required == ip_address:
                        response_messege('trump Loging Fresh')
                        if earntrump:
                            #sb1.open_new_window()
                            if faucetlayout == 1:
                                earntrump_window = handle_site(sb1, "https://earn-trump.com/member/faucet","Faucet | Earn-Trump" , "Free $Trump Coin Faucet | Earn $Trump Crypto Instantly", 3, [], ip_required, ip_check = True)
                                close_extra_windows(sb1, [earntrump_window])
                                if earntrump_window == 404:
                                    print('404 Errore')
                                    raise Exception(" earntrump_window == 404")
                                print(f"earntrump window handle: {earntrump_window}")


                        else:
                            earntrump_window = None
                    else:
                        raise Exception("Ip changed")
                    
                    ip_address = get_ip_OS()
                    if ip_required == ip_address:
                        response_messege('earnbonk Loging Fresh')
                        if earnbonk:
                            #sb1.open_new_window()
                            if faucetlayout == 1:
                                earnbonk_window = handle_site(sb1, "https://earn-bonk.com/member/faucet", "Faucet | Earn-Bonk" , "Earn Bonk", 4, [], ip_required,ip_check =  True)
                                close_extra_windows(sb1, [earnbonk_window])
                                if earnbonk_window == 404:
                                    print('404 Errore')
                                    raise Exception(" earnbonk == 404")
                                print(f"Feyorra window handle: {earnbonk_window}")
                                time.sleep(3)
                                Click_Understand()

                        else:
                            earnbonk_window = None
                    else:
                        raise Exception("Ip changed")

                pyautogui.moveTo(100, 200)
                pyautogui.moveTo(200, 400)

                ################################################################
                if ip_required == ip_address:
                    response_messege('EarnPP Loging')
                    if earnpp:
                        if faucetlayout == 1:
                            earnpp_window = handle_site(sb1, "https://earn-pepe.com/member/faucet","Faucet | Earn-pepe" , "Home | Earn-pepe", 1, [], ip_required)
                            if earnpp_window == 404:
                                print('404 Errore')
                                raise Exception(" earnpp_window == 404")
                            print(f"EarnPP window handle: {earnpp_window}")

                    else:
                        earnpp_window = None
                else:
                    raise Exception("Ip changed")
                
                if ip_required == ip_address:
                    response_messege('Feyorra Loging')
                    if feyorra:
                        sb1.open_new_window()
                        if faucetlayout == 1:
                            feyorra_window = handle_site(sb1, "https://feyorra.site/member/faucet", "Faucet | Feyorra" , "Best - Meme Coins Faucet", 2, [earnpp_window], ip_required)
                            if feyorra_window == 404:
                                print('404 Errore')
                                raise Exception(" feyorra_window == 404")
                            elif feyorra_window == 405:
                                login_faucet_detect = True
                                raise Exception(" login_faucet_detect == 404")
                            print(f"Feyorra window handle: {feyorra_window}")



                    else:
                        feyorra_window = None
                else:
                    raise Exception("Ip changed")
                

                if ip_required == ip_address:
                    response_messege('trump Loging')
                    if earntrump:
                        sb1.open_new_window()
                        if faucetlayout == 1:
                            earntrump_window = handle_site(sb1, "https://earn-trump.com/member/faucet","Faucet | Earn-Trump" , "Free $Trump Coin Faucet | Earn $Trump Crypto Instantly", 3, [earnpp_window,feyorra_window], ip_required)
                            if earntrump_window == 404:
                                raise Exception(" earntrump_window == 404")
                            elif feyorra_window == 405:
                                login_faucet_detect = True
                                raise Exception(" login_faucet_detect == 404")
                            print(f"earntrump window handle: {earntrump_window}")


                    else:
                        earntrump_window = None
                else:
                    raise Exception("Ip changed")
                
                if ip_required == ip_address:
                    response_messege('earnbonk Loging')
                    if earnbonk:
                        sb1.open_new_window()
                        if faucetlayout == 1:
                            earnbonk_window = handle_site(sb1, "https://earn-bonk.com/member/faucet", "Faucet | Earn-Bonk" , "Earn Bonk", 4, [earnpp_window,feyorra_window,earntrump_window], ip_required)
                            if earnbonk_window == 404:
                                raise Exception(" earnbonk == 404")
                            elif feyorra_window == 405:
                                login_faucet_detect = True
                                raise Exception(" login_faucet_detect == 404")
                            print(f"Feyorra window handle: {earnbonk_window}")


                    else:
                        earnbonk_window = None
                else:
                    raise Exception("Ip changed")
                
                
                ip_address = get_ip_OS()
                if ip_required == ip_address:
                    response_messege('Ready IP | Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'mainscript'}}
                    result = collection.update_one(query, update)

                    all_window_handles = [earnpp_window,feyorra_window,earntrump_window,earnbonk_window]
                    close_extra_windows(sb1, all_window_handles)
                    sb1.switch_to.window(earnpp_window)
                    print(f"Windows: EarnPP: {earnpp_window}, Feyorra: {feyorra_window}")
                    global reset_count 
                    global reset_count_isacc 
                    global previous_reset_count
                    global earnpp_limit_reached 
                    global feyorra_limit_reached 
                    global earntrump_limit_reached 
                    global earnbonk_limit_reached

                    earnpp_limit_reached = None
                    feyorra_limit_reached = None
                    earnbonk_limit_reached = None
                    earntrump_limit_reached = None
                    No_understand_Feyorra = True
                    No_understand_BONK = True
                    reset_count = 0
                    reset_count_isacc = 0
                    previous_reset_count = 0

                    login_faucet_detect = False
                    pyautogui.moveTo(100, 200)
                    pyautogui.moveTo(200, 400)
                    for frm in CSB1_farms:
                        collection_csb = db[f'Farm{frm}']
                        query = {"type": "main"}
                        doc = collection_csb.find_one(query)
                        res = doc["response"]
                        req = doc["request"]
                        if req == 'ipfixer':
                            if 'Changed' in res:
                                raise Exception(" earnbonk == 404")
                    ip_memory_cache = ip_address
                    already_ready = True

                    return earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required
        except Exception as e:
                response_messege(f'Resetting Browser: {e}')
                try:
                    sb1.quit()
                    time.sleep(2)
                except Exception as e:
                    print(f"sb1.quit() failed: {e}")
                time.sleep(4)
                sb1 = open_browsers()
                reset_count +=15

def debug_messages(messages):
    if debug_mode:
        print(messages)

earnpp_count = 0 
feyorra_count = 0
claimcoin_count = 0

No_understand_Feyorra = True
No_understand_BONK = True
earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required = open_faucets()
start_time4 = 0
time.sleep(2)
print('Starting Loop')

Script_Started = time.time()
script_seconds_only = 0

solving_accuracy = 0
failed_captchas = 0
total_captchas_received = 0


previous_script_seconds_only = '0 | 0'

while True:
    try:
        mainscript = control_panel()
        print('control_panel', mainscript)
        if mainscript == 10:
            mainscript = 1
            reset_count = 50

        if mainscript == 1:
            
            debug_messages(f'Ip address Found:{ip_address}')
            set_refresh_faucets = 0
            cc_faucet = None
            script_elapsed_time = time.time() - Script_Started
            script_seconds_only = int(script_elapsed_time)
            #debug_messages(f'script_elapsed_time Seconds:{script_seconds_only}')
            if script_seconds_only > 2200:
                #print('Script 5m')
                solving_accuracy = 0
                failed_captchas = 0
                total_captchas_received = 0


                Script_Started = time.time()
                try:
                    sb1.quit()
                    time.sleep(1)
                except Exception as e:
                    print(f"sb1.quit() failed: {e}")
                        

                sb1 = open_browsers()

                earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required = open_faucets()
                previous_script_seconds_only = previous_script_seconds_cal(previous_script_seconds_only,script_seconds_only) #script_seconds_only
                Script_Started = time.time()


            #ip_address = get_ip(sb1) 
            if reset_count >= 20:
                print('reset count hut')
                solving_accuracy = 0
                failed_captchas = 0
                total_captchas_received = 0
                print('reset count higher')
                try:
                    sb1.quit()
                    time.sleep(2)
                except Exception as e:
                    print(f"sb1.quit() failed: {e}")

                # Fallback kill
                for proc_name in ['chrome', 'chromium']:
                    try:
                        subprocess.run(['pkill', '-f', proc_name], check=False, stderr=subprocess.DEVNULL)
                        print(f"All {proc_name} reset_count killed (if any).")
                    except Exception as e:
                        print(f"Failed to kill {proc_name} reset_count: {e}")
                time.sleep(2)
                sb1 = open_browsers()
                earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required = open_faucets()
                reset_count = 0
                reset_count_isacc = 0
                Script_Started = time.time()
                previous_script_seconds_only = previous_script_seconds_cal(previous_script_seconds_only,script_seconds_only)

            if previous_reset_count == reset_count:
                reset_count = 0
            else:
                previous_reset_count = reset_count

            if ip_address == ip_required:
                debug_messages(f'Ip address Match:{ip_address}')

                all_window_handles = [earnpp_window,feyorra_window,earntrump_window,earnbonk_window]
                gg23g= close_extra_windows(sb1, all_window_handles)
                if gg23g:
                    reset_count +=3

                print(f'Reset_count:{reset_count}')

                if earnpp:
                    try:
                        debug_messages(f'Switching Pages to EarnPP')
                        sb1.switch_to.window(earnpp_window)
                        debug_messages(f'Getting Pages Titile:EarnPP')
                        title =sb1.get_title()
                        if 'Faucet | Earn-pepe' in title:
                            debug_messages(f'Solving Icon Captcha on EarnPP')
                            val = get_coins(sb1, 1)
                            if val:
                                earnpp_coins = val
                            gg = solve_icon_captcha(sb1)
                            if gg:
                                if gg == 201:
                                    #wrong detect:
                                    failed_captchas += 1
                                total_captchas_received += 1
                                earnpp_limit_reached = None
                            else:
                                if Limit_Checked():
                                    if earnpp_limit_reached:
                                        print('Limit Reached')
                                    else:
                                        debug_messages(f'Pepe Limit Reached')
                                        response_messege('Pepe Limit Reached')
                                        earnpp_limit_reached =True
                                else:
                                    refresh_count +=2
                            debug_messages(f'Solved Icon Captcha on EarnPP')


                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on EarnPP')
                            response_messege('Lock.. Found on EarnPP')
                            earnpp_coins = 0
                        elif 'Google' in title:
                            response_messege('Google.. Found on EarnPP')
                            reset_count +=25
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on EarnPP')

                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed EarnPP')
                        elif 'aintenance' in title:
                            debug_messages(f'maintenance.. Found on EarnPP')
                            response_messege('maintenance.. Found on EarnPP')
                            earnpp_coins = 0
                        elif 'Home | Earn-pepe' in title or 'Login' in title:
                            debug_messages(f'LOGIN.. Found on EarnPP')
                            response_messege('LOGIN.. Found on EarnPP')
                            earnpp_coins = 0
                            reset_count +=7
                        else:
                            debug_messages(f'EarnPP not Found:{title} | reset:{reset_count}')
                            reset_count +=1

                    except Exception as e:
                        if Limit_Checked():
                            if earnpp_limit_reached:
                                print('Limit Reached')
                            else:
                                debug_messages(f'Pepe Limit Reached')
                                response_messege('Pepe Limit Reached')
                                earnpp_limit_reached =True
                        else:
                            debug_messages(f'ERR on EarnPP:{e}')
                            reset_count +=1

                
                if feyorra:
                    try:
                        debug_messages(f'Switching Pages to Feyorra')
                        sb1.switch_to.window(feyorra_window)
                        debug_messages(f'Getting Pages Titile:Feyorra')
                        #pyautogui.press('enter')
                        title =sb1.get_title()

                        if 'Faucet | Feyorra' in title:
                            debug_messages(f'Solving Icon Captcha on Feyorra')
                            if No_understand_Feyorra:
                                Click_Understand()
                            val = get_coins(sb1, 2)
                            if val:
                                if feyorra_coins and val and No_understand_Feyorra:
                                    if val > feyorra_coins:
                                        No_understand_Feyorra = False

                                feyorra_coins = val
                            gg = solve_icon_captcha(sb1)
                            if gg:
                                if gg == 201:
                                    #wrong detect:
                                    failed_captchas += 1

                                total_captchas_received += 1
                                feyorra_limit_reached =None
                                
                            else:
                                if Limit_Checked():
                                    if feyorra_limit_reached:
                                        print('Limit Reached')
                                    else:
                                        debug_messages(f'Feyorra Limit Reached')
                                        response_messege('Feyorra Limit Reached')
                                        feyorra_limit_reached =True
                                else:
                                    refresh_count +=2

                                
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on Feyorra')
                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed Feyorra')
                        elif 'Google' in title:
                            response_messege('Google.. Found on Feyorra')
                            reset_count +=25
                        elif 'aintenance' in title:
                            debug_messages(f'maintenance.. Found on Feyorra')
                            response_messege('maintenance.. Found on Feyorra')
                            feyorra_coins = 0

                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on Feyorra')
                            response_messege('Lock.. Found on Feyorra')
                            feyorra_coins =0
                        elif 'Best - Meme Coins Faucet' == title or 'Login' in title:
                            debug_messages(f'LOGIN.. Found on Feyorra')
                            response_messege('LOGIN.. Found on Feyorra')
                            feyorra_coins = 0
                            reset_count +=5
                        else:
                            debug_messages(f'Feyorra not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                    except Exception as e:
                        pyautogui.press('enter')

                        if Limit_Checked():
                            if feyorra_limit_reached:
                                print('Limit Reached')
                            else:
                                debug_messages(f'Feyorra Limit Reached')
                                response_messege('Feyorra Limit Reached')
                                feyorra_limit_reached =True
                        else:
                            debug_messages(f'ERR on Feyorra:{e}')
                            reset_count +=1


                
                if earntrump:
                    try:
                        debug_messages(f'Switching Pages to earntrump')
                        sb1.switch_to.window(earntrump_window)
                        debug_messages(f'Getting Pages Titile:earntrump')
                        #pyautogui.press('enter')
                        title =sb1.get_title()

                        if 'Faucet | Earn-Trump' in title:
                            debug_messages(f'Solving Icon Captcha on Earn-Trump')

                            val = get_coins(sb1, 1)
                            if val:
                                earntrump_coins = val
                            gg = solve_icon_captcha(sb1)
                            if gg:
                                if gg == 201:
                                    #wrong detect:
                                    failed_captchas += 1

                                total_captchas_received += 1
                                earntrump_limit_reached =None
                            else:
                                if Limit_Checked():
                                    if earntrump_limit_reached:
                                        print('Limit Reached')
                                    else:
                                        debug_messages(f'Trump Limit Reached')
                                        response_messege('Trump Limit Reached')
                                        earntrump_limit_reached =True
                                else:
                                    refresh_count +=2

                                
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on Trump')
                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed Trump')
                        elif 'Google' in title:
                            response_messege('Google.. Found on Trump')
                            reset_count +=25
                        elif 'aintenance' in title:
                            debug_messages(f'maintenance.. Found on Trump')
                            response_messege('maintenance.. Found on Trump')
                            feyorra_coins = 0

                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on Trump')
                            response_messege('Lock.. Found on Trump')
                            feyorra_coins =0
                        elif  "Free $Trump Coin Faucet | Earn $Trump Crypto Instantly" == title or 'Login' in title:
                            debug_messages(f'LOGIN.. Found on Trump')
                            response_messege('LOGIN.. Found on Trump')
                            feyorra_coins = 0
                            reset_count +=5
                        else:
                            debug_messages(f'Trump not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                    except Exception as e:
                        pyautogui.press('enter')

                        if Limit_Checked():
                            if earntrump_limit_reached:
                                print('Limit Reached')
                            else:
                                debug_messages(f'Trump Limit Reached')
                                response_messege('Trump Limit Reached')
                                earntrump_limit_reached =True
                        else:
                            debug_messages(f'ERR on Trump:{e}')
                            reset_count +=1

                if earnbonk:
                    try:
                        debug_messages(f'Switching Pages to earnbonk')
                        sb1.switch_to.window(earnbonk_window)
                        debug_messages(f'Getting Pages Titile:earnbonk')
                        #pyautogui.press('enter')
                        title =sb1.get_title()

                        if 'Faucet | Earn-Bonk' in title:
                            debug_messages(f'Solving Icon Captcha on Earn-Bonk')
                            if No_understand_BONK:
                                Click_Understand()
                            val = get_coins(sb1, 2)
                            if val:
                                if earnbonk_coins and val and No_understand_BONK:
                                    if val > earnbonk_coins:
                                        No_understand_BONK = False
                                earnbonk_coins = val
                            gg = solve_icon_captcha(sb1)
                            if gg:
                                if gg == 201:
                                    #wrong detect:
                                    failed_captchas += 1

                                total_captchas_received += 1
                                earnbonk_limit_reached =None

                            else:
                                if Limit_Checked():

                                    if earnbonk_limit_reached:
                                        print('Limit Reached')
                                    else:
                                        debug_messages(f'Bonk Limit Reached')
                                        response_messege('Bonk Limit Reached')
                                        earnbonk_limit_reached =True
                                else:
                                    #Click_Understand()
                                    refresh_count +=2

                                
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on Bonk')
                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed Bonk')
                        elif 'Google' in title:
                            response_messege('Google.. Found on Bonk')
                            reset_count +=25
                        elif 'aintenance' in title:
                            debug_messages(f'maintenance.. Found on Bonk')
                            response_messege('maintenance.. Found on Bonk')
                            feyorra_coins = 0

                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on Bonk')
                            response_messege('Lock.. Found on Bonk')
                            feyorra_coins =0
                        elif "Earn Bonk" == title or 'Login' in title:
                            debug_messages(f'LOGIN.. Found on Bonk')
                            response_messege('LOGIN.. Found on Bonk')
                            feyorra_coins = 0
                            reset_count +=5
                        else:
                            debug_messages(f'Bonk not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                    except Exception as e:
                        pyautogui.press('enter')

                        if Limit_Checked():
                            if earnbonk_limit_reached:
                                print('Limit Reached')
                            else:
                                debug_messages(f'BONK Limit Reached')
                                response_messege('BONK Limit Reached')
                                earnbonk_limit_reached =True
                        else:
                            debug_messages(f'ERR on Bonk:{e}')
                            reset_count +=1



###################################################################################################################


                elapsed_time = time.time() - start_time
                seconds_only = int(elapsed_time)
                debug_messages(f'ClaimCoins Seconds:{seconds_only}')
                if seconds_only > 80:
                    start_time = time.time()
                    if earnpp_coins == earnpp_coins_pre:
                        start_time = time.time()


                        if refresh_count >= 30 and not earnpp_limit_reached:
                            response_messege(f'earnpp_coins same {earnpp_coins}| count:{refresh_count} | {seconds_only}')
                            sb1.switch_to.window(earnpp_window)

                            sb1.uc_open('https://earn-pepe.com/member/faucet')

                            refresh_count = 0

                        if earnpp_limit_reached:
                            pass
                        else:
                            if refresh_count >= 50:
                                reset_count +=5
                            refresh_count +=1
                    elif feyorra_coins == feyorra_coins_pre:
                        start_time = time.time()

                        if refresh_count >= 30 and not feyorra_limit_reached:
                            pyautogui.press('enter')
                            response_messege(f'feyorra_coins same {feyorra_coins}| count:{refresh_count} | {seconds_only}')
                            refresh_count = 0
                            sb1.switch_to.window(feyorra_window)

                            sb1.uc_open('https://feyorra.site/member/faucet')
                        if feyorra_limit_reached or earnpp_limit_reached or earnbonk_limit_reached or earntrump_limit_reached:
                            pass
                        else:
                            if refresh_count >= 50:
                                reset_count +=5
                            refresh_count +=1
                    elif earnbonk_coins == earnbonk_coins_pre:
                        start_time = time.time()

                        if refresh_count >= 30 and not earnbonk_limit_reached:
                            pyautogui.press('enter')
                            response_messege(f'earnbonk_coins same {earnbonk_coins}| count:{refresh_count} | {seconds_only}')
                            refresh_count = 0
                            sb1.switch_to.window(earnbonk_window)
                            sb1.uc_open('https://earn-bonk.com/member/faucet')
                        if feyorra_limit_reached or earnpp_limit_reached or earnbonk_limit_reached or earntrump_limit_reached:
                            pass
                        else:
                            if refresh_count >= 50:
                                reset_count +=5
                            refresh_count +=1
                    elif earntrump_coins == earntrump_coins_pre:
                        start_time = time.time()

                        if refresh_count >= 30 and not earntrump_limit_reached:
                            pyautogui.press('enter')
                            response_messege(f'earntrump_coins same {earntrump_coins}| count:{refresh_count} | {seconds_only}')
                            refresh_count = 0
                            sb1.switch_to.window(earntrump_window)
                            sb1.uc_open('https://earn-trump.com/member/faucet')


                        if feyorra_limit_reached or earnpp_limit_reached or earnbonk_limit_reached or earntrump_limit_reached:
                            pass
                        else:
                            if refresh_count >= 50:
                                reset_count +=5
                            refresh_count +=1
                    else:
                        earnpp_coins_pre = earnpp_coins
                        feyorra_coins_pre = feyorra_coins
                        claimc_coins_pre = claimc_coins
                        earntrump_coins_pre = earntrump_coins
                        earnbonk_coins_pre = earnbonk_coins
                        refresh_count = 0

                elapsed_time3 = time.time() - start_time3
                seconds_only3 = int(elapsed_time3)
                debug_messages(f'MangoDB Seconds:{seconds_only3}')
                if seconds_only3 > 130:
                    quer2y = {"type": "main"}
                    dochh2 = collection.find_one(quer2y)
                    layout_test = dochh2["withdraw_mail"]
                    if layout_test != layout:
                        print('Wrong Farm layout')
                        reset_count +=30

                    print(f'EarnPP:{earnpp_coins} | Feyorra:{feyorra_coins} | Trump:{earntrump_coins}|BONK:{earnbonk_coins} ')
                    if earnpp_coins and feyorra_coins and earnbonk_coins and earntrump_coins: 
                        start_time3 = time.time()
                        Script_Started_elsg = time.time() - Script_Started
                        emailgg = f'{earnpp_email} <br>country: {server_name1} <br>Current Layout:{layout} <br>Farm:{farm_id} <br>Pre-Session Reset:{previous_script_seconds_only} <br>Session Reset:{script_seconds_only}'
                        solving_accuracy = calculate_accuracy_captchas(total_captchas_received, failed_captchas)
                        winning_captcha_amount = total_captchas_received - failed_captchas
                        accuracy_info = f'Ratio: {winning_captcha_amount} / {total_captchas_received} <br> Accuracy : {solving_accuracy}%'

                        insert_data(ip_address, earnpp_coins, feyorra_coins, earntrump_coins, earnbonk_coins, accuracy_info, emailgg)
                    else:
                        response_messege(f'EarnPP:{earnpp_coins} | Feyorra:{feyorra_coins} | Trump:{earntrump_coins}|BONK:{earnbonk_coins} ')
                    #elif earnpp_coins and feyorra_coins and claimc_coins:
                    #    start_time3 = time.time()
                    #    insert_data(ip_address, earnpp_coins, feyorra_coins, claimc_coins, 0)
                    
                    

                else:
                    print(f'MngoDB:{seconds_only3}')
            else:
                print('Ip fucked')
                reset_count +=4
                response_messege(f'Ip fucked|{reset_count}|{ip_address}')
                #ip_required = fix_ip(sb1, server_name1)
                #ip_address = get_ip(sb1)
    

        if mainscript == 2:
            earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required = open_faucets()
            reset_count = 0

        if mainscript == 3:
            response_messege('Ip Resettinggg...')
            reset_count_isacc = 10
            query = {"type": "main"}
            update = {"$set": {"request": 'mainscript'}}
            result = collection.update_one(query, update)



        if mainscript == 4:
            withdraw_faucet(sb1, 1) 
            reset_count +=30

        if mainscript == 6:
            pass

        if mainscript == 8:
            sb1.quit()
            break

        if mainscript == 5:
            for i in range(1,6):
                time.sleep(1)
                print('Pause...')


    except Exception as e:
        print(f'Oh Hell No{e}')
        ip_address = get_ip_OS()
        if ip_address == None:
            for i in range(5):
                ip_address = get_ip_OS()
                if vps_ip == ip_address:
                    break

                else:
                    focus_and_maximize_window("Mysterium")
                    time.sleep(2)
                    pyautogui.click(1319, 878)
                    time.sleep(4)

        response_messege(f'Oh Hell No{e}')

        if 'no such window' in str(e) or 'invalid session' in str(e) or 'NoHTTPConnectionPool' in str(e):
            response_messege(f'Resetting Browser')
            try:
                sb1.quit()
                time.sleep(2)
            except Exception as e:
                print(f"sb1.quit() failed: {e}")

            # Fallback kill
            for proc_name in ['chrome', 'chromium']:
                try:
                    subprocess.run(['pkill', '-f', proc_name], check=False, stderr=subprocess.DEVNULL)
                    print(f"All {proc_name} Hell killed (if any).")
                except Exception as e:
                    print(f"Failed to kill {proc_name} Hell: {e}")
            time.sleep(10)
            sb1 = open_browsers()
            earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required = open_faucets()
            reset_count = 0
            reset_count_isacc = 0
            Script_Started = time.time()
            previous_script_seconds_only = previous_script_seconds_cal(previous_script_seconds_only,script_seconds_only)
        reset_count +=2
     
