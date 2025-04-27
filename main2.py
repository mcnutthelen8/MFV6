

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
            server_name1 = 'sri lanka'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'khabibmakanzie2@gmail.com'
            earnpp_pass = 'khabibmakanzie2'
            feyorra_email = 'khabibmakanzie2@gmail.com'
            feyorra_pass = 'khabibmakanzie2'

        elif '2' in layout:
            server_name1 = 'sri lanka' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'anrogedyyr@gmail.com'
            earnpp_pass = ''
            feyorra_email = 'anrogedyyr@gmail.com'
            feyorra_pass = ''
        elif '3' in layout:
            server_name1 = 'sri lanka' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'grandkolla999br@gmail.com'
            earnpp_pass = 'grandkolla999br'
            feyorra_email = 'grandkolla999br@gmail.com'
            feyorra_pass = 'grandkolla999br'


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
            server_name1 = 'france'
            CSB1_farms = [1, 2, 3, 4, 5]
            earnpp_email = 'sevensevengk@gmail.com'
            earnpp_pass = 'sevensevengk'
            feyorra_email = 'sevensevengk@gmail.com'
            feyorra_pass = 'sevensevengk'

        elif '2' in layout:
            server_name1 = 'france' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'kg7seven@gmail.com'
            earnpp_pass = 'kg7seven'
            feyorra_email = 'kg7seven@gmail.com'
            feyorra_pass = 'kg7seven'

        elif '3' in layout:
            server_name1 = 'france' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'neyov32511@gmail.com'
            earnpp_pass = 'neyov32511'
            feyorra_email = 'neyov32511@gmail.com'
            feyorra_pass = 'neyov32511'
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
            server_name1 = 'hungary' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'shiladid323@gmail.com'
            earnpp_pass = 'shiladid323'
            feyorra_email = 'shiladid323@gmail.com'
            feyorra_pass = 'shiladid323'


        elif '3' in layout:
            server_name1 = 'hungary' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'andrpewrea@gmail.com'
            earnpp_pass = 'andrpewrea'
            feyorra_email = 'andrpewrea@gmail.com'
            feyorra_pass = 'andrpewrea'

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
            server_name1 = 'italy' #'chile'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'ferhng790@gmail.com'
            earnpp_pass = 'ferhng790'
            feyorra_email = 'ferhng790@gmail.com'
            feyorra_pass = 'ferhng790'
        elif '3' in layout:
            server_name1 = 'italy' #'chile'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            earnpp_email = 'giferhan079@gmail.com'
            earnpp_pass = 'giferhan079'
            feyorra_email = 'giferhan079@gmail.com'
            feyorra_pass = 'giferhan079'

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
feyorra = False
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
        #print(blacklistedIP)
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
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cookie_icon.png", region=(1525, 43, 600, 300), confidence=0.99)
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

def clean_string2(s):
    # Replace '-' with whitespace
    s = s.replace('-', ' ')
    s = s.replace('.', ' ')
    
    # List of words/phrases to remove (ensure spaces are handled properly)
    words_to_remove = {"bxs", "bx", "la", "fa", "fas fa", "ri", "far", "ti ti", "bi bi", "far fa", "fas", "fa", "bi", "la la", "la"}
    
    # Use regex to remove exact words or phrases (word boundaries ensure whole words match)
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    
    # Remove the words and extra spaces
    cleaned_s = re.sub(pattern, '', s, flags=re.IGNORECASE)
    
    # Normalize spaces
    return ' '.join(cleaned_s.split())

