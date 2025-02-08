
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
import Levenshtein
import json
import argparse
import clipboard
import shutil
import os
import math
import subprocess
 
 
# Example usage
 
 
 
mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"
 
client = MongoClient(mongo_uri)
db = client['MoneyFarmV6'] 
def add_messages(farm,ip):
    try:
        sri_lanka_tz = pytz.timezone('Asia/Colombo')
        utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
        sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
        now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
 
        query = {"type": 'ip_history'}
        collectionbip = db[f'LocalCSB']
        existing_doc = collectionbip.find_one(query)
        print("Existing document before update")
        new_message =  {now: f"{farm} | {ip}"} # {'2024-09-06 03:47:14': 220}  # Use a new timestamp
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
 
satoshifaucet_email = 'Nooo'
satoshifaucet_pass = 'Nooo'
feyorra_email = 'Nooo'
feyorra_pass = 'Nooo'
claimc_email = 'yvonne12463@gmail.com'
claimc_pass = 'Uwuinsta@2005'
 
collection = db[f'Farm{farm_id}']
 
collectionbip = db[f'LocalCSB']
quer2y = {"type": "main"}
dochh = collectionbip.find_one(quer2y)
blacklistedIP = dochh["blacklistedIP"]
print(blacklistedIP)
 
 
server_name1 = ''
CSB1_farms  = ''
satoshifaucet_email = ''
satoshifaucet_pass = ''
feyorra_email = ''
feyorra_pass = ''
layout = ''
 
 
def get_mails_passowrds(farm_id):
    global server_name1
    global CSB1_farms
    global satoshifaucet_email
    global satoshifaucet_pass
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
            satoshifaucet_email = 'khabibmakanzie2@gmail.com'
            satoshifaucet_pass = 'khabibmakanzie2'
            feyorra_email = 'khabibmakanzie2@gmail.com'
            feyorra_pass = 'khabibmakanzie2'
 
        elif '2' in layout:
            server_name1 = 'thailand' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'amytanisha250@gmail.com'
            satoshifaucet_pass = 'amytanisha250'
            feyorra_email = 'amytanisha250@gmail.com'
            feyorra_pass = 'amytanisha250'
        elif '3' in layout:
            server_name1 = 'bulgaria' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'grandkolla999br@gmail.com'
            satoshifaucet_pass = 'grandkolla999br'
            feyorra_email = 'grandkolla999br@gmail.com'
            feyorra_pass = 'grandkolla999br'
 
        elif '4' in layout:
            server_name1 = 'thailand' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'makanziekb@gmail.com'
            satoshifaucet_pass = 'makanziekb'
            feyorra_email = 'makanziekb@gmail.com'
            feyorra_pass = 'makanziekb'
        else:
            print('Layout issue', layout)
 
    elif farm_id == 2:
 
        if '1' in layout:
            server_name1 = 'estonia'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'metroboom910@gmail.com'
            satoshifaucet_pass = 'metroboom910'
            feyorra_email = 'metroboom910@gmail.com'
            feyorra_pass = 'metroboom910'
 
        elif '2' in layout:
            server_name1 = 'finland' #'portugal'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'merlelcn@gmail.com'
            satoshifaucet_pass = 'I2Ne7C329jJt'
            feyorra_email = 'merlelcn@gmail.com'
            feyorra_pass = 'I2Ne7C329jJt'
 
        elif '3' in layout:
            server_name1 = 'finland' #'portugal'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'anrogedyyr@gmail.com'
            satoshifaucet_pass = 'anrogedyyr'
            feyorra_email = 'anrogedyyr@gmail.com'
            feyorra_pass = 'anrogedyyr'
        elif '4' in layout:
            server_name1 = 'estonia'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'bmetoomro190@gmail.com'
            satoshifaucet_pass = 'bmetoomro190'
            feyorra_email = 'bmetoomro190@gmail.com'
            feyorra_pass = 'bmetoomro190'
        else:
            print('Layout issue', layout)
 
 
    elif farm_id == 3:
 
        if '1' in layout:
            server_name1 = 'france'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'yvonne12463@gmail.com'
            satoshifaucet_pass = 'Uwuinsta@2005'
            feyorra_email = 'yvonne12463@gmail.com'
            feyorra_pass = 'Uwuinsta@2005'
 
            claimc_email = 'yvonne12463@gmail.com'
            claimc_pass = 'Uwuinsta@2005'
 
        elif '2' in layout:
            server_name1 = 'spain' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'pennyscrambble@gmail.com'
            satoshifaucet_pass = 'pennyscrambble'
            feyorra_email = 'pennyscrambble@gmail.com'
            feyorra_pass = 'pennyscrambble'
 
        elif '3' in layout:
            server_name1 = 'spain' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'berendkalpana2@gmail.com'
            satoshifaucet_pass = 'berendkalpana2'
            feyorra_email = 'berendkalpana2@gmail.com'
            feyorra_pass = 'berendkalpana2'
        elif '4' in layout:
            server_name1 = 'france'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'voyn3642ovene@gmail.com'
            satoshifaucet_pass = 'voyn3642ovene'
            feyorra_email = 'voyn3642ovene@gmail.com'
            feyorra_pass = 'voyn3642ovene'
 
        else:
            print('Layout issue', layout)
 
 
    elif farm_id == 4:
 
        if '1' in layout:
            server_name1 = 'hungary'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'ddilakshi232@gmail.com'
            satoshifaucet_pass = 'Uwuinsta@2005'
            feyorra_email = 'ddilakshi232@gmail.com'
            feyorra_pass = 'Uwuinsta@2005'
        elif '2' in layout:
            server_name1 = 'hong kong' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'kumarsheln@gmail.com'
            satoshifaucet_pass = 'kumarsheln'
            feyorra_email = 'kumarsheln@gmail.com'
            feyorra_pass = 'kumarsheln'
        elif '3' in layout:
            server_name1 = 'hong kong' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'andrpewrea@gmail.com'
            satoshifaucet_pass = 'andrpewrea'
            feyorra_email = 'andrpewrea@gmail.com'
            feyorra_pass = 'andrpewrea'
        elif '4' in layout:
            server_name1 = 'hungary'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'shiladid323@gmail.com'
            satoshifaucet_pass = 'shiladid323'
            feyorra_email = 'shiladid323@gmail.com'
            feyorra_pass = 'shiladid323'
        else:
            print('Layout issue', layout)
 
 
    elif farm_id == 5:
 
        if '1' in layout:
            server_name1 = 'italy'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'gihanfer907@gmail.com' #gihanfer907@gmail.com
            satoshifaucet_pass = 'gihanfer907'
            feyorra_email = 'gihanfer907@gmail.com'
            feyorra_pass = 'gihanfer907'
 
        elif '2' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'howardrahul838@gmail.com'
            satoshifaucet_pass = 'howardrahul838'
            feyorra_email = 'howardrahul838@gmail.com'
            feyorra_pass = 'howardrahul838'
        elif '3' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            satoshifaucet_email = 'redgta362@gmail.com'
            satoshifaucet_pass = 'redgta362'
            feyorra_email = 'redgta362@gmail.com'
            feyorra_pass = 'redgta362'
        elif '4' in layout:
            server_name1 = 'italy'
            CSB1_farms = [1, 2, 3, 4, 5]
            satoshifaucet_email = 'ferhng790@gmail.com'
            satoshifaucet_pass = 'ferhng790'
            feyorra_email = 'ferhng790@gmail.com'
            feyorra_pass = 'ferhng790'
        else:
            print('Layout issue', layout)
 
