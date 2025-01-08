

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
import shutil
import os
import math
import subprocess


# Example usage

# Initialize the argument parser
parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument('--farm', type=int, help="Farm")
parser.add_argument('--fresh', type=int, help="Fresh")
args = parser.parse_args()
farm_id = args.farm
fresh = args.fresh
facebook_cookies = '0'



CSB1_farms = []



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


def get_mails_passowrds(farm_id):
    global server_name1
    global CSB1_farms
    global earnpp_email
    global earnpp_pass
    global feyorra_email
    global feyorra_pass
    global layout
    global mysterium_raw

    collection = db[f'Farm{farm_id}']
    quer2y = {"type": "main"}
    dochh2 = collection.find_one(quer2y)
    layout = dochh2["withdraw_mail"]
    print(f'Farm ID:{farm_id} | Layout: {layout}')

    if farm_id <= 5:
        mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
        CSB1_farms = [1, 2, 3, 4, 5]
    else:

        mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie.json"
        CSB1_farms = [6,7,8,9,10]


    if farm_id == 1:

        if '1' in layout:
            server_name1 = 'thailand'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'khabibmakanzie2@gmail.com'
            earnpp_pass = 'khabibmakanzie2'
            feyorra_email = 'khabibmakanzie2@gmail.com'
            feyorra_pass = 'khabibmakanzie2'

        elif '2' in layout:
            server_name1 = 'bulgaria' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'amytanisha250@gmail.com'
            earnpp_pass = 'amytanisha250'
            feyorra_email = 'amytanisha250@gmail.com'
            feyorra_pass = 'amytanisha250'
        elif '3' in layout:
            server_name1 = 'bulgaria' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'grandkolla999br@gmail.com'
            earnpp_pass = 'grandkolla999br'
            feyorra_email = 'grandkolla999br@gmail.com'
            feyorra_pass = 'grandkolla999br'

        elif '4' in layout:
            server_name1 = 'thailand' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'makanziekb@gmail.com'
            earnpp_pass = 'makanziekb'
            feyorra_email = 'makanziekb@gmail.com'
            feyorra_pass = 'makanziekb'
        else:
            print('Layout issue', layout)

    elif farm_id == 2:

        if '1' in layout:
            server_name1 = 'estonia'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'metroboom910@gmail.com'
            earnpp_pass = 'metroboom910'
            feyorra_email = 'metroboom910@gmail.com'
            feyorra_pass = 'metroboom910'

        elif '2' in layout:
            server_name1 = 'serbia' #'portugal'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'merlelcn@gmail.com'
            earnpp_pass = 'I2Ne7C329jJt'
            feyorra_email = 'merlelcn@gmail.com'
            feyorra_pass = 'I2Ne7C329jJt'

        elif '3' in layout:
            server_name1 = 'serbia' #'portugal'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'anrogedyyr@gmail.com'
            earnpp_pass = 'anrogedyyr'
            feyorra_email = 'anrogedyyr@gmail.com'
            feyorra_pass = 'anrogedyyr'
        elif '4' in layout:
            server_name1 = 'estonia'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'bmetoomro190@gmail.com'
            earnpp_pass = 'bmetoomro190'
            feyorra_email = 'bmetoomro190@gmail.com'
            feyorra_pass = 'bmetoomro190'
        else:
            print('Layout issue', layout)


    elif farm_id == 3:

        if '1' in layout:
            server_name1 = 'france'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'neyov32511@gmail.com'
            earnpp_pass = 'neyov32511'
            feyorra_email = 'neyov32511@gmail.com'
            feyorra_pass = 'neyov32511'

            claimc_email = 'yvonne12463@gmail.com'
            claimc_pass = 'Uwuinsta@2005'

        elif '2' in layout:
            server_name1 = 'spain' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'pennyscrambble@gmail.com'
            earnpp_pass = 'pennyscrambble'
            feyorra_email = 'pennyscrambble@gmail.com'
            feyorra_pass = 'pennyscrambble'

        elif '3' in layout:
            server_name1 = 'spain' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'berendkalpana2@gmail.com'
            earnpp_pass = 'berendkalpana2'
            feyorra_email = 'berendkalpana2@gmail.com'
            feyorra_pass = 'berendkalpana2'
        elif '4' in layout:
            server_name1 = 'france'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'voyn3642ovene@gmail.com'
            earnpp_pass = 'voyn3642ovene'
            feyorra_email = 'voyn3642ovene@gmail.com'
            feyorra_pass = 'voyn3642ovene'

        else:
            print('Layout issue', layout)


    elif farm_id == 4:

        if '1' in layout:
            server_name1 = 'hungary'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'ishdiklla333@gmail.com'
            earnpp_pass = 'ishdiklla333'
            feyorra_email = 'ishdiklla333@gmail.com'
            feyorra_pass = 'ishdiklla333'
        elif '2' in layout:
            server_name1 = 'hong kong' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'kumarsheln@gmail.com'
            earnpp_pass = 'kumarsheln'
            feyorra_email = 'kumarsheln@gmail.com'
            feyorra_pass = 'kumarsheln'
        elif '3' in layout:
            server_name1 = 'hong kong' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'andrpewrea@gmail.com'
            earnpp_pass = 'andrpewrea'
            feyorra_email = 'andrpewrea@gmail.com'
            feyorra_pass = 'andrpewrea'
        elif '4' in layout:
            server_name1 = 'hungary'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'shiladid323@gmail.com'
            earnpp_pass = 'shiladid323'
            feyorra_email = 'shiladid323@gmail.com'
            feyorra_pass = 'shiladid323'
        else:
            print('Layout issue', layout)


    elif farm_id == 5:

        if '1' in layout:
            server_name1 = 'italy'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'gihanfer907@gmail.com' #gihanfer907@gmail.com
            earnpp_pass = 'gihanfer907'
            feyorra_email = 'gihanfer907@gmail.com'
            feyorra_pass = 'gihanfer907'

        elif '2' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'howardrahul838@gmail.com'
            earnpp_pass = 'howardrahul838'
            feyorra_email = 'howardrahul838@gmail.com'
            feyorra_pass = 'howardrahul838'
        elif '3' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'redgta362@gmail.com'
            earnpp_pass = 'redgta362'
            feyorra_email = 'redgta362@gmail.com'
            feyorra_pass = 'redgta362'
        elif '4' in layout:
            server_name1 = 'italy'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'ferhng790@gmail.com'
            earnpp_pass = 'ferhng790'
            feyorra_email = 'ferhng790@gmail.com'
            feyorra_pass = 'ferhng790'
        else:
            print('Layout issue', layout)

##################################################
    elif farm_id == 6:

        if '1' in layout:
            server_name1 = 'indonesia'
            CSB1_farms = [6,7,8,9,10]
            earnpp_email = 'sevensevengk@gmail.com'
            earnpp_pass = 'sevensevengk'
            feyorra_email = 'sevensevengk@gmail.com'
            feyorra_pass = 'sevensevengk'


        elif '2' in layout:
            server_name1 = 'indonesia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'gksevn77@gmail.com'
            earnpp_pass = 'gksevn77'
            feyorra_email = 'gksevn77@gmail.com'
            feyorra_pass = 'gksevn77'

        elif '3' in layout:
            server_name1 = 'south korea' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'kg7seven@gmail.com'
            earnpp_pass = 'kg7seven'
            feyorra_email = 'kg7seven@gmail.com'
            feyorra_pass = 'kg7seven'
        elif '4' in layout:
            server_name1 = 'south korea'
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'fosengklla@gmail.com'
            earnpp_pass = 'fosengklla'
            feyorra_email = 'fosengklla@gmail.com'
            feyorra_pass = 'fosengklla'


    elif farm_id == 7:

        if '1' in layout:
            server_name1 = 'belgium'
            CSB1_farms = [6,7,8,9,10]
            earnpp_email = 'shevgraaa@gmail.com'
            earnpp_pass = 'shevgraaa'
            feyorra_email = 'shevgraaa@gmail.com'
            feyorra_pass = 'shevgraaa'

        elif '2' in layout:
            server_name1 = 'belgium' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'grshevvvv@gmail.com'
            earnpp_pass = 'grshevvvv'
            feyorra_email = 'grshevvvv@gmail.com'
            feyorra_pass = 'grshevvvv'


        elif '3' in layout:
            server_name1 = 'denmark' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'grevonshld@gmail.com'
            earnpp_pass = 'grevonshld'
            feyorra_email = 'grevonshld@gmail.com'
            feyorra_pass = 'grevonshld'
        elif '4' in layout:
            server_name1 = 'denmark'
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'sheforldnmk@gmail.com'
            earnpp_pass = 'sheforldnmk'
            feyorra_email = 'sheforldnmk@gmail.com'
            feyorra_pass = 'sheforldnmk'


    elif farm_id == 8:

        if '1' in layout:
            server_name1 = 'croatia'
            CSB1_farms = [6,7,8,9,10]
            earnpp_email = 'ahenrxaaa@gmail.com'
            earnpp_pass = 'ahenrxaaa'
            feyorra_email = 'ahenrxaaa@gmail.com'
            feyorra_pass = 'ahenrxaaa'

        elif '2' in layout:
            server_name1 = 'croatia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'rxshenaxa@gmail.com'
            earnpp_pass = 'rxshenaxa'
            feyorra_email = 'rxshenaxa@gmail.com'
            feyorra_pass = 'rxshenaxa'


        elif '3' in layout:
            server_name1 = 'saudi arabia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'rhexnargg@gmail.com'
            earnpp_pass = 'rhexnargg'
            feyorra_email = 'rhexnargg@gmail.com'
            feyorra_pass = 'rhexnargg'

        elif '4' in layout:
            server_name1 = 'saudi arabia'
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'senarxbiag@gmail.com'
            earnpp_pass = 'senarxbiag'
            feyorra_email = 'senarxbiag@gmail.com'
            feyorra_pass = 'senarxbiag'

    elif farm_id == 9:

        if '1' in layout:
            server_name1 = 'canada'
            CSB1_farms = [6,7,8,9,10]
            earnpp_email = 'semiprraaa@gmail.com'
            earnpp_pass = 'semiprraaa'
            feyorra_email = 'semiprraaa@gmail.com'
            feyorra_pass = 'semiprraaa'

        elif '2' in layout:
            server_name1 = 'canada' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'pereramishee@gmail.com'
            earnpp_pass = 'pereramishee'
            feyorra_email = 'pereramishee@gmail.com'
            feyorra_pass = 'pereramishee'



        elif '3' in layout:
            server_name1 = 'sweden' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'ramishepera@gmail.com'
            earnpp_pass = 'ramishepera'
            feyorra_email = 'ramishepera@gmail.com'
            feyorra_pass = 'ramishepera'
        elif '4' in layout:
            server_name1 = 'sweden'
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'pesheswendemi@gmail.com'
            earnpp_pass = 'pesheswendemi'
            feyorra_email = 'pesheswendemi@gmail.com'
            feyorra_pass = 'pesheswendemi'


    elif farm_id == 10:

        if '1' in layout:
            server_name1 = 'austria'
            CSB1_farms = [6,7,8,9,10]
            earnpp_email = 'melosandsong@gmail.com'
            earnpp_pass = 'melosandsong'
            feyorra_email = 'melosandsong@gmail.com'
            feyorra_pass = 'melosandsong'

        elif '2' in layout:
            server_name1 = 'austria' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'sadrameloonsan@gmail.com'
            earnpp_pass = 'sadrameloonsan'
            feyorra_email = 'sadrameloonsan@gmail.com'
            feyorra_pass = 'sadrameloonsan'


        elif '3' in layout:
            server_name1 = 'lithuania' 
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'mlsansonone@gmail.com'
            earnpp_pass = 'mlsansonone'
            feyorra_email = 'mlsansonone@gmail.com'
            feyorra_pass = 'mlsansonone'
        elif '4' in layout:
            server_name1 = 'lithuania'
            CSB1_farms = [6, 7, 8, 9, 10]
            earnpp_email = 'saradmsnire@gmail.com'
            earnpp_pass = 'saradmsnire'
            feyorra_email = 'saradmsnire@gmail.com'
            feyorra_pass = 'saradmsnire'




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


debug_mode = True
get_mails_passowrds(farm_id)
ip_required = 0
#farm_id = 1

run_sb1 = True
with_baymack = True


chrome_binary_path = '/opt/google/chrome/google-chrome'
chrome_user_data_dir = '/root/.config/google-chrome/'


bitmoon = False
earnpp = True
claimcoin = False
feyorra = True
feyorratop = False
baymack = False


ocr = None #PaddleOCR(use_angle_cls=True, lang='en',  drop_score=0)



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

def insert_data(ip, amount1, amount2, amount3,emailg):
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')

    query = {"type": "main"}
    sample_document = {
        "Email": emailg,
        "pepelom": amount1,
        "feyorramack": amount2,
        "claimcoins": amount3,
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
    add_messages('pepelom', {now: amount1})
    add_messages('feyorramack', {now: amount2})
    add_messages('claimcoins', {now: amount3})

    return






def get_ip(driver):
    for i in range(1,5):
        try:
            original_window = driver.current_window_handle
            driver.open_new_window()
            try:
                #driver.switch_to.newest_window()
                driver.get('https://api.ipify.org/')
                ip_address = driver.get_text('body')
                print('IP =', ip_address)
                driver.close()
                driver.connect()
                driver.switch_to.window(original_window)
                
                return ip_address
            
            except Exception as e:
                print(e)
            driver.close() 
            driver.connect()
            driver.switch_to.window(original_window)
        except Exception as e:
            print(e)

    return None


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

        print(f"IP Address: {ip} \nProxy Status: {proxy_status} \nCountry: {country}")
        if country.lower() in server_name.lower():
            if proxy_status == 'no':
                val = 200
            else:
                print(f'{country} is valid with not proxy status.')
                val = 50
        else:
            return 301
        sb1.close()
        sb1.connect()
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
                return 301
        else:
            print("Error: Status not OK : Trying Inbrowser Way")
            val = get_proxycheck_inbrowser(driver, ip, server_name)
            return val
    except requests.RequestException as e:
        print(f"Error retrieving IP address and proxy status: {e}")
        return False


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
            and fraud_score <= 95
        ):
            print("Conditions met: Returning True")
            return True
        else:
            print("Conditions not met: Returning None")
            return None

    except requests.RequestException as e:
        print(f"Error retrieving IP data: {e}")
        return None


def mysterium_vpn_Recon_ip(server_name, driver):
    mysterium_reinstaller()
    fix_wrong_pins()
    print('Rcon')
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.95)
        pyautogui.click(x, y)
        print("mysterium_icon_empty Found")
        time.sleep(5)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/myserium_disconnect.png", region=(1325, 190, 800, 400), confidence=0.95)
            #pyautogui.click(x, y)
            print("myserium_disconnect Found")
            unknown_con = True
            while unknown_con == True:
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/Unknown.png", region=(1345, 90, 800, 400), confidence=0.95)
                    #pyautogui.click(x, y)
                    print("Unkown Found")
                    unknown_con = True
                except pyautogui.ImageNotFoundException:
                    print("No Unkown .")
                    unknown_con = False
            
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/recon.png", region=(1345, 90, 800, 600), confidence=0.95)
                pyautogui.click(x, y)
                print("recon Found")
                time.sleep(5)
                return True
            except pyautogui.ImageNotFoundException:
                print("No recon .")

        except pyautogui.ImageNotFoundException:
            print("No myserium_disconnect .")

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_login.png", region=(1375, 543, 600, 300), confidence=0.9)
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
                    time.sleep(10)
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