#V2
def filter_and_replace(text):
    word_dict = {
        "coin": ["database", "penny"],
        "mouse": ['cursor', 'point'],
        "upload": [ "angle-up", "caret-square-up", "level-up", "transition-top","amount-up","chevron-double-up", "arrow-bar-up",  "arrow-up","arrow-alt-circle-up", "arrow-alt-up", "arrow-in-up","sort-up", "chevrons-up",  "chevron-up", "angle-double-up", "caret-up"],
        "download": [ "angle-down", "caret-square-down", "level-down", "transition-bottom","amount-down", "chevron-double-down", "arrow-bar-down","arrow-alt-circle-down", "arrow-down","arrow-alt-down", "arrow-in-down","sort-down" , "chevrons-down", "chevron-down","angle-double-down", "caret-down"],
        "paint": ["paint","spray","palette", "paint-bucket", "brush","color", "colour"],
        "rocket": ["flight-takeoff","airplane", "plane","fight", "space-shuttle" ,"space", "helicopter", "flight", "rocket"],
        "gem": ["diamond", "jewel"],
        "bird": ["twitter", "crow", "dove","yuque", "earlybirds", "kiwi"],
        "volume": ["megaphone","volume-up", "volume-down", "volume", "bullhorn", "megaphone", "loudspeaker"],
        "child": ["child","person","friends","female", "male","pray", "team", "group", "people", "running", "user", "restroom", "walking"],
        "tractor": ["bus-school","camper","truck", "ambulance", "roadster", "taxi","forklift"],
        "riding": ["motorcycle", "cycling","bicycle","motorbike", "bike","scooter", "moped", "biking"],
        "water": ["tint", "moisture", "rain", "droplet","contrast-drop", "blur-off","drop", "blur"],
        #"computer": ["mac", "laptop", "desktop", "device", "macbook", "imac", "display"],
        "heart": ["poker-hearts","suit-heart","heart-pulse","service-line", "gratipay", "service", "heart", "hearts"],
        #"tree": ["leaf", "seedling"],
        "glass": ["wine", "cup", "cocktail", "goblet","cup-straw","glass"],

        "bank": ['university'],
        "house": [ "community" ,"hospital", 'home', "city", "buildings","building", "hotel", "school", 'build',],
        "emo": ['mood','smile'],
        "bluetooth": ['blue'],
        "file": ['folder'],
        "display": ['laptop', 'computer',"mac", "laptop", "desktop", "macbook", "imac", "pc"],
        "comment": ["chat-left", "message-dots","message-square-detail",'message', 'chat','text','sms', "twitch", "comment", "chat" , "message", "text"],
        "bell": ['notifi'],
        "leaf": [ "cactus","canadian-maple-leaf", "growth", "pagelines" ,"flower", 'envira', 'pageline', 'seeding','grass', "leaf", "seedling","tree", "raspberry", "plant"],
        "chart": ['signal'],
        "cloud": ['weather'],
        "energy": ['lightning', 'zap', 'bolt',"flash"],
        #"camera": ["selfie","phone", "polaroid", "video","image","pic"],
        "spider": ['bug','insect'],
        "setting": ['cog', 'gear'],
        "fire": ["burn","hot", "flame", "torch"],
        "trash": ["bin", "garbage "],
        "flag": ["pennant", "banner"],
        #new list
        "pen": ["ballpen", "edit", "pencil","highlight"],
    
        "knife": ["slice", "utensils", "fork", "knife", "spoon" ,"kitchen"],

        "guitar": ["headset","playlist", "guitar", "bandlab", "music", "disc" ,"airpods","headphone","radio", "tiktok"],
        "close": ["times", "close", "xrp", "window-close", "x-lg"],
        "browser": ["edge","chrome", "google", "firefox", "explora", "browser", "world","www"],
        "hand": ["hand", "allergies", "finger", "thumb"],
    }
    # First, replace hyphens with spaces in the text
    text = text.replace('-', ' ')


    # Iterate over the word_dict and replace words in the text
    for category, words in word_dict.items():
        for word in words:
            # Replace hyphens with spaces in the word
            word = word.replace('-', ' ')
            # Replace the word with the category if it exists in the text
            if word in text:# or text in word:
                text = category#text.replace(word, category) #category # .replace(word, category)
                return text
    second_dict = {
        "upload": [  "top", "pull","-up"],
        "download": [ "-down", "bottom", "push"],
        "tractor": ["car", "bus","tir"],
        "close": ["x"],
    }
    for category, words in second_dict.items():
        for word in words:
            # Replace hyphens with spaces in the word
            word = word.replace('-', ' ')
            # Replace the word with the category if it exists in the text
            if word in text:# or text in word:
                text = category#text.replace(word, category) #category # .replace(word, category)
                return text

    return text


import re

def clean_string(s):
    # Replace '-' with whitespace
    s = s.replace('-', ' ')
    s = s.replace('.', ' ')
    
    # List of words/phrases to remove (ensure spaces are handled properly)
    words_to_remove = {"front","bxs", "bx bx", "la", "fa", "fas fa", "split", "ri", "far", "ti ti", "bi bi", "far fa", "fas", "fa", "bi", "la la", "la", "line", "lines", "engines", "brand", "alt"}
    
    # Use regex to remove exact words or phrases (word boundaries ensure whole words match)
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    
    # Remove the words and extra spaces
    cleaned_s = re.sub(pattern, '', s, flags=re.IGNORECASE)
    
    # Normalize spaces
    return ' '.join(cleaned_s.split())

def filter_string(s):
    # Define words that act as stop points
    stop_words = {"bxs", "bx bx", "la", "fa", "fas", "split", "ri", "far", "ti", "bi", "far", "fas", "fa", "bi",  "la", "line", "lines", "engines", "brand", "alt"}
    
    # Replace '-' with whitespace
    s = s.replace('.', ' ')
    s = s.replace('-', ' ')
    
    # Split the string into words
    words = s.split()
    
    # Iterate and remove words until we find a stop word
    while words and words[0] not in stop_words:
        words.pop(0)
    
    # Return the remaining words as a string
    return ' '.join(words)

def append_to_notepad(filename, captcha, answers):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"Captcha : {captcha}\n")
        f.write("Answers :\n")
        for answer in answers:
            f.write(f"{answer}\n")
        f.write("--------------------------------\n")

# Example usage
def mouse_moveclick(cropped_path="element_screenshot.png"):
    try:
        x, y = pyautogui.locateCenterOnScreen(cropped_path, confidence=0.9)
        pyautogui.moveTo(x, y , duration=0.1)
        pyautogui.click()
        return True
    except Exception as e:
        print(f"Error moving and clicking: {e}")


import glob

# Load and preprocess image
def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.GaussianBlur(img, (3, 3), 0)  # Denoise
    return img