##################################################
    elif farm_id == 6:
 
        if '1' in layout:
            server_name1 = 'indonesia'
            CSB1_farms = [6,7,8,9,10]
            satoshifaucet_email = 'sevensevengk@gmail.com'
            satoshifaucet_pass = 'sevensevengk'
            feyorra_email = 'sevensevengk@gmail.com'
            feyorra_pass = 'sevensevengk'
 
 
        elif '2' in layout:
            server_name1 = 'indonesia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'gksevn77@gmail.com'
            satoshifaucet_pass = 'gksevn77'
            feyorra_email = 'gksevn77@gmail.com'
            feyorra_pass = 'gksevn77'
 
        elif '3' in layout:
            server_name1 = 'south korea' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'kg7seven@gmail.com'
            satoshifaucet_pass = 'kg7seven'
            feyorra_email = 'kg7seven@gmail.com'
            feyorra_pass = 'kg7seven'
        elif '4' in layout:
            server_name1 = 'south korea'
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'fosengklla@gmail.com'
            satoshifaucet_pass = 'fosengklla'
            feyorra_email = 'fosengklla@gmail.com'
            feyorra_pass = 'fosengklla'
 
 
    elif farm_id == 7:
 
        if '1' in layout:
            server_name1 = 'belgium'
            CSB1_farms = [6,7,8,9,10]
            satoshifaucet_email = 'shevgraaa@gmail.com'
            satoshifaucet_pass = 'shevgraaa'
            feyorra_email = 'shevgraaa@gmail.com'
            feyorra_pass = 'shevgraaa'
 
        elif '2' in layout:
            server_name1 = 'belgium' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'grshevvvv@gmail.com'
            satoshifaucet_pass = 'grshevvvv'
            feyorra_email = 'grshevvvv@gmail.com'
            feyorra_pass = 'grshevvvv'
 
 
        elif '3' in layout:
            server_name1 = 'denmark' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'grevonshld@gmail.com'
            satoshifaucet_pass = 'grevonshld'
            feyorra_email = 'grevonshld@gmail.com'
            feyorra_pass = 'grevonshld'
        elif '4' in layout:
            server_name1 = 'denmark'
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'sheforldnmk@gmail.com'
            satoshifaucet_pass = 'sheforldnmk'
            feyorra_email = 'sheforldnmk@gmail.com'
            feyorra_pass = 'sheforldnmk'
 
 
    elif farm_id == 8:
 
        if '1' in layout:
            server_name1 = 'croatia'
            CSB1_farms = [6,7,8,9,10]
            satoshifaucet_email = 'ahenrxaaa@gmail.com'
            satoshifaucet_pass = 'ahenrxaaa'
            feyorra_email = 'ahenrxaaa@gmail.com'
            feyorra_pass = 'ahenrxaaa'
 
        elif '2' in layout:
            server_name1 = 'croatia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'rxshenaxa@gmail.com'
            satoshifaucet_pass = 'rxshenaxa'
            feyorra_email = 'rxshenaxa@gmail.com'
            feyorra_pass = 'rxshenaxa'
 
 
        elif '3' in layout:
            server_name1 = 'saudi arabia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'rhexnargg@gmail.com'
            satoshifaucet_pass = 'rhexnargg'
            feyorra_email = 'rhexnargg@gmail.com'
            feyorra_pass = 'rhexnargg'
 
        elif '4' in layout:
            server_name1 = 'saudi arabia'
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'senarxbiag@gmail.com'
            satoshifaucet_pass = 'senarxbiag'
            feyorra_email = 'senarxbiag@gmail.com'
            feyorra_pass = 'senarxbiag'
 
    elif farm_id == 9:
 
        if '1' in layout:
            server_name1 = 'canada'
            CSB1_farms = [6,7,8,9,10]
            satoshifaucet_email = 'semiprraaa@gmail.com'
            satoshifaucet_pass = 'semiprraaa'
            feyorra_email = 'semiprraaa@gmail.com'
            feyorra_pass = 'semiprraaa'
 
        elif '2' in layout:
            server_name1 = 'canada' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'pereramishee@gmail.com'
            satoshifaucet_pass = 'pereramishee'
            feyorra_email = 'pereramishee@gmail.com'
            feyorra_pass = 'pereramishee'
 
 
 
        elif '3' in layout:
            server_name1 = 'sweden' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'ramishepera@gmail.com'
            satoshifaucet_pass = 'ramishepera'
            feyorra_email = 'ramishepera@gmail.com'
            feyorra_pass = 'ramishepera'
        elif '4' in layout:
            server_name1 = 'sweden'
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'pesheswendemi@gmail.com'
            satoshifaucet_pass = 'pesheswendemi'
            feyorra_email = 'pesheswendemi@gmail.com'
            feyorra_pass = 'pesheswendemi'
 
 
    elif farm_id == 10:
 
        if '1' in layout:
            server_name1 = 'austria'
            CSB1_farms = [6,7,8,9,10]
            satoshifaucet_email = 'melosandsong@gmail.com'
            satoshifaucet_pass = 'melosandsong'
            feyorra_email = 'melosandsong@gmail.com'
            feyorra_pass = 'melosandsong'
 
        elif '2' in layout:
            server_name1 = 'austria' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'sadrameloonsan@gmail.com'
            satoshifaucet_pass = 'sadrameloonsan'
            feyorra_email = 'sadrameloonsan@gmail.com'
            feyorra_pass = 'sadrameloonsan'
 
 
        elif '3' in layout:
            server_name1 = 'lithuania' 
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'mlsansonone@gmail.com'
            satoshifaucet_pass = 'mlsansonone'
            feyorra_email = 'mlsansonone@gmail.com'
            feyorra_pass = 'mlsansonone'
        elif '4' in layout:
            server_name1 = 'lithuania'
            CSB1_farms = [6, 7, 8, 9, 10]
            satoshifaucet_email = 'saradmsnire@gmail.com'
            satoshifaucet_pass = 'saradmsnire'
            feyorra_email = 'saradmsnire@gmail.com'
            feyorra_pass = 'saradmsnire'
 
 
 
 
    else:
        while True:
            print('SOmething Wrong Did u use --farm')
    print(server_name1)
    print(CSB1_farms)
    print(satoshifaucet_email)
    print(satoshifaucet_pass)
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
satoshifaucet = True
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