def mysterium_vpn_connect(server_name, driver):
    mysterium_reinstaller()
    fix_wrong_pins()
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
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_login.png", region=(1375, 543, 600, 300), confidence=0.9)
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
                time.sleep(10)
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
        get_mails_passowrds(farm_id)
        ip_address = get_ip(drive)
        quer2y = {"type": "main"}
        dochh2 = collection.find_one(quer2y)
        layout2 = dochh2["withdraw_mail"]
        global blacklistedIP
        collectionbip = db[f'LocalCSB']
        quer2y = {"type": "main"}
        dochh = collectionbip.find_one(quer2y)
        blacklistedIP2 = dochh["blacklistedIP"]
        if len(blacklistedIP) <= len(blacklistedIP2):
            blacklistedIP += blacklistedIP2
        print(blacklistedIP)
        lay = re.search(r'\d+', layout2).group()
        other_blacklists = get_blacklistedip2(f'F{farm_id}L{lay}')
        if other_blacklists:
                blacklistedIP = blacklistedIP + other_blacklists
        if ip_address in blacklistedIP:
            print(f'Bad IP detected: {ip_address}. Changing IP...1')
            query = {"type": "main"}
            update = {"$set": {"response": f'Blacklisted IP🔴: {ip_address}'}}
            result = collection.update_one(query, update)
            for i in CSB1_farms:
                collection_csb = db[f'Farm{i}']
                update = {"$set": {"request": 'ipfixer'}}
                result = collection_csb.update_one(query, update)
                print('Update Farm', i)
                
            # Ensure this block is properly indented
            proxycheck = get_proxycheck(drive, ip_address, server_name=name)
            if proxycheck == 50 or proxycheck == 200 or proxycheck != 301:
                #mysterium_vpn_Recon_ip(name, drive)
                mysterium_vpn_connect(name, drive)
            else:
                mysterium_vpn_connect(name, drive)
                
            print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
            time.sleep(5)
        else:
            ipscore = get_ipscore(ip_address)
            proxycheck = get_proxycheck(drive, ip_address, server_name= name)
            if ipscore and proxycheck == 200:
                print(f'Good IP found: {ip_address}')
                return ip_address
            else:
                print(f'Bad IP detected: {ip_address}. Changing IP...2')
                query = {"type": "main"}
                update = {"$set": {"response": f'Changed IP🔴: {ip_address}'}}
                result = collection.update_one(query, update)
                for i in CSB1_farms:
                    collection_csb = db[f'Farm{i}']
                    update = {"$set": {"request": 'ipfixer'}}
                    result = collection_csb.update_one(query, update)
                    print('Update Farm', i)
                if proxycheck == 50 or proxycheck == 200 or proxycheck != 301:
                    #mysterium_vpn_Recon_ip(name, drive)
                    mysterium_vpn_connect(name, drive)
                else:
                    mysterium_vpn_connect(name, drive)
                print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
                time.sleep(5)


####################################Control Panel Shit##########################################################
def mysterium_web_login(driver):
    driver.uc_open('https://app.mysteriumvpn.com/')
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
                time.sleep(3)
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
                        clipboard.copy(text_content)
                        pyautogui.click(1385, 310)
                        time.sleep(1)
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('v')
                        pyautogui.keyUp('ctrl')
                        #pyautogui.typewrite(text_content)
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
        mysterium_reinstaller()
        response_messege('Changed IP🔴 :Mys installed')
        fix_wrong_pins()
        time.sleep(1)
        sweet_enable()
        driver.uc_open('https://app.mysteriumvpn.com/')
        time.sleep(7)
        titile = sb1.get_title()
        pyautogui.click(113, 100)
        

        if 'Home' in titile:

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.95)
                pyautogui.click(x, y)
                print("mysterium_icon_empty Found")
                i = 1
                for i in range(1, 10):
                    time.sleep(1)
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_login.png", region=(1375, 543, 600, 300), confidence=0.9)
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
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/settings_mysterium.png", region=(1445, 630, 400, 300), confidence=0.9)
                                            pyautogui.click(x, y)
                                            print("settings_mysterium 2 Found")
                                            time.sleep(1)
                                        except pyautogui.ImageNotFoundException:
                                            print("No settings_mysterium 2.")

                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/connection_mysterium_option.png", region=(1325, 109, 800, 900), confidence=0.9)
                                            pyautogui.click(x, y)
                                            print("connection_mysterium_option Found")
                                            time.sleep(1)
                                        except pyautogui.ImageNotFoundException:
                                            print("No connection_mysterium_option.")

                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/refresh_ip_off.png", region=(1325, 109, 800, 900), confidence=0.9)
                                            pyautogui.click(1640, 300)
                                            pyautogui.click(1668, 300)
                                            pyautogui.click(1714, 300)
                                            print("refresh_ip_off Found")
                                            time.sleep(1)
                                        except pyautogui.ImageNotFoundException:
                                            print("No refresh_ip_off.")

                                        try:
                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/refresh_ip_on.png", region=(1325, 109, 800, 900), confidence=0.9)
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
        elif 'Just' in titile:
            cloudflare(driver, login = False)
        elif 'Dashboard' in titile:
            mysterium_web_login(driver)
        else:
            try:
                response_messege('Mysterium Login')
            except Exception as e:
                pass


def ipfixer():
    ip = 0
    preip = 0
    respo = 0
    gg2344 = 0
    query = {"type": "main"}
    update = {"$set": {"response": 'Fixing...🟠'}}
    result = collection.update_one(query, update)
    #for i in CSB1_farms:
    #    collection_csb = db[f'Farm{i}']
    #    update = {"$set": {"request": 'ipfixer'}}
    #    result = collection_csb.update_one(query, update)
    #    print('Update Farm', i)

    while True:
        
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        doc = collection.find_one(query)
        request = doc["request"]
        if request == 'ipfixer':
            preip = get_ip(sb1)
            if preip:
                if ip == preip:
                        sri_lanka_tz = pytz.timezone('Asia/Colombo')
                        utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                        sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                        now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                        print(now)
                        print(f'Good IP found: {ip} |{now}')
                        query = {"type": "main"}
                        update = {"$set": {"response": f'Ready IP🟢: {ip} | {now}'}}
                        result = collection.update_one(query, update)
                        time.sleep(6)
                        print('Result:',result)
                        print(f"repo {respo}")
                        res_farms = []
                        for frm in CSB1_farms:
                            collection_csb = db[f'Farm{frm}']
                            query = {"type": "main"}
                            doc = collection_csb.find_one(query)
                            res = doc["response"]
                            req = doc["request"]
                            if req == 'ipfixer' and 'Ready IP' in res:
                                res_farms.append(res)
                            elif req == 'ipfixer' and 'Loging' in res:
                                res_farms.append(res)
                            elif req == 'mainscript': #and 'Running' in res:
                                res_farms.append(res)
                            elif req == 'mainscript': #and 'Ready IP' in res:
                                res_farms.append(res)
                            else:
                                print('aiyo', req)
                        if len(res_farms) == len(CSB1_farms):
                            time.sleep(8)
                            if gg2344 > 6:

                                query = {"type": "main"}
                                update = {"$set": {"request": 'mainscript'}}
                                result = collection.update_one(query, update)
                            else:
                                gg2344 += 1
                        else:
                            gg2344 = 1
                        time.sleep(7)
                            

                    
                else:
                    respo = 0
                    
                    sri_lanka_tz = pytz.timezone('Asia/Colombo')
                    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                    print(now)
                    update = {"$set": {"response": f'Changed IP🔴: {preip} |{now}'}}
                    result = collection.update_one(query, update)
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
    return None