# Feature detection using SIFT
def detect_keypoints(img):
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)
    return keypoints, descriptors

# Match keypoints with stored templates
def match_images(captcha, templates):
    best_match = None
    max_good_matches = 0

    kp1, des1 = detect_keypoints(captcha)

    if des1 is None:
        print("No descriptors found in captcha.")
        return None

    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    for template_path in templates:
        template = load_image(template_path)
        kp2, des2 = detect_keypoints(template)

        if des2 is None:
            continue

        matches = flann.knnMatch(des1, des2, k=2)

        # Apply Lowe's Ratio Test to filter matches
        good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]

        if len(good_matches) > max_good_matches:
            max_good_matches = len(good_matches)
            best_match = template_path

    return best_match

# Main function
def solve_captcha(captcha_path, template_folder):
    captcha = load_image(captcha_path)
    template_paths = glob.glob(f"{template_folder}/*.png")

    best_template = match_images(captcha, template_paths)

    if best_template:
        print(f"Best match found: {best_template}")
        return best_template
    else:
        print("No match found!")
        return None

def rename_with_code(filepath, category):
    if not os.path.exists(filepath):
        print(f"File '{filepath}' does not exist.")
        return
    
    # Get the directory and base filename
    directory, filename = os.path.split(filepath)
    base_name, ext = os.path.splitext(filename)

    # Loop until we find a unique filename
    while True:
        # Generate a random 6-digit code
        random_code = random.randint(100000, 999999)
        new_filename = f"{category}{random_code}{ext}"
        new_filepath = os.path.join(directory, new_filename)
        
        # Check if the new file exists
        if not os.path.exists(new_filepath):
            os.rename(filepath, new_filepath)
            print(f"File renamed to '{new_filepath}'")
            return

#V2
def solve_icon_captcha_v2(sb1):
    try:
        #pyautogui.scroll(1000,1808 ,-1500 )
        # Extract all captcha icons
        script = """
        // Define XPath expression to find elements inside the form with the specified class patterns or text
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

        return filteredElements.map(el => el.id ? `#${el.id}.${el.className}` : `.${el.className}`);
        """

        # Execute JavaScript and get the filtered elements
        filtered_elements = sb1.execute_script(script)

        # Print each element
        print("Filtered elements:")
        # Assign the first element to captchaElement
        if filtered_elements:
            captchaElement = filtered_elements[0]
            print("\nCaptcha Element:", captchaElement)

        if len(filtered_elements) < 4:
            # Define the base64 image lists
            base64_images = [
                "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAAXCAIAAAAuvD5IAAAACXB",
            ]
            base64_images2 = [
                "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUgAAAAXCAIAAADm2UHyAAAACXB",
                "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAV0AAAAXCAIAAAAnXgteAAAACXBI",
            ]

            # Check if any image on the page matches a base64 image from the list
            image_exists = any(
                img.get_attribute("src").startswith(base64_prefix) 
                for img in sb1.find_elements("form img") 
                for base64_prefix in base64_images
            )

            image_exists2 = any(
                img.get_attribute("src").startswith(base64_prefix) 
                for img in sb1.find_elements("form img") 
                for base64_prefix in base64_images2
            )

            # Print the results
            print("Verified: ", image_exists)
            print("Opps Error: ", image_exists2)

            if image_exists:
                print("Verified found in the first list.")
                #button = sb1.find_element(By.CSS_SELECTOR, 'button#ClaimBtn')
                #capture_element_screenshot(sb1, 'button#ClaimBtn', screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png")
                #mouse_moveclick(cropped_path="element_screenshot.png")
                #button.uc_click()
                return
            elif image_exists2:
                print("Opps Error found in the first list.")
                #button = sb1.find_element(By.CSS_SELECTOR, 'button#ClaimBtn')
                #capture_element_screenshot(sb1, 'button#ClaimBtn', screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png")
                #mouse_moveclick(cropped_path="element_screenshot.png")
                #button.uc_click()
                pyautogui.press('f5')
                return
        # Remove first two and specific element
        to_remove = [
            filtered_elements[0],  # First element
            filtered_elements[1],  # Second element
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none"
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none me-6"  # Specific element
        ]

        filtered_elements = [el for el in filtered_elements if el not in to_remove]

        # Print the final list after removal
        print("\nFiltered elements after removal:", filtered_elements)
        # Execute JavaScript in Selenium and get the results
                
        #captcha_word = captchaElement #'nfvabpjo9wvn#xrikqozisnn.zCpvNsbks bi bi-arrow-down'
        answers = filtered_elements
        #remove unnecessary 
        captcha_image = "element_screenshot.png"  # Replace with your captcha
        template_folder = "icons"  # Folder with stored icons
        capture_element_screenshot(sb1, captchaElement, screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png")
        captcha_word = solve_captcha(captcha_image, template_folder)
        rename_with_code("element_screenshot.png", captcha_word)
        cleaned_text = re.sub(r'\d', '', captcha_word)

        #filter everything
        #captcha_word = filter_string(captcha_word)
        #captcha_word = clean_string(captcha_word)
        captcha_word = filter_and_replace(captcha_word)
        #if '.' == captcha_word:
        #    captcha_word = filtered_elements
        #    captcha_word = filter_and_replace(captcha_word)
        #answers = [filter_and_replace(answer) for answer in answers]
        #answers = [filter_string(answer) for answer in answers]
        #answers = [filter_and_replace(answer) for answer in answers]

        #captcha_word = clean_string(captcha_word)
        #answers = [clean_string(answer) for answer in answers]
        #check if the word is in the list
        print(captcha_word, "gfg")
        print(answers)

        filterd_answrs = []
        for answer in answers:
            print(answer)
            copy_answer = answer
            copy_answer = clean_string2(copy_answer)
            copy_answer = filter_and_replace(copy_answer)
            #copy_answer = filter_string(copy_answer)
            #copy_answer = filter_and_replace(copy_answer)
            copy_answer = clean_string(copy_answer)
            print(copy_answer)
            filterd_answrs.append(copy_answer)
            if '' == captcha_word:
                print("ng it")
                continue
            if captcha_word in copy_answer or copy_answer in captcha_word:
                print(answer, "Found it")
                answer = answer.replace(' ', '.')
                print('uc click before')
                button = sb1.find_element(By.CSS_SELECTOR, answer)
                #button.uc_click()
                capture_element_screenshot(sb1, answer, screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png")
                mouse_moveclick(cropped_path="element_screenshot.png")

                return True
        print("No matching icon found.")
        #append_to_notepad("notepad.txt", captchaElement, filtered_elements)
        append_to_notepad("notepad.txt", captcha_word, filterd_answrs)

        return False
    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False
        pyautogui.press('f5')
        time.sleep(7)

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


import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import torch.nn.functional as F

def load_image(image_path, image_size=(60, 60)):
    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.ToTensor(),
    ])
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)  # Add batch dimension
    return image