def preprocess_image(image_path):
    """Loads an image, resizes it, and converts it to grayscale."""
    image = cv2.imread(image_path)
    if image is None:
        return None, None
    image = cv2.resize(image, (300, 300))  # Resize for consistency
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray

def generate_transformed_images(gray):
    """Creates all possible transformations of an image: flips, rotations (including 15° steps)."""
    transformations = {"original": gray}

    # 🔹 Flip transformations
    flips = {
        "horizontal_flip": cv2.flip(gray, 1),
        "vertical_flip": cv2.flip(gray, 0),
        "both_axes_flip": cv2.flip(gray, -1),
    }

    # 🔹 Standard 90° rotations
    rotations_90 = {
        "90°": cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE),
        "180°": cv2.rotate(gray, cv2.ROTATE_180),
        "270°": cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE),
    }

    # 🔹 Extra incremental 15° rotations
    center = tuple(np.array(gray.shape[1::-1]) / 2)  # Image center for rotation
    angle_list = list(range(15, 360, 15))  # Generate 15°, 30°, 45° ... 345°
    rotated_extra = {f"{angle}°": cv2.warpAffine(gray, cv2.getRotationMatrix2D(center, angle, 1.0), gray.shape[1::-1], flags=cv2.INTER_LINEAR) for angle in angle_list}

    # 🔹 Combine all transformations
    transformations.update(flips)
    transformations.update(rotations_90)
    transformations.update(rotated_extra)

    return transformations

def compute_similarity(image1, transformations2):
    """Compares an image with multiple rotated/flipped versions of another image and returns best match."""
    best_similarity = 0
    best_transformation = None

    for transform_name, transformed in transformations2.items():
        similarity = ssim(image1, transformed)
        if similarity > best_similarity:
            best_similarity = similarity
            best_transformation = transform_name

    return best_similarity, best_transformation


def group_similar_images(folder_path, similarity_threshold=0.7):
    """Finds groups of similar images in a folder, considering flips and rotations."""
    images = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    image_variants = {}
    most_similar_image = None
    most_similar_image_count = 0
    images_len = len(images)
    single_image = None

    # Preprocess all images
    for img_file in images:
        img_path = os.path.join(folder_path, img_file)
        image, gray = preprocess_image(img_path)
        if image is None:
            continue
        image_variants[img_file] = generate_transformed_images(gray)

    grouped_images = []
    match_results = {}
    used_images = set()

    if len(grouped_images) <= 1:
        #similarity_threshold = 0.6
        while similarity_threshold <= 0.9:
            grouped_images = []
            match_results = {}
            used_images = set()
            while True:
                found_match = False  # Track if any new match is found

                for img1 in images:
                    if img1 in used_images:
                        continue

                    for img2 in images:
                        if img1 == img2 or img2 in used_images:
                            continue

                        similarity, matched_transformation = compute_similarity(image_variants[img1]["original"], image_variants[img2])
                        similarity_threshold2 = 0.65
                        
                        if similarity >= similarity_threshold:
                            # Check if these images are already in a group
                            added_to_group = False
                            for group in grouped_images:
                                if img1 in group or img2 in group:
                                    group.update([img1, img2])
                                    added_to_group = True
                                    break
                            
                            # If not, create a new group
                            if not added_to_group:
                                grouped_images.append(set([img1, img2]))

                            # Save match details
                            match_results[(img1, img2)] = (matched_transformation, similarity)
                            used_images.add(img1)
                            used_images.add(img2)
                            found_match = True
                            if most_similar_image_count < similarity:
                                most_similar_image_count = similarity
                                most_similar_image = img2

                            print(f"{img1} -> {img2}: {matched_transformation} (Similarity: {similarity:.2f})")
                            #plt.imshow(image_variants[img1][matched_transformation], cmap='gray')  # For grayscale images
                            #plt.show()
                if not found_match:
                    break  # If no new matches found, exit loop and finalize groups
            grouped_images_count = len(grouped_images) 
            if grouped_images_count <= 1:
                similarity_threshold += 0.1
                print("Increasing threshold to", similarity_threshold)
            if grouped_images_count > 1:
                print("grouped_images", len(grouped_images))
                similarity_threshold = 1
                all_similar_images =0
                for group in grouped_images:
                    print(group)
                    all_similar_images += len(group)
                    print("all_similar_images", all_similar_images)
                print("All_similar_images", all_similar_images)
                if all_similar_images == (images_len - 1):
                    print('One image is match')
                    grouped_images = [list(group) for group in grouped_images]
                    print("grouped_images", grouped_images)
                    merged_list = sum(grouped_images, [])

                    print("merged_list", merged_list)

                    unmatched_items = list(set(images) - set(merged_list))

                    #unmatched_image = [img for img in images if img not in grouped_images[0]]
                    print("\n=9 **Unmatched Image 1:**", unmatched_items[0])
                    single_image = unmatched_items[0] #unmatched_image[0]

                break


    # Convert sets to lists for final output
    grouped_images = [list(group) for group in grouped_images]

    # Identify least similar images (ones that never got matched)
    least_similar_group = None
    least_similar_group_count = 10


    # Print results
    print("\n🔹 **Similar Image Groups:**")
    for group in grouped_images:
        print(group)
        if len(group) < least_similar_group_count:
            least_similar_group_count = len(group)
            least_similar_group = group
            print("least_similar_group", len(group) , least_similar_group_count)

    least_similar_image = least_similar_group[0] if least_similar_group else "None"


    if single_image:
        least_similar_image =single_image

    # Ensure we handle the case where least similar image group is found
    if least_similar_group:
        print("\n🔹 **Least Similar Image Group:**", least_similar_group)
        print("\n🔹 **Least Similar Image:**", least_similar_image)
    else:
        print("\n🔹 **Least Similar Image Group:** None")
        print("\n🔹 **Least Similar Image:** None")

    return f"output_pieces/{least_similar_image}"


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