def capture_element_screenshot(driver, selector, screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png"):
    # Step 1: Find the element using SeleniumBase
    element = driver.find_element(selector)
    
    # Step 2: Get element's location and size
    location = element.location
    size = element.size
    y_location = location['y'] + 100
    driver.execute_script(f"window.scrollTo(0, {y_location});")
    #time.sleep(1)

    # Step 3: Capture the full-page screenshot
    driver.save_screenshot(screenshot_path)
    element = driver.find_element(selector)
    
    # Step 2: Get element's location and size
    location = element.location
    size = element.size
    # Step 4: Load the full screenshot with Pillow
    screenshot = Image.open(screenshot_path)
    scroll_y = driver.execute_script("return window.scrollY;")
    # Step 5: Define the crop area using the element's location and size
    left = location['x']
    top = location['y'] - scroll_y
    right = left + size['width']
    bottom = top + size['height'] 
    print(left, top, right, bottom)
    # Step 6: Crop the image to the element's size
    cropped_image = screenshot.crop((left, top, right, bottom))
    
    # Step 7: Save the cropped image
    cropped_image.save(cropped_path)
    
    print(f"Cropped screenshot saved at {cropped_path}")



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

def solve_icon_captcha_v1(sb1):
    try:
        # Extract all captcha icons
        #captcha_icons = sb1.find_elements('div[class*="fas fa-"]')  # Locate 'div' with 'fas fa-' in class
        captcha_icons = sb1.find_elements('[class*="fas fa-"]')
        
        for captcha_icon in captcha_icons:
            # Get the class names of the captcha icon
            captcha_icon_classes = captcha_icon.get_attribute('class').split()
            captcha_icon_classes = [cls for cls in captcha_icon_classes if cls.startswith("fa-")]

            if not captcha_icon_classes:
                continue  # Skip if no valid 'fa-' class found

            captcha_icon_class = captcha_icon_classes[0]  # Use the first valid 'fa-' class

            # Get the available icon options (filter out decoys)
            icon_options = sb1.find_elements('i[class*="fas fa-"]')  # Find 'i' elements with 'fas fa-' in class

            for option in icon_options:
                option_classes = option.get_attribute('class').split()
                if captcha_icon_class in option_classes:
                    try:
                        option.uc_click()  # Custom click method to handle undetected Selenium
                        print(f"Clicked on the matching icon: {captcha_icon_class}")
                        return True  # Return immediately after a successful click
                    except Exception as e:
                        print(f"Error clicking on icon: {e}")
                        continue  # Continue to the next option if clicking fails

        print("No matching icon found.")
        return False  # Return False if no matching icon was clicked
    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False

icon_path_list = {
    "heart": "M473.7 73.8l-2.4-2.5c-46-47-118-51.7-169.6-14.8L336 159.9l-96 64 48 128-144-144 96-64-28.6-86.5C159.7 19.6 87 24 40.7 71.4l-2.4 2.4C-10.4 123.6-12.5 202.9 31 256l212.1 218.6c7.1 7.3 18.6 7.3 25.7 0L481 255.9c43.5-53 41.4-132.3-7.3-182.1z",
    "coin": "M12.0049 4.00281C18.08 4.00281 23.0049 6.6891 23.0049 10.0028V14.0028C23.0049 17.3165 18.08 20.0028 12.0049 20.0028C6.03824 20.0028 1.18114 17.4116 1.00957 14.1797L1.00488 14.0028V10.0028C1.00488 6.6891 5.92975 4.00281 12.0049 4.00281ZM12.0049 16.0028C8.28443 16.0028 4.99537 14.9953 3.00466 13.4533L3.00488 14.0028C3.00488 15.885 6.88751 18.0028 12.0049 18.0028C17.0156 18.0028 20.8426 15.9723 20.9999 14.1207L21.0049 14.0028L21.0061 13.4525C19.0155 14.995 15.726 16.0028 12.0049 16.0028ZM12.0049 6.00281C6.88751 6.00281 3.00488 8.12061 3.00488 10.0028C3.00488 11.885 6.88751 14.0028 12.0049 14.0028C17.1223 14.0028 21.0049 11.885 21.0049 10.0028C21.0049 8.12061 17.1223 6.00281 12.0049 6.00281Z",
    "volume": "M215 71.1L126.1 160H24c-13.3 0-24 10.7-24 24v144c0 13.3 10.7 24 24 24h102.1l89 89c15 15 41 4.5 41-17V88c0-21.5-26-32-41-17zm233.3-51.1c-11.2-7.3-26.2-4.2-33.5 7-7.3 11.2-4.2 26.2 7 33.5 66.3 43.5 105.8 116.6 105.8 195.6 0 79-39.6 152.1-105.8 195.6-11.2 7.3-14.3 22.3-7 33.5 7 10.7 21.9 14.6 33.5 7C528.3 439.6 576 351.3 576 256S528.3 72.4 448.4 20zM480 256c0-63.5-32.1-121.9-85.8-156.2-11.2-7.1-26-3.8-33.1 7.5s-3.8 26.2 7.4 33.4C408.3 166 432 209.1 432 256s-23.7 90-63.5 115.4c-11.2 7.1-14.5 22.1-7.4 33.4 6.5 10.4 21.1 15.1 33.1 7.5C447.9 377.9 480 319.5 480 256zm-141.8-76.9c-11.6-6.3-26.2-2.2-32.6 9.5-6.4 11.6-2.2 26.2 9.5 32.6C328 228.3 336 241.6 336 256c0 14.4-8 27.7-20.9 34.8-11.6 6.4-15.8 21-9.5 32.6 6.4 11.7 21.1 15.8 32.6 9.5 28.2-15.6 45.8-45 45.8-76.9s-17.5-61.3-45.8-76.9z",
    "android": "M420.6 301.9a24 24 0 1 1 24-24 24 24 0 0 1 -24 24m-265.1 0a24 24 0 1 1 24-24 24 24 0 0 1 -24 24m273.7-144.5 47.9-83a10 10 0 1 0 -17.3-10h0l-48.5 84.1a301.3 301.3 0 0 0 -246.6 0L116.2 64.5a10 10 0 1 0 -17.3 10h0l47.9 83C64.5 202.2 8.2 285.6 0 384H576c-8.2-98.5-64.5-181.8-146.9-226.6",
    "chrome": "M16 8a8 8 0 0 1-7.022 7.94l1.902-7.098a3 3 0 0 0 .05-1.492A3 3 0 0 0 10.237 6h5.511A8 8 0 0 1 16 8M0 8a8 8 0 0 0 7.927 8l1.426-5.321a3 3 0 0 1-.723.255 3 3 0 0 1-1.743-.147 3 3 0 0 1-1.043-.7L.633 4.876A8 8 0 0 0 0 8m5.004-.167L1.108 3.936A8.003 8.003 0 0 1 15.418 5H8.066a3 3 0 0 0-1.252.243 2.99 2.99 0 0 0-1.81 2.59M8 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4",
    "mouse": "M15.3873 13.4975L17.9403 20.5117L13.2418 22.2218L10.6889 15.2076L6.79004 17.6529L8.4086 1.63318L19.9457 12.8646L15.3873 13.4975ZM15.3768 19.3163L12.6618 11.8568L15.6212 11.4459L9.98201 5.9561L9.19088 13.7863L11.7221 12.1988L14.4371 19.6583L15.3768 19.3163Z",
    "truck": "M624 224h-16v-64c0-17.7-14.3-32-32-32h-73.6L419.2 24A64 64 0 0 0 369.2 0H256c-17.7 0-32 14.3-32 32v96H48c-8.8 0-16 7.2-16 16v80H16c-8.8 0-16 7.2-16 16v32c0 8.8 7.2 16 16 16h16.7c29.2-38.7 75.1-64 127.3-64s98.1 25.4 127.3 64h65.5c29.2-38.7 75.1-64 127.3-64s98.1 25.4 127.3 64H624c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zm-336-96V64h81.2l51.2 64H288zm304 224h-5.2c-2.2-7.3-5.1-14.3-8.7-20.9l3.7-3.7c6.3-6.3 6.3-16.4 0-22.6l-22.6-22.6c-6.3-6.3-16.4-6.3-22.6 0l-3.7 3.7A110.9 110.9 0 0 0 512 277.2V272c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v5.2c-7.3 2.2-14.3 5.1-20.9 8.7l-3.7-3.7c-6.3-6.3-16.4-6.3-22.6 0l-22.6 22.6c-6.3 6.3-6.3 16.4 0 22.6l3.7 3.7A110.9 110.9 0 0 0 373.2 352H368c-8.8 0-16 7.2-16 16v32c0 8.8 7.2 16 16 16h5.2c2.2 7.3 5.1 14.3 8.7 20.9l-3.7 3.7c-6.3 6.3-6.3 16.4 0 22.6l22.6 22.6c6.3 6.3 16.4 6.3 22.6 0l3.7-3.7c6.6 3.6 13.6 6.5 20.9 8.7v5.2c0 8.8 7.2 16 16 16h32c8.8 0 16-7.2 16-16v-5.2c7.3-2.2 14.3-5.1 20.9-8.7l3.7 3.7c6.3 6.3 16.4 6.3 22.6 0l22.6-22.6c6.3-6.3 6.3-16.4 0-22.6l-3.7-3.7a110.9 110.9 0 0 0 8.7-20.9h5.2c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zm-112 80c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm-208-80h-5.2c-2.2-7.3-5.1-14.3-8.7-20.9l3.7-3.7c6.3-6.3 6.3-16.4 0-22.6l-22.6-22.6c-6.3-6.3-16.4-6.3-22.6 0l-3.7 3.7A110.9 110.9 0 0 0 192 277.2V272c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v5.2c-7.3 2.2-14.3 5.1-20.9 8.7l-3.7-3.7c-6.3-6.3-16.4-6.3-22.6 0L58.2 304.8c-6.3 6.3-6.3 16.4 0 22.6l3.7 3.7a110.9 110.9 0 0 0 -8.7 20.9H48c-8.8 0-16 7.2-16 16v32c0 8.8 7.2 16 16 16h5.2c2.2 7.3 5.1 14.3 8.7 20.9l-3.7 3.7c-6.3 6.3-6.3 16.4 0 22.6l22.6 22.6c6.3 6.3 16.4 6.3 22.6 0l3.7-3.7c6.6 3.6 13.6 6.5 20.9 8.7v5.2c0 8.8 7.2 16 16 16h32c8.8 0 16-7.2 16-16v-5.2c7.3-2.2 14.3-5.1 20.9-8.7l3.7 3.7c6.3 6.3 16.4 6.3 22.6 0l22.6-22.6c6.3-6.3 6.3-16.4 0-22.6l-3.7-3.7a110.9 110.9 0 0 0 8.7-20.9h5.2c8.8 0 16-7.2 16-16v-32C288 359.2 280.8 352 272 352zm-112 80c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48z",
    "rocket": "M4 13a8 8 0 0 1 7 7a6 6 0 0 0 3 -5a9 9 0 0 0 6 -8a3 3 0 0 0 -3 -3a9 9 0 0 0 -8 6a6 6 0 0 0 -5 3",
    "apple": "M15.778 8.20793C15.3053 8.1711 14.7974 8.28434 14.0197 8.58067C14.085 8.55577 13.2775 8.87173 13.0511 8.95077C12.5494 9.12593 12.1364 9.22198 11.6734 9.22198C11.2151 9.22198 10.7925 9.13042 10.3078 8.96683C10.1524 8.91441 9.99616 8.8564 9.80283 8.7809C9.71993 8.74852 9.41997 8.62947 9.3544 8.60379C8.70626 8.34996 8.34154 8.25434 8.03885 8.26181C6.88626 8.2765 5.79557 8.9421 5.16246 10.0442C3.87037 12.2875 4.58583 16.3428 6.47459 19.075C7.4802 20.5189 8.03062 21.035 8.25199 21.0279C8.4743 21.0183 8.63777 20.9713 9.03567 20.8026C9.11485 20.7689 9.11485 20.7689 9.202 20.7317C10.2077 20.3032 10.9118 20.114 11.9734 20.114C12.9944 20.114 13.6763 20.2997 14.6416 20.7159C14.7302 20.7542 14.7302 20.7542 14.8097 20.7884C15.2074 20.9588 15.3509 20.9962 15.6016 20.9902C15.9591 20.9846 16.4003 20.5726 17.3791 19.1362C17.6471 18.7447 17.884 18.3333 18.0895 17.9168C17.9573 17.8077 17.826 17.6917 17.6975 17.5693C16.4086 16.3408 15.6114 14.6845 15.5895 12.6391C15.5756 11.0186 16.1057 9.61487 16.999 8.45797C16.6293 8.3142 16.2216 8.23805 15.778 8.20793ZM15.9334 6.21398C16.6414 6.26198 18.6694 6.47798 19.9894 8.40998C19.8814 8.46998 17.5654 9.81397 17.5894 12.622C17.6254 15.982 20.5294 17.098 20.5654 17.11C20.5414 17.194 20.0974 18.706 19.0294 20.266C18.1054 21.622 17.1454 22.966 15.6334 22.99C14.1454 23.026 13.6654 22.114 11.9734 22.114C10.2694 22.114 9.74138 22.966 8.33738 23.026C6.87338 23.074 5.76938 21.562 4.83338 20.218C2.92538 17.458 1.47338 12.442 3.42938 9.04597C4.40138 7.35397 6.12938 6.28598 8.01338 6.26198C9.44138 6.22598 10.7974 7.22198 11.6734 7.22198C12.5374 7.22198 14.0854 6.06998 15.9334 6.21398ZM14.7934 4.38998C14.0134 5.32598 12.7414 6.05798 11.5054 5.96198C11.3374 4.68998 11.9614 3.35798 12.6814 2.52998C13.4854 1.59398 14.8294 0.897976 15.9454 0.849976C16.0894 2.14598 15.5734 3.45398 14.7934 4.38998Z",
    "thumb": "M7 11v8a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-7a1 1 0 0 1 1 -1h3a4 4 0 0 0 4 -4v-1a2 2 0 0 1 4 0v5h3a2 2 0 0 1 2 2l-1 5a2 3 0 0 1 -2 2h-7a3 3 0 0 1 -3 -3",
    "bank": "M2 20H22V22H2V20ZM4 12H6V19H4V12ZM9 12H11V19H9V12ZM13 12H15V19H13V12ZM18 12H20V19H18V12ZM2 7L12 2L22 7V11H2V7ZM12 8C12.5523 8 13 7.55228 13 7C13 6.44772 12.5523 6 12 6C11.4477 6 11 6.44772 11 7C11 7.55228 11.4477 8 12 8Z",
    "music": "M470.4 1.5L150.4 96A32 32 0 0 0 128 126.5v261.4A139 139 0 0 0 96 384c-53 0-96 28.7-96 64s43 64 96 64 96-28.7 96-64V214.3l256-75v184.6a138.4 138.4 0 0 0 -32-3.9c-53 0-96 28.7-96 64s43 64 96 64 96-28.7 96-64V32a32 32 0 0 0 -41.6-30.5z",
    "award": "M97.1 362.6c-8.7-8.7-4.2-6.2-25.1-11.9-9.5-2.6-17.9-7.5-25.4-13.3L1.2 448.7c-4.4 10.8 3.8 22.5 15.4 22l52.7-2L105.6 507c8 8.4 22 5.8 26.4-5l52.1-127.6c-10.8 6-22.9 9.6-35.3 9.6-19.5 0-37.8-7.6-51.6-21.4zM382.8 448.7l-45.4-111.2c-7.6 5.9-15.9 10.8-25.4 13.3-21.1 5.6-16.5 3.2-25.1 11.9-13.8 13.8-32.1 21.4-51.6 21.4-12.4 0-24.5-3.6-35.3-9.6L252 502c4.4 10.8 18.4 13.4 26.4 5l36.3-38.3 52.7 2c11.6 .4 19.8-11.3 15.4-22zM263 340c15.3-15.6 17-14.2 38.8-20.1 13.9-3.8 24.8-14.8 28.5-29 7.5-28.4 5.5-25 26-45.8 10.2-10.4 14.1-25.4 10.4-39.6-7.5-28.4-7.5-24.4 0-52.8 3.7-14.1-.3-29.2-10.4-39.6-20.4-20.8-18.5-17.4-26-45.8-3.7-14.1-14.6-25.2-28.5-29-27.9-7.6-24.5-5.6-45-26.4-10.2-10.4-25-14.4-38.9-10.6-27.9 7.6-24 7.6-51.9 0-13.9-3.8-28.7 .3-38.9 10.6-20.4 20.8-17.1 18.8-44.9 26.4-13.9 3.8-24.8 14.8-28.5 29-7.5 28.4-5.5 25-26 45.8-10.2 10.4-14.2 25.4-10.4 39.6 7.5 28.4 7.5 24.4 0 52.8-3.7 14.1 .3 29.2 10.4 39.6 20.4 20.8 18.5 17.4 26 45.8 3.7 14.1 14.6 25.2 28.5 29C104.6 326 106.3 325 121 340c13.2 13.5 33.8 15.9 49.7 5.8a39.7 39.7 0 0 1 42.5 0c15.9 10.1 36.5 7.7 49.7-5.8zM97.7 176c0-53 42.2-96 94.3-96s94.3 43 94.3 96-42.2 96-94.3 96-94.3-43-94.3-96z",
    "house": "m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25",
    "emo": "M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm33.8 161.7l80-48c11.6-6.9 24 7.7 15.4 18L343.6 180l33.6 40.3c8.7 10.4-3.9 24.8-15.4 18l-80-48c-7.7-4.7-7.7-15.9 0-20.6zm-163-30c-8.6-10.3 3.8-24.9 15.4-18l80 48c7.8 4.7 7.8 15.9 0 20.6l-80 48c-11.5 6.8-24-7.6-15.4-18l33.6-40.3-33.6-40.3zM398.9 306C390 377 329.4 432 256 432h-16c-73.4 0-134-55-142.9-126-1.2-9.5 6.3-18 15.9-18h270c9.6 0 17.1 8.4 15.9 18z",
    "blue": "m8.543 3.948 1.316 1.316L8.543 6.58zm0 8.104 1.316-1.316L8.543 9.42zm-1.41-4.043L4.275 5.133l.827-.827L7.377 6.58V1.128l4.137 4.136L8.787 8.01l2.745 2.745-4.136 4.137V9.42l-2.294 2.274-.827-.827zM7.903 16c3.498 0 5.904-1.655 5.904-8.01 0-6.335-2.406-7.99-5.903-7.99S2 1.655 2 8.01C2 14.344 4.407 16 7.904 16Z",
    "file": "M6 7V4C6 3.44772 6.44772 3 7 3H13.4142L15.4142 5H21C21.5523 5 22 5.44772 22 6V16C22 16.5523 21.5523 17 21 17H18V20C18 20.5523 17.5523 21 17 21H3C2.44772 21 2 20.5523 2 20V8C2 7.44772 2.44772 7 3 7H6ZM6 9H4V19H16V17H6V9ZM8 5V15H20V7H14.5858L12.5858 5H8Z",
    "gift": "M21 11.25v8.25a1.5 1.5 0 0 1-1.5 1.5H5.25a1.5 1.5 0 0 1-1.5-1.5v-8.25M12 4.875A2.625 2.625 0 1 0 9.375 7.5H12m0-2.625V7.5m0-2.625A2.625 2.625 0 1 1 14.625 7.5H12m0 0V21m-8.625-9.75h18c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125h-18c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z",
    "display": "M8 1a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1zm1 13.5a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0m2 0a.5.5 0 1 0 1 0 .5.5 0 0 0-1 0M9.5 1a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM9 3.5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 0-1h-5a.5.5 0 0 0-.5.5M1.5 2A1.5 1.5 0 0 0 0 3.5v7A1.5 1.5 0 0 0 1.5 12H6v2h-.5a.5.5 0 0 0 0 1H7v-4H1.5a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .5-.5H7V2z",
    "flag": "M3 3v1.5M3 21v-6m0 0 2.77-.693a9 9 0 0 1 6.208.682l.108.054a9 9 0 0 0 6.086.71l3.114-.732a48.524 48.524 0 0 1-.005-10.499l-3.11.732a9 9 0 0 1-6.085-.711l-.108-.054a9 9 0 0 0-6.208-.682L3 4.5M3 15V4.5",
    "cat": "M20 3v10a8 8 0 1 1 -16 0v-10l3.432 3.432a7.963 7.963 0 0 1 4.568 -1.432c1.769 0 3.403 .574 4.728 1.546l3.272 -3.546z",
    "comment": "M8.625 9.75a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 0 1 .778-.332 48.294 48.294 0 0 0 5.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z",
    "cake": "M12 8.25v-1.5m0 1.5c-1.355 0-2.697.056-4.024.166C6.845 8.51 6 9.473 6 10.608v2.513m6-4.871c1.355 0 2.697.056 4.024.166C17.155 8.51 18 9.473 18 10.608v2.513M15 8.25v-1.5m-6 1.5v-1.5m12 9.75-1.5.75a3.354 3.354 0 0 1-3 0 3.354 3.354 0 0 0-3 0 3.354 3.354 0 0 1-3 0 3.354 3.354 0 0 0-3 0 3.354 3.354 0 0 1-3 0L3 16.5m15-3.379a48.474 48.474 0 0 0-6-.371c-2.032 0-4.034.126-6 .371m12 0c.39.049.777.102 1.163.16 1.07.16 1.837 1.094 1.837 2.175v5.169c0 .621-.504 1.125-1.125 1.125H4.125A1.125 1.125 0 0 1 3 20.625v-5.17c0-1.08.768-2.014 1.837-2.174A47.78 47.78 0 0 1 6 13.12M12.265 3.11a.375.375 0 1 1-.53 0L12 2.845l.265.265Zm-3 0a.375.375 0 1 1-.53 0L9 2.845l.265.265Zm6 0a.375.375 0 1 1-.53 0L15 2.845l.265.265Z",
    "notifi": "M14.857 17.082a23.848 23.848 0 0 0 5.454-1.31A8.967 8.967 0 0 1 18 9.75V9A6 6 0 0 0 6 9v.75a8.967 8.967 0 0 1-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 0 1-5.714 0m5.714 0a3 3 0 1 1-5.714 0M3.124 7.5A8.969 8.969 0 0 1 5.292 3m13.416 0a8.969 8.969 0 0 1 2.168 4.5",
    "leaf": "M20.998 3V5C20.998 14.6274 15.6255 19 8.99805 19L5.24077 18.9999C5.0786 19.912 4.99805 20.907 4.99805 22H2.99805C2.99805 20.6373 3.11376 19.3997 3.34381 18.2682C3.1133 16.9741 2.99805 15.2176 2.99805 13C2.99805 7.47715 7.4752 3 12.998 3C14.998 3 16.998 4 20.998 3ZM12.998 5C8.57977 5 4.99805 8.58172 4.99805 13C4.99805 13.3624 5.00125 13.7111 5.00759 14.0459C6.26198 12.0684 8.09902 10.5048 10.5019 9.13176L11.4942 10.8682C8.6393 12.4996 6.74554 14.3535 5.77329 16.9998L8.99805 17C15.0132 17 18.8692 13.0269 18.9949 5.38766C17.6229 5.52113 16.3481 5.436 14.7754 5.20009C13.6243 5.02742 13.3988 5 12.998 5Z",
    "signal": "M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 0 1 3 19.875v-6.75ZM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V8.625ZM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 0 1-1.125-1.125V4.125Z",
    "cloud": "M2.25 15a4.5 4.5 0 0 0 4.5 4.5H18a3.75 3.75 0 0 0 1.332-7.257 3 3 0 0 0-3.758-3.848 5.25 5.25 0 0 0-10.233 2.33A4.502 4.502 0 0 0 2.25 15Z",
    "energy": "m3.75 13.5 10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75Z",
    "eye": "M2.036 12.322a1.012 1.012 0 0 1 0-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178Z",
    "plane": "M15.59 14.37a6 6 0 0 1-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 0 0 6.16-12.12A14.98 14.98 0 0 0 9.631 8.41m5.96 5.96a14.926 14.926 0 0 1-5.841 2.58m-.119-8.54a6 6 0 0 0-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 0 0-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 0 1-2.448-2.448 14.9 14.9 0 0 1 .06-.312m-2.24 2.39a4.493 4.493 0 0 0-1.757 4.306 4.493 4.493 0 0 0 4.306-1.758M16.5 9a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z",
    "flask": "M9.75 3.104v5.714a2.25 2.25 0 0 1-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 0 1 4.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0 1 12 15a9.065 9.065 0 0 0-6.23-.693L5 14.5m14.8.8 1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0 1 12 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5",
    "camera": "M6.827 6.175A2.31 2.31 0 0 1 5.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 0 0-1.134-.175 2.31 2.31 0 0 1-1.64-1.055l-.822-1.316a2.192 2.192 0 0 0-1.736-1.039 48.774 48.774 0 0 0-5.232 0 2.192 2.192 0 0 0-1.736 1.039l-.821 1.316Z",
    "spider": "M12 12.75c1.148 0 2.278.08 3.383.237 1.037.146 1.866.966 1.866 2.013 0 3.728-2.35 6.75-5.25 6.75S6.75 18.728 6.75 15c0-1.046.83-1.867 1.866-2.013A24.204 24.204 0 0 1 12 12.75Zm0 0c2.883 0 5.647.508 8.207 1.44a23.91 23.91 0 0 1-1.152 6.06M12 12.75c-2.883 0-5.647.508-8.208 1.44.125 2.104.52 4.136 1.153 6.06M12 12.75a2.25 2.25 0 0 0 2.248-2.354M12 12.75a2.25 2.25 0 0 1-2.248-2.354M12 8.25c.995 0 1.971-.08 2.922-.236.403-.066.74-.358.795-.762a3.778 3.778 0 0 0-.399-2.25M12 8.25c-.995 0-1.97-.08-2.922-.236-.402-.066-.74-.358-.795-.762a3.734 3.734 0 0 1 .4-2.253M12 8.25a2.25 2.25 0 0 0-2.248 2.146M12 8.25a2.25 2.25 0 0 1 2.248 2.146M8.683 5a6.032 6.032 0 0 1-1.155-1.002c.07-.63.27-1.222.574-1.747m.581 2.749A3.75 3.75 0 0 1 15.318 5m0 0c.427-.283.815-.62 1.155-.999a4.471 4.471 0 0 0-.575-1.752M4.921 6a24.048 24.048 0 0 0-.392 3.314c1.668.546 3.416.914 5.223 1.082M19.08 6c.205 1.08.337 2.187.392 3.314a23.882 23.882 0 0 1-5.223 1.082",
    "setting": "M10.343 3.94c.09-.542.56-.94 1.11-.94h1.093c.55 0 1.02.398 1.11.94l.149.894c.07.424.384.764.78.93.398.164.855.142 1.205-.108l.737-.527a1.125 1.125 0 0 1 1.45.12l.773.774c.39.389.44 1.002.12 1.45l-.527.737c-.25.35-.272.806-.107 1.204.165.397.505.71.93.78l.893.15c.543.09.94.559.94 1.109v1.094c0 .55-.397 1.02-.94 1.11l-.894.149c-.424.07-.764.383-.929.78-.165.398-.143.854.107 1.204l.527.738c.32.447.269 1.06-.12 1.45l-.774.773a1.125 1.125 0 0 1-1.449.12l-.738-.527c-.35-.25-.806-.272-1.203-.107-.398.165-.71.505-.781.929l-.149.894c-.09.542-.56.94-1.11.94h-1.094c-.55 0-1.019-.398-1.11-.94l-.148-.894c-.071-.424-.384-.764-.781-.93-.398-.164-.854-.142-1.204.108l-.738.527c-.447.32-1.06.269-1.45-.12l-.773-.774a1.125 1.125 0 0 1-.12-1.45l.527-.737c.25-.35.272-.806.108-1.204-.165-.397-.506-.71-.93-.78l-.894-.15c-.542-.09-.94-.56-.94-1.109v-1.094c0-.55.398-1.02.94-1.11l.894-.149c.424-.07.765-.383.93-.78.165-.398.143-.854-.108-1.204l-.526-.738a1.125 1.125 0 0 1 .12-1.45l.773-.773a1.125 1.125 0 0 1 1.45-.12l.737.527c.35.25.807.272 1.204.107.397-.165.71-.505.78-.929l.15-.894Z",
    "flame": "M15.362 5.214A8.252 8.252 0 0 1 12 21 8.25 8.25 0 0 1 6.038 7.047 8.287 8.287 0 0 0 9 9.601a8.983 8.983 0 0 1 3.361-6.867 8.21 8.21 0 0 0 3 2.48Z"


    }
#V2

def filter_and_replace(text):
    word_dict = {
        "coin": ["database", "penny"],
        "mouse": ['cursor', 'point'],
        "rocket": ["plane","fight", "space", "flight"],
        "gem": ["diamond", "jewel"],
        "bank": ['university'],
        "house": ['build', 'home'],
        "emo": ['mood','smile'],
        "bluetooth": ['blue'],
        "file": ['folder'],
        "display": ['pc', 'laptop', 'device', 'computer'],
        "comment": ['message', 'chat','text'],
        "bell": ['notifi'],
        "leaf": ['envira', 'pageline', 'seeding','grass'],
        "chart": ['signal'],
        "cloud": ['weather'],
        "energy": ['lightning', 'zap', 'bolt',"flash"],
        "camera": ["selfie","phone", "polaroid", "video","image","pic"],
        "spider": ['bug','insect'],
        "setting": ['cog', 'gear'],
        "fire": ["burn","hot", "flame", "torch"],
        "trash": ["bin", "garbage "],
        "flag": ["pennant", "banner"],
    }

    for category, words in word_dict.items():
        for word in words:
            # Replace the word with the category, ensuring word boundaries are respected
            text = text.replace(word, category)
    return text


def solve_icon_captcha_v2(sb, fey = True):
    solve_icon_captchagg = time.time()
    test_mode = True

    try:
        # Extract all captcha icon
        #captcha_icons = sb.find_elements('[class*="bxs-"]:not([class*="fa2"]), [class*="bx-"]:not([class*="fa2"]), [class*="la-"]:not([class*="fa2"]), [class*="fa-"]:not([class*="fa2"]), [class*="fas fa-"]:not([class*="fa2"]), [class*="far fa-"]:not([class*="fa2"]), [class*="ri-"]:not([class*="fa2"]), [class*="ti ti-"]:not([class*="fa2"]), [class*="bi bi-"]:not([class*="fa2"])')
        # Find potential captcha icons based on class names
        #captcha_icons = sb.find_elements('[class*="bxs-"][class*="bxs-"], [class*="bx-"], [class*="la-"], [class*="fa-"], [class*="fas fa-"], [class*="far fa-"], [class*="ri-"], [class*="ti ti-"], [class*="bi bi-"]')
 
        sb.execute_script("window.scrollTo(0, 1000);")
        #captcha_icons = sb.find_elements('[class="mb-2 badge bg-danger"],[class="mb-16 badge hp-text-color-black-100 hp-bg-danger-3"], [class="mb-3 badge bg-warning font-xssss"],[class="mb-16 badge hp-text-color-black-100 hp-bg-warning-3"],[class*="bxs-"]:not([class*="fa2"]):not([style]), [class*="bx-"]:not([class*="fa2"]):not([style]), [class*="la-"]:not([class*="fa2"]):not([style]), [class*="fa-"]:not([class*="fa2"]):not([style]), [class*="fas fa-"]:not([class*="fa2"]):not([style]), [class*="far fa-"]:not([class*="fa2"]):not([style]), [class*="ri-"]:not([class*="fa2"]):not([style]), [class*="ti ti-"]:not([class*="fa2"]):not([style]), [class*="bi bi-"]:not([class*="fa2"]):not([style])')
        captcha_icons = sb.find_elements('//*[contains(text(), "Pick the one Big, clear icon from above.")], [class="mb-3 badge bg-warning font-xssss"],[class="mb-16 badge hp-text-color-black-100 hp-bg-warning-3"],[class*="bxs-"]:not([class*="fa2"]):not([style]), [class*="bx-"]:not([class*="fa2"]):not([style]), [class*="la-"]:not([class*="fa2"]):not([style]), [class*="fa-"]:not([class*="fa2"]):not([style]), [class*="fas fa-"]:not([class*="fa2"]):not([style]), [class*="far fa-"]:not([class*="fa2"]):not([style]), [class*="ri-"]:not([class*="fa2"]):not([style]), [class*="ti ti-"]:not([class*="fa2"]):not([style]), [class*="bi bi-"]:not([class*="fa2"]):not([style])')

        #valid_captcha_icons = []
        #icon_options = []

        #for icon in captcha_icons:
        #    if icon.tag_name.lower() == "i":
        #        icon_options.append(icon)
        #    else:
        #        valid_captcha_icons.append(icon)


        valid_captcha_icons = []
        icon_options = []
        split_point_class_1 = "mb-16 badge"
        split_point_class_2 = "mb-3 badge"
        split_point_class_3 = "mb-2 badge"
        split_condition = False
        valid_captcha_icons2 = []
        for icon in captcha_icons:
            icon_class = icon.get_attribute("class")
            print('Class:',icon_class)
            if split_point_class_1 in icon_class or split_point_class_2 in icon_class or split_point_class_3 in icon_class:
                split_condition = True
                continue
            # Check if the icon belongs to valid_captcha_icons
            if 'fa-spin d-none' in icon_class or icon.tag_name.lower() == "i":
                continue
            if split_condition:
                icon_options.append(icon)
            else:  
                valid_captcha_icons2.append(icon_class)


                # Filter valid captcha icons
        #icon_options = [icon for icon in captcha_icons if not icon.get_attribute("style") and not icon.get_attribute("id") and icon.tag_name.lower() == "i" and "fa2" not in icon.get_attribute("class")]
        #valid_captcha_icons = [icon for icon in captcha_icons if icon.tag_name.lower() != "i"]
        #icon_options = [icon for icon in captcha_icons if icon.tag_name.lower() == "i"]
        #valid_captcha_icons = [icon for icon in captcha_icons if not icon.get_attribute("style") and not icon.get_attribute("id") and icon.tag_name.lower() != "i"]
        
        #valid_captcha_icons2 = []
        #class_name = 'b'
        #for icon in valid_captcha_icons:
        #    class_name = icon.get_attribute("class")
        #    if class_name:
        #        valid_captcha_icons2.append(class_name)

        if fey:
            if len(valid_captcha_icons2) > 1:
                valid_captcha_icons = valid_captcha_icons2[1]
            else:
                print("Not enough icons in valid_captcha_icons2 for index [1].")
                return False  # Exit or handle appropriately
        else:
            if len(valid_captcha_icons2) > 0:
                valid_captcha_icons = valid_captcha_icons2[-1]
            else:
                print("Not enough icons in valid_captcha_icons2 for index [-1].")
                return False  # Exit or handle appropriately
            
        valid_captcha_icons = filter_and_replace(valid_captcha_icons)
        if test_mode:
            print("Icon options:", [icon.get_attribute('class') for icon in icon_options])
            print(valid_captcha_icons2)
            print(valid_captcha_icons)

        unvalid_shit = ['fill','line','fa2']
        for option in icon_options:
            option_classes = option.get_attribute('class')
            item = option_classes.replace('-', ' ')
            item = re.sub(r'\b(bxs|bx|la|fa|fas|fab|far|ti|bi|ri)\b', '', item)
            option_classes = item.split()
            for val in option_classes:
                val = filter_and_replace(val)
                if test_mode:
                    print('iconS:',val)
                if len(val) < 2 or val in unvalid_shit:
                    print('its invalid icon',val)
                    continue
                if val in valid_captcha_icons:
                        option.uc_click()  # Custom click method to handle undetected Selenium

                        print(f"Clicked on the matching icon: {val}")
                        print(f"Original function execution time: {time.time() - solve_icon_captchagg:.2f} seconds")
                        return True  # Return immediately after a successful click


        # Find all SVG elements
        #svg_elements = sb.find_elements(By.TAG_NAME,"svg")
        svg_elements = sb.find_elements("svg[width='26px'][height='26px'], svg[width='24px'][height='24px']")
        svg_valid = False
        if test_mode:
            print(f"Total SVG elements found: {len(svg_elements)}")
        for svg in svg_elements:
            #try:
                # Look for 'path' element inside the SVG
                path_elements = svg.find_elements(By.TAG_NAME, "path")
                
                # Check if any path elements were found
                if path_elements:
                    for path_element in path_elements:
                        path_data = path_element.get_attribute("d").strip()
                        if test_mode:
                            print('path_data:',path_data)
                        if path_data:

                            # Compare pathData with the iconPathList dictionary
                            for icon_name, icon_path in icon_path_list.items():
                                if path_data.strip() in icon_path.strip():
                                    icon_name = filter_and_replace(icon_name)
                                    print(f"Match found: {icon_name}")
                                    svg_valid = True
                                    if icon_name in valid_captcha_icons:
                                        print(f"Answer found for icon: {icon_name}")
                                        print(f"Original function execution time: {time.time() - solve_icon_captchagg:.2f} seconds")
                                        svg.uc_click()
                                        
                                        return True  # Exit after successful click

                            
                else:
                    print(f"No 'path' elements found in this SVG: {svg}.")

            #except Exception as svg_error:
            #    print(f"Skipping SVG (error: {svg_error}).")
        if svg_valid:
            if test_mode:
                query = {"type": "main"}
                update = {"$set": {"request": 'pause'}}
                result = collection.update_one(query, update)
                response_messege(f'New Element Found{valid_captcha_icons}')
                print(f'New Element Found{valid_captcha_icons}')
            else:
                pyautogui.press('f5')

    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False


def solve_icon_captcha_v4(sb, fey = True):
    solve_icon_captchagg = time.time()
    test_mode = True

    try:

        sb.execute_script("window.scrollTo(0, 1000);")
        #captcha_icons = sb.find_elements('[class*="bxs-"]:not([class*="fa2"]):not([style]), [class*="bx-"]:not([class*="fa2"]):not([style]), [class*="la-"]:not([class*="fa2"]):not([style]), [class*="fa-"]:not([class*="fa2"]):not([style]), [class*="fas fa-"]:not([class*="fa2"]):not([style]), [class*="far fa-"]:not([class*="fa2"]):not([style]), [class*="ri-"]:not([class*="fa2"]):not([style]), [class*="ti ti-"]:not([class*="fa2"]):not([style]), [class*="bi bi-"]:not([class*="fa2"]):not([style])')
        captcha_icons = sb.find_elements('[class*="bxs-"]:not([class*="fa2"]):not([style]):not(i),[class*="bx-"]:not([class*="fa2"]):not([style]):not(i),[class*="la-"]:not([class*="fa2"]):not([style]):not(i),[class*="fa-"]:not([class*="fa2"]):not([style]):not(i),[class*="fas fa-"]:not([class*="fa2"]):not([style]):not(i),[class*="far fa-"]:not([class*="fa2"]):not([style]):not(i),[class*="ri-"]:not([class*="fa2"]):not([style]):not(i),[class*="ti ti-"]:not([class*="fa2"]):not([style]):not(i), [class*="bi bi-"]:not([class*="fa2"]):not([style]):not(i)')
        
        if test_mode:
            print(f"Total captcha_icons elements found: {len(captcha_icons)}")
            print("captcha_icons options:", [icon.get_attribute('class') for icon in captcha_icons])

        valid_captcha_icons = []
        icon_options = []
        valid_captcha_icons2 = []
        if len(captcha_icons) > 2:
            valid_captcha_icons2 = captcha_icons[:3]
            icon_options = captcha_icons[3:]
            

        if fey:
            if len(valid_captcha_icons2) > 1:
                valid_captcha_icons = valid_captcha_icons2[1]
            else:
                print("Not enough icons in valid_captcha_icons2 for index [1].")
                return False  # Exit or handle appropriately
        else:
            if len(valid_captcha_icons2) > 0:
                valid_captcha_icons = valid_captcha_icons2[-1]
            else:
                print("Not enough icons in valid_captcha_icons2 for index [-1].")
                return False  # Exit or handle appropriately
        valid_captcha_icons = valid_captcha_icons.get_attribute('class')    
        valid_captcha_icons = filter_and_replace(valid_captcha_icons)
        if test_mode:
            print("Icon options:", [icon.get_attribute('class') for icon in icon_options])
            print(valid_captcha_icons2)
            print(valid_captcha_icons)

        unvalid_shit = ['fill','line','fa2']
        for option in icon_options:
            option_classes = option.get_attribute('class')
            if 'circle-notch' in option_classes:
                continue
            item = option_classes.replace('-', ' ')
            item = re.sub(r'\b(bxs|bx|la|fa|fas|fab|far|ti|bi|ri)\b', '', item)
            option_classes = item.split()
            for val in option_classes:
                val = filter_and_replace(val)
                if test_mode:
                    print('iconS:',val)
                if len(val) < 2 or val in unvalid_shit:
                    print('its invalid icon',val)
                    continue
                if val in valid_captcha_icons:
                        option.uc_click()  # Custom click method to handle undetected Selenium

                        print(f"Clicked on the matching icon: {val}")
                        print(f"Original function execution time: {time.time() - solve_icon_captchagg:.2f} seconds")
                        return True  # Return immediately after a successful click


        # Find all SVG elements
        #svg_elements = sb.find_elements(By.TAG_NAME,"svg")
        svg_elements = sb.find_elements("svg[width='26px'][height='26px'], svg[width='24px'][height='24px']")
        svg_valid = False
        if test_mode:
            print(f"Total SVG elements found: {len(svg_elements)}")
        for svg in svg_elements:
            #try:
                # Look for 'path' element inside the SVG
                path_elements = svg.find_elements(By.TAG_NAME, "path")
                
                # Check if any path elements were found
                if path_elements:
                    for path_element in path_elements:
                        path_data = path_element.get_attribute("d").strip()
                        if test_mode:
                            print('path_data:',path_data)
                        if path_data:

                            # Compare pathData with the iconPathList dictionary
                            for icon_name, icon_path in icon_path_list.items():
                                if path_data.strip() in icon_path.strip():
                                    icon_name = filter_and_replace(icon_name)
                                    print(f"Match found: {icon_name}")
                                    svg_valid = True
                                    if icon_name in valid_captcha_icons:
                                        print(f"Answer found for icon: {icon_name}")
                                        print(f"Original function execution time: {time.time() - solve_icon_captchagg:.2f} seconds")
                                        svg.uc_click()
                                        
                                        return True  # Exit after successful click

                            
                else:
                    print(f"No 'path' elements found in this SVG: {svg}.")

            #except Exception as svg_error:
            #    print(f"Skipping SVG (error: {svg_error}).")
        if svg_valid:
            if test_mode:
                query = {"type": "main"}
                update = {"$set": {"request": 'pause'}}
                result = collection.update_one(query, update)
                response_messege(f'New Element Found{valid_captcha_icons}')
                print(f'New Element Found{valid_captcha_icons}')
            else:
                pyautogui.press('f5')

    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False




def solve_icon_captcha(sb, fey = True):
    solve_icon_captchagg = time.time()
    test_mode = True

    try:

        sb.execute_script("window.scrollTo(0, 1000);")
        #captcha_icons = sb.find_elements('[class*="bxs-"]:not([class*="fa2"]):not([style]), [class*="bx-"]:not([class*="fa2"]):not([style]), [class*="la-"]:not([class*="fa2"]):not([style]), [class*="fa-"]:not([class*="fa2"]):not([style]), [class*="fas fa-"]:not([class*="fa2"]):not([style]), [class*="far fa-"]:not([class*="fa2"]):not([style]), [class*="ri-"]:not([class*="fa2"]):not([style]), [class*="ti ti-"]:not([class*="fa2"]):not([style]), [class*="bi bi-"]:not([class*="fa2"]):not([style])')
        #captcha_icons = sb.find_elements('[class*="bxs-"]:not([class*="fa2"]):not([style]):not(i),[class*="bx-"]:not([class*="fa2"]):not([style]):not(i),[class*="la-"]:not([class*="fa2"]):not([style]):not(i),[class*="fa-"]:not([class*="fa2"]):not([style]):not(i),[class*="fas fa-"]:not([class*="fa2"]):not([style]):not(i),[class*="far fa-"]:not([class*="fa2"]):not([style]):not(i),[class*="ri-"]:not([class*="fa2"]):not([style]):not(i),[class*="ti ti-"]:not([class*="fa2"]):not([style]):not(i), [class*="bi bi-"]:not([class*="fa2"]):not([style]):not(i)')
        captcha_icons = sb.execute_script("""
            let captchaIcons = document.evaluate(
                '//*[('
                + 'contains(@class, "bxs-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "bx-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "la-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "fa-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "fas fa-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "far fa-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "ri-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "ti ti-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(@class, "bi bi-") and not(contains(@class, "fa2")) and not(@style) and not(self::i)'
                + ') or ('
                + 'contains(text(), "Pick the one clear icon from above.")'
                + ')]',
                document,
                null,
                XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                null
            );

            let captchaIconsArray = [];
            for (let i = 0; i < captchaIcons.snapshotLength; i++) {
                captchaIconsArray.push(captchaIcons.snapshotItem(i));
            }

            return captchaIconsArray;
        """)

        if test_mode:
            print(f"Total captcha_icons elements found: {len(captcha_icons)}")
            

        valid_captcha_icons = []
        icon_options = []
        valid_captcha_icons2 = []
        if len(captcha_icons) > 2:
            split_condition = False
            for icon in captcha_icons:
                icon_text = icon.text.strip()
                #print('Class:',icon)
                if 'Pick' in icon_text:
                    print('Found Pick')
                    split_condition = True
                    continue
                if split_condition:
                    icon_options.append(icon)
                else:  
                    valid_captcha_icons2.append(icon)
            print(f"Total valid_captcha_icons2 elements found: {len(valid_captcha_icons2)}")
            print(f"Total icon_options elements found: {len(icon_options)}")

            for icon in valid_captcha_icons2:
                try:
                    opacity = sb.execute_script(
                        "return window.getComputedStyle(arguments[0]).getPropertyValue('opacity');",
                        icon
                    )
                    if float(opacity) > 0.8:
                        valid_captcha_icons = icon
                        break
                except Exception as e:
                    print(f"Error checking opacity: {e}")


        valid_captcha_icons = valid_captcha_icons.get_attribute('class')    
        valid_captcha_icons = filter_and_replace(valid_captcha_icons)
        if test_mode:
            #print("Icon options:", [icon.get_attribute('class') for icon in icon_options])
            print('valid_captcha_icons2:',valid_captcha_icons2)
            print('valid_captcha_icons:',valid_captcha_icons)

        unvalid_shit = ['fill','line','fa2']
        for option in icon_options:
            option_classes = option.get_attribute('class')
            if 'circle-notch' in option_classes:
                continue
            item = option_classes.replace('-', ' ')
            item = re.sub(r'\b(bxs|bx|la|fa|fas|fab|far|ti|bi|ri)\b', '', item)
            option_classes = item.split()
            for val in option_classes:
                val = filter_and_replace(val)
                if test_mode:
                    print('iconS:',val)
                if len(val) < 2 or val in unvalid_shit:
                    print('its invalid icon',val)
                    continue
                if val in valid_captcha_icons:
                        option.uc_click()  # Custom click method to handle undetected Selenium

                        print(f"Clicked on the matching icon: {val}")
                        print(f"Original function execution time: {time.time() - solve_icon_captchagg:.2f} seconds")
                        return True  # Return immediately after a successful click


        # Find all SVG elements
        #svg_elements = sb.find_elements(By.TAG_NAME,"svg")
        svg_elements = sb.find_elements("svg[width='26px'][height='26px'], svg[width='24px'][height='24px']")
        svg_valid = False
        if test_mode:
            print(f"Total SVG elements found: {len(svg_elements)}")
        for svg in svg_elements:
            #try:
                # Look for 'path' element inside the SVG
                path_elements = svg.find_elements(By.TAG_NAME, "path")
                
                # Check if any path elements were found
                if path_elements:
                    for path_element in path_elements:
                        path_data = path_element.get_attribute("d").strip()
                        #if test_mode:
                        #    print('path_data:',path_data)
                        if path_data:

                            # Compare pathData with the iconPathList dictionary
                            for icon_name, icon_path in icon_path_list.items():
                                if path_data.strip() in icon_path.strip():
                                    icon_name = filter_and_replace(icon_name)
                                    print(f"Match found: {icon_name}")
                                    svg_valid = True
                                    if icon_name in valid_captcha_icons:
                                        print(f"Answer found for icon: {icon_name}")
                                        print(f"Original function execution time: {time.time() - solve_icon_captchagg:.2f} seconds")
                                        svg.uc_click()
                                        
                                        return True  # Exit after successful click

                            
                else:
                    print(f"No 'path' elements found in this SVG: {svg}.")

            #except Exception as svg_error:
            #    print(f"Skipping SVG (error: {svg_error}).")
        if svg_valid:
            if test_mode:
                query = {"type": "main"}
                update = {"$set": {"request": 'pause'}}
                result = collection.update_one(query, update)
                response_messege(f'New Element Found{valid_captcha_icons}')
                print(f'New Element Found{valid_captcha_icons}')
            else:
                pyautogui.press('f5')

    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False




def get_current_window_title():
    try:
        # Use xdotool to get the active window's title
        result = subprocess.run(
            ["xdotool", "getwindowfocus", "getwindowname"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            raise Exception(result.stderr.strip())
    except FileNotFoundError:
        return "xdotool is not installed. Please install it using: sudo apt install xdotool"
    except Exception as e:
        return f"An error occurred: {e}"


def cloudflare(sb, login = True):
    try:
        page_title = get_current_window_title()
        gg = False
        if 'Just' in page_title and login == False:
            sb.disconnect() 
            while gg == False:


                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                    print("verify_cloudflare git Found")
                    if x and y: 
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.7)
                            pyautogui.click(x, y)
                            time.sleep(5)
                        except Exception as e:
                            print(e)
                        #
                except Exception as e:
                    print(e)
                page_title = get_current_window_title()
                if 'Just' in page_title:
                    pass
                else:
                    sb.connect() 
                    gg = True
            



        while gg == False:
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                print("verify_cloudflare git Found")
                if x and y:
                    sb.disconnect() 
                    for i in range(1, 300):
                        #pyautogui.moveTo(100, 200)

                        if 'Login' in page_title or 'Just' in page_title or 'Faucet' in page_title or 'Earnbitmoon' in page_title:
                            try:
                                time.sleep(1)
                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                                print("verify_cloudflare git Found")
                                try:
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.7)
                                    pyautogui.click(x, y)
                                    time.sleep(5)
                                    if login == False: 
                                        sb.connect()
                                        return True

                                except Exception as e:
                                    print(e)
                                    
                                try:
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_success.png", confidence=0.7)
                                    pyautogui.click(x, y)
                                    time.sleep(1)
                                    if login == True: 
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





def click_element_with_pyautogui(driver, selector):
    # Step 1: Find the element using SeleniumBase
    element = driver.find_element(selector)
    
    # Step 2: Get element's location and size
    location = element.location
    size = element.size
    y_location = location['y'] + 100
    driver.execute_script(f"window.scrollTo(0, {y_location});")
    time.sleep(1)
    element = driver.find_element(selector)
    
    # Step 2: Get element's location and size
    location = element.location
    size = element.size
    scroll_y = driver.execute_script("return window.scrollY;")
    top = location['y'] #- scroll_y
    # Step 3: Calculate the center of the element
    center_x = location['x'] + size['width'] / 2
    center_y = (top) + size['height'] + (size['height'] /2) 
    # Step 4: Adjust coordinates for the full screen    if the browser is maximized
    window_position = driver.get_window_position()
    center_x += window_position['x']
    center_y += window_position['y']
    
    # Step 5: Move the cursor to the center of the element and click
    pyautogui.moveTo(center_x, center_y)
    #pyautogui.click(center_x, center_y)
    
    #driver.uc_click(selector)
    pyautogui.click()
    print(f'y_location:{y_location} | top:{top} | scroll_y:{scroll_y}', location['y'])
    print(f"Clicked on element at ({center_x}, {center_y})")

import base64
# Function to find and save the Anti-Bot instruction image
def save_antibot_image(driver, output_filename='captcha.png'):
    try:
        # Locate the instruction element
        antibot_element = driver.find_element("id", "atb-instruction")
        
        if antibot_element:
            # Locate the image element within the instruction
            image_element = antibot_element.find_element("tag name", "img")
            
            # Get the src attribute which contains the base64 string
            image_src = image_element.get_attribute("src")
            
            # Check if the src starts with 'data:image/png;base64,'
            if image_src.startswith("data:image/png;base64,"):
                base64_data = image_src.split(",")[1]
                
                # Decode the base64 string
                image_data = base64.b64decode(base64_data)
                
                # Save the image to a file
                with open(output_filename, "wb") as image_file:
                    image_file.write(image_data)
                print(f"Image saved as {output_filename}")
                return True
            else:
                print("Image src does not contain base64 data")
        else:
            print("Anti-Bot instruction element not found")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to find and save images from Anti-Bot links
def save_antibot_link_images(driver):
    try:
        # Locate all link elements containing Anti-Bot images
        antibot_link_elements = driver.find_elements(".antibotlinks a img")
        
        for i, img_element in enumerate(antibot_link_elements):
            # Get the src attribute containing the base64 string
            image_src = img_element.get_attribute("src")
            
            if image_src.startswith("data:image/png;base64,"):
                base64_data = image_src.split(",")[1]
                
                # Decode the base64 string
                image_data = base64.b64decode(base64_data)
                
                # Save the image with a unique filename
                output_filename = f"answer{i + 1}.png"
                with open(output_filename, "wb") as image_file:
                    image_file.write(image_data)
                print(f"Image saved as {output_filename}")
            else:
                print(f"Image {i + 1} src does not contain base64 data")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")

def get_ocr(image):
    result = ocr.ocr(image)
    result = ''.join([item[1][0] for item in result[0]])
    result = ''.join(filter(str.isdigit, str(result)))
    print(result)
    if result:
        return result
    else:
        print(f"Error: Results Empty with get_ocr{image}.")
        return None
def words_or_roman_to_numbers(input_string):
    # Dictionary for word to number conversion
    word_to_num = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20
    }

    # Dictionary for Roman numeral to number conversion
    roman_to_num = {
        "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5,
        "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,
        "xi": 11, "xii": 12, "xiii": 13, "xiv": 14, "xv": 15,
        "xvi": 16, "xvii": 17, "xviii": 18, "xix": 19, "xx": 20
    }

    # Normalize input to lowercase and split by commas
    words = input_string.lower().replace(" ", "").split(',')

    # Convert words or Roman numerals to numbers
    result = []
    for word in words:
        if word in word_to_num:
            result.append(str(word_to_num[word]))
        elif word in roman_to_num:
            result.append(str(roman_to_num[word]))
        else:
            result.append("?")  # Placeholder for unrecognized values

    # Join the converted numbers into a string
    return ','.join(result)