def extract_features(image_tensor, model):
    with torch.no_grad():
        features = model(image_tensor)
    return features
#import timm
def compute_similarity(img_path1, img_path2):
    # Load model
    model = models.efficientnet_v2_s(pretrained=True)#timm.create_model('convnext_large', pretrained=True) #models.resnet101(pretrained=True) #models.efficientnet_b3(pretrained=True) #models.resnet101(pretrained=True)
    model.fc = torch.nn.Identity()  # remove final classification layer
    model.eval()

    # Load images
    img1 = load_image(img_path1)
    img2 = load_image(img_path2)

    # Extract features
    feat1 = extract_features(img1, model)
    feat2 = extract_features(img2, model)

    # Cosine similarity
    similarity = F.cosine_similarity(feat1, feat2).item()

    return similarity


def get_image_list(folder_path):
    img_list = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_list.append(os.path.join(folder_path, filename))
    return img_list

def fill_background_black(pil_img):
    """Fill transparent background with black color."""
    bg = Image.new("RGBA", pil_img.size, (0, 0, 0, 255))
    bg.paste(pil_img, (0, 0), mask=pil_img)
    return bg


def remove_image_border(cv2_img, border_px):
    """Remove a uniform border from all sides of the image."""
    if cv2_img is None:
        raise FileNotFoundError("Image is None")

    h, w = cv2_img.shape[:2]

    if border_px * 2 >= h or border_px * 2 >= w:
        raise ValueError("Border size too large for image dimensions.")

    return cv2_img[border_px:h-border_px, border_px:w-border_px]