def check_similar_images_exist(image_dir, similarity_threshold=0.8):
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
    if check_similar_images_exist("output_pieces", similarity_threshold=0.8):
        val = group_similar_images("output_pieces")
        if val:
            return val
    split_image_by_width('element_screenshot.png', 6, output_dir="output_pieces")
    if check_similar_images_exist("output_pieces", similarity_threshold=0.8):
        val = group_similar_images("output_pieces")
        if val:
            return val
    split_image_by_width('element_screenshot.png', 7, output_dir="output_pieces")
    if check_similar_images_exist("output_pieces", similarity_threshold=0.8):
        val = group_similar_images("output_pieces")
        if val:
            return val
    split_image_by_width('element_screenshot.png', 8, output_dir="output_pieces")
    if check_similar_images_exist("output_pieces", similarity_threshold=0.8):
        val = group_similar_images("output_pieces")
        if val:
            return val
    return val



def solve_rscaptcha(driver):
    # Find the CAPTCHA image
    if driver.is_element_visible("img#rscaptcha_img"):
        driver.execute_script("""
            document.querySelector('img#rscaptcha_img')
            .scrollIntoView({ behavior: 'smooth', block: 'center' });
        """)
        time.sleep(2)
        print("Captcha found")
        capture_element_screenshot(driver, "img#rscaptcha_img", screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png")
        print("Image saved as 'captcha_image.svg'")
        image = solve_least_captcha("element_screenshot.png")
        if image:
            try:
                x, y = pyautogui.locateCenterOnScreen(image, confidence=0.85)
                pyautogui.click(x, y)
                return True
            except Exception as e:
                print(f'ERR in click rscaptcha:{e}')
        else:
            print("No image found")

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
                                    print("verify_cloudflare git Found")
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
                            #pyautogui.moveTo(100, 200)
    
                            if 'Login' in page_title or 'Faucet' in page_title or 'Earnbitmoon' in page_title:
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
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input#email'))
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
                        solve_rscaptcha(sb1)
                        if 'Feyorra' in current_title:
                            pyautogui.click(932 ,728)
                            time.sleep(1)
                            pyautogui.click(943 ,788)
                                    #x:943 y:788
                            time.sleep(5)
                            return
                        if 'ClaimCoin' in current_title:
                            button = sb1.find_element(By.CSS_SELECTOR, submit_button)
                            actions = ActionChains(sb1)
                            actions.move_to_element(button).click().perform()  
                        #pyautogui.click(957 ,886)
                        #time.sleep(5)
                        if driver.is_element_visible(submit_button):
                            sb1.uc_click(submit_button)
                        time.sleep(5)
                        return
                    except Exception as e:
                        print(f'ERR:{e}') 
 
            elif 'recaptcha' in captcha_image:
                sb1.execute_script("window.scrollTo(0, 1000);")
                for i in range(1, 50):
                    time.sleep(2)
                    try:
                        #x,y = pyautogui.locateCenterOnScreen(f"notrobotdone.png", confidence=0.75)
                        x,y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/notrobotdone.png", confidence=0.85)
                        if x and y:
                            pyautogui.click(x, y)
                            break
                    except Exception as e:
                        print(f'Element Not Found Recaptcha :{e}')
 
                button = sb1.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
                actions = ActionChains(sb1)
                actions.move_to_element(button).click().perform()      
 
            else:
                for i in range(1, 10):
                    time.sleep(1)
                    #pyautogui.moveTo(100, 200)
 
                    sb1.execute_script("window.scrollTo(0, 1000);")
                    #cloudflare(driver, True)
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
        time.sleep(3)
        print("🚀 Login attempt made!")
 
 
def satoshifaucet_login(driver,url,email,restrict_pages):
 
    driver.uc_open(url)
    time.sleep(2)
 
    all_windows = driver.window_handles
    for window in all_windows:
        if window not in restrict_pages:
            driver.switch_to.window(window)
 
    print("WebDriver Check")
    current_title = driver.get_title()
    print(f"Current g title: {current_title}")
    if current_title in current_title:
        # Wait for the email input by type attribute
        email_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        email_input.send_keys(email)

        cloudflare(driver, login = True)
        button = sb1.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        actions = ActionChains(sb1)
        actions.move_to_element(button).click().perform()  
        print("✅ CAPTCHA validated")
        time.sleep(3)
        print("🚀 Login attempt made!")
 
 
bitmoon_window = None
satoshifaucet_window = None
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
 
        ip_address = get_ip(sb1)
        if ip_required != ip_address:
            return 404
        #get_mails_passowrds(farm_id)
 
 
        if "SatoshiFaucet | Satoshi faucet" in current_title:

            if function == 1:
                satoshifaucet_login(sb1,'https://satoshifaucet.io/','grandkolla@gmail.com',window_list)
 
 
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
            cloudflare(driver, login = False)
 
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
 
 
reset_count = 0
reset_count_isacc = 0
previous_reset_count = 0
start_time = 0
start_time3 = 0
satoshifaucet_coins = None
feyorra_coins = None
claimc_coins = None
bitmoon_coins = None
satoshifaucet_coins_pre = None
feyorra_coins_pre = None
claimc_coins_pre = None
satoshifaucet_limit_reached = None
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
 
from skimage.metrics import structural_similarity as ssim
 
 
 
def capture_element_screenshot(driver, selector, screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png"):
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
 
def process_and_match(q_image_path, icons_folder):
    invert= True
    def convert_to_bw(image, invert):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        return cv2.bitwise_not(bw) if invert else bw
 
    q_image = cv2.imread(q_image_path)
    q_bw = convert_to_bw(q_image, False)
 
    best_match = None
    highest_similarity = -1
    similarity_scores = {}
 
    for icon_name in os.listdir(icons_folder):
        icon_path = os.path.join(icons_folder, icon_name)
        icon_image = cv2.imread(icon_path)
 
        if icon_image is None:
            continue
 
        icon_bw = convert_to_bw(icon_image, invert)
 
        # Ensure that both images are resized to the same dimensions
        resize_dim = (100, 100)
        q_resized = cv2.resize(q_bw, resize_dim)
        icon_resized = cv2.resize(icon_bw, resize_dim)
 
        # Calculate SSIM
        similarity, _ = ssim(q_resized, icon_resized, full=True)
 
        # Optionally, calculate Histogram Comparison
        q_hist = cv2.calcHist([q_resized], [0], None, [256], [0, 256])
        icon_hist = cv2.calcHist([icon_resized], [0], None, [256], [0, 256])
        hist_similarity = cv2.compareHist(q_hist, icon_hist, cv2.HISTCMP_CORREL)
 
        # Combine similarities
        combined_similarity = (similarity + hist_similarity) / 2
 
        similarity_scores[icon_name] = combined_similarity
 
        if combined_similarity > highest_similarity:
            highest_similarity = combined_similarity
            best_match = icon_name
 
    # Print all similarity scores
    print("Similarity scores for all images:")
    for icon_name, score in similarity_scores.items():
        print(f"{icon_name}: {score}")
 
    return best_match, highest_similarity

def rename_with_code(filepath):
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
        new_filename = f"{base_name}{random_code}{ext}"
        new_filepath = os.path.join(directory, new_filename)
        
        # Check if the new file exists
        if not os.path.exists(new_filepath):
            os.rename(filepath, new_filepath)
            print(f"File renamed to '{new_filepath}'")
            return



def find_similar_image(input_image_path, folder_path, similarity_threshold=0.95):
    # Load the input image
    input_image = cv2.imread(input_image_path)
    if input_image is None:
        return "Input image could not be loaded. Check the path."

    input_image = cv2.resize(input_image, (300, 300))  # Resize for consistent comparison
    input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Initialize variables for tracking the most similar image
    most_similar_image = None
    highest_similarity = 0

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Ensure it's an image
        if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg')):
            continue

        # Load and process the folder image
        folder_image = cv2.imread(file_path)
        if folder_image is None:
            continue

        folder_image = cv2.resize(folder_image, (300, 300))  # Resize to match input image
        folder_gray = cv2.cvtColor(folder_image, cv2.COLOR_BGR2GRAY)

        # Compute histogram similarity
        hist_input = cv2.calcHist([input_image], [0, 1, 2], None, [8, 8, 8],
                                  [0, 256, 0, 256, 0, 256])
        hist_folder = cv2.calcHist([folder_image], [0, 1, 2], None, [8, 8, 8],
                                   [0, 256, 0, 256, 0, 256])
        cv2.normalize(hist_input, hist_input)
        cv2.normalize(hist_folder, hist_folder)
        hist_similarity = cv2.compareHist(hist_input, hist_folder, cv2.HISTCMP_CORREL)

        # Compute Structural Similarity Index (SSIM)
        ssim_value = ssim(input_gray, folder_gray)

        # Combine metrics (weighted average or simply choose one)
        overall_similarity = (0.5 * hist_similarity) + (0.5 * ssim_value)

        # Update the most similar image if needed
        if overall_similarity > highest_similarity and overall_similarity >= similarity_threshold:
            highest_similarity = overall_similarity
            most_similar_image = file_path

    if most_similar_image:
        return os.path.splitext(os.path.basename(most_similar_image))[0]

    else:
        return None


def image_onscreeen(image_path, confidence=0.95, onlick = True):
    x = None
    y = None 
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if onlick:
            pyautogui.click(x, y)
            return True
        else:
            return None
    except pyautogui.ImageNotFoundException:
        return None




def earnow_online(window1):
    scrolled = False
    last_step = False
    timeout = 1
    pre_element = None
    window = window1
    wrong_captcha = 1
    win1 = True
    win2 = True

    while True:
        try:

            sb1.switch_to_window(window)
            title = sb1.get_title() #get_active_window_title()
            if "Shortlink" in title:
                return True
            #    if window2 == window:
            #        win2 = False
            #    if window1 == window:
            #        win1 = False
                       
            #    continue
            print(title)
 
            if sb1.is_element_visible("div.captcha-icon img"):
                sb1.execute_script("""
                    document.querySelectorAll('iframe').forEach((e, i) => i % 2 === 0 && e.remove());


                """)


                
                sb1.execute_script("""
                    const button = document.querySelector('button.btn.btn-lg.btn-primary.mb-2');
                    button.scrollIntoView({ behavior: 'smooth', block: 'end' });

                    // Slightly adjust the scroll position after a short delay
                    setTimeout(() => {
                        window.scrollBy(0, -200); // Move up by 50 pixels (adjust as needed)
                    }, 500);

                """)

                time.sleep(2)
                print("Captcha found")
                rename_with_code("element_screenshot.png")

                capture_element_screenshot(sb1, "div.captcha-icon img", screenshot_path="full_screenshot.png", cropped_path="element_screenshot.png")
                print("Image saved as 'captcha_image.svg'")
                icon_options = sb1.find_elements(By.CSS_SELECTOR, '#icon-options i[class*="fas fa-"]')
                icons_folder = 'icons'
                if not os.path.exists(icons_folder):
                    os.makedirs(icons_folder)
                    print(f"Created folder: {icons_folder}")
                else:
                    print(f"Folder already exists: {icons_folder}")
 
                # Delete the contents of the icons folder
                for filename in os.listdir(icons_folder):
                    file_path = os.path.join(icons_folder, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)  # Remove file or symbolic link
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)  # Remove directory
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Failed to delete {file_path}. Reason: {e}")
                result_mem = None
                result_mem = find_similar_image("element_screenshot.png", "element_icons")
                print("result:g ",result_mem)
                
                for icon in icon_options:
                    icon_class = icon.get_attribute('class').replace(' ', '.')     
                    if result_mem and result_mem in icon_class:
                        button = sb1.find_element(By.CSS_SELECTOR, f"i.{icon_class}")
                        actions = ActionChains(sb1)
                        #time.sleep(1)
                        actions.move_to_element(button).click().perform()  
                        print(f"Icon Found match: {icon_class}")
                        break
                    icon_class = "." + icon_class
                    print(f"Icon 1: {icon_class}")
                    # Delete all items in the icons folder before starting
                    capture_element_screenshot(sb1, icon_class, screenshot_path="full_screenshot.png", cropped_path=f"icons/{icon_class}.png")      
                if result_mem == None:
                    q_image = 'element_screenshot.png'
                    icons_folder = 'icons'
                    invert_filter = True  # Change to True to invert black and white
                    timeout = 1

                    best_match, similarity = process_and_match(q_image, icons_folder)
                    print(f"Most similar image: {best_match}, Similarity score: {similarity}")
                    best_match = best_match.replace('.png', '')
                    print(f"Icon 2: {best_match}")
                    button = sb1.find_element(By.CSS_SELECTOR, f"i{best_match}")
                    actions = ActionChains(sb1)
                    #sb1.disconnect()
                    time.sleep(1)
                    actions.move_to_element(button).click().perform()  
                    time.sleep(3)
                    #sb1.connect()
                    #return True



            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickad10sec.png", confidence=0.85)
                if x and y:
                    sb1.execute_script("""
                        (function() {
                            function removeIframes(element) {
                                element.querySelectorAll('iframe').forEach(el => el.remove());
                            }

                            function observeMutations() {
                                const observer = new MutationObserver(mutationsList => {
                                    for (const mutation of mutationsList) {
                                        if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                                            mutation.addedNodes.forEach(addedNode => {
                                                if (addedNode instanceof Element) {
                                                    removeIframes(addedNode);
                                                }
                                            });
                                        }
                                    }
                                });

                                observer.observe(document.documentElement, { childList: true, subtree: true });
                            }

                            console.log('Removing iframes and observing mutations...');
                            observeMutations();

                            setInterval(() => {
                                document.querySelectorAll('iframe').forEach(el => el.remove());
                            }, 100);
                        })();


                    """)


                    print("Click any ad and open in new tab, and wait 10 seconds before you can return and continue.")
                    pyautogui.rightClick(639, 568 )
                    time.sleep(1) 
                    #pyautogui.rightClick(645, 900 )  
            except Exception as e:  
                print("Not found clickad10sec")
            


            
            if "Wait" in title:
                sb1.open_new_tab()
                time.sleep(4)
                pyautogui.click(529, 568)
                time.sleep(2)
                sb1.close()
                sb1.switch_to_window(0)

            if "Just a moment" in title:
                sb1.disconnect()
                for i in range(20):
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                        pyautogui.click(x, y)
                        print('CloudFlare Box Found 1')
                        time.sleep(5)
 
                    except Exception as e:  
                        print("Not found cloudflare_box 2")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickheretostart.png", confidence=0.85)
                        if x and y:
                            print('clickheretostart Found 2')
                            break
                    except Exception as e:  
                        print("Not found clickheretostart 2")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickad10sec.png", confidence=0.85)
                        if x and y:
                            print('clickad10sec Found 2')
                            break
                    except Exception as e:  
                        print("Not found clickad10sec 2")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/vpnerror.png", confidence=0.85)
                        if x and y:
                            print("VPN Error 2")
                            break
                    except Exception as e:  
                        print("Not found vpnerror 2")

                    time.sleep(1)
                    print(i,'CloudFlare Just')
                sb1.connect()
                #cloudflare(sb1, login = True)
 
 
 
            if sb1.is_text_visible("Failed! Please reload the page."):
                print("Failed! Please reload the page.")
                
                sb1.disconnect()
                pyautogui.press('f5')
                time.sleep(5)
                for i in range(20):
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                        pyautogui.click(x, y)
                        print('CloudFlare Box Found 3')
                        time.sleep(5)
 
                    except Exception as e:  
                        print("Not found cloudflare_box 3")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickheretostart.png", confidence=0.85)
                        if x and y:
                                print('clickheretostart Found 3')
                                break
                    except Exception as e:  
                        print("Not found clickheretostart 3")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickad10sec.png", confidence=0.85)
                        if x and y:
                                print('clickad10sec Found 3')

                                break
                    except Exception as e:  
                        print("Not found clickad10sec 3")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/vpnerror.png", confidence=0.85)
                        if x and y:
                                break
                    except Exception as e:  
                        print("Not found vpnerror 3")

                    time.sleep(1)
                    print(i,'CloudFlare Just')
                sb1.connect()
                timeout = 1
                wrong_captcha += 1

            if sb1.is_element_visible("button.btn.btn-primary"):
                print("Button found g")
 
                # Use ActionChains to move to the button and click it
                button = sb1.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
                if button.text == "Click Here To Start":
                    actions = ActionChains(sb1)
                    actions.move_to_element(button).click().perform()      
                    sb1.disconnect()
                    #time.sleep(5)
                    for i in range(35):
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                            pyautogui.click(x, y)
                            time.sleep(4)
    
                        except Exception as e:  
                            print("Not found cloudflare_box 4")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/complete_captcha_earnow.png", confidence=0.85)
                            print('complete_captcha_earnow Found 4')
                            if x and y:
                                break
                        except Exception as e:  
                            print("Not found complete_captcha_earnow 4")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/scroll_down_earnow.png", confidence=0.85)
                            print('scroll_down_earnow Found 4')
                            if x and y:
                                break
                        except Exception as e:  
                            print(" Not found scroll_down_earnow 4")
                        time.sleep(1)
                        print("Waiting For Icon Image to Pop up:",i)
                    sb1.connect()
                    if sb1.is_text_visible("STEP 5/5"):
                        print("Steps 5/5 found")
                        last_step =True
                else:
                    print(f"Button Not found | {button.text}")

                #return True
            else:
                time.sleep(1)
                print("Waiting for button")


            if sb1.is_element_visible("div.mb-2.badge.bg-success"):
                print("verified found")
                timeout = 1
                wrong_captcha =1
                # Use ActionChains to move to the button and click it
                button = sb1.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.mb-2')
                actions = ActionChains(sb1)
                actions.move_to_element(button).click().perform() 
                scrolled = False 
                if last_step:  
                    time.sleep(2)  
                    return True
                sb1.disconnect()
                time.sleep(5)
                #pyautogui.press('f5')
                for i in range(20):
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                        pyautogui.click(x, y)
                        print('CloudFlare Box Found 6')
                        time.sleep(5)
 
                    except Exception as e:  
                        print("Not found cloudflare_box 6")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickheretostart.png", confidence=0.85)
                        if x and y:
                            print('clickheretostart Found 6')
                            break
                    except Exception as e:  
                        print("Not found clickheretostart 6")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickad10sec.png", confidence=0.85)
                        if x and y:
                            print('clickad10sec Found 6')
                            break
                    except Exception as e:  
                        print("Not found clickad10sec 6")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/vpnerror.png", confidence=0.85)
                        if x and y:
                            print('vpnerror Found 6')
                            break
                    except Exception as e:  
                        print("Not found vpnerror 6")

                    time.sleep(1)
                    print(i,'CloudFlare Just')
                sb1.connect()
            # List of element IDs to check
            element_ids = [
                "loadingDiv",
                "rewardMessage",
                "clickMessage",
                "captchaMessage",
                "scrollMessage"
            ]
            
            # Iterate through the element IDs
            for element_id in element_ids:
                if sb1.is_element_present(f"#{element_id}"):
                    # Get the style attribute of the element
                    style = sb1.get_attribute(f"#{element_id}", "style")
                
                    # Check if the element is visible
                    if "display: block;" in style:
                        print(f"Element with ID '{element_id}' is visible (style='display: block;'). timeout :{timeout}")
                        if pre_element == element_id:
                            timeout += 1
                            break
                        else:
                            timeout = 1
                            pre_element = element_id
                            break
                else:
                    print(f"Element with ID '{element_id}' is not present on the page. timeout :{timeout}")

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/vpnerror.png", confidence=0.85)
                if x and y:
                    print("VPN or Proxy detected. Please disable it and reload the page.")
                    sb1.disconnect()
                    pyautogui.press('f5')
                    time.sleep(5)
                    for i in range(20):
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                            pyautogui.click(x, y)
                            print('CloudFlare Box Found 5')
                            time.sleep(5)
    
                        except Exception as e:  
                            print("Not found cloudflare_box 5")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickheretostart.png", confidence=0.85)
                            if x and y:
                                print('clickheretostart Found 5')
                                break
                        except Exception as e:  
                            print("Not found clickheretostart 5")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickad10sec.png", confidence=0.85)
                            if x and y:
                                print('clickad10sec Found 5')
                                break
                        except Exception as e:  
                            print("Not found clickad10sec 5")
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/vpnerror.png", confidence=0.85)
                            if x and y:
                                print('vpnerror Found 5')
                                break
                        except Exception as e:  
                            print("Not found vpnerror 5")

                        time.sleep(1)
                        print(i,'CloudFlare Just')
                    sb1.connect()
            except Exception as e:  
                print(e)



            if timeout >= 8:
                #pyautogui.press('f5')
                timeout = 1
            if wrong_captcha >= 5:
                print('too many Wrong Captcha')
                #return 404
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                sb1.disconnect()
                time.sleep(1)
                pyautogui.click(x, y)
                for i in range(8):
                    try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                            pyautogui.click(x, y)
                            time.sleep(4)
    
                    except Exception as e:  
                        print("Not found cloudflare_box 7")
                    time.sleep(1)
                    print(i)
                sb1.connect()
 
            except Exception as e:  
                print('no cloudflare box')

        except Exception as e:
            print(e)
            sb1.switch_to.default_content()




def switch_extra_windows(driver, keep_window_handles):
    all_windows = driver.window_handles
    for window in all_windows:
        if window not in keep_window_handles:
            driver.switch_to.window(window)
            return window
 
def process_link_blocks(sb):
    # Find all "div.link-block" elements
    link_blocks = sb.find_elements("div.link-block")
    for index, block in enumerate(link_blocks):
        print(f"Processing block {index + 1}:")
 
        # Scroll the block into view
        sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
        try:
            # Get the link-name
            link_name_element = block.find_element(By.CSS_SELECTOR,"span.link-name")
            link_name = link_name_element.text
            print(f"Link Name: {link_name}")
 
            # Check if it's "Earnow"
 
            # Get the link-rmn
            link_rmn_element = block.find_element(By.CSS_SELECTOR,"span.link-rmn")
            link_rmn = link_rmn_element.text
            print(f"Link Remaining: {link_rmn}")
 
            if link_name == "Earnow":
                # Click the claim-button
                button = block.find_element(By.CSS_SELECTOR,"button[type='submit']")
 
                button.uc_click()
                #actions = ActionChains(sb1)
                #actions.move_to_element(button).click().perform()      
                print("Clicked the claim button.")
                return True
        except Exception as e:
            print(f"An error occurred in block {index + 1}: {e}")
            pyautogui.click(600,500 )



 
def process_link_blocks_claimtrx(sb):
    # Find all "div.link-block" elements
    link_blocks = sb.find_elements("div.col-md-6.col-lg-4.mb-3.mb-lg-0")
    for index, block in enumerate(link_blocks):
        print(f"Processing block {index + 1}:")
 
        # Scroll the block into view
        #sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
        try:
            # Get the link-name
            link_name_element = block.find_element(By.CSS_SELECTOR,"h5.card-title.text-center")
            link_name = link_name_element.text
            print(f"Link Name: {link_name}")
 
            # Check if it's "Earnow"
 
            # Get the link-rmn
            link_rmn_element = block.find_element(By.CSS_SELECTOR,"div.card-badge mb-3.text-center")
            link_rmn = link_rmn_element.text
            print(f"Link Remaining: {link_rmn}")
 
            if link_name == "Earnow":
                # Click the claim-button
                button = block.find_element(By.CSS_SELECTOR,"button[type='submit']")
                button.uc_click()
                #actions = ActionChains(sb1)
                #actions.move_to_element(button).click().perform()      
                print("Clicked the claim button.")
                return True
        except Exception as e:
            print(f"An error occurred in block {index + 1}: {e}")
            pyautogui.click(600,500 )


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
 
    sb1 = Driver(uc=True, headed=True, undetectable=True, undetected=True, user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path, page_load_strategy='eager')#, proxy=browser_proxy )
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
            fingerprint = True #install_extensions('fingerprint')
            nopecha = install_extensions('nopecha')
            if fingerprint and mysterium and sweet and cookie and nopecha:
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
 
    #time.sleep(999)
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
                    response_messege('satoshifaucet Loging')
                    if satoshifaucet:
 
                        satoshifaucet_window = handle_site(sb1, "https://satoshifaucet.io/links/currency/ltc", "Shortlinks", "Home", 1, [], ip_required)
                        if satoshifaucet_window == 404:
                            raise Exception(" satoshifaucet_window == 404")
                        print(f"satoshifaucet window handle: {satoshifaucet_window}")

                    

                else:
                    raise Exception("Ip changed")
 
 
 
                ip_address = get_ip(sb1)
                ip_required = ip_address
                if ip_required == ip_address:
                    response_messege('Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'mainscript'}}
                    result = collection.update_one(query, update)
 
                    all_window_handles = [satoshifaucet_window]
                    close_extra_windows(sb1, all_window_handles)
                    sb1.switch_to.window(satoshifaucet_window)
                    print(f"Windows: satoshifaucet: {satoshifaucet_window},")
                    global reset_count 
                    global reset_count_isacc 
                    global previous_reset_count
                    global satoshifaucet_limit_reached 
                    global feyorra_limit_reached 
 
                    satoshifaucet_limit_reached = None
                    feyorra_limit_reached = None
 
                    reset_count = 0
                    reset_count_isacc = 0
                    previous_reset_count = 0
 
 
                    return satoshifaucet_window,  ip_address, ip_required
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
 
satoshifaucet_count = 0 
feyorra_count = 0
claimcoin_count = 0

 
satoshifaucet_window,  ip_address, ip_required = open_faucets()
start_time4 = 0
#time.sleep(9999)
print('Starting Loop')
 
def switch_to_earnow(now = 1, window_lists=[]):
    valid_links = ['cryptowidgets', 'earnow', 'satoshifaucet', 'freeoseocheck',"giftmagic", "coinsvalue"]
    current_window = satoshifaucet_window
    all_windows = sb1.window_handles
    for window in all_windows:
        if window not in window_lists:
            sb1.switch_to.window(window)
            if 'Shortlink' in sb1.get_title():
                print("satoshifaucet is in the title")
                continue
            else:
                time.sleep(1)
                current_url = sb1.execute_script("return window.location.href;")
                for link in valid_links:
                    if link in current_url:
                        return sb1.current_window_handle
 
    print("Waiting for button")
    
    close_extra_windows(sb1, window_lists)
    if 'Shortlink' in sb1.get_title():
        print("satoshifaucet is in the title")
    else:
        if now == 1:
            sb1.switch_to_window(satoshifaucet_window)
            sb1.uc_open("https://satoshifaucet.io/links/currency/ltc")
        if now == 2:
            sb1.switch_to_window(feyorra_window)
            sb1.uc_open("https://satoshifaucet.io/links/currency/ltc")
    return None

def process_link_blocks(sb):
    # Find all "div.link-block" elements
    link_blocks = sb.find_elements("div.common_card.sl_card")
    for index, block in enumerate(link_blocks):
        print(f"Processing block {index + 1}:")
 
        # Scroll the block into view
        #sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
        try:
            # Get the link-name
            link_name_element = block.find_element(By.CSS_SELECTOR,"h5")
            link_name = link_name_element.text
            print(f"Link Name: {link_name}")
 
            # Check if it's "Earnow"
 
            # Get the link-rmn
            link_rmn_element = block.find_element(By.CSS_SELECTOR,"div.pill.sec")
            link_rmn = link_rmn_element.text
            print(f"Link Remaining: {link_rmn}")
 
            if link_name == "Earnow":
                # Click the claim-button
                button = block.find_element(By.CSS_SELECTOR,"button.btn_sl.link_bt")
                #button.uc_click()
                actions = ActionChains(sb1)
                actions.move_to_element(button).click().perform()  
                time.sleep(5) 
                print("Clicked the claim button.")
                return True
            
        except Exception as e:
            print(f"An error occurred in block {index + 1}: {e}")
            pyautogui.click(600,500 )


def process_link_blocks_fey(sb):
    # Find all "div.link-block" elements
    try:
        # Find the CAPTCHA image
        if sb.is_element_visible("img#rscaptcha_img"):
            solve_rscaptcha(sb)
            time.sleep(3)
            pyautogui.click(962,460)
            time.sleep(5)
            return
    except Exception as e:
        print(f"No rscaptcha processing: {e}")
        

    link_blocks = sb.find_elements("div.col-lg-4.mb-3")
    for index, block in enumerate(link_blocks):
        print(f"Processing block {index + 1}:")
 
        # Scroll the block into view
        #sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
        try:
            # Get the link-name
            link_name_element = block.find_element(By.CSS_SELECTOR,"div.linkname")
            link_name = link_name_element.text
            print(f"Link Name: {link_name}")
 
            # Check if it's "Earnow"
 
            # Get the link-rmn
            link_rmn_element = block.find_element(By.CSS_SELECTOR,"div.pill.sec")
            link_rmn = link_rmn_element.text
            print(f"Link Remaining: {link_rmn}")
 
            if link_name == "Earnow":
                # Click the claim-button
                button = block.find_element(By.CSS_SELECTOR,"button.btn.sl_claim.waves-effect")
                button.uc_click()
                #actions = ActionChains(sb1)
                #actions.move_to_element(button).click().perform()  
                time.sleep(5) 
                try:
                    # Find the CAPTCHA image
                    if sb.is_element_visible("img#rscaptcha_img"):
                        solve_rscaptcha(sb)
                        time.sleep(3)
                        pyautogui.click(962,460)
                        time.sleep(5)
                except Exception as e:
                    print(f"No rscaptcha processing: {e}")
                    
                print("Clicked the claim button.")
                return True
            
        except Exception as e:
            print(f"An error occurred in block {index + 1}: {e}")
            pyautogui.click(600,500 )

time.sleep(9990)
feyorra_window_shortlink = None
earnow_window = None
while True:
    try:
        mainscript = control_panel()
        print('control_panel', mainscript)
        if mainscript == 1:            
            ip_address = get_ip(sb1)
            debug_messages(f'Ip address Found:{ip_address}')
            if ip_address == ip_required:

                if satoshifaucet and earnow_window == None:
                    try:
                        debug_messages(f'Switching Pages to satoshifaucet')
                        sb1.switch_to.window(satoshifaucet_window)
                        debug_messages(f'Getting Pages Titile:satoshifaucet')
                        title =sb1.get_title()
                        if 'Shortlinks' in title:
                            process_link_blocks(sb1)
                            earnow_window = switch_to_earnow(1,[satoshifaucet_window])
                            if earnow_window:
                                close_extra_windows(sb1, [earnow_window])
                                result = earnow_online(earnow_window)

                                time.sleep(2)
                                satoshifaucet_window = earnow_window
                                #sb1.uc_open("https://claimtrx.com/links")
                                earnow_window = None
                                feyorra_window_shortlink = None
                                print('Done.....')
                            
 
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on satoshifaucet')
                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed satoshifaucet')
                        elif 'Home' in title or 'Login' in title:
                            debug_messages(f'LOGIN.. Found on satoshifaucet')
                            response_messege('LOGIN.. Found on satoshifaucet')
                            earnpp_coins = 0
                            reset_count +=5
                        else:
                            debug_messages(f'satoshifaucet not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                            sb1.uc_open('https://claimtrx.com/links')
                    except Exception as e:
                        print(f'ggg:{e}')
                        response_messege(f'ERR:{e}')
                        #time.sleep(999999)
            

                    
            else:
                print('IP Changed',ip_required)



    except Exception as e:
        print(f'ERR:{e}')
        response_messege(f'ERR:{e}')
        continue
 