# Function to find the correct order to match quiz and answer lists
def get_correct_order(quiz, answers):
    try:
        # Create a dictionary to map answers to their indices
        answer_index_map = {value: idx + 1 for idx, value in enumerate(answers)}

        # Create a list for the correct order
        correct_order = [answer_index_map[q] for q in quiz]
        
        return correct_order
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def solve_antibotlinks(driver):
    g1 = save_antibot_image(driver, output_filename='captcha.jpg')
    g2 = save_antibot_link_images(driver)
    if g1 and g2:
        antibot_link_elements = driver.find_elements(".antibotlinks a img")
        quiz = get_ocr('captcha.jpg')
        a1 = get_ocr('answer1.jpg')
        a2 = get_ocr('answer2.jpg')
        a3 = get_ocr('answer3.jpg')
        if quiz and a1 and a2 and a3:
            #-----------------------------------------
            quiz = words_or_roman_to_numbers(quiz)
            a1 = words_or_roman_to_numbers(a1)
            a2 = words_or_roman_to_numbers(a2)
            a3 = words_or_roman_to_numbers(a3)
            #-----------------------------------------
            if any(char.isdigit() for char in quiz):
                answer = get_correct_order(quiz, [a1, a2, a3])
                print('Correct Order is', answer)
                for i in answer:
                    if '1' in i:
                        antibot_link_elements[0].click()
                    elif '2' in i:
                        antibot_link_elements[1].click()
                    elif '3' in i:
                        antibot_link_elements[2].click()

                return True
            else:
                print('There are no Numbers in', quiz)
        else:
            print(f'quiz:{quiz} | a1:{a1}| a2:{a2}| a3:{a3}|')
                    

        