def fix_rotation(cv2_img):
    """Fix slight rotation issues by detecting white edges."""
    if cv2_img is None:
        raise FileNotFoundError("Image is None")

    if len(cv2_img.shape) == 2:
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_GRAY2BGRA)
    elif cv2_img.shape[2] == 3:
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2BGRA)
    elif cv2_img.shape[2] != 4:
        raise ValueError(f"Unsupported image format: {cv2_img.shape}")

    h, w, _ = cv2_img.shape

    def is_white(px):
        b, g, r, a = px
        return (r > 0 or g > 0 or b > 0) and a > 0

    points = []

    # Check top, right, bottom, left edges
    for x in range(w):
        if is_white(cv2_img[0, x]):
            points.append((x, 0))
            break
    for y in range(h):
        if is_white(cv2_img[y, w-1]):
            points.append((w-1, y))
            break
    for x in range(w):
        if is_white(cv2_img[h-1, x]):
            points.append((x, h-1))
            break
    for y in range(h):
        if is_white(cv2_img[y, 0]):
            points.append((0, y))
            break

    if len(points) != 4:
        print("Warning: Not all 4 edges detected.")
        return 4  # Special signal

    pts = np.array(points, dtype="float32")
    pts_sorted_y = pts[np.argsort(pts[:, 1])]
    top_pts = pts_sorted_y[:2]
    bottom_pts = pts_sorted_y[2:]
    top_left, top_right = top_pts[np.argsort(top_pts[:, 0])]
    bottom_left, bottom_right = bottom_pts[np.argsort(bottom_pts[:, 0])]

    ordered_pts = np.array([top_left, top_right, bottom_right, bottom_left], dtype="float32")

    dst_size = 50
    dst_pts = np.array([
        [0, 0],
        [dst_size - 1, 0],
        [dst_size - 1, dst_size - 1],
        [0, dst_size - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(ordered_pts, dst_pts)
    warped = cv2.warpPerspective(cv2_img, M, (dst_size, dst_size), flags=cv2.INTER_LINEAR)

    return warped


def denoise_image(cv2_img):
    """Denoise the image and convert to binary."""
    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def denoise_image3(image):
    try:
        if isinstance(image, str):
            filename = image
            image = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        else:
            filename = None
        img = image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        cleaned = cv2.bitwise_not(thresh)
        if filename:
            cv2.imwrite(filename, cleaned)
        return cleaned
    except Exception as e:
        print(f"Error in denoising image: {e}")
        return None

def add_black_border(image_path, output_path, border_size=5):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    bordered = cv2.copyMakeBorder(
        img,
        top=border_size,
        bottom=border_size,
        left=border_size,
        right=border_size,
        borderType=cv2.BORDER_CONSTANT,
        value=[0, 0, 0]  # black color
    )
    cv2.imwrite(output_path, bordered)

def captcha_image_filter(captcha_image_path, answer_image_path):
    """Process captcha image."""
    try:
        captcha_orig = cv2.imread(captcha_image_path, cv2.IMREAD_UNCHANGED)

        if captcha_orig is None:
            raise FileNotFoundError(f"Captcha image not found: {captcha_image_path}")

        # Fill transparent areas with black
        captcha_pil = Image.fromarray(cv2.cvtColor(captcha_orig, cv2.COLOR_BGRA2RGBA))
        captcha_filled = fill_background_black(captcha_pil)

        # Convert back to OpenCV
        captcha_cv = cv2.cvtColor(np.array(captcha_filled), cv2.COLOR_RGBA2BGRA)

        # Fix rotation
        fixed = fix_rotation(captcha_cv)

        border_size = 1
        while isinstance(fixed, int) and fixed == 4 and border_size <= 3:
            captcha_cv = remove_image_border(captcha_cv, border_size)
            fixed = fix_rotation(captcha_cv)
            border_size += 1

        if isinstance(fixed, int) and fixed == 4:
            print("Error: Unable to fix rotation of captcha image.")
            return

        # Denoise
        denoised = denoise_image(fixed)

        # Final cut (remove some extra edges)
        final_captcha = remove_image_border(denoised, 2)

        # Save final image
        cv2.imwrite("processed_captcha.png", final_captcha)
        print(f"Captcha image processed and saved to processed_captcha.png")

        # Filtering Answer Images
        # Get the list of images in the folder
        img_list = get_image_list(answer_image_path)
        print(f"Answer images found: {img_list}")

        # Loop through each image and process it
        for img in img_list:
            denoise_image3(img)
            add_black_border(img, img, border_size=5)
            print(f"Filtering {img} with processed captcha")
        
        print("All answer images processed.")
        best_match = None
        highest_similarity = 0.0
        similarity_list = []

        for img in img_list:
            similarity = compute_similarity("processed_captcha.png", img)
            print(f"Similarity: {similarity:.4f} Comparing {img}")
            similarity_list.append((img, similarity))  # Store img with its score

            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = img

        print(f"\nBest match: {best_match} with similarity {highest_similarity:.4f}")
        return best_match


    except Exception as e:
        print(f"Error processing captcha image: {e}")
        return

def filename_to_css_property(filename):
    # Remove the prefix and suffix
    name = filename.replace("cropped_icons/captchaimg.", "").replace(".png", "")
    # Remove any leading/trailing spaces just in case
    name = name.strip()
    # Replace spaces with dots
    css_property = "." + name.replace(" ", ".")
    return css_property
#V3
#Steps to solve the captcha:
#1. Get the captcha 
def solve_icon_captcha(sb1):
    try:
        print("solve_icon_captcha_v3")
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
        print("Filtered elements:")
        # Assign the first element to captchaElement
        if filtered_elements:
            captchaElement = filtered_elements[0]
            print("\nCaptcha Element:", captchaElement)
            save_base64_image(captchaElement, 'captchaElement.png')

        if len(filtered_elements) < 4:
            return False
        to_remove = [
            filtered_elements[0],  # First element
            filtered_elements[1],  # Second element
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none"
            "#loginBtnSpinner.fas fa-circle-notch fa-spin d-none me-6"  # Specific element
        ]

        filtered_elements = [el for el in filtered_elements if el not in to_remove]

        # Print the final list after removal
        print("\nFiltered elements after removal:", filtered_elements)
        for item in filtered_elements:
            capture_element_screenshot(sb1, item, screenshot_path="full_screenshot.png", cropped_path=f"cropped_icons/captchaimg{item}.png")

        best_match = captcha_image_filter("captchaElement.png", "cropped_icons")
        best_match = filename_to_css_property(best_match)
        print("Best match:", best_match)
        sb1.uc_click(best_match)
        return True

    except Exception as e:
        print(f"Error solving captcha: {e}")
        return False


def get_active_window_title():
    try:
        # Get the window ID of the active window
        window_id = subprocess.check_output(["xdotool", "getactivewindow"], text=True).strip()
        
        # Get the window title using the window ID
        window_title = subprocess.check_output(["xdotool", "getwindowname", window_id], text=True).strip()
        
        return window_title
    except subprocess.CalledProcessError:
        return None  # Return None if there's an error (e.g., no active window)

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
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                                    print("verify_cloudflare git Found Just")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.7)
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
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                    print("verify_cloudflare git Found")
                    if x and y:
                        sb.disconnect() 
                        for i in range(1, 300):
                            page_title = get_active_window_title()
    
                            if 'Login' in page_title or 'Faucetpay' in page_title:
                                try:
                                    time.sleep(1)
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.7)
                                    print("verify_cloudflare git Found")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.7)
                                        pyautogui.click(x, y)
                                        time.sleep(5)
    
                                    except Exception as e:
                                        print(e)
    
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_success.png", confidence=0.7)
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
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_dark.png", confidence=0.7)
                                    print("verify_cloudflare git Found Just")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box_dark.png", confidence=0.7)
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
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_dark.png", confidence=0.7)
                    print("verify_cloudflare git Found")
                    if x and y:
                        sb.disconnect() 
                        for i in range(1, 300):
                            #pyautogui.moveTo(100, 200)
    
                            if 'Login' in page_title or 'Faucet' in page_title or 'Earnbitmoon' in page_title:
                                try:
                                    time.sleep(1)
                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_dark.png", confidence=0.7)
                                    print("verify_cloudflare git Found")
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box_dark.png", confidence=0.7)
                                        pyautogui.click(x, y)
                                        time.sleep(5)
    
                                    except Exception as e:
                                        print(e)
    
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_success_dark.png", confidence=0.7)
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
                        #solve_least_img(sb1)
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
                    all_windows = driver.window_handles
                    for window in all_windows:
                        if window not in restrict_pages:
                            driver.switch_to.window(window)
                    try:
                        x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{captcha_image}.png", confidence=0.85)
                        if x and y: 

                            #login_button = driver.find_element(By.CSS_SELECTOR, submit_button)
                            #click_element_with_pyautogui(driver, login_button)
                            #click_element_with_pyautogui(sb1, 'button[type="submit"]')
                            if 'Feyorra' in current_title:
                                pyautogui.click(939 ,760)
                                time.sleep(1)
                                pyautogui.click(943 ,788)
                                #x:943 y:788
                                time.sleep(5)
     
                            if 'ClaimCoin' in current_title:
                                pyautogui.click(973, 833)
                                time.sleep(5)
                                #return
                            if driver.is_element_visible(submit_button):
                                sb1.uc_click(submit_button)
                            pyautogui.click(939 ,760)
                            #pyautogui.click(939 ,760)

                            
                            
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


        if not_expected_title in current_title:
            if function == 1:
                login_to_faucet('https://earn-pepe.com/login', sb1, earnpp_email, earnpp_pass, 'cloudflare_success', window_list, 'button#ClaimBtn')
                #login_to_faucet('https://earn-pepe.com/login', sb1, earnpp_email, earnpp_pass, 'rscaptcha', window_list, 'button#loginBtn')
            elif function == 2:
                login_to_faucet('https://feyorra.site/login', sb1, feyorra_email, feyorra_pass, 'cloudflare_success', window_list, 'button#ClaimBtn')
            elif function == 3:
                login_to_faucet('https://earn-trump.com/login', sb1, earnpp_email, earnpp_pass,  'cloudflare_success', window_list, 'button#ClaimBtn') #'not_a_robot'
            elif function == 4:
                login_to_faucet('https://earn-bonk.com/login', sb1, feyorra_email, feyorra_pass,  'cloudflare_success', window_list, 'button#ClaimBtn')  #'not_a_robot'


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
            if driver.is_element_present('li a span span'):
                select_element = driver.find_element('css selector', 'li a span span')
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

 
def withdraw_faucet(driver, sitekey):

    try:
        #        quer2y = {"type": "main"}
        #        dochh2 = collection.find_one(quer2y)
        #        faucetlayout = dochh2["mainfaucet"]
        #        print(f'Farm ID:{farm_id} | Faucet Layout: {faucetlayout}')
        collectionbip = db[f'LocalCSB']
        quer2y = {"type": "main"}
        dochh = collectionbip.find_one(quer2y)
        currency = dochh["currency"]
        pep_x = 602
        pep_y =  778

        fey_x =  679 
        fey_y =  414

        if faucetlayout == 1:
            if 'LTC' in currency:
                pep_x = 966 
                pep_y =  615

                fey_x =  982
                fey_y =  602
            elif 'SOL' in currency:
                pep_x = 602
                pep_y =  778

                fey_x =  679 
                fey_y =  414
            elif 'TRX' in currency:
                pep_x = 1329 
                pep_y =  452

                fey_x =  679
                fey_y =  602
        else:
            if 'LTC' in currency:
                pep_x = 1388 
                pep_y =  284

                fey_x =  884
                fey_y =  648
            elif 'SOL' in currency:
                pep_x = 1388
                pep_y =  284

                fey_x =  375 
                fey_y =  647
            elif 'TRX' in currency:
                pep_x = 334 
                pep_y =  457

                fey_x =  375
                fey_y =  466

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
            if faucetlayout == 1:
                driver.uc_open('https://earn-pepe.com/member/faucetpay')
            else:
                driver.uc_open('https://earn-trump.com/member/faucetpay')
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, 300);")
            time.sleep(1)
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
                    if faucetlayout == 1:
                        driver.execute_script(f"window.scrollTo(0, 1000);")
                    time.sleep(2)
                    cloudflare(sb1, login = True)
                    time.sleep(2)
                    driver.uc_click('button#ClaimBtn')
                    time.sleep(5)
                    response_messege(f'EarnPP FaucetPay Withdrawed{currency}')
                    #response_messege('Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'withdrawfeyorra'}}
                    result = collection.update_one(query, update)
                    return

                else:
                    print(title, 'restarting')
                    driver.uc_open('https://earn-pepe.com/member/faucetpay')
                    time.sleep(10)

    
        
        if sitekey == 2:
            print('Strting Feyorra withdraw')
            
            if faucetlayout == 1:
                driver.uc_open('https://feyorra.site/member/faucetpay')
            else:
                driver.uc_open('https://earn-bonk.com/member/faucetpay')
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, 300);")
            time.sleep(1)
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
                    cloudflare(sb1, login = True)
                    time.sleep(2)
                    driver.uc_click('button#ClaimBtn')
                    time.sleep(5)
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
                    #solve_least_img(driver)
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
    #sb1.execute_script("window.scrollTo(0, 300);")
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
    
    #time.sleep(99999)
    return sb1

