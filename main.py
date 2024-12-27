

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
            server_name1 = 'finland' #'portugal'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'merlelcn@gmail.com'
            earnpp_pass = 'I2Ne7C329jJt'
            feyorra_email = 'merlelcn@gmail.com'
            feyorra_pass = 'I2Ne7C329jJt'

        elif '3' in layout:
            server_name1 = 'finland' #'portugal'
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
            server_name1 = 'egypt'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'yvonne12463@gmail.com'
            earnpp_pass = 'Uwuinsta@2005'
            feyorra_email = 'yvonne12463@gmail.com'
            feyorra_pass = 'Uwuinsta@2005'

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
            server_name1 = 'egypt'
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
            earnpp_email = 'ddilakshi232@gmail.com'
            earnpp_pass = 'Uwuinsta@2005'
            feyorra_email = 'ddilakshi232@gmail.com'
            feyorra_pass = 'Uwuinsta@2005'
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
claimcoin = True
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
            if vpn == False and tor == False and fraud_score <= 90: #and active_vpn == False and active_tor == False and fraud_score < 90:
                return True
            else:
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
            print(f'Bad IP detected: {ip_address}. Changing IP...')
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
                print(f'Bad IP detected: {ip_address}. Changing IP...')
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
        fix_wrong_pins()
        time.sleep(1)
        sweet_enable()
        driver.uc_open('https://app.mysteriumvpn.com/')
        time.sleep(5)
        titile = sb1.get_title()
        pyautogui.click(113, 100)
        time.sleep(1)

        if 'Home' in titile:

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.95)
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
                                            pyautogui.click(1714, 300)
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


#V2
def solve_icon_captcha(sb1):
    try:
        # Extract all captcha icons
        captcha_icons = sb1.find_elements('[class*="fas fa-"]')

        for captcha_icon in captcha_icons:
            # Skip icons with inline styles
            if captcha_icon.get_attribute('style'):
                continue

            # Get the class names of the captcha icon
            captcha_icon_classes = captcha_icon.get_attribute('class').split()
            captcha_icon_classes = [cls for cls in captcha_icon_classes if cls.startswith("fa-")]

            if not captcha_icon_classes:
                continue  # Skip if no valid 'fa-' class found

            captcha_icon_class = captcha_icon_classes[0]  # Use the first valid 'fa-' class

            # Get the available icon options (filter out decoys)
            icon_options = sb1.find_elements('i[class*="fas fa-"]')

            for option in icon_options:
                # Skip options with inline styles
                if option.get_attribute('style'):
                    continue

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


def cloudflare(sb, login = True):
    try:
        page_title = sb.get_title()
        gg = False
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


def cloudflare_withoutSB():
    try:
        gg = False
        while gg == False:
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                print("verify_cloudflare git Found")
                if x and y:
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                        print("verify_cloudflare git Found")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.7)
                            pyautogui.click(x, y)
                            time.sleep(5)

                        except Exception as e:
                            print(e)
                    except Exception as e:
                        print(e)             
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_success.png", confidence=0.7)
                        pyautogui.click(x, y)
                        time.sleep(1)
                        return True

                    except Exception as e:
                        print(e)
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
                    solve_icon_captcha(driver)
                    time.sleep(2)
                    #driver.uc_click('button.claim-button')
                    driver.uc_open('https://earn-pepe.com/member/faucet')
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
                    solve_icon_captcha(driver)
                    time.sleep(2)
                    #driver.uc_click('button.claim-button')
                    driver.uc_open('https://feyorra.site/member/faucet')
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

def solve_icon_captcha_gui():
    clipboard.copy('gg')
    pyautogui.scroll(2000)
    time.sleep(1)
    clip = clipboard.paste()
    print(clip)
    if 'x is' in clip:
        coin = clip.split()[0]
        x_match = re.search(r"x is (\d+)", clip)
        x = int(x_match.group(1)) if x_match else None
        ip_match = re.search(r"ip is (\d+\.\d+\.\d+\.\d+)", clip)
        ip = ip_match.group(1) if ip_match else None
        if x > 1:
            for i in range(1,11):
                z = 5 * i
                y = 400 + z
                pyautogui.moveTo(x,y)
                pyautogui.click(x,y)
        
        return coin, ip

    else:
        print('There is no X is :',clip)
    return None, None



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
                ip_address = get_ip(sb1)
                if ip_required == ip_address:
                    response_messege('ClaimC Loging')
                    if claimcoin:
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

def switching_tabs(tab_name):
    if tab_name ==1:
        pyautogui.click(55,102)
        pyautogui.mouseDown('ctrl')
        pyautogui.press('1')
        pyautogui.mouseUp('ctrl')

while True:
    try:
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        mainscript = control_panel()
        print('control_panel', mainscript)
        if mainscript == 1:
            sb1.disconnect()
            if earnpp:
                if earnpp:
                    try:
                        debug_messages(f'Switching Pages to EarnPP')
                        pyautogui.click(55,102)
                        pyautogui.mouseDown('ctrl')
                        pyautogui.press('1')
                        pyautogui.mouseUp('ctrl')
                        debug_messages(f'Getting Pages Titile:EarnPP')
                        title = get_current_window_title()
                        print(title)
                        if 'Faucet | Earn-pepe' in title:
                            debug_messages(f'Solving Icon Captcha on EarnPP')
                            earnpp_coins, ip_address = solve_icon_captcha_gui()
                            
                            if ip_address:
                                earnpp_limit_reached = None
                            else:
                                
                                cloudflare_withoutSB()
                                try:
                                    x,y = pyautogui.locateCenterOnScreen(image='/root/Desktop/MFV6/images/claim_pp.png',confidence=0.94)
                                    pyautogui.click(x,y)
                                except Exception as e:
                                    print('not found claim on pp')
                                refresh_count +=3
                            debug_messages(f'Solved Icon Captcha on EarnPP')


                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on EarnPP')
                            response_messege('Lock.. Found on EarnPP')
                            earnpp_coins = 0
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on EarnPP')
                            sb1.connect()
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
                        else:
                            debug_messages(f'EarnPP not Found:{title} | reset:{reset_count}')
                            reset_count +=1

                    except Exception as e:
                            debug_messages(f'ERR on EarnPP:{e}')
                            reset_count +=1
                
            else:
                print('Ip fucked')
                reset_count +=4
                response_messege(f'Ip fucked|{reset_count}|{ip_address}')
                #ip_required = fix_ip(sb1, server_name1)
                #ip_address = get_ip(sb1)
    

        if mainscript == 2:
            sb1.connect()
            earnpp_window, feyorra_window, claimcoin_window,  ip_address, ip_required = open_faucets()
            reset_count = 0

        if mainscript == 3:
            sb1.connect()
            response_messege('Ip Resettinggg...')
            reset_count_isacc = 10
            query = {"type": "main"}
            update = {"$set": {"request": 'mainscript'}}
            result = collection.update_one(query, update)



        if mainscript == 4:
            sb1.connect()
            withdraw_faucet(sb1, 1) 

        if mainscript == 6:
            sb1.connect()
            withdraw_faucet(sb1, 2) 
        if mainscript == 7:
            sb1.connect()
            withdraw_faucet(sb1, 3) 

        if mainscript == 8:
            sb1.connect()
            sb1.quit()
            break

        if mainscript == 5:
            
            for i in range(1,6):
                time.sleep(1)
                print('Pause...')


    except Exception as e:
        sb1.connect()
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