def find_and_click_collect_button(sb1):
    # Selector for the button

    button_selector = 'button.btn.btn-primary.btn-lg.claim-button'
    #hide_ads(sb1)
    # Check if the "Collect your reward" button exists and contains the correct text
    if sb1.is_element_visible(button_selector):
        sb1.execute_script("window.scrollTo(0, 1000);")
        button_text = sb1.get_text(button_selector)
        
        if "Collect your reward" in button_text:
            solve_antibotlinks(sb1)
            print(f"Button with 'Collect your reward' text found.{button_text}")
            original_window = sb1.current_window_handle
            all_windows_before_click = sb1.window_handles.copy()
            pyautogui.click(350, 200)

            all_windows = sb1.window_handles
            for window in all_windows:
                if window not in all_windows_before_click:
                    print(f"Closing new tab: {window}")
                    sb1.switch_to.window(window)
                    sb1.close()
                    sb1.connect()
            sb1.switch_to.window(original_window)
            
            sb1.execute_script("window.scrollTo(0, 1000);")
            time.sleep(1)
            sb1.uc_click(button_selector)
            print("Collect button Not clicked.")
                #sb1.connect()
            return True
        else:
            print("Button found, but it doesn't contain 'Collect your reward' text.")
            return None
    else:
        print("Collect your reward button not found.")
        return None