faucetlayout = None
def open_faucets():
    global sb1
    while True:
        try:
            global faucetlayout
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

                quer2y = {"type": "main"}
                dochh2 = collection.find_one(quer2y)
                faucetlayout = dochh2["mainfaucet"]
                print(f'Farm ID:{farm_id} | Faucet Layout: {faucetlayout}')
                update_ip(ip_address, config_path="mfhelper/config.json")
                ip_address = get_ip(sb1)
                if ip_required == ip_address:
                    response_messege('EarnPP Loging')
                    if earnpp:
                        if faucetlayout == 1:
                            earnpp_window = handle_site(sb1, "https://earn-pepe.com/member/faucet","Faucet | Earn-pepe" , "Home | Earn-pepe", 1, [], ip_required)
                            if earnpp_window == 404:
                                raise Exception(" earnpp_window == 404")
                            print(f"EarnPP window handle: {earnpp_window}")
                        else:
                            earnpp_window = handle_site(sb1, "https://earn-trump.com/member/faucet","Faucet | Earn-Trump" , "Free $Trump Coin Faucet | Earn $Trump Crypto Instantly", 3, [], ip_required)
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
                        #sb1.open_new_window()
                        if faucetlayout == 1:
                            feyorra_window = handle_site(sb1, "https://feyorra.site/member/faucet", "Faucet | Feyorra" , "Home | Feyorra", 2, [], ip_required)
                            if feyorra_window == 404:
                                raise Exception(" feyorra_window == 404")
                            print(f"Feyorra window handle: {feyorra_window}")

                        else:
                            feyorra_window = handle_site(sb1, "https://earn-bonk.com/member/faucet", "Faucet | Earn-Bonk" , "Next-Gen BONK Crypto Faucet", 4, [], ip_required)
                            if feyorra_window == 404:
                                raise Exception(" feyorra_window == 404")
                            print(f"Feyorra window handle: {feyorra_window}")

                    else:
                        feyorra_window = None
                else:
                    raise Exception("Ip changed")
                if ip_required == ip_address:
                    response_messege('EarnPP Loging')
                    if earnpp:
                        if faucetlayout == 1:
                            earnpp_window = handle_site(sb1, "https://earn-pepe.com/member/faucet","Faucet | Earn-pepe" , "Home | Earn-pepe", 1, [], ip_required)
                            if earnpp_window == 404:
                                raise Exception(" earnpp_window == 404")
                            print(f"EarnPP window handle: {earnpp_window}")
                        else:
                            earnpp_window = handle_site(sb1, "https://earn-trump.com/member/faucet","Faucet | Earn-Trump" , "Free $Trump Coin Faucet | Earn $Trump Crypto Instantly", 3, [], ip_required)
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
                        if faucetlayout == 1:
                            feyorra_window = handle_site(sb1, "https://feyorra.site/member/faucet", "Faucet | Feyorra" , "Home | Feyorra", 2, [earnpp_window], ip_required)
                            if feyorra_window == 404:
                                raise Exception(" feyorra_window == 404")
                            print(f"Feyorra window handle: {feyorra_window}")

                        else:
                            feyorra_window = handle_site(sb1, "https://earn-bonk.com/member/faucet", "Faucet | Earn-Bonk" , "Next-Gen BONK Crypto Faucet", 4, [earnpp_window], ip_required)
                            if feyorra_window == 404:
                                raise Exception(" feyorra_window == 404")
                            print(f"Feyorra window handle: {feyorra_window}")

                    else:
                        feyorra_window = None
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

            #ip_address = get_ip(sb1) 
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
                        if 'Faucet | Earn-pepe' in title or 'Faucet | Earn-Trump' in title:
                            debug_messages(f'Solving Icon Captcha on EarnPP')
                            val = get_coins(sb1, 1)
                            if val:
                                earnpp_coins = val
                            gg = solve_icon_captcha(sb1)
                            if gg:
                                earnpp_limit_reached = None
                            else:
                                if sb1.is_text_visible('Timeout, Please refresh the page!'):
                                    sb1.uc_click('button#ClaimBtn')
                                if sb1.is_text_visible('Oops, wrong selection! Please refresh the page.'):
                                    sb1.uc_click('button#ClaimBtn')
                                #if sb1.is_text_visible('Verified!'):
                                #    sb1.uc_click('button#ClaimBtn')
                                if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!'):
                                    debug_messages(f'EarnPP Limit Reached')
                                    response_messege('EarnPP Limit Reached')
                                    earnpp_limit_reached = True
                                else:
                                    refresh_count +=5
                            debug_messages(f'Solved Icon Captcha on EarnPP')


                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on EarnPP')
                            response_messege('Lock.. Found on EarnPP')
                            earnpp_coins = 0
                        elif 'Google' in title:
                            reset_count +=5
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
                        else:
                            debug_messages(f'EarnPP not Found:{title} | reset:{reset_count}')
                            reset_count +=1

                    except Exception as e:
                        if mainscript == 1:
                            if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!'):
                                debug_messages(f'EarnPP Limit Reached')
                                response_messege('EarnPP Limit Reached')
                                earnpp_limit_reached = True
                            else:
                                debug_messages(f'ERR on EarnPP:{e}')
                                reset_count +=1
                        else:
                            if sb1.is_text_visible('Limit Reached, Claim Shortlinks to increase the claim limit..'):
                                debug_messages(f'EarnPP Limit Reached')
                                response_messege('EarnPP Limit Reached')
                                earnpp_limit_reached = True
                            else:
                                debug_messages(f'ERR on EarnPP:{e}')
                                reset_count +=1
                
                if feyorra:
                    try:
                        debug_messages(f'Switching Pages to Feyorra')
                        sb1.switch_to.window(feyorra_window)
                        debug_messages(f'Getting Pages Titile:Feyorra')
                        pyautogui.press('enter')
                        title =sb1.get_title()

                        if 'Faucet | Feyorra' in title or 'Faucet | Earn-Bonk' in title:
                            debug_messages(f'Solving Icon Captcha on Feyorra')

                            val = get_coins(sb1, 2)
                            if val:
                                feyorra_coins = val
                            gg = solve_icon_captcha(sb1)
                            if gg:
                                feyorra_limit_reached =None
                            else:
                                if sb1.is_text_visible('Timeout, Please refresh the page!'):
                                    sb1.uc_click('button#ClaimBtn')
                                if sb1.is_text_visible('Oops, wrong selection! Please refresh the page.'):
                                    sb1.uc_click('button#ClaimBtn')
                                #if sb1.is_text_visible('Verified!'):
                                #    sb1.uc_click('button#ClaimBtn')
                                if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!'):
                                    debug_messages(f'Feyorra Limit Reached')
                                    response_messege('Feyorra Limit Reached')
                                    feyorra_limit_reached =True
                                else:
                                    refresh_count +=5

                                
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on Feyorra')
                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed Feyorra')
                        elif 'Google' in title:
                            reset_count +=5
                        elif 'aintenance' in title:
                            debug_messages(f'maintenance.. Found on Feyorra')
                            response_messege('maintenance.. Found on Feyorra')
                            feyorra_coins = 0

                        elif 'Lock' in title:
                            debug_messages(f'Lock.. Found on Feyorra')
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
                        if mainscript == 1:
                            if sb1.is_text_visible('Limit Reached, Comeback Again Tomorrow!'):
                                debug_messages(f'Feyorra Limit Reached')
                                response_messege('Feyorra Limit Reached')
                                feyorra_limit_reached =True
                            else:
                                debug_messages(f'ERR on Feyorra:{e}')
                                reset_count +=1
                        else:

                            if sb1.is_text_visible('Limit Reached, Claim Shortlinks to increase the claim limit..'):
                                debug_messages(f'Feyorra Limit Reached')
                                response_messege('Feyorra Limit Reached')
                                feyorra_limit_reached =True
                            else:
                                debug_messages(f'ERR on Feyorra:{e}')
                                reset_count +=1

###################################################################################################################



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
                            if faucetlayout == 1:
                                sb1.uc_open('https://earn-pepe.com/member/faucet')
                            else:
                                sb1.uc_open('https://earn-trump.com/member/faucet')
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
                            #sb1.uc_open('https://feyorra.site/member/faucet')
                            if faucetlayout == 1:
                                sb1.uc_open('https://feyorra.site/member/faucet')
                            else:
                                sb1.uc_open('https://earn-bonk.com/member/faucet')
                                
                        if feyorra_limit_reached:
                            pass
                        else:
                            if refresh_count >= 50:
                                reset_count +=5
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
                reset_count +=4
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
            for i in range(1,6):
                time.sleep(1)
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
     