def login_to_faucet(url, driver, email, password, captcha_image, restrict_pages, submit_button):

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
            if 'rscaptcha'in captcha_image:
                    try:
                        solve_least_img(sb1)
                        if 'Feyorra' in current_title:
                            pyautogui.click(932 ,728)
                            time.sleep(1)
                            pyautogui.click(943 ,788)
                                    #x:943 y:788
                            time.sleep(5)
                            return
                        if 'ClaimCoin' in current_title:
                            pyautogui.click(973, 833)
                            time.sleep(5)
                            return
                        pyautogui.click(957 ,886)
                        time.sleep(5)
                        if driver.is_element_visible(submit_button):
                            sb1.uc_click(submit_button)
                        time.sleep(5)
                        return
                    except Exception as e:
                        print(f'ERR:{e}') 
            else:
                for i in range(1, 10):
                    time.sleep(1)
                    #pyautogui.moveTo(100, 200)

                    sb1.execute_script("window.scrollTo(0, 1000);")
                    cloudflare(driver, True)
                    try:
                        x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{captcha_image}.png", confidence=0.85)
                        if x and y: 

                            #login_button = driver.find_element(By.CSS_SELECTOR, submit_button)
                            #click_element_with_pyautogui(driver, login_button)
                            #click_element_with_pyautogui(sb1, 'button[type="submit"]')
                            if 'Feyorra' in current_title:
                                pyautogui.click(932 ,728)
                                time.sleep(1)
                                pyautogui.click(943 ,788)
                                #x:943 y:788
                                time.sleep(5)
                                return
                            if 'ClaimCoin' in current_title:
                                pyautogui.click(973, 833)
                                time.sleep(5)
                                return
                            if driver.is_element_visible(submit_button):
                                sb1.uc_click(submit_button)
                            #sb1.uc_click('button[type="submit"]')
                            
                            #driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                            #login_button.click(submit_button)
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
    




bitmoon_window = None
earnpp_window = None
claimcoin_window = None
feyorra_window = None
baymack_window = None
feyorratop_window = None

def close_extra_windows(driver, keep_window_handles):
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window not in keep_window_handles:
            driver.switch_to.window(window)
            driver.close()
            driver.connect()
    driver.switch_to.window(current_window)

def handle_captcha_and_cloudflare(driver):
    cloudflare(driver, login = False)

def handle_site(driver, url, expected_title, not_expected_title , function, window_list ,ip_required):
    driver.uc_open(url)
    ready = False
    while not ready:
        time.sleep(1)
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        all_windows = driver.window_handles
        for window in all_windows:
            if window not in window_list:
                driver.switch_to.window(window)
        current_title = driver.get_title()
        print(f"Current title: {current_title}")

        ip_address = get_ip(driver)
        if ip_required != ip_address:
            return 404
        get_mails_passowrds(farm_id)


        if not_expected_title == current_title:
            if function == 1:
                login_to_faucet('https://earn-pepe.com/login', sb1, earnpp_email, earnpp_pass, 'cloudflare_success', window_list, 'button#ClaimBtn')
                #login_to_faucet('https://earn-pepe.com/login', sb1, earnpp_email, earnpp_pass, 'rscaptcha', window_list, 'button#loginBtn')
            elif function == 2:
                login_to_faucet('https://feyorra.site/login', sb1, feyorra_email, feyorra_pass, 'cloudflare_success', window_list, 'button#loginBtn')
            elif function == 3:
                login_to_faucet('https://claimcoin.in/login', sb1, claimc_email, claimc_pass,  'cloudflare_success', window_list, 'button[type="submit"]') #'not_a_robot'
            elif function == 6:
                login_to_faucet('https://feyorra.top/login', sb1, 'khabibmakanzie@gmail.com', '%aYYcsSfcYjN%5x', 'rscaptcha', window_list, 'button[type="submit"]') #'not_a_robot'


        elif expected_title in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Lock' in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Maintenance' in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Just' in current_title:
            handle_captcha_and_cloudflare(driver)
        
        else:
            print(f"{current_title} is not the expected title. Reconnecting...")
            all_windows = driver.window_handles
            for window in all_windows:
                if window not in window_list:
                    driver.switch_to.window(window)
            driver.uc_open(url)
            handle_captcha_and_cloudflare(driver)

    return driver.current_window_handle


def pin_extensions():
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/extension_icon.png", region=(1700, 30, 300, 300), confidence=0.9)
        pyautogui.click(x, y)
        print("extension_icon Button Found")

        for i in range(1,50):
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
        return False
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
    try:
        
        if sitekey == 1:
            if driver.is_element_present('small span span'):
                select_element = driver.find_element('css selector', 'small span span')
                selected_text = select_element.text.strip()  # Extract and clean the text
                coins = selected_text
            else:
                print(f'Sitekey:{sitekey} not found')
            #coins = float(coins.split()[0]) 
        if sitekey == 2:
            if driver.is_element_present('select'):
                select_element = driver.find_element('css selector', 'select.form-select option[selected]')  # Locate the selected option
                selected_text = select_element.text.strip()  # Extract and clean the text
                print(f"Selected option text: {selected_text}")
                coins = selected_text
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
    # Step 1: Find the element using SeleniumBase
    element = driver.find_element(selector)
    
    # Step 2: Get element's location and size
    location = element.location
    size = element.size
    y_location = location['y'] + 100
    driver.execute_script(f"window.scrollTo(0, {y_location});")
    #time.sleep(1)

    # Step 3: Capture the full-page screenshot
    driver.save_screenshot(screenshot_path)
    element = driver.find_element(selector)
    
    # Step 2: Get element's location and size
    location = element.location
    size = element.size
    # Step 4: Load the full screenshot with Pillow
    screenshot = Image.open(screenshot_path)
    scroll_y = driver.execute_script("return window.scrollY;")
    # Step 5: Define the crop area using the element's location and size
    left = location['x']
    top = location['y'] - scroll_y
    right = left + size['width']
    bottom = top + size['height'] 
    print(left, top, right, bottom)
    # Step 6: Crop the image to the element's size
    cropped_image = screenshot.crop((left, top, right, bottom))
    
    # Step 7: Save the cropped image
    cropped_image.save(cropped_path)
    
    print(f"Cropped screenshot saved at {cropped_path}")



def split_image_by_width(image_path, num_pieces, output_dir="output_pieces"):
    # Open the image
    image = Image.open(image_path)
    img_width, img_height = image.size
    
    # Calculate the width of each piece
    piece_width = img_width // num_pieces
    if os.path.exists(output_dir):
        # Remove all files in the directory
        for filename in os.listdir(output_dir):
            file_path = os.path.join(output_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove directory
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        # Create the directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    
    # Loop through the number of pieces and save each slice
    for i in range(num_pieces):
        # Calculate the bounding box for each piece
        left = i * piece_width
        right = left + piece_width
        piece = image.crop((left, 0, right, img_height))
        
        # Save the piece
        piece_filename = os.path.join(output_dir, f"piece_{i+1}.png")
        piece.save(piece_filename)
        print(f"Saved {piece_filename}")

from skimage.metrics import structural_similarity as ssim

def find_least_similar_image(image_dir):
    if not os.path.isdir(image_dir):
        print("Directory does not exist.")
        return False

    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    if len(image_files) == 0:
        print("No images found in the directory.")
        return False

    # Dictionary to store image similarities
    similarities = {}

    # Iterate over all image pairs and calculate their structural similarity
    for i, img_file in enumerate(image_files):
        img_path = os.path.join(image_dir, img_file)
        img1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        for j in range(i + 1, len(image_files)):
            other_img_file = image_files[j]
            other_img_path = os.path.join(image_dir, other_img_file)
            img2 = cv2.imread(other_img_path, cv2.IMREAD_GRAYSCALE)

            # Ensure images are valid and have the same dimensions
            if img1 is None or img2 is None or img1.shape != img2.shape:
                continue

            similarity, _ = ssim(img1, img2, full=True)
            similarities[(img_path, other_img_path)] = similarity
            similarities[(other_img_path, img_path)] = similarity

    # Calculate the average similarity score for each image
    image_scores = {}
    for img_path in image_files:
        img_full_path = os.path.join(image_dir, img_path)
        similar_scores = [v for k, v in similarities.items() if k[0] == img_full_path]
        if similar_scores:
            avg_score = np.mean(similar_scores)
            image_scores[img_full_path] = avg_score

    # Find the image with the least similarity to other images
    min_score = min(image_scores.values())
    min_images = [k for k, v in image_scores.items() if v == min_score]

    if len(min_images) == 1:
        min_image_name = os.path.basename(min_images[0])
        print(f"Image {min_image_name} has the least similarity with an average score of {min_score}")
        return f'{image_dir}/{min_image_name}'
    else:
        # If multiple images have the same minimum similarity score, pick the smallest file size
        min_size = float('inf')
        min_image = None
        for image in min_images:
            size = os.path.getsize(image)
            if size < min_size:
                min_size = size
                min_image = image

        min_image_name = os.path.basename(min_image)
        print(f"Image {min_image_name} has the least similarity with an average score of {min_score}")
        return f'{image_dir}/{min_image_name}'

def image_counter(image_path):
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Crop the image to a 1-pixel high horizontal line in the middle
    middle_height = height // 2
    cropped_image = image.crop((0, middle_height, width, middle_height + 1))

    # Convert the image to RGBA mode (in case it is in a different mode)
    cropped_image = cropped_image.convert("RGBA")


    # Get the pixels of the cropped image
    pixels = cropped_image.load()

    # Define the target RGBA color to count
    target_rgba = (70, 70, 70, 255)
    background = (76,76,76, 255)

    # Set the tolerance level for each channel (e.g., ±5 for each color component)
    tolerance = 1

    # Function to calculate the Euclidean distance between two colors
    def color_distance(c1, c2):
        return math.sqrt(sum((c1[i] - c2[i]) ** 2 for i in range(4)))

    # Initialize a counter for the target color
    color_count = 0

    # Loop through the pixels and count how many match the target RGBA color within tolerance
    for i in range(1, 20):
        color_count = 0
        for x in range(width):
            pixel_color = pixels[x, 0]
            if color_distance(pixel_color, target_rgba) <= i:
                if pixel_color == background:
                    pass
                    #print('fuck')
                else:
                    color_count += 1
        if color_count >= 4:
            return color_count+1
            #break

    # Output the result
    print(f"The number of lines with a color similar to rgba(70, 70, 70, 255) is: {color_count+1}")

    return color_count+1


def check_similar_images_exist(image_dir, similarity_threshold=0.9):
    """
    Checks if there are any similar images in the given directory based on SSIM.

    :param image_dir: Directory containing the images.
    :param similarity_threshold: Threshold above which images are considered similar (default: 0.9).
    :return: True if similar images are found, False otherwise.
    """
    if not os.path.isdir(image_dir):
        print("Directory does not exist.")
        return False

    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    if len(image_files) < 2:
        print("Not enough images to compare.")
        return False

    # Iterate over all image pairs and calculate their structural similarity
    for i, img_file in enumerate(image_files):
        img_path = os.path.join(image_dir, img_file)
        img1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        for j in range(i + 1, len(image_files)):
            other_img_file = image_files[j]
            other_img_path = os.path.join(image_dir, other_img_file)
            img2 = cv2.imread(other_img_path, cv2.IMREAD_GRAYSCALE)

            # Ensure images are valid and have the same dimensions
            if img1 is None or img2 is None or img1.shape != img2.shape:
                continue

            similarity, _ = ssim(img1, img2, full=True)

            # If similarity exceeds the threshold, similar images exist
            if similarity >= similarity_threshold:
                print(f"Similar images found: {img_file} and {other_img_file} with similarity {similarity:.2f}")
                return True

    print("No similar images found.")
    return False


def solve_least_captcha(image):
    #count = image_counter(image)
    #if count >= 8:
    #    count//=2
    val = None
    split_image_by_width('element_screenshot.png', 5, output_dir="output_pieces")
    if check_similar_images_exist("output_pieces", similarity_threshold=0.9):
        val = find_least_similar_image("output_pieces")
        if val:
            return val
    split_image_by_width('element_screenshot.png', 6, output_dir="output_pieces")
    if check_similar_images_exist("output_pieces", similarity_threshold=0.9):
        val = find_least_similar_image("output_pieces")
        if val:
            return val
    split_image_by_width('element_screenshot.png', 7, output_dir="output_pieces")
    if check_similar_images_exist("output_pieces", similarity_threshold=0.9):
        val = find_least_similar_image("output_pieces")
        if val:
            return val
    split_image_by_width('element_screenshot.png', 8, output_dir="output_pieces")
    if check_similar_images_exist("output_pieces", similarity_threshold=0.9):
        val = find_least_similar_image("output_pieces")
        if val:
            return val
    return val



def solve_least_img(driver):
    for i in range(15):
        pyautogui.moveTo(400, 400)
        time.sleep(1)
        #driver.switch_to.default_content()
        #scroll_height = driver.execute_script("return document.body.scrollHeight")
        #print(scroll_height, 'height')
        #driver.execute_script(f"window.scrollTo(0, {scroll_height});")
        time.sleep(1)
        
        if driver.is_element_visible('div.iconcaptcha-modal__body-title'):
            print('iconcaptcha-modal__body-title Found')
            if driver.is_element_visible('div.iconcaptcha-modal__body-title'):
                
                text = driver.get_text('div.iconcaptcha-modal__body-title')
                print(text,'text')
                if 'Verification complete' in text or 'VERIFICATION COMPLETE' in text:
                    return True
            for i in range(5):
                if driver.is_element_visible('div.iconcaptcha-modal__body-title'):
                    text = driver.get_text('div.iconcaptcha-modal__body-title')
                    print(text,'text')
                    if 'Verification complete' in text or 'VERIFICATION COMPLETE' in text:
                        return True
                if driver.is_element_visible('div.iconcaptcha-modal__body-title'):
                    print('still found iconcaptcha-modal__body-title')
                    driver.uc_click("div.iconcaptcha-modal__body-title")
                    #click_element_with_pyautogui(driver, "div.iconcaptcha-modal__body-title")
                    time.sleep(3)
                else:
                    print('not found body titile')
                    break
        print('hellow') 
        if driver.is_element_visible('canvas.iconcaptcha-modal__body-icons'):
            print('canvas.iconcaptcha-modal__body-icons Found')    
            capture_element_screenshot(sb1, "canvas.iconcaptcha-modal__body-icons")
            val = solve_least_captcha("element_screenshot.png")
            print('val', val)
            if val:
                try:
                    x, y = pyautogui.locateCenterOnScreen(val, confidence=0.85)
                    if x and y:
                        pyautogui.click(x, y)

                        #return True
                except Exception as e:
                    print(e)
            else:
                return None
        elif driver.is_element_visible('iconcaptcha-modal__body-selection'):
            print('canvas.iconcaptcha-modal__body-selection Found THo')  
            print('canvas.iconcaptcha-modal__body-selection')    
            capture_element_screenshot(sb1, "canvas.iconcaptcha-modal__body-selection")
            val = solve_least_captcha("element_screenshot.png")
            print('val', val)
            if val:
                try:
                    x, y = pyautogui.locateCenterOnScreen(val, confidence=0.85)
                    if x and y:
                        pyautogui.click(x, y)

                        #return True
                except Exception as e:
                    print(e)
            else:
                return None
        else:
            print('not found enything')
            driver.execute_script("window.scrollTo(0, 1000);")



def earnbitmoon_claim():
    white_del = 0
    captcha_found = False
    for i in range(3):
        time.sleep(1)
        if captcha_found:
            break
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/verifyhuman_gray.png", region=(671, 118, 873, 892), confidence=0.85)
            pyautogui.click(x, y)
            time.sleep(2)
            print("Verify Human Found")
            captcha_found = True
        except pyautogui.ImageNotFoundException:
            print("No Verify Human.")
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/verified_complete_icons.png", region=(671, 118, 873, 892), confidence=0.85)
            pyautogui.click(x, y)
            print("Verify Human Found")
            captcha_found = True
        except pyautogui.ImageNotFoundException:
            print("No Verify Human.")
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/icon_image_loaded.png", region=(671, 118, 873, 892), confidence=0.85)
            pyautogui.click(x, y)

            print("Verify Human Found")
            captcha_found = True
        except pyautogui.ImageNotFoundException:
            print("No Verify Human.")

    if captcha_found:
        for i in range(10):
            time.sleep(1)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/verifyhuman_gray.png", region=(671, 118, 873, 892), confidence=0.85)
                pyautogui.click(x, y)
                time.sleep(4)
                print("Verify Human Found")

            except pyautogui.ImageNotFoundException:
                print("No Verify Human.")
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/icon_image_loaded.png", region=(671, 118, 873, 892), confidence=0.85)
                #pyautogui.click(x, y)
                pyautogui.moveTo(100,130)
                print("icon_image_loaded Found")
                screenshot = pyautogui.screenshot(region=(794, 420, 55, 43))
                screenshot.save('captcha.png') 
                image = Image.open('captcha.png')

                # Convert the image to a numpy array
                image_np = np.array(image)

                # Get the first pixel color (this is the color to compare all pixels against)
                first_pixel = image_np[0, 0]
                is_single_color = np.all(image_np == first_pixel)
                if is_single_color:
                    print('Image is all white')
                    white_del += 1
                    if white_del > 10:
                        pyautogui.press('f5')
                        return None
                else:

                    print('Image is not all white')
                    pyautogui.moveTo(100,130)
                    time.sleep(1)
                    screenshot = pyautogui.screenshot(region=(794, 415, 312, 50))
                    screenshot.save('element_screenshot.png') 
                    val = solve_least_captcha("element_screenshot.png")
                    print('val', val)
                    if val:
                        try:
                            x, y = pyautogui.locateCenterOnScreen(val, confidence=0.85)
                            if x and y:
                                pyautogui.click(x, y)
                        except Exception as e:
                            print(e)
                    else:
                        #pyautogui.press('f5')
                        pyautogui.click(810, 425,)
                        #return None
                        

            except pyautogui.ImageNotFoundException:
                print("No icon_image_loaded Human.")

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/verified_complete_icons.png", region=(671, 118, 873, 892), confidence=0.85)
                #pyautogui.click(x, y)
                print("icon_image_loaded Found")
                pyautogui.click(944,470)
                return True

            except pyautogui.ImageNotFoundException:
                print("No icon_image_loaded Human.")

  
      
def withdraw_faucet(driver, sitekey):

    try:
        collectionbip = db[f'LocalCSB']
        quer2y = {"type": "main"}
        dochh = collectionbip.find_one(quer2y)
        currency = dochh["currency"]
        pep_x =605
        pep_y = 754
        fey_x = 1288
        fey_y = 517

        #defualts are for TRX
        if 'LTC' in currency:
            pep_x = 1330
            pep_y =  592
            fey_x =  983
            fey_y =  707
        elif 'SOL' in currency:
            pep_x = 606
            pep_y =  916
            fey_x =  681
            fey_y =  897
        elif 'BNB' in currency:
            pep_x = 1330
            pep_y =  756
            fey_x =  1288
            fey_y =  707
        elif 'TRX' in currency:
            pep_x = 605
            pep_y =  754
            fey_x =  1288
            fey_y =  517
        elif 'Doge' in currency:
            pep_x = 967
            pep_y =  754
            fey_x =  679 
            fey_y =  704

        current_window = sb1.current_window_handle
        all_windows = sb1.window_handles
        for window in all_windows:
            if window != current_window:
                sb1.switch_to.window(window)
                sb1.close()  # Close the tab
                sb1.connect()
        sb1.switch_to.window(current_window)
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)

        if sitekey == 1:
            print('Strting PePe withdraw')
            driver.uc_open('https://earn-pepe.com/member/faucetpay')
            time.sleep(5)
            for i in range(1,10):
                time.sleep(1)
                title =sb1.get_title()
                print(title)
                if 'Just' in title:
                    cloudflare(sb1, login = False)
                elif 'Faucetpay Transfer' in title:
                    print(title, 'FaucetPay found')
                    response_messege(f'EarnPP FaucetPay Loaded{currency}')
                    pyautogui.click(pep_x, pep_y)
                    #pyautogui.click(605, 754) #trx
                    #pyautogui.click(967, 754)
                    time.sleep(5)
                    driver.execute_script(f"window.scrollTo(0, 1000);")
                    time.sleep(2)
                    solve_icon_captcha(driver, fey=False)
                    time.sleep(2)
                    #driver.uc_click('button.claim-button')
                    #driver.uc_open('https://earn-pepe.com/member/faucet')
                    response_messege(f'EarnPP FaucetPay Withdrawed{currency}')
                    #response_messege('Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'ipfixer'}}
                    result = collection.update_one(query, update)
                    return

                else:
                    print(title, 'restarting')
                    driver.uc_open('https://earn-pepe.com/member/faucetpay')
                    time.sleep(10)

    
        
        if sitekey == 2:
            print('Strting Feyorra withdraw')
            driver.uc_open('https://feyorra.site/member/faucetpay')
            time.sleep(5)
            for i in range(1,10):
                time.sleep(1)
                title =sb1.get_title()
                print(title)
                if 'Just' in title:
                    cloudflare(sb1, login = False)
                elif 'Faucetpay Transfer' in title:
                    print(title, 'FaucetPay found')
                    response_messege(f'Feyorra FaucetPay Loaded{currency}')
                    pyautogui.click(fey_x, fey_y)
                    #pyautogui.click(1288, 517) #trx
                    #pyautogui.click(679, 704) #doge
                    time.sleep(5)
                    driver.execute_script(f"window.scrollTo(0, 700);")
                    time.sleep(2)
                    #cloudflare(driver, True)
                    solve_icon_captcha(driver, fey=True)
                    time.sleep(2)
                    #driver.uc_click('button.claim-button')
                    #driver.uc_open('https://feyorra.site/member/faucet')
                    response_messege(f'Feyorra FaucetPay Withdrawed{currency}')
                    #response_messege('Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'ipfixer'}}
                    result = collection.update_one(query, update)
                    return

                else:
                    print(title, 'restarting')
                    driver.uc_open('https://feyorra.site/member/faucetpay')
                    time.sleep(10)


        if sitekey == 3:
            print('Strting ClaimC withdraw')
            driver.uc_open('https://claimcoin.in/withdraw')
            time.sleep(5)
            for i in range(1,10):
                time.sleep(1)
                title =sb1.get_title()
                print(title)
                if 'Just' in title:
                    cloudflare(sb1, login = False)
                elif 'Withdraw' in title:
                    print(title, 'FaucetPay found')
                    response_messege('ClaimC FaucetPay Loaded')
                    pyautogui.click(1381, 602) #trx
                    #pyautogui.click(564, 737) #doge
                    time.sleep(5)
                    driver.execute_script(f"window.scrollTo(0, 1000);")
                    time.sleep(2)
                    response_messege('ClaimC Captcha Withdrawed')
                    solve_least_img(driver)
                    time.sleep(2)
                    password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][name="wallet"].form-control')
                    password_input.clear()
                    password_input.send_keys(claimc_email)
                    time.sleep(2)
                    #driver.uc_click('button.btn.btn-dark')
                    driver.uc_open('https://claimcoin.in/withdraw')
                    response_messege('ClaimC FaucetPay Withdrawed')
                    #response_messege('Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'ipfixer'}}
                    result = collection.update_one(query, update)
                    return

                else:
                    print(title, 'restarting')
                    driver.uc_open('https://claimcoin.in/withdraw')
                    time.sleep(10)

    
    
    except Exception as e:
        print(f'ERR on withdraw{e}')
        response_messege(f'EarnPP FaucetPay ERR on withdraw{e}')
    

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
bitmoon_coins = None
earnpp_coins_pre = None
feyorra_coins_pre = None
claimc_coins_pre = None
earnpp_limit_reached = None
feyorra_limit_reached = None
#if run_sb1:
sb1 = None
def are_extensions_exist():
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cookie_icon.png", region=(1625, 43, 400, 300), confidence=0.9)
            #pyautogui.click(x, y)
            print("extension_icon Button Found")
            return False

        except pyautogui.ImageNotFoundException:
            print("No extension_icon Button.")
            return True
        


def get_blacklistedip2(input):
    ips = []
    collectionbip = db[f'LocalCSB']
    quer2y = {"type": "main"}
    dochh = collectionbip.find_one(quer2y)
    blacklistedIP = dochh["blacklistedIP2"]

    for x in range(1,5):
        fn = f'F{farm_id}L{x}'
        try:
            if fn == input:
                continue
            else:
                data_list = blacklistedIP[fn]
                ips = ips + data_list
                print('Layout:',x)

        except Exception as e:
            pass
    print(ips)
    return ips


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



def get_browser_proxy():
    collectionbip = db[f'LocalCSB']
    quer2y = {"type": "main"}
    dochh = collectionbip.find_one(quer2y)
    proxy = dochh["browser_proxy"]
    print('BRowser PRoxy :', proxy)
    global browser_proxy
    browser_proxy = proxy
    return browser_proxy

def get_icon_path_list():
    global icon_path_list
    collectionbip = db[f'LocalCSB']
    quer2y = {"type": "main"}
    dochh = collectionbip.find_one(quer2y)
    icon_path_list = dochh["icon_path_list"]
    print('icon_path_list :', icon_path_list)
    return icon_path_list

def sweet_enable():
    for x in range(2):
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/sweet_dis_icon.png",  region=(1625, 43, 400, 300), confidence=0.9)
            pyautogui.click(x, y)
            for i in range(5):
                time.sleep(3)
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/sweet_connect.png", confidence=0.8)
                    pyautogui.click(x, y)
                    time.sleep(5)
                    pyautogui.click(300, 300)
                    time.sleep(3)
                    return
                except pyautogui.ImageNotFoundException:
                    print("Waiting for Sweet to pop")
        except pyautogui.ImageNotFoundException:
            print("No icon_image_loaded Human.")


def mysterium_reinstaller():
    #find externsion
    #delete
    #install 
    response_messege('Changed IP🔴 :Mys Reinstaller')
    current_window = sb1.current_window_handle
    all_windows = sb1.window_handles
    for window in all_windows:
        if window != current_window:
            sb1.switch_to.window(window)
            sb1.close()  # Close the tab
            sb1.connect()
    sb1.switch_to.window(current_window)
    sb1.uc_open("chrome://extensions/")
    pyautogui.click(300, 300)
    time.sleep(3)
    for i in range(4):
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_connected.png", region=(1625, 43, 400, 300), confidence=0.99)
            pyautogui.rightClick(x, y)
            for i in range(5):
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/remove_from_chrome.png", confidence=0.95)
                    pyautogui.click(x, y)
                    for i in range(5):
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/remove_button.png", confidence=0.95)
                            pyautogui.click(x, y)
                            time.sleep(3)
                            pyautogui.click(x, y)
                            time.sleep(1)
                            pyautogui.click(x, y)
                            time.sleep(1)

                            mysterium = install_extensions('mysterium')
                            time.sleep(2)
                            gg = pin_extensions()
                            
                            if gg:
                                fix_wrong_pins()
                                return mysterium
                            else:
                                break
                        except pyautogui.ImageNotFoundException:
                            print("No icon_image_loaded Human.")

                except pyautogui.ImageNotFoundException:
                    print("No icon_image_loaded Human.")

        except pyautogui.ImageNotFoundException:
            print("No icon_image_loaded Human.")
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.99)
            return
        except pyautogui.ImageNotFoundException:
            print("No icon_image_loaded Human.")
            mysterium = install_extensions('mysterium')
            time.sleep(2)
            gg = pin_extensions()
            if gg:
                fix_wrong_pins()
                return mysterium
            


def fix_wrong_pins():
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/wrong_pin.png", region=(1625, 40, 400, 300), confidence=0.98)
        pyautogui.moveTo( 1778,82)
        time.sleep(1)
        pyautogui.mouseDown( 1778,82 ,button='left')
        time.sleep(1)
        pyautogui.moveTo( 1741,82 )
        time.sleep(1)
        pyautogui.mouseUp( 1741,82 ,button='left')
        time.sleep(1)
    except Exception as e:
        print('ERR fix wrong pin',e)



browser_proxy = ''
query = {"type": "main"}
refresh_count = 0
get_mails_passowrds(farm_id)
for frm in CSB1_farms:
    collection_csb = db[f'Farm{frm}']
    update = {"$set": {"response": f'Changed IP🔴: Starting Farm:{farm_id}'}}
    result = collection_csb.update_one(query, update)
    update = {"$set": {"request": 'ipfixer'}}
    result = collection_csb.update_one(query, update)

def open_browsers():
    global sb1
    global chrome_user_data_dir
    global layout
    global browser_proxy

    browser_proxy  =get_browser_proxy()

    quer2y = {"type": "main"}
    dochh2 = collection.find_one(quer2y)
    layout = dochh2["withdraw_mail"]
    print(f'Farm ID:{farm_id} | Layout: {layout}')
    chrome_user_data_dir = f'/root/.config/google-chrome/{browser_proxy}{layout}'

    sb1 = Driver(uc=True, headed=True, undetectable=True, undetected=True, user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path, page_load_strategy='none')#, proxy=browser_proxy )
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
    time.sleep(7)
    print(sb1.get_title())
    gggv = are_extensions_exist()
    get_mails_passowrds(farm_id)
    if gggv:
        if fresh >= 3:
            
            sweet = install_extensions('sweet')
            cookie = install_extensions('cookie')
            mysterium = install_extensions('mysterium')
            fingerprint = install_extensions('fingerprint')
            mfhelper = install_extensions('mfhelper')
            if fingerprint and mysterium and sweet and cookie and mfhelper:
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
    
    time.sleep(10)
    return sb1

def update_target_ip(new_ip):
    try:
        file_path = "mfhelper/config.json"
        # Open the JSON file and load its contents
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Update the targetIP field
        data["targetIP"] = new_ip
        
        # Write the updated data back to the JSON file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"targetIP updated to {new_ip}")
    except Exception as e:
        print(f"An error occurred: {e}")
def open_faucets():
    global sb1
    while True:
        try:
            quer2y = {"type": "main"}
            dochh2 = collection.find_one(quer2y)
            layout2 = dochh2["withdraw_mail"]
            print(f'Farm ID:{farm_id} | Layout: {layout2}')
            browser_proxy2  =get_browser_proxy()
            chrome_user_data_dir2 = f'/root/.config/google-chrome/{browser_proxy2}{layout2}'
            if chrome_user_data_dir == chrome_user_data_dir2 and layout == layout2 and browser_proxy2 == browser_proxy:
                response_messege('Same Browser ...')
                pass
            else:
                response_messege(f'Resetting Browser')
                try:
                    subprocess.run(['pkill', '-f', 'chrome'], check=True)
                    print(f"All chrome processes killed successfully.")
                except subprocess.CalledProcessError:
                    print(f"Failed to kill chrome processes or no processes found.")
                time.sleep(10)
                sb1 = open_browsers()
                continue
            pyautogui.moveTo(100, 200)
            pyautogui.moveTo(200, 400)
            current_window = sb1.current_window_handle
            all_windows = sb1.window_handles
            for window in all_windows:
                if window != current_window:
                    sb1.switch_to.window(window)
                    sb1.close()  # Close the tab
                    sb1.connect()
            sb1.switch_to.window(current_window)
            sb1.uc_open("chrome://extensions/")
            time.sleep(1)
            global blacklistedIP
            collectionbip = db[f'LocalCSB']
            quer2y = {"type": "main"}
            dochh = collectionbip.find_one(quer2y)
            blacklistedIP2 = dochh["blacklistedIP"]
            if len(blacklistedIP) <= len(blacklistedIP2):
                blacklistedIP += blacklistedIP2
            print(blacklistedIP)
            lay = re.search(r'\d+', layout2).group()
            other_blacklists = get_blacklistedip2(f'F{farm_id}L{lay}')
            if other_blacklists:
                blacklistedIP = blacklistedIP + other_blacklists
            response_messege('Fixing IP')
            ip_address = get_ip(sb1)
            ipscore = get_ipscore(ip_address)
            proxycheck = get_proxycheck(sb1, ip_address, server_name= server_name1)
            if ipscore and proxycheck == 200:
                if ip_address in blacklistedIP:
                    print('IP Blacklisted')
                    response_messege(f'IP Blacklisted{ip_address}')
                    ipfixer()
                    ip_required = fix_ip(sb1, server_name1)
                    ip_address = get_ip(sb1)

                else:
                    print(f'Good IP found: {ip_address}')
                    for frm in CSB1_farms:
                        collection_csb = db[f'Farm{frm}']
                        query = {"type": "main"}
                        doc = collection_csb.find_one(query)
                        res = doc["response"]
                        req = doc["request"]
                        if req == 'ipfixer' and 'Changed IP' in res:
                            ipfixer()
                            ip_required = fix_ip(sb1, server_name1)
                            ip_address = get_ip(sb1)

            else:
                ipfixer()
                ip_required = fix_ip(sb1, server_name1)
                ip_address = get_ip(sb1)

            ip_address = get_ip(sb1)
            
            if ip_address:
                current_window = sb1.current_window_handle
                all_windows = sb1.window_handles
                for window in all_windows:
                    if window != current_window:
                        sb1.switch_to.window(window)
                        sb1.close()  # Close the tab
                        sb1.connect()
                sb1.switch_to.window(current_window)
                sb1.uc_open("chrome://extensions/")
                time.sleep(2)
                ip_required = ip_address
                add_blacklistedip2(f'F{farm_id}L{lay}', ip_address)
                get_mails_passowrds(farm_id)
                update_target_ip(ip_address)
                ip_address = get_ip(sb1)
                if ip_required == ip_address:
                    response_messege('EarnPP Loging')
                    if earnpp:

                        earnpp_window = handle_site(sb1, "https://earn-pepe.com/member/faucet","Faucet | Earn-pepe" , "Home | Earn-pepe", 1, [], ip_required)
                        if earnpp_window == 404:
                            raise Exception(" earnpp_window == 404")
                        print(f"EarnPP window handle: {earnpp_window}")
                    else:
                        earnpp_window = None
                else:
                    raise Exception("Ip changed")
                ip_address = get_ip(sb1)
                if ip_required == ip_address:
                    response_messege('Feyorra Loging')
                    if feyorra:
                        sb1.open_new_window()
                        feyorra_window = handle_site(sb1, "https://feyorra.site/member/faucet", "Faucet | Feyorra" , "Home | Feyorra", 2, [earnpp_window], ip_required)
                        if feyorra_window == 404:
                            raise Exception(" feyorra_window == 404")
                        print(f"Feyorra window handle: {feyorra_window}")
                    else:
                        feyorra_window = None
                else:
                    raise Exception("Ip changed")
                
                if ip_required == ip_address:
                    response_messege('ClaimC Loging')
                    if claimcoin:
                        ip_address = get_ip(sb1)
                        sb1.open_new_window()
                        claimcoin_window = handle_site(sb1, "https://claimcoin.in/faucet", "Faucet | ClaimCoin - ClaimCoin Faucet", "ClaimCoin - MultiCurrency Crypto Earning Platform", 3, [earnpp_window, feyorra_window], ip_required)
                        if claimcoin_window == 404:
                            raise Exception(" claimcoin_window == 404")
                        print(f"ClaimCoin window handle: {claimcoin_window}")
                    else:
                        claimcoin_window = None
                else:
                    raise Exception("Ip changed")

                
                ip_address = get_ip(sb1)
                if ip_required == ip_address:
                    response_messege('Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'mainscript'}}
                    result = collection.update_one(query, update)

                    all_window_handles = [earnpp_window, feyorra_window, claimcoin_window]
                    close_extra_windows(sb1, all_window_handles)
                    sb1.switch_to.window(earnpp_window)
                    print(f"Windows: EarnPP: {earnpp_window}, Feyorra: {feyorra_window}, ClaimCoin: {claimcoin_window}")
                    global reset_count 
                    global reset_count_isacc 
                    global previous_reset_count
                    global earnpp_limit_reached 
                    global feyorra_limit_reached 

                    earnpp_limit_reached = None
                    feyorra_limit_reached = None
                    
                    reset_count = 0
                    reset_count_isacc = 0
                    previous_reset_count = 0


                    return earnpp_window, feyorra_window, claimcoin_window,  ip_address, ip_required
        except Exception as e:
                response_messege(f'Resetting Browser{e}')
                try:
                    subprocess.run(['pkill', '-f', 'chrome'], check=True)
                    print(f"All chrome processes killed successfully.{e}")
                except subprocess.CalledProcessError:
                    print(f"Failed to kill chrome processes or no processes found.{e}")
                time.sleep(10)
                sb1 = open_browsers()
                reset_count +=15

def debug_messages(messages):
    if debug_mode:
        print(messages)

earnpp_count = 0 
feyorra_count = 0
claimcoin_count = 0


earnpp_window, feyorra_window, claimcoin_window,  ip_address, ip_required = open_faucets()
start_time4 = 0
time.sleep(2)
print('Starting Loop')


while True:
    try:
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        mainscript = control_panel()
        print('control_panel', mainscript)
        if mainscript == 1:
            pyautogui.press('enter')
            
            debug_messages(f'Ip address Found:{ip_address}')
            cc_faucet = None
            if reset_count_isacc >= 7:
                response_messege('oops.. reset_count_isacc triggers')
                blacklistedIP.append(ip_address)
                mysterium_vpn_connect(server_name1, sb1)
                time.sleep(7)
                mysterium_vpn_connect(server_name1, sb1)
                time.sleep(5)
                
                reset_count = 16
                reset_count_isacc = 0

            ip_address = get_ip(sb1) 
            if reset_count >= 15:
                print('reset count higher')
                
                earnpp_window, feyorra_window, claimcoin_window,  ip_address, ip_required = open_faucets()
                reset_count = 0
                reset_count_isacc = 0

            if previous_reset_count == reset_count:
                reset_count = 0
            else:
                previous_reset_count = reset_count

            if ip_address == ip_required:
                debug_messages(f'Ip address Match:{ip_address}')

                all_window_handles = [earnpp_window, feyorra_window, claimcoin_window]
                close_extra_windows(sb1, all_window_handles)

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
                            gg = solve_icon_captcha(sb1 , False)
                            if gg:
                                earnpp_limit_reached = None
                            else:
                                if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!') or sb1.is_text_visible('Limit Reached, Please claim shortlinks to increase your claim limit!'):
                                    debug_messages(f'EarnPP Limit Reached')
                                    if earnpp_limit_reached == None:
                                        response_messege('EarnPP Limit Reached')
                                    earnpp_limit_reached = True
                                else:
                                    refresh_count +=5
                            debug_messages(f'Solved Icon Captcha on EarnPP')
                            

                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on EarnPP')
                            response_messege('Lock.. Found on EarnPP')
                            earnpp_coins = 0
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
                            reset_count +=5
                        elif 'Google' in title:
                            reset_count +=5
                        else:
                            debug_messages(f'EarnPP not Found:{title} | reset:{reset_count}')
                            reset_count +=1

                    except Exception as e:
                        if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!') or sb1.is_text_visible('Limit Reached, Please claim shortlinks to increase your claim limit!'):
                            debug_messages(f'EarnPP Limit Reached')
                            response_messege('EarnPP Limit Reached')
                            earnpp_limit_reached = True
                        else:
                            debug_messages(f'ERR on EarnPP:{e}')
                            reset_count +=3
                
                if feyorra:
                    try:
                        debug_messages(f'Switching Pages to Feyorra')
                        pyautogui.press('enter')
                        sb1.switch_to.window(feyorra_window)
                        debug_messages(f'Getting Pages Titile:Feyorra')
                        pyautogui.press('enter')
                        title =sb1.get_title()

                        if 'Faucet | Feyorra' in title:
                            debug_messages(f'Solving Icon Captcha on Feyorra')
                            val = get_coins(sb1, 2)
                            if val:
                                feyorra_coins = val
                            gg = solve_icon_captcha(sb1, True)
                            if gg:
                                feyorra_limit_reached =None
                            else:
                                try:
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                                    print("verify_cloudflare git Found")
                                    debug_messages(f'cloudflare Found')
                                    cloudflare(sb1, login=True)
                                    time.sleep(1)
                                    sb1.uc_click('#loginBtnText')
                                except Exception as e:
                                    print('No clousflare on feyorra')
                                if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!'):
                                    debug_messages(f'Feyorra Limit Reached')
                                    if feyorra_limit_reached == None:   
                                        response_messege('Lock.. Found on Feyorra')
                                    feyorra_limit_reached =True
                                else:
                                    refresh_count +=5

                                
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on Feyorra')
                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed Feyorra')
                        elif 'aintenance' in title:
                            debug_messages(f'maintenance.. Found on Feyorra')
                            response_messege('maintenance.. Found on Feyorra')
                            feyorra_coins = 0
                        elif 'Google' in title:
                            reset_count +=5
                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on Feyorra')
                            if feyorra_limit_reached == None:   
                                response_messege('Lock.. Found on Feyorra')
                            feyorra_coins =0
                        elif 'Home | Feyorra' in title or 'Login' in title:
                            debug_messages(f'LOGIN.. Found on Feyorra')
                            response_messege('LOGIN.. Found on Feyorra')
                            feyorra_coins = 0
                            reset_count +=5
                        else:
                            debug_messages(f'Feyorra not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                    except Exception as e:
                        pyautogui.press('enter')
                        if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!'):
                            debug_messages(f'Feyorra Limit Reached')
                            response_messege('Feyorra Limit Reached')
                            feyorra_limit_reached =True
                        else:
                            debug_messages(f'ERR on Feyorra:{e}')
                            reset_count +=3

                if claimcoin:

                    try:
                        debug_messages(f'Time capture in ClaimCoins')
                        if claimcoin: #seconds_only > 14:
                            debug_messages(f'Switching Pages to ClaimCoins:{seconds_only}')
                            sb1.switch_to.window(claimcoin_window)
                            #pyautogui.press('enter')
                            debug_messages(f'Getting Pages Titile:ClaimCoins')
                            title =sb1.get_title()
                            if 'Faucet | ClaimCoin' in title:
                                if claimcoin_count == 0:
                                    if sb1.is_text_visible(' Invalid Captcha') or sb1.is_text_visible('Invalid Captcha'):
                                        debug_messages(f' Invalid Captcha | reset:{reset_count_isacc}')
                                        if reset_count_isacc > 1:
                                            response_messege(f'Invalid Captcha | reset:{reset_count_isacc}')
                                        pyautogui.press('f5')
                                        claimcoin_count = 1 
                                    else:
                                        if sb1.is_text_visible('Ready'):
                                            claimcoin_count = 1 
                                        else:
                                            reset_count_isacc = 0
                                debug_messages(f'Solving Icon Captcha on ClaimCoins')
                                val = get_coins(sb1, 3)
                                if val:
                                    claimc_coins = val
                                cc_faucet =  find_and_click_collect_button(sb1)
                                if cc_faucet:
                                    claimcoin_count = 0
                                    debug_messages(f'Solved Icon Captcha on Claimcoins')
                                sb1.switch_to.window(claimcoin_window)
                            elif 'ust a' in title:
                                debug_messages(f'Just.. Found on Claimcoins')

                                cloudflare(sb1, login = False)
                                debug_messages(f'Just Fixed Claimcoins')

                            elif 'Lock' in title:
                                debug_messages(f'Lock.. Found on Claimcoins')
                                response_messege('Lock.. Found on Claimcoins')
                                claimc_coins = 0
                            elif 'ClaimCoin - MultiCurrency Crypto Earning Platform' in title or 'Login' in title:
                                debug_messages(f'LOGIN.. Found on ClaimCoin')
                                response_messege('LOGIN.. Found on ClaimCoin')
                                claimc_coins = 0
                                reset_count +=5
                            elif 'aintenance' in title:
                                debug_messages(f'aintenance.. Found on Claimcoins')
                                response_messege('aintenance.. Found on Claimcoins')
                                claimc_coins = 0
                            else:
                                debug_messages(f'ClamCoim not Found:{title} | reset:{reset_count}')
                                reset_count +=1
                        
                    except Exception as e:
                        debug_messages(f'ERR on ClamCoim:{e}')
                        reset_count +=1



                elapsed_time = time.time() - start_time
                seconds_only = int(elapsed_time)
                debug_messages(f'ClaimCoins Seconds:{seconds_only}')
                if seconds_only > 20:
                    start_time = time.time()
                    if earnpp_coins == earnpp_coins_pre:
                        start_time = time.time()

                        if refresh_count >= 30:
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

                        if refresh_count >= 30:
                            pyautogui.press('enter')
                            response_messege(f'feyorra_coins same {feyorra_coins}| count:{refresh_count} | {seconds_only}')
                            refresh_count = 0
                            sb1.switch_to.window(feyorra_window)
                            sb1.uc_open('https://feyorra.site/member/faucet')
                        if feyorra_limit_reached:
                            pass
                        else:
                            if refresh_count >= 50:
                                reset_count +=5
                            refresh_count +=1
                    elif claimc_coins == claimc_coins_pre and cc_faucet and claimcoin:
                        start_time = time.time()
                        if refresh_count >= 30:
                            response_messege(f'claimc_coins same {claimc_coins}| count:{refresh_count} | {seconds_only}')
                            sb1.switch_to.window(claimcoin_window)
                            sb1.uc_open("https://claimcoin.in/faucet")
                            refresh_count = 0
                        
                        refresh_count +=1
                    else:
                        earnpp_coins_pre = earnpp_coins
                        feyorra_coins_pre = feyorra_coins
                        claimc_coins_pre = claimc_coins
                        refresh_count = 0

                elapsed_time3 = time.time() - start_time3
                seconds_only3 = int(elapsed_time3)
                debug_messages(f'MangoDB Seconds:{seconds_only3}')
                if seconds_only3 > 130:
                    print(f'EarnPP:{earnpp_coins} | Feyorra:{feyorra_coins} | ClaimC:{claimc_coins}| ')
                    if earnpp_coins and feyorra_coins: #and claimc_coins: #and bitmoon_coins:
                        start_time3 = time.time()
                        emailgg = f'{earnpp_email} <br>country: {server_name1} <br>Current Layout:{layout} <br>Farm:{farm_id}'
                        insert_data(ip_address, earnpp_coins, feyorra_coins, claimc_coins, emailgg)
                    else:
                        response_messege(f'EarnPP:{earnpp_coins} | Feyorra:{feyorra_coins} | ClaimC:{claimc_coins}')
                    #elif earnpp_coins and feyorra_coins and claimc_coins:
                    #    start_time3 = time.time()
                    #    insert_data(ip_address, earnpp_coins, feyorra_coins, claimc_coins, 0)
                    
                    

                else:
                    print(f'MngoDB:{seconds_only3}')
            else:
                print('Ip fucked')
                reset_count +=5
                response_messege(f'Ip fucked|{reset_count}|{ip_address}')
                #ip_required = fix_ip(sb1, server_name1)
                #ip_address = get_ip(sb1)
    

        if mainscript == 2:
            earnpp_window, feyorra_window, claimcoin_window,  ip_address, ip_required = open_faucets()
            reset_count = 0

        if mainscript == 3:
            response_messege('Ip Resettinggg...')
            reset_count_isacc = 10
            query = {"type": "main"}
            update = {"$set": {"request": 'mainscript'}}
            result = collection.update_one(query, update)



        if mainscript == 4:
            withdraw_faucet(sb1, 1) 

        if mainscript == 6:
            withdraw_faucet(sb1, 2) 
        if mainscript == 7:
            withdraw_faucet(sb1, 3) 

        if mainscript == 8:
            sb1.quit()
            break

        if mainscript == 5:
            time.sleep(15)
            print('Pause...')

    except Exception as e:
        print(f'Oh Hell No{e}')
        response_messege(f'Oh Hell No{e}')
        if 'no such window' in str(e) or 'invalid session' in str(e) or 'NoHTTPConnectionPool' in str(e):
            response_messege(f'Resetting Browser')
            try:
                subprocess.run(['pkill', '-f', 'chrome'], check=True)
                print("All chrome processes killed successfully.")
            except subprocess.CalledProcessError:
                print("Failed to kill chrome processes or no processes found.")
            time.sleep(10)
            sb1 = open_browsers()
            reset_count +=15
        reset_count +=1
