
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
 
mainfaucet_email = 'Nooo'
mainfaucet_pass = 'Nooo'
feyorra_email = 'Nooo'
feyorra_pass = 'Nooo'
claimc_email = 'yvonne12463@gmail.com'
claimc_pass = 'Uwuinsta@2005'
 
collection = db[f'Farm{farm_id}']
 
collectionbip = db[f'LocalCSB']
quer2y = {"type": "main"}
dochh = collectionbip.find_one(quer2y)
blacklistedIP = dochh["blacklistedIP"]
#print(blacklistedIP)
 
 
server_name1 = ''
CSB1_farms  = ''
mainfaucet_email = ''
mainfaucet_pass = ''
bitbitzz_email = ''
bitbitzz_pass = ''
feyorra_email = ''
feyorra_pass = ''
layout = ''
 
 
def get_mails_passowrds(farm_id):
    global server_name1
    global CSB1_farms
    global mainfaucet_email
    global mainfaucet_pass
    global feyorra_email
    global feyorra_pass
    global bitbitzz_email
    global bitbitzz_pass
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
            mainfaucet_email = 'khabibmakanzie@gmail.com'
            mainfaucet_pass = 'khabibmakanzie2'
            bitbitzz_email = 'khabibmakanzie2'
            bitbitzz_pass = 'khabibmakanzie'
            feyorra_email = 'khabibmakanz.ie@gmail.com'
            feyorra_pass = 'khabibmakanzie'

        elif '2' in layout:
            server_name1 = 'thailand' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'amytanisha250@gmail.com'
            mainfaucet_pass = 'amytanisha250'
            bitbitzz_email = 'amytanisha250' #'grandkoll.a@gmail.com'
            bitbitzz_pass = 'amytanisha250'
            feyorra_email = 'amytanisha250@gmail.com'
            feyorra_pass = 'amytanisha250'

        elif '3' in layout:
            server_name1 = 'bulgaria' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'grandkolla999br@gmail.com'
            mainfaucet_pass = 'grandkolla999br'
            feyorra_email = 'grandkolla999br@gmail.com'
            feyorra_pass = 'grandkolla999br'
 
        elif '4' in layout:
            server_name1 = 'thailand' # 'morocco' #'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'makanziekb@gmail.com'
            mainfaucet_pass = 'makanziekb'
            feyorra_email = 'makanziekb@gmail.com'
            feyorra_pass = 'makanziekb'
        else:
            print('Layout issue', layout)
 
    elif farm_id == 2:
 
        if '1' in layout:
            server_name1 = 'bulgaria'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'ashenrox1997@gmail.com'
            mainfaucet_pass = 'ashenrox1997'
            bitbitzz_email = 'ashenrox1997'
            bitbitzz_pass = 'ashenrox1997'
            feyorra_email = 'ashenrox1997@gmail.com'
            feyorra_pass = 'ashenrox1997'
 
        elif '2' in layout:
            server_name1 = 'bulgaria' #'portugal'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'ashenrox19.97@gmail.com'
            mainfaucet_pass = 'ashenrox1997'
            bitbitzz_email = 'ashenrox19972'
            bitbitzz_pass = 'ashenrox1997'
            feyorra_email = 'ashenrox19.97@gmail.com'
            feyorra_pass = 'ashenrox1997'


        elif '3' in layout:
            server_name1 = 'finland' #'portugal'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'anrogedyyr@gmail.com'
            mainfaucet_pass = 'anrogedyyr'
            feyorra_email = 'anrogedyyr@gmail.com'
            feyorra_pass = 'anrogedyyr'
        elif '4' in layout:
            server_name1 = 'estonia'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'bmetoomro190@gmail.com'
            mainfaucet_pass = 'bmetoomro190'
            feyorra_email = 'bmetoomro190@gmail.com'
            feyorra_pass = 'bmetoomro190'
        else:
            print('Layout issue', layout)
 
 
    elif farm_id == 3:
 
 
        if '1' in layout:
            server_name1 = 'france'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'grandkolla77@gmail.com'
            mainfaucet_pass = 'grandkolla77'
            bitbitzz_email = 'grandkolla77'
            bitbitzz_pass = 'grandkolla77'
            feyorra_email = 'grandkolla77@gmail.com'
            feyorra_pass = 'grandkolla77'

        elif '2' in layout:
            server_name1 = 'france' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]

            mainfaucet_email = 'grandkolla.7.7@gmail.com'
            mainfaucet_pass = 'grandkolla77'
            bitbitzz_email = 'grandkolla772'
            bitbitzz_pass = 'grandkolla77'
            feyorra_email = 'grandkolla.7.7@gmail.com'
            feyorra_pass = 'grandkolla77'
 
        elif '3' in layout:
            server_name1 = 'spain' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'berendkalpana2@gmail.com'
            mainfaucet_pass = 'berendkalpana2'
            feyorra_email = 'berendkalpana2@gmail.com'
            feyorra_pass = 'berendkalpana2'
        elif '4' in layout:
            server_name1 = 'france'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'voyn3642ovene@gmail.com'
            mainfaucet_pass = 'voyn3642ovene'
            feyorra_email = 'voyn3642ovene@gmail.com'
            feyorra_pass = 'voyn3642ovene'
 
        else:
            print('Layout issue', layout)
 
 
    elif farm_id == 4:
 
        if '1' in layout:
            server_name1 = 'hungary'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'metroboom910@gmail.com'
            mainfaucet_pass = 'metroboom910'
            bitbitzz_email = 'metroboom910'
            bitbitzz_pass = 'metroboom910'
            feyorra_email = 'metroboom910@gmail.com'
            feyorra_pass = 'metroboom910'

        elif '2' in layout:
            server_name1 = 'hungary' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'metroboom.9.1.0@gmail.com'
            mainfaucet_pass = 'metroboom.9102'
            bitbitzz_email = 'metroboom.9102'
            bitbitzz_pass = 'metroboom.9102'
            feyorra_email = 'metroboom.9.1.0@gmail.com'
            feyorra_pass = 'metroboom.9102'


        elif '3' in layout:
            server_name1 = 'hong kong' #'georgia'# 
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'andrpewrea@gmail.com'
            mainfaucet_pass = 'andrpewrea'
            feyorra_email = 'andrpewrea@gmail.com'
            feyorra_pass = 'andrpewrea'
        elif '4' in layout:
            server_name1 = 'hungary'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'shiladid323@gmail.com'
            mainfaucet_pass = 'shiladid323'
            feyorra_email = 'shiladid323@gmail.com'
            feyorra_pass = 'shiladid323'
        else:
            print('Layout issue', layout)
 
 
    elif farm_id == 5:
 
        if '1' in layout:
            server_name1 = 'italy'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'gihanfer907@gmail.com'
            mainfaucet_pass = 'gihanfer907'
            bitbitzz_email = 'gihanfer907'
            bitbitzz_pass = 'gihanfer907'
            feyorra_email = 'gihanfer907@gmail.com'
            feyorra_pass = 'gihanfer907'

        elif '2' in layout:
            server_name1 = 'italy' #'belgium'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]

            mainfaucet_email = 'gihanfer.9.0.7@gmail.com'
            mainfaucet_pass = 'gihanfer907'
            bitbitzz_email = 'gihanfer9072'
            bitbitzz_pass = 'gihanfer907'
            feyorra_email = 'gihanfer.9.0.7@gmail.com'
            feyorra_pass = 'gihanfer907'

        elif '3' in layout:
            server_name1 = 'malaysia' #'chile'
            CSB1_farms = [1, 2, 3, 4, 5] #[6, 7, 8, 9, 10]
            mainfaucet_email = 'redgta362@gmail.com'
            mainfaucet_pass = 'redgta362'
            feyorra_email = 'redgta362@gmail.com'
            feyorra_pass = 'redgta362'
        elif '4' in layout:
            server_name1 = 'italy'
            CSB1_farms = [1, 2, 3, 4, 5]
            mainfaucet_email = 'ferhng790@gmail.com'
            mainfaucet_pass = 'ferhng790'
            feyorra_email = 'ferhng790@gmail.com'
            feyorra_pass = 'ferhng790'
        else:
            print('Layout issue', layout)
 
##################################################
    elif farm_id == 6:
 
        if '1' in layout:
            server_name1 = 'indonesia'
            CSB1_farms = [6,7,8,9,10]
            mainfaucet_email = 'sevensevengk@gmail.com'
            mainfaucet_pass = 'sevensevengk'
            feyorra_email = 'sevensevengk@gmail.com'
            feyorra_pass = 'sevensevengk'
 
 
        elif '2' in layout:
            server_name1 = 'indonesia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'gksevn77@gmail.com'
            mainfaucet_pass = 'gksevn77'
            feyorra_email = 'gksevn77@gmail.com'
            feyorra_pass = 'gksevn77'
 
        elif '3' in layout:
            server_name1 = 'south korea' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'kg7seven@gmail.com'
            mainfaucet_pass = 'kg7seven'
            feyorra_email = 'kg7seven@gmail.com'
            feyorra_pass = 'kg7seven'
        elif '4' in layout:
            server_name1 = 'south korea'
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'fosengklla@gmail.com'
            mainfaucet_pass = 'fosengklla'
            feyorra_email = 'fosengklla@gmail.com'
            feyorra_pass = 'fosengklla'
 
 
    elif farm_id == 7:
 
        if '1' in layout:
            server_name1 = 'belgium'
            CSB1_farms = [6,7,8,9,10]
            mainfaucet_email = 'shevgraaa@gmail.com'
            mainfaucet_pass = 'shevgraaa'
            feyorra_email = 'shevgraaa@gmail.com'
            feyorra_pass = 'shevgraaa'
 
        elif '2' in layout:
            server_name1 = 'belgium' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'grshevvvv@gmail.com'
            mainfaucet_pass = 'grshevvvv'
            feyorra_email = 'grshevvvv@gmail.com'
            feyorra_pass = 'grshevvvv'
 
 
        elif '3' in layout:
            server_name1 = 'denmark' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'grevonshld@gmail.com'
            mainfaucet_pass = 'grevonshld'
            feyorra_email = 'grevonshld@gmail.com'
            feyorra_pass = 'grevonshld'
        elif '4' in layout:
            server_name1 = 'denmark'
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'sheforldnmk@gmail.com'
            mainfaucet_pass = 'sheforldnmk'
            feyorra_email = 'sheforldnmk@gmail.com'
            feyorra_pass = 'sheforldnmk'
 
 
    elif farm_id == 8:
 
        if '1' in layout:
            server_name1 = 'croatia'
            CSB1_farms = [6,7,8,9,10]
            mainfaucet_email = 'ahenrxaaa@gmail.com'
            mainfaucet_pass = 'ahenrxaaa'
            feyorra_email = 'ahenrxaaa@gmail.com'
            feyorra_pass = 'ahenrxaaa'
 
        elif '2' in layout:
            server_name1 = 'croatia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'rxshenaxa@gmail.com'
            mainfaucet_pass = 'rxshenaxa'
            feyorra_email = 'rxshenaxa@gmail.com'
            feyorra_pass = 'rxshenaxa'
 
 
        elif '3' in layout:
            server_name1 = 'saudi arabia' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'rhexnargg@gmail.com'
            mainfaucet_pass = 'rhexnargg'
            feyorra_email = 'rhexnargg@gmail.com'
            feyorra_pass = 'rhexnargg'
 
        elif '4' in layout:
            server_name1 = 'saudi arabia'
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'senarxbiag@gmail.com'
            mainfaucet_pass = 'senarxbiag'
            feyorra_email = 'senarxbiag@gmail.com'
            feyorra_pass = 'senarxbiag'
 
    elif farm_id == 9:
 
        if '1' in layout:
            server_name1 = 'canada'
            CSB1_farms = [6,7,8,9,10]
            mainfaucet_email = 'semiprraaa@gmail.com'
            mainfaucet_pass = 'semiprraaa'
            feyorra_email = 'semiprraaa@gmail.com'
            feyorra_pass = 'semiprraaa'
 
        elif '2' in layout:
            server_name1 = 'canada' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'pereramishee@gmail.com'
            mainfaucet_pass = 'pereramishee'
            feyorra_email = 'pereramishee@gmail.com'
            feyorra_pass = 'pereramishee'
 
 
 
        elif '3' in layout:
            server_name1 = 'sweden' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'ramishepera@gmail.com'
            mainfaucet_pass = 'ramishepera'
            feyorra_email = 'ramishepera@gmail.com'
            feyorra_pass = 'ramishepera'
        elif '4' in layout:
            server_name1 = 'sweden'
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'pesheswendemi@gmail.com'
            mainfaucet_pass = 'pesheswendemi'
            feyorra_email = 'pesheswendemi@gmail.com'
            feyorra_pass = 'pesheswendemi'
 
 
    elif farm_id == 10:
 
        if '1' in layout:
            server_name1 = 'austria'
            CSB1_farms = [6,7,8,9,10]
            mainfaucet_email = 'melosandsong@gmail.com'
            mainfaucet_pass = 'melosandsong'
            feyorra_email = 'melosandsong@gmail.com'
            feyorra_pass = 'melosandsong'
 
        elif '2' in layout:
            server_name1 = 'austria' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'sadrameloonsan@gmail.com'
            mainfaucet_pass = 'sadrameloonsan'
            feyorra_email = 'sadrameloonsan@gmail.com'
            feyorra_pass = 'sadrameloonsan'
 
 
        elif '3' in layout:
            server_name1 = 'lithuania' 
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'mlsansonone@gmail.com'
            mainfaucet_pass = 'mlsansonone'
            feyorra_email = 'mlsansonone@gmail.com'
            feyorra_pass = 'mlsansonone'
        elif '4' in layout:
            server_name1 = 'lithuania'
            CSB1_farms = [6, 7, 8, 9, 10]
            mainfaucet_email = 'saradmsnire@gmail.com'
            mainfaucet_pass = 'saradmsnire'
            feyorra_email = 'saradmsnire@gmail.com'
            feyorra_pass = 'saradmsnire'
 
 
 
 
    else:
        while True:
            print('SOmething Wrong Did u use --farm')
    print(server_name1)
    print(CSB1_farms)
    print(mainfaucet_email)
    print(mainfaucet_pass)
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
mainfaucet = True
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
    #add_messages('pepelom', {now: amount1})
    #add_messages('feyorramack', {now: amount2})
    #add_messages('claimcoins', {now: amount3})
 
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
                            if 'Ready IP' in res:
                                res_farms.append(res)
                            elif req == 'ipfixer' and 'Loging' in res:
                                res_farms.append(res)
                            elif req == 'mainscript': #and 'Running' in res:
                                res_farms.append(res)
                            elif req == 'mainscript': #and 'Ready IP' in res:
                                res_farms.append(res)
                            else:
                                print('aiyo', req)
                        if len(res_farms) >= len(CSB1_farms):
                            time.sleep(8)
                            if gg2344 > 4:
 
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
        if 'bitBitz' in current_title:
            email_input = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input#username'))
            )
            email_input.send_keys(email)
        else:
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
 
                            button = sb1.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
                            actions = ActionChains(sb1)
                            actions.move_to_element(button).click().perform()    
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
 
               # button = sb1.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
               # actions = ActionChains(sb1)
               # actions.move_to_element(button).click().perform()      
 
            else:
                for i in range(1, 10):
                    time.sleep(1)
                    pyautogui.moveTo(100, 200)
 
                    sb1.execute_script("window.scrollTo(0, 1000);")
                    cloudflare(driver, True)
                    button = sb1.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
                    actions = ActionChains(sb1)
                    actions.move_to_element(button).click().perform()      
    
       #pyautogui.click(955, 916 )
        #time.sleep(1)
        #pyautogui.click(955, 900 )
        print("✅ CAPTCHA validated")
        time.sleep(3)
        print("🚀 Login attempt made!")
 
 
def mainfaucet_login(driver,url,email,restrict_pages):
 
    #driver.uc_open(url)
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
 
def hafaucet_login(driver,url,email,restrict_pages):
    try:
        driver.uc_open(url)
        time.sleep(3)
    
        all_windows = driver.window_handles
        for window in all_windows:
            if window not in restrict_pages:
                driver.switch_to.window(window)
        driver.uc_click('button.login_bt')
        print("WebDriver Check")
        current_title = driver.get_title()
        print(f"Current g title: {current_title}")
        if current_title in current_title:
            # Wait for the email input by type attribute
            email_input = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
            )
            email_input.send_keys(email)


            for i in range(1, 50):
                time.sleep(2)
                try:
                    #x,y = pyautogui.locateCenterOnScreen(f"notrobotdone.png", confidence=0.75)
                    x,y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/notrobotdone.png", confidence=0.8)
                    if x and y:
                        pyautogui.click(x, y)
                        break
                except Exception as e:
                    print(f'Element Not Found Recaptcha :{e}')
    
            button = sb1.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
            actions = ActionChains(sb1)
            actions.move_to_element(button).click().perform()  
            print("✅ CAPTCHA validated")
            time.sleep(3)
            print("🚀 Login attempt made!")
    except Exception as e:
        pass


bitmoon_window = None
mainfaucet_window = None
claimcoin_window = None
feyorra_window = None
baymack_window = None
feyorratop_window = None
 
def close_extra_windows(driver, keep_window_handles):
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    if len(all_windows) == 1:
        driver.switch_to.window(current_window)
        return
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

        if 'bitBitz' in current_title:
            if driver.is_element_visible('li.nav-item a.nav-link[href="/login"]'):
                if function == 4:
                    login_to_faucet('https://bitbitz.cc/login', sb1, bitbitzz_email, bitbitzz_pass, 'cloudflare', window_list, 'submit_button')
            if driver.is_element_visible('li.nav-item a.nav-link[href="/dashboard"]'):
                if 'Shortlink' in current_title:
                    if driver.current_window_handle not in window_list:
                        ready = True
            continue
        if expected_title in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif "SatoshiFaucet | Satoshi faucet" in current_title or 'CoinPayz - Multicurrency Crypto Earning Platform' in current_title or 'Home' in current_title or 'Earn Free Bitcoin & Crypto - Faucet, PTC, Surveys / bitBitz' in current_title:

            if function == 1:
                mainfaucet_login(sb1,'https:/satoshifaucet.io/',mainfaucet_email,window_list)
            if function == 2:
                login_to_faucet('https://coinpayz.xyz/login', sb1, 'grandkolla@gmail.com', 'Uwuinsta2005', 'cloudflare', window_list, 'submit_button')
            if function == 3:
                hafaucet_login(sb1,'https://helpfpcoin.site/','grandkolla@gmail.com',window_list)
 
            #if function == 4:
            #    login_to_faucet('https://bitbitz.cc/login', sb1, bitbitzz_email, bitbitzz_pass, 'cloudflare', window_list, 'submit_button')
            if function == 5:
                login_to_faucet('https://feyorra.top/login', sb1, feyorra_email, feyorra_pass, 'rscaptcha', window_list, "button[type='submit']")
            

        elif 'Lock' in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Maintenance' in current_title:
            if driver.current_window_handle not in window_list:
                ready = True
        elif 'Just' in current_title:
            cloudflare(driver, login = False)
            time.sleep(8)
 
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
mainfaucet_coins = None
feyorra_coins = None
claimc_coins = None
bitmoon_coins = None
mainfaucet_coins_pre = None
feyorra_coins_pre = None
claimc_coins_pre = None
mainfaucet_limit_reached = None
feyorra_limit_reached = None
#if run_sb1:
sb1 = None
def are_extensions_exist():
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cookie_icon.png", region=(1525, 43, 700, 300), confidence=0.9)
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
 
        #if combined_similarity > highest_similarity:
        #    highest_similarity = combined_similarity
        #    best_match = icon_name
 
    list1 = []
    list2 = []
    print("Similarity scores for all images:")
    for icon_name, score in similarity_scores.items():
        print(f"{icon_name}: {score}")
        list1.append(score)
        list2.append(icon_name)

     # Get the maximum value
    gg = max(list1)

    # Get the index of the maximum value
    print("List of scores:", list1)
    print("List of icons:", list2)

    best_match, highest_similarity = max(zip(list2, list1), key=lambda x: x[1])

    print(f"Final Best Match: {best_match} with Score: {highest_similarity}")
    print("Max value:", gg)
    #best_match = index_gg2

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

def copy_image_if_not_exists(input_path, output_path):
    # Check if the input image exists
    if not os.path.isfile(input_path):
        print(f"Error: The input file '{input_path}' does not exist.")
        return

    # Check if the output image already exists
    if os.path.isfile(output_path):
        print(f"The image already exists at '{output_path}'. No action needed.")
        return

    # Ensure the output directory exists (create it if not)
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Created directory: '{output_dir}'")
        except Exception as e:
            print(f"Error creating directory: {e}")
            return

    # Copy the input file to the output path
    try:
        shutil.copy(input_path, output_path)
        print(f"Image copied from '{input_path}' to '{output_path}'.")
    except Exception as e:
        print(f"Error occurred while copying the image: {e}")


def find_similar_image(input_image_path, folder_path, similarity_threshold=0.7):
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



def earnow_loading(driver):
    print('start earnow_loading')
    #images_list = ['cloudflare_box', 'clickheretostart', 'clickad10sec', 'vpnerror', 'complete_captcha_earnow', 'scroll_down_earnow', 'adsoff', 'loading_linkwait2']
    refresh_list = ['vpnerror','adsoff','page_notload' ]
    clicking_list = ['cloudflare_box', 'clickheretostart','agree-cookie-earnow', 'countinue-cookie-earnow']
    return_list =[ 'clickad10sec', 'complete_captcha_earnow', 'scroll_down_earnow']
    bugs_list = ['loading_linkwait2']
    tolerance = 0.8
    ggg = 1
    bug = 1
    try:
        while ggg < 24:
            pyautogui.scroll(1000,1808 ,190 )
            ggg += 1
            print(f'Bug Loading Attempt:',bug)
            print(f'Trying Loading Attempt:',ggg)
            title = get_active_window_title()
            if "Shortlink" in title:
                return
            pyautogui.moveTo(200,100)
            time.sleep(1)
            #cloudflare

            for item in clicking_list:
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{item}.png", confidence=tolerance)
                    pyautogui.click(x, y)
                    bug = 1
                    print(f'{item} Box clicking_list 1')
                    time.sleep(4)
                except Exception as e:  
                    print(f"Not clicking_list {item} 2")
                    
            
            #refresh list
            for item in refresh_list:
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{item}.png", confidence=tolerance)
                    pyautogui.click(x, y)
                    print(f'{item} Box refresh_list 1')
                    pyautogui.press('f5')
                    ggg = 1
                    bug = 1
                    time.sleep(4)
                except Exception as e:  
                    print(f"Not refresh_list {item} 2")

            #Return List
            for item in return_list:
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{item}.png", confidence=tolerance)
                    pyautogui.click(x, y)
                    print(f'{item} Box return_list 1')
                    time.sleep(1)

                    return True
                except Exception as e:  
                    print(f"Not return_list {item} 2")

            #Loding Bug Fix
            for item in bugs_list:
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{item}.png", confidence=tolerance)
                    pyautogui.click(x, y)
                    print(f'{item} Box bugs_list 1')
                    bug += 3
                    time.sleep(2)
                    if bug > 6:
                        pyautogui.press('f5')
                        bug = 1
                    
                except Exception as e:  
                    print(f"Not bugs_list {item} 2")
                    bug = 1

            try:
                x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/site_permission.png", confidence=tolerance)
                print(f'{item} Box refresh_list 1')
                pyautogui.click(x, y)
                time.sleep(1)
                pyautogui.click(1064,829)
                pyautogui.click(1063,802)
            except Exception as e:  
                print(f"Not refresh_list {item} 2")


    except Exception as e:
        print('earnow_loading',e)
    #driver.connect()
    return False


def remove_noise_with_median_and_morphology(image_path, output_path):
    # Load the image
    img = cv2.imread(image_path)

    # Check if the image was loaded correctly
    if img is None:
        print("Error loading image.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a median filter to reduce noise while preserving edges
    denoised = cv2.medianBlur(gray, 1)  # Kernel size 3, adjust if necessary

    # Create a kernel for morphological operations (increase size if needed)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))  # Increased kernel size

    # Apply the closing morphological operation
    morph = cv2.morphologyEx(denoised, cv2.MORPH_CLOSE, kernel)

    # Optionally, apply a second round of median blur if the image still has noise
    final_output = cv2.medianBlur(morph, 1)

    # Save the result to the output path
    cv2.imwrite(output_path, final_output)
    print(f"Image saved to {output_path}")

def process_and_match_bygiven(q_image_path,class_names,icons_folder):
    invert= False
    def convert_to_bw(image, invert):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        return cv2.bitwise_not(bw) if invert else bw
 
    q_image = cv2.imread(q_image_path)
    q_bw = convert_to_bw(q_image, False)
    best_match = None
    highest_similarity = -1
    similarity_scores = {}
 
    list1 = []
    list2 = []



    for icon_name in os.listdir(icons_folder):
        icon_path = os.path.join(icons_folder, icon_name)
        icon_image = cv2.imread(icon_path)
        icon_name2 = icon_name.replace("2", "")
        icon_name2 = icon_name.replace("3", "")
        icon_name2 = icon_name.replace("4", "")
        icon_name2 = icon_name.replace("5", "")
        icon_name2 = icon_name.replace("6", "")
        icon_name2 = icon_name.replace(".png", "")


        if icon_image is None:
            continue
        
        if f"fas.fa-{icon_name2}.icon-option" not in class_names:
            #print(f'icon_image{icon_name} | class_names{class_names}')
            continue
        print(f'icon_image{icon_name2} | class_names{class_names}')
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
 
        #if combined_similarity > highest_similarity:
        #    highest_similarity = combined_similarity
        #    best_match = icon_name


    print("Similarity scores for all images:",similarity_scores)
    for icon_name, score in similarity_scores.items():
        print(f"{icon_name}: {score}")
        list1.append(score)
        list2.append(icon_name)

     # Get the maximum value
    gg = max(list1)

    # Get the index of the maximum value
    index_gg = list1.index(gg)
    index_gg2= list2[index_gg]

    print("Max value:", gg)
    print("Index of max value:", index_gg)
    print("Index of max value2:", index_gg2)
    index_gg2 = index_gg2.replace("2", "")
    index_gg2 = index_gg2.replace("3", "")
    index_gg2 = index_gg2.replace("4", "")
    index_gg2 = index_gg2.replace("5", "")
    index_gg2 = index_gg2.replace("6", "")
    index_gg2 = index_gg2.replace(".png", "")
    print("Best Match:", index_gg2)
    best_match = index_gg2

    return best_match, highest_similarity


def earnow_online(window, ip_required):
    scrolled = False
    last_step = False
    timeout = 1
    pre_element = None
    wrong_captcha = 1
    bug = 1


    while True:
        try:

            sb1.switch_to_window(window)

            pyautogui.scroll(1000,1808 ,190 )
            if timeout >= 7:
                pyautogui.press('f5')
                timeout = 1
                print("Timeout ", timeout)
                wrong_captcha +=2
                
            if wrong_captcha >= 5:
                print('too many Wrong Captcha')
                return 404
                #time.sleep(99999)
            mainscript = control_panel()
            if mainscript != 1:
                print('mainscript is changed....')
                return
            title = sb1.get_title() #get_active_window_title()



            if "Shortlink" in title or 'Link' in title or 'Dashboard of Coin' in title:
                return True
            if sb1.is_element_present("h1.title.ttu.text-center"):
                step_text = sb1.get_text("h1.title.ttu.text-center")
                if 'STEP' not in step_text:
                    print('Stes not found')
                    wrong_captcha +=1


            print(title)
            if sb1.is_element_visible("button.btn.btn-primary"):
                print("Button found g")
 
                # Use ActionChains to move to the button and click it
                button = sb1.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
                if button.text == "Click Here To Start":
                    actions = ActionChains(sb1)
                    actions.move_to_element(button).click().perform()      
                    sb1.disconnect()
                    earnow_loading(sb1)
                    sb1.connect()
                    if sb1.is_text_visible("STEP 5/5"):
                        print("Steps 5/5 found")
                        last_step =True
                else:
                    print(f"Button Not found | {button.text}")
            else:
                print("Waiting for button")

            for item in ['cloudflare_box', 'clickheretostart','loading_linkwait2', 'vpnerror','adsoff']:
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/earnow_verifying_bug.png", confidence=0.85)
                    if x and y:
                        ip_address = get_ip(sb1)
                        if ip_address != ip_required:
                            wrong_captcha +=2
                            print('wrong Ip address')
                            continue
                        break
                except Exception as e:  
                    print("Not found earnow_verifying_bug")


            if sb1.is_element_present("div.mb-2.badge.bg-success"):
                print("verified found")
                timeout = 1
                wrong_captcha =1
                # Use ActionChains to move to the button and click it
                button = sb1.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.mb-2')
                actions = ActionChains(sb1)
                actions.move_to_element(button).click().perform() 
                
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/verify_earnow.png", confidence=0.85)
                except Exception as e:
                    print('No Page Image found')
                    pyautogui.scroll(-1,1021,475)
                scrolled = False 
                if last_step:  
                    time.sleep(2)  
                    return True
                sb1.disconnect()
                earnow_loading(sb1)
                sb1.connect()
                #time.sleep(5)

            else:
                print("Not found div.mb-2.badge.bg-success")

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/earnow_verifying_bug.png", confidence=0.85)
                if x and y:
                    timeout += 1
                    time.sleep(1)
                    print("found earnow_verifying_bug")
                    continue 

            except Exception as e:  
                print("Not found earnow_verifying_bug")
            
            for item in ['clickheretostart', 'agree-cookie-earnow', 'countinue-cookie-earnow']:
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{item}.png", confidence=0.8)
                    if x and y:
                        pyautogui.click(x,y)
                except Exception as e:  
                    print("Not found earnow_verifying_bug")

            for item in ['complete_captcha_earnow', 'scroll_down_earnow']:
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{item}.png", confidence=0.85)
                    if x and y:
                        if sb1.is_element_visible("div.captcha-icon img"):
                            #remove ads
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


                            try:
                                x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/verify_earnow.png", confidence=0.85)
                                print("Verify Button found")
                            except Exception as e:
                                print('No Page Image found')
                                sb1.execute_script("""
                                    const button = document.querySelector('button.btn.btn-lg.btn-primary.mb-2');
                                    button.scrollIntoView({ behavior: 'smooth', block: 'center' });

                                    // Slightly adjust the scroll position after a short delay
                                    setTimeout(() => {
                                    window.scrollBy(0, -20); // Move up by 50 pixels (adjust as needed)
                                    }, 500);

                            """)

                            time.sleep(2)
                            try:
                                x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/verify_earnow.png", confidence=0.8)
                                if x and y:
                                    print("Captcha found")
                                    

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
                                    classes_list2 = []
                                    for icon in icon_options:
                                        icon_class = icon.get_attribute('class').replace(' ', '.')     
                                        classes_list2.append(icon_class)

                                    #result_mem = find_similar_image("element_screenshot.png", "element_icons")
                                    best_match, highest_similarity = process_and_match_bygiven("element_screenshot.png",classes_list2,"element_icons")
                                    result_mem = best_match
                                    print("result:g ",result_mem)
                                    if result_mem:
                                        result_mem = result_mem.replace("2", "")
                                        result_mem = result_mem.replace("3", "")
                                        result_mem = result_mem.replace("4", "")
                                        result_mem = result_mem.replace("5", "")

                                    print("result:g without2",result_mem)
                                    print('lngth of icons:',len(icon_options))
                                    

                                    for icon in icon_options:
                                        icon_class = icon.get_attribute('class').replace(' ', '.')     
                                        #classes_list2.append(icon_class)
                                        if result_mem and result_mem in icon_class:
                                            button = sb1.find_element(By.CSS_SELECTOR, f"i.{icon_class}")
                                            actions = ActionChains(sb1)
                                            #time.sleep(1)
                                            actions.move_to_element(button).click().perform()  
                                            print(f"Icon Found match: {icon_class}")
                                            break
                                        icon_class = "." + icon_class
                                        print(f"Icon 1: {icon_class}")
                                    time.sleep(2)
                            except Exception as e:
                                print('No Page Image found',e)
                            
                        else:
                            print('Captcha not loading...')
                            timeout += 3
                            
                except Exception as e:  
                    print(f"Not found {item}")

            if "Wait" in title:
                sb1.open_new_tab()
                sb1.switch_to_newest_window()

                time.sleep(9)
                pyautogui.click(529, 568)
                time.sleep(2)
                sb1.close()
                sb1.switch_to_window(window)
                timeout += 1
                print('Wait found')
                continue

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/clickad10sec.png", confidence=0.85)
                if x and y:
                    pyautogui.scroll(2000,1021,475)

                    print("Click any ad and open in new tab, and wait 10 seconds before you can return and continue.")
                    pyautogui.rightClick(639, 555 )
                    time.sleep(2) 
                    pyautogui.rightClick(1303 ,548 )  
                    time.sleep(2) 
                    pyautogui.rightClick(1303 ,548 )
                    timeout += 1
                    continue 
            except Exception as e:  
                print("Not found clickad10sec")
            


            if "Just" in title:
                sb1.disconnect()
                earnow_loading(sb1)
                sb1.connect()
                continue
 
 
 
            if sb1.is_text_visible("Failed! Please reload the page."):

                print("Failed! Please reload the page.")
                #time.sleep(999999)
                scrolled = False
                current_url = sb1.execute_script("return window.location.href;")
                current_window = sb1.current_window_handle
                geo_location_changer()
                sb1.open_new_tab()
                sb1.uc_open(current_url)
                time.sleep(3)
                all_windows = sb1.window_handles
                for window in all_windows:
                    if window == current_window:
                        sb1.switch_to.window(window)
                        sb1.close()  # Close the tab
                        break
                all_windows = sb1.window_handles
                window = all_windows[0]
                sb1.switch_to.window(window)
                sb1.uc_open(current_url)
                
                
                sb1.disconnect()
                #pyautogui.press('f5')
                earnow_loading(sb1)
                sb1.connect()
                #rename_with_code("element_screenshot.png")

                wrong_captcha += 1





            # List of element IDs to check
            images_list = ['cloudflare_box', 'clickheretostart', 'clickad10sec', 'vpnerror', 'complete_captcha_earnow', 'scroll_down_earnow', 'adsoff', 'loading_linkwait2']
            
            # Iterate through the element IDs
            for item in images_list:
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{item}.png", confidence=0.85)
                    if x and y:
                        if pre_element == item:
                            timeout += 1
                            break
                        else:
                            timeout = 1
                            
                            pre_element = item
                            break

                except Exception as e:
                    print('No Page Image found')




            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.85)
                sb1.disconnect()
                
                earnow_loading(sb1)
                sb1.connect()
            except Exception as e:  
                print('no cloudflare box')

            timeout += 1

        except Exception as e:
            print('issuegg',e)
            sb1.switch_to.default_content()
            all_windows = sb1.window_handles
            window = all_windows[0]
            sb1.switch_to.default_content()
            wrong_captcha += 0.5

 
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



def geo_location_changer():
    for i in range(10):
        try:
            #open extension
            #wait for pop
            #check settings if mot match
                #change the settings
            #return 
            try:
                x,y = pyautogui.locateCenterOnScreen('/root/Desktop/MFV6/images/geo.png', confidence=0.95)
                pyautogui.click(x,y)
                time.sleep(3)
            except Exception as e:
                print('Geo extension not found')
            try:
                x,y = pyautogui.locateCenterOnScreen('/root/Desktop/MFV6/images/vroxy_logo.png', confidence=0.95)
                time.sleep(1)
                try:
                    x,y = pyautogui.locateCenterOnScreen('/root/Desktop/MFV6/images/matchip.png', confidence=0.95)
                    try:
                        x,y = pyautogui.locateCenterOnScreen('/root/Desktop/MFV6/images/refresh_geo.png', confidence=0.95)
                        pyautogui.click(x,y)
                        time.sleep(3)
                        return True
                    except Exception as e:
                        print('matchip extension not found')
                except Exception as e:
                    print('matchip extension not found')
                    pyautogui.click(1589,227)
                    time.sleep(3)
                    pyautogui.click(1589,308)
                    
            except Exception as e:
                print('vroxy_logo extension not found')

        except Exception as e:
            print('Issue on geo location', e)


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
    sb1.set_page_load_timeout(18)


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
 
    #time.sleep(99999)
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
 
sitekey = 1
 
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
            #print(blacklistedIP)
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
            geo_location_changer()


            dochh5 = collection.find_one(quer2y)
            mainfaucet_key = dochh5["mainfaucet"]
            
            sitekey = mainfaucet_key  #$4
            print('MAINFAUCET IS ',sitekey)


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
                    response_messege('mainfaucet Loging')
                    if mainfaucet:
                        if sitekey == 1:
                            mainfaucet_window = handle_site(sb1, "https://satoshifaucet.io/links/currency/sol", "Shortlinks", "Home", 1, [], ip_required)
                        if sitekey == 2:
                            mainfaucet_window = handle_site(sb1, "https://coinpayz.xyz/links", "Shortlinks", "Home", 2, [], ip_required)
                        if sitekey == 3:
                            mainfaucet_window = handle_site(sb1, "https://helpfpcoin.site/link/ltc", "Help FP Coin - Link", "Home", 3, [], ip_required)
                        if sitekey == 4:
                            mainfaucet_window = handle_site(sb1, "https://bitbitz.cc/shortlinks", "Shortlink", "Home", 4, [], ip_required)
                        if sitekey == 5:
                            mainfaucet_window = handle_site(sb1, "https://feyorra.top/links", "Shortlinks", "Home", 5, [], ip_required)

                        if mainfaucet_window == 404:
                            raise Exception(" mainfaucet_window == 404")
                        print(f"mainfaucet window handle: {mainfaucet_window}")

                    

                else:
                    raise Exception("Ip changed")
 
 
 
                ip_address = get_ip(sb1)
                ip_required = ip_address
                if ip_required == ip_address:
                    response_messege('Started')
                    query = {"type": "main"}
                    update = {"$set": {"request": 'mainscript'}}
                    result = collection.update_one(query, update)
 
                    all_window_handles = [mainfaucet_window]
                    close_extra_windows(sb1, all_window_handles)
                    sb1.switch_to.window(mainfaucet_window)
                    print(f"Windows: mainfaucet: {mainfaucet_window},")
                    global reset_count 
                    global reset_count_isacc 
                    global previous_reset_count
                    global mainfaucet_limit_reached 
                    global feyorra_limit_reached 
                    #global sitekey
                    
                    mainfaucet_limit_reached = None
                    feyorra_limit_reached = None
 
                    reset_count = 0
                    reset_count_isacc = 0
                    previous_reset_count = 0
 
 
                    return mainfaucet_window,sitekey,  ip_address, ip_required
        except Exception as e:
                response_messege(f'Resetting Browser{e}')
                try:
                    subprocess.run(['pkill', '-f', 'chrome'], check=True)
                    print(f"All chrome processes killed successfully.{e}")
                except subprocess.CalledProcessError:
                    print(f"Failed to kill chrome processes or no processes found")
                time.sleep(10)
                sb1 = open_browsers()
                reset_count +=15
 
def debug_messages(messages):
    if debug_mode:
        print(messages)
 
mainfaucet_count = 0 
feyorra_count = 0
claimcoin_count = 0

 
mainfaucet_window, sitekey,  ip_address, ip_required = open_faucets()
start_time4 = 0
#time.sleep(9999)
print('Starting Loop')
 
def switch_to_earnow(now = 1, window_lists=[]):
    try:
        valid_links = ['cryptowidgets', 'earnow', 'mainfaucet', 'freeoseocheck',"shortano", "shortino","petsguide.net" "wiki-topia"]
        current_window = mainfaucet_window
        all_windows = sb1.window_handles
        for window in all_windows:
            if window not in window_lists:
                try:
                    sb1.switch_to.window(window)
                except Exception as e:
                    print('ggge',e)
                if 'Shortlink' in sb1.get_title():
                    print("mainfaucet is in the title")
                    continue
                else:
                    time.sleep(1)
                    current_url = sb1.execute_script("return window.location.href;")
                    if sb1.is_element_present("h1.title.ttu.text-center"):
                        step_text = sb1.get_text("h1.title.ttu.text-center")
                        if 'STEP' in step_text:
                            return sb1.current_window_handle
                    for link in valid_links:
                        if link in current_url:
                            return sb1.current_window_handle
    
        print("Waiting for button")
        
        close_extra_windows(sb1, window_lists)
        if 'Shortlink' in sb1.get_title():
            print("mainfaucet is in the title")
        else:
            if now == 1:
                sb1.switch_to_window(mainfaucet_window)
                sb1.uc_open("https://satoshifaucet.io/links/currency/sol")
            if now == 2:
                sb1.switch_to_window(mainfaucet_window)
                sb1.uc_open("https://coinpayz.xyz/links")
            if now == 3:
                sb1.switch_to_window(mainfaucet_window)
                sb1.uc_open("https://helpfpcoin.site/link/ltc")
            if now == 4:
                sb1.switch_to_window(mainfaucet_window)
                sb1.uc_open("https://bitbitz.cc/shortlinks")
            if now == 5:
                sb1.switch_to_window(mainfaucet_window)
                sb1.uc_open("https://feyorra.top/links")
        return None
    except Exception as e:
        print('sitch.',e)


def switch_mainfaucets(name):
    if name == 5:
        quer2y = {"type": "main"}
        dochh2 = collection.find_one(quer2y)
        layout = dochh2["withdraw_mail"]
        if "Layout1" in layout:
            layout = "Layout2"

        elif "Layout2" in layout:
            layout = "Layout1"

        print('switch themup')
        query = {"type": "main"}
        sample_document = {

            "mainfaucet": 1,
            "response": 'Changing Faucet...',
            "request": "ipfixer",
            "withdraw_mail": layout

        }
        update = {"$set": sample_document}
        result = collection.update_one(query, update)      
        if result.modified_count > 0:
            print(f"Updated {result.modified_count} document(s).")
        print("Clicked the claim button.")
        return True
    print('switch themup')
    query = {"type": "main"}
    sample_document = {

        "mainfaucet": name,
        "response": 'Changing Faucet...',
        "request": "ipfixer"

    }
    update = {"$set": sample_document}
    result = collection.update_one(query, update)      
    if result.modified_count > 0:
        print(f"Updated {result.modified_count} document(s).")
    print("Clicked the claim button.")
################################################################

def process_link_blocks(sb,ip_address):
    try:
        other = None
        # Find all "div.link-block" elements
        #link_blocks = sb.find_elements("div.common_card.sl_card")
        js_script = """
        return Array.from(document.querySelectorAll("div.common_card.sl_card"))
            .filter(block => ["Earnow", "Shortano", "Shortino"].some(keyword => block.innerText.includes(keyword)))
            .reduce((sum, block) => {
                const linkRmnElement = block.querySelector("div.pill.sec");
                if (linkRmnElement) {
                    let linkRmn = linkRmnElement.innerText.trim();
                    let count = parseInt(linkRmn.split('/')[0], 10);  // Extract first number
                    if (!isNaN(count)) {
                        sum += count;
                    }
                }
                return sum;
            }, 0);
        """
        full_values = sb.execute_script(js_script)
        print(f"Total Sum: {full_values}")

        js_script = """
        return Array.from(document.querySelectorAll("div.common_card.sl_card")).filter(block =>
            ["Earnow", "Shortano", "Shortino"].some(keyword => block.innerText.includes(keyword))
        );
        """
        link_blocks = sb.execute_script(js_script)



        for index, block in enumerate(link_blocks):
            print(f"Processing block {index + 1}:")
    
            # Scroll the block into view
            sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
            time.sleep(2)
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

                if len(link_name) >= 3:
                    other = True

                sri_lanka_tz = pytz.timezone('Asia/Colombo')
                utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                
    
                if "Earnow" in link_name:
                    link_rmn = int(link_rmn.split('/')[0])
                    query = {"type": "main"}
                    add_messages('pepelom', {now: full_values})
                    sample_document = {

                        "pepelom": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")
                    if link_rmn >= 1:
                        # Click the claim-button
                        button = block.find_element(By.CSS_SELECTOR,"button.btn_sl.link_bt")
                        actions = ActionChains(sb1)

                        actions.move_to_element(button).click().perform()  
                        #time.sleep(5) 

                        print("Clicked the claim button.")
                        cloudflare(sb1, login = True)
                        button = sb.find_element(By.CSS_SELECTOR,"button.btn.btn_sl.link_form_bt.mt-2")
                        #button.uc_click()
                        actions = ActionChains(sb1)
                        actions.move_to_element(button).click().perform()  
                        time.sleep(3) 
                        return True


                elif "Shortano" in link_name:
                    link_rmn = int(link_rmn.split('/')[0])
                    add_messages('pepelom', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "pepelom": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")

                    if link_rmn >= 1:
                        # Click the claim-button
                        button = block.find_element(By.CSS_SELECTOR,"button.btn_sl.link_bt")
                        actions = ActionChains(sb1)

                        actions.move_to_element(button).click().perform()  
                        #time.sleep(5) 

                        print("Clicked the claim button.")
                        cloudflare(sb1, login = True)
                        button = sb.find_element(By.CSS_SELECTOR,"button.btn.btn_sl.link_form_bt.mt-2")
                        #button.uc_click()
                        actions = ActionChains(sb1)
                        actions.move_to_element(button).click().perform()  
                        time.sleep(3) 
                        return True
                
                elif "Shortino" in link_name:
                    link_rmn = int(link_rmn.split('/')[0])
                    add_messages('pepelom', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "pepelom": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")
                    if link_rmn >= 1:
                        # Click the claim-button
                        button = block.find_element(By.CSS_SELECTOR,"button.btn_sl.link_bt")
                        actions = ActionChains(sb1)

                        actions.move_to_element(button).click().perform()  
                        #time.sleep(5) 

                        print("Clicked the claim button.")
                        cloudflare(sb1, login = True)
                        button = sb.find_element(By.CSS_SELECTOR,"button.btn.btn_sl.link_form_bt.mt-2")
                        #button.uc_click()
                        actions = ActionChains(sb1)
                        actions.move_to_element(button).click().perform()  
                        time.sleep(3) 
                        return True
                

            except Exception as e:
                print(f"An error occurred in block {index + 1}: {e}")
                pyautogui.click(600,500 ) 
                
            
    except Exception as e:
        print(f"An error occurred in block {index + 1}: {e}")
        pyautogui.click(600,500 )
    if other:
        print('END OF LINKS')
        switch_mainfaucets(4)



def process_link_blocks_coinpayz(sb,ip_address ):
    # Find all "div.link-block" elements
    link_blocks = sb.find_elements("div.flex.flex-col.shadow-lg.bg-paper-dark.rounded-lg.col-span-1")
    for index, block in enumerate(link_blocks):
        print(f"Processing block {index + 1}:")
 
        # Scroll the block into view
        sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
        time.sleep(2)
        try:
            # Get the link-name
            link_name_element = block.find_element(By.CSS_SELECTOR,"span.text-2xl.text-blue-300.font-semibold.pl-1")
            link_name = link_name_element.text
            print(f"Link Name: {link_name}")
 
            # Check if it's "Earnow"
 
            # Get the link-rmn
            link_rmn_element = block.find_element(By.CSS_SELECTOR,"span.flex.text-sm.items-center.justify-center.font-medium")
            link_rmn = link_rmn_element.text
            print(f"Link Remaining: {link_rmn}")
 
            if "Earnow" in link_name or "Shortano" in link_name or "Shortino" in link_name:
                # Click the claim-button
                button = block.find_element(By.CSS_SELECTOR,"span.px-1.text-info-lighter")
                #button.uc_click()
                actions = ActionChains(sb1)
                actions.move_to_element(button).click().perform()  
                time.sleep(5) 
                print("Clicked the claim button.")
                time.sleep(3) 
                return True
            
        except Exception as e:
            print(f"An error occurred in block {index + 1}: {e}")
            pyautogui.click(600,500 )


def process_link_blocks_helpfpcoin(sb):
    # Find all "div.link-block" elements
    try:
        link_blocks = sb.find_elements("div.link-div")
        for index, block in enumerate(link_blocks):
            print(f"Processing block {index + 1}:")
    
            # Scroll the block into view
            sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
            time.sleep(2)
            try:
                # Get the link-name
                link_name_element = block.find_element(By.CSS_SELECTOR,"span")
                link_name = link_name_element.text
                print(f"Link Name: {link_name}")
    
                # Check if it's "Earnow"
    
                # Get the link-rmn
                link_rmn_element = block.find_element(By.CSS_SELECTOR,"a.link-go i")
                link_rmn = link_rmn_element.text
                print(f"Link Remaining: {link_rmn}")
    
                if "Earnow" in link_name or "Shortano" in link_name or "Shortino" in link_name:
                    # Click the claim-button
                    button = block.find_element(By.CSS_SELECTOR,"a.link-go")
                    #button.uc_click()
                    actions = ActionChains(sb1)
                    actions.move_to_element(button).click().perform()  
                    time.sleep(5) 
                    pyautogui.click(946 ,345)
                    
                    return True
                
            except Exception as e:
                print(f"An error occurred in block {index + 1}: {e}")
                pyautogui.click(600,500 )
    except Exception as e:
        print('process link hafaucet',e)

def process_link_blocks_bitbitzz(sb,ip_address):
    # Find all "div.link-block" elements
    other = None
    try:
        js_script = """
        return Array.from(document.querySelectorAll("div.col-lg-6.mt-4"))
            .filter(block => ["Earnow", "Shortano", "Shortino"].some(keyword => block.innerText.includes(keyword)))
            .reduce((sum, block) => {
                const linkRmnElement = block.querySelector("span.float-end:not(.text-muted)");
                if (linkRmnElement) {
                    let linkRmn = linkRmnElement.innerText.trim();
                    let count = parseInt(linkRmn.split('/')[0], 10);  // Extract first number
                    if (!isNaN(count)) {
                        sum += count;
                    }
                }
                return sum;
            }, 0);
        """
        full_values = sb.execute_script(js_script)
        print(f"Total Sum: {full_values}")

        js_script = """
        return Array.from(document.querySelectorAll("div.col-lg-6.mt-4")).filter(block =>
            ["Earnow", "Shortano", "Shortino"].some(keyword => block.innerText.includes(keyword))
        );
        """
        #link_blocks = sb.execute_script(js_script)

        link_blocks = sb.find_elements("div.col-lg-6.mt-4")
        for index, block in enumerate(link_blocks):
            print(f"Processing block {index + 1}:")
    
            # Scroll the block into view
            sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
            time.sleep(2)
            try:
                # Get the link-name
                link_name_element = block.find_element(By.CSS_SELECTOR,"span.fw-bold")
                link_name = link_name_element.text
                print(f"Link Name: {link_name}")
    
                # Check if it's "Earnow"
    
                # Get the link-rmn
                link_clicks_element = block.find_element(By.XPATH, ".//span[contains(@class, 'float-end') and not(contains(@class, 'text-muted'))]")
                link_rmn = link_clicks_element.text
                print(f"Link Remaining: {link_rmn}")
    


                sri_lanka_tz = pytz.timezone('Asia/Colombo')
                utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')


                if "Earnow" in link_name:
                    link_rmn = int(link_rmn.strip().split()[0])
                    add_messages('feyorramack', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "feyorramack": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")
                    print("Clicked the claim button.")
                    if link_rmn >= 1:
                        button = block.find_element(By.CSS_SELECTOR,"a.text-decoration-none.shortlink")
                        #button.uc_click()
                        actions = ActionChains(sb1)
                        actions.move_to_element(button).click().perform()  
                        time.sleep(3) 
                        pyautogui.click(946 ,345)
                        return True
                
                elif "Shortano" in link_name:
                    link_rmn = int(link_rmn.strip().split()[0])
                    add_messages('feyorramack', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "feyorramack": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")

                    if link_rmn >= 1:
                        button = block.find_element(By.CSS_SELECTOR,"a.text-decoration-none.shortlink")
                        #button.uc_click()
                        actions = ActionChains(sb1)
                        actions.move_to_element(button).click().perform()  
                        time.sleep(3) 
                        pyautogui.click(946 ,345)
                        return True
                    

                elif "Shortino" in link_name:
                    link_rmn = int(link_rmn.strip().split()[0])
                    add_messages('feyorramack', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "feyorramack": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")

                    if link_rmn >= 1:
                        button = block.find_element(By.CSS_SELECTOR,"a.text-decoration-none.shortlink")
                        #button.uc_click()
                        actions = ActionChains(sb1)
                        actions.move_to_element(button).click().perform()  
                        time.sleep(3) 
                        pyautogui.click(946 ,345)
                        return True

                if len(link_name) >= 3:
                    other = True
                
                
            except Exception as e:
                print(f"An error occurred in block {index + 1}: {e}")
                pyautogui.click(600,500 )

        if other:
            print('END OF LINKS')
            switch_mainfaucets(5)
    
    except Exception as e:
        print('process link hafaucet',e)




def process_link_blocks_fey(sb,ip_address):
    # Find all "div.link-block" elements
    other = None
    try:
        # Find the CAPTCHA image
        if sb.is_element_visible("img#rscaptcha_img"):
            solve_rscaptcha(sb)
            time.sleep(3)
            pyautogui.click(940,484)
            time.sleep(5)
            return
    except Exception as e:
        print(f"No rscaptcha processing: {e}")

    try: 
        js_script = """
        return Array.from(document.querySelectorAll("div.col-lg-4.mb-3"))
            .filter(block => ["Earnow", "Shortano", "Shortino"].some(keyword => block.innerText.includes(keyword)))
            .reduce((sum, block) => {
                const linkRmnElement = block.querySelector("div.pill.sec");
                if (linkRmnElement) {
                    let linkRmn = linkRmnElement.innerText.trim();
                    let count = parseInt(linkRmn.split('/')[0], 10);  // Extract first number
                    if (!isNaN(count)) {
                        sum += count;
                    }
                }
                return sum;
            }, 0);
        """
        full_values = sb.execute_script(js_script)
        print(f"Total Sum: {full_values}")

        js_script = """
        return Array.from(document.querySelectorAll("div.col-lg-4.mb-3")).filter(block =>
            ["Earnow", "Shortano", "Shortino"].some(keyword => block.innerText.includes(keyword))
        );
        """
        link_blocks = sb.execute_script(js_script)
       
        for index, block in enumerate(link_blocks):
            try:
                print(f"Processing block {index + 1}:")
    
            # Scroll the block into view
            #sb.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", block)
                # Get the link-name
                link_name_element = block.find_element(By.CSS_SELECTOR,"div.linkname")
                link_name = link_name_element.text
                print(f"Link Name: {link_name}")
    
                # Check if it's "Earnow"
    
                # Get the link-rmn
                link_rmn_element = block.find_element(By.CSS_SELECTOR,"div.pill.sec")
                link_rmn = link_rmn_element.text
                print(f"Link Remaining: {link_rmn}")
                if len(link_name) >= 3:
                    other = True
                sri_lanka_tz = pytz.timezone('Asia/Colombo')
                utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                
    
                if "Earnow" in link_name:
                    link_rmn = int(link_rmn.split('/')[0])
                    add_messages('claimcoins', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "claimcoins": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")
                    if link_rmn >= 1:
                        # Click the claim-button
                        button = block.find_element(By.CSS_SELECTOR,"a.btn.sl_claim.w-100")
                        button.uc_click()
                        time.sleep(5) 
                        try:
                            # Find the CAPTCHA image
                            if sb.is_element_visible("img#rscaptcha_img"):
                                ggg =solve_rscaptcha(sb)
                                time.sleep(3)
                                if ggg:
                                    button = sb1.find_element(By.CSS_SELECTOR,"button.btn.sl_claim.w-100.link_form_bt")
                                    button.uc_click()
                                else:
                                    pyautogui.press('f5')
                                time.sleep(5)
                                #pyautogui.click(400,700)
                        except Exception as e:
                            print(f"No rscaptcha processing: {e}")
                            
                        print("Clicked the claim button.")
                        return True
                        


                elif "Shortano" in link_name:
                    link_rmn = int(link_rmn.split('/')[0])
                    add_messages('claimcoins', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "claimcoins": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")

                    if link_rmn >= 1:
                        # Click the claim-button
                        button = block.find_element(By.CSS_SELECTOR,"a.btn.sl_claim.w-100")
                        button.uc_click()
                        time.sleep(5) 
                        try:
                            # Find the CAPTCHA image
                            if sb.is_element_visible("img#rscaptcha_img"):
                                ggg =solve_rscaptcha(sb)
                                time.sleep(3)
                                if ggg:
                                    button = sb1.find_element(By.CSS_SELECTOR,"button.btn.sl_claim.w-100.link_form_bt")
                                    button.uc_click()
                                else:
                                    pyautogui.press('f5')
                                time.sleep(5)
                                #pyautogui.click(400,700)
                        except Exception as e:
                            print(f"No rscaptcha processing: {e}")
                            
                        print("Clicked the claim button.")
                        return True
                        
                
                elif "Shortino" in link_name:
                    link_rmn = int(link_rmn.split('/')[0])
                    add_messages('claimcoins', {now: full_values})
                    query = {"type": "main"}
                    sample_document = {

                        "claimcoins": full_values,
                        "Status": now,
                        "Ip": ip_address,
                        "response": 'Running'
                
                    }
                    update = {"$set": sample_document}
                    result = collection.update_one(query, update)      
                    if result.modified_count > 0:
                        print(f"Updated {result.modified_count} document(s).")
                    if link_rmn >= 1:
                        # Click the claim-button
                        button = block.find_element(By.CSS_SELECTOR,"a.btn.sl_claim.w-100")
                        button.uc_click()
                        time.sleep(5) 
                        try:
                            # Find the CAPTCHA image
                            if sb.is_element_visible("img#rscaptcha_img"):
                                ggg =solve_rscaptcha(sb)
                                time.sleep(3)
                                if ggg:
                                    button = sb1.find_element(By.CSS_SELECTOR,"button.btn.sl_claim.w-100.link_form_bt")
                                    button.uc_click()
                                else:
                                    pyautogui.press('f5')
                                time.sleep(5)
                                #pyautogui.click(400,700)
                        except Exception as e:
                            print(f"No rscaptcha processing: {e}")
                            
                        print("Clicked the claim button.")
                        return True
                        
                
            except Exception as e:
                print(f"An error occurred in block {index + 1}: {e}")
                pyautogui.click(600,500 )

                
    except Exception as e:
        print(f"An error occurred in block {index + 1}: {e}")
        pyautogui.click(600,500 )

    
    if other:
        print('END OF LINKS')
        switch_mainfaucets(5)


#withdows
def withdraw_bitbitzz(sb):
    try:
        sb.uc_open("https://bitbitz.cc/account")
        time.sleep(3)
        if sb.is_element_present("button.btn.btn-blue.btn-lg.w-100"):
            sb.uc_click("button.btn.btn-blue.btn-lg.w-100")
            time.sleep(3)
            if sb.is_element_present("input#withdrawlAddress"):
                address = sb.find_element(By.CSS_SELECTOR, "input#withdrawlAddress")
                address.send_keys(mainfaucet_email)
                time.sleep(2)
                faucet_button = sb.find_elements(By.CSS_SELECTOR, "div.card.h-100.gateway-card")
                for element in faucet_button:
                    element_txt = element.text
                    if 'FaucetPay' in element_txt:
                        element.click()
                        time.sleep(2)
                        currency_element = sb.find_element(By.CSS_SELECTOR, 'div.col.currency-col[data-currency-id="8"]')
                        currency_element.click()
                        break
                time.sleep(2)
                sb.uc_click("button#makeWithdrawal[type='submit']")
                time.sleep(3)
                response_messege(f'withdraw_bitbitzz FaucetPay Withdrawed')
                        #response_messege('Started')
                query = {"type": "main"}
                update = {"$set": {"request": 'ipfixer'}}
                result = collection.update_one(query, update)
        pass

    except Exception as e:
        print('withdraw_bitbitzz',e)
#withdows
def withdraw_feyorra(sb):
    try:
        sb.uc_open("https://feyorra.top/withdraw")
        time.sleep(3)
        if sb.is_element_present("input#wallet[type='submit']"):
            address = sb.find_element(By.CSS_SELECTOR, "input#wallet[type='submit']")
            address.send_keys(mainfaucet_email)
            sb.uc_click("button[type='submit']")
            time.sleep(3)
            response_messege(f'withdraw_feyorra FaucetPay Withdrawed')
                    #response_messege('Started')
            query = {"type": "main"}
            update = {"$set": {"request": 'ipfixer'}}
            result = collection.update_one(query, update)
        pass

    except Exception as e:
        print('withdraw_bitbitzz',e)

#time.sleep(9990)
hard_reset_count = 1
feyorra_window_shortlink = None
earnow_window = None
sholinks_done = 1
while True:
    try:
        mainscript = control_panel()
        
        print('control_panel', mainscript)
        if mainscript == 1:  


            if reset_count > 15:
                sholinks_done = 1
                reset_count = 1
                title =sb1.get_title()
                if 'Just' in title:
                    debug_messages(f'Just.. Found on mainfaucet')
                    cloudflare(sb1, login = False)
                    debug_messages(f'Just Fixed mainfaucet')

                time.sleep(3)
                try:
                    subprocess.run(['pkill', '-f', 'chrome'], check=True)
                    print(f"All chrome processes killed successfully")
                except subprocess.CalledProcessError:
                    print(f"Failed to kill chrome processes or no processes found.")
                time.sleep(3)
                sb1 = Driver(uc=True, headed=True, undetectable=True, undetected=True, user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path, page_load_strategy='eager')#, proxy=browser_proxy )
                sb1.maximize_window()
                sb1.uc_open("chrome://extensions/")
                current_window = sb1.current_window_handle
                mainfaucet_window = sb1.current_window_handle
                if sitekey == 1:
                    sb1.uc_open("https://satoshifaucet.io/links/currency/sol")
                if sitekey == 2:
                    sb1.uc_open("https://coinpayz.xyz/links")
                if sitekey == 3:
                    sb1.uc_open("https://helpfpcoin.site/link/ltc")
                if sitekey == 4:
                    sb1.uc_open("https://bitbitz.cc/shortlinks")
                if sitekey == 5:
                    sb1.uc_open("https://feyorra.top/links")
                earnow_window = None

            if hard_reset_count > 15:
                try:
                    subprocess.run(['pkill', '-f', 'chrome'], check=True)
                    print(f"All chrome processes killed successfully")
                except subprocess.CalledProcessError:
                    print(f"Failed to kill chrome processes or no processes found.")
                time.sleep(3)
                sb1 = open_browsers()
                
                mainfaucet_window, sitekey,  ip_address, ip_required = open_faucets()


                mainfaucet_window = sb1.current_window_handle
                earnow_window = None
                hard_reset_count = 1


            ip_address = get_ip(sb1)
            debug_messages(f'Ip address Found:{ip_address}')


            if ip_address == ip_required:
                if mainfaucet and mainfaucet_window:
                    try:
                        debug_messages(f'Switching Pages to mainfaucet')
                        sb1.switch_to.window(mainfaucet_window)
                        debug_messages(f'Getting Pages Titile:mainfaucet')
                        title =sb1.get_title()
                        if sb1.is_element_present("h1.title.ttu.text-center"):
                            step_text = sb1.get_text("h1.title.ttu.text-center")
                            if 'STEP' in step_text:
                                title = 'Shortlinks'
                        if 'Shortlinks' in title or 'Link' in title:
                            #process_link_blocks(sb1)
                            if sitekey == 1:
                                process_link_blocks(sb1,ip_address)
                                earnow_window = switch_to_earnow(2,[mainfaucet_window])

                            elif sitekey == 2:
                                process_link_blocks_coinpayz(sb1,ip_address)
                                earnow_window = switch_to_earnow(2,[mainfaucet_window])

                            elif sitekey == 3:
                                process_link_blocks_helpfpcoin(sb1,ip_address)
                                earnow_window = switch_to_earnow(3,[])

                            elif sitekey == 4:
                                process_link_blocks_bitbitzz(sb1,ip_address)
                                earnow_window = switch_to_earnow(4,[mainfaucet_window])

                            elif sitekey == 5:
                                process_link_blocks_fey(sb1,ip_address)
                                earnow_window = switch_to_earnow(5,[mainfaucet_window])
                            
                            if earnow_window:
                                close_extra_windows(sb1, [earnow_window])
                                result = earnow_online(earnow_window, ip_required)
                                if result == 404:
                                    continue 

                                sholinks_done += 1
                                if sholinks_done > 4:
                                    sholinks_done = 1
                                    reset_count = 20
                                time.sleep(2)
                                mainfaucet_window = sb1.current_window_handle
                                #mainfaucet_window = earnow_window
                                sb1.switch_to.window(mainfaucet_window)
                                title =sb1.get_title()
                                if 'Just' in title:
                                    #debug_messages(f'Just.. Found on mainfaucet')
                                    cloudflare(sb1, login = False)
                                    time.sleep(2)
                                pyautogui.press('f5')
                                time.sleep(2)
                                earnow_window = None
                                feyorra_window_shortlink = None
                                print('Done.....')
                            
 
                        elif 'Home' in title or 'Login' in title or "SatoshiFaucet | Satoshi faucet" in title:
                            debug_messages(f'LOGIN.. Found on mainfaucet')
                            response_messege('LOGIN.. Found on mainfaucet')
                            hard_reset_count +=5
                        else:
                            debug_messages(f'mainfaucet not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                            if sitekey == 1:
                                sb1.uc_open("https://satoshifaucet.io/links/currency/sol")
                            elif sitekey == 2:
                                sb1.uc_open("https://coinpayz.xyz/links")
                            elif sitekey == 3:
                                sb1.uc_open("https://helpfpcoin.site/link/ltc")
                            elif sitekey == 4:
                                sb1.uc_open("https://bitbitz.cc/shortlinks")
                            elif sitekey == 5:
                                sb1.uc_open("https://feyorra.top/links")

                        title =sb1.get_title()
                        if 'Just' in title:
                            debug_messages(f'Just.. Found on mainfaucet')
                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed mainfaucet')
                        if 'bitBitz' in title:
                            if sb1.is_element_visible('li.nav-item a.nav-link[href="/login"]'):
                                hard_reset_count +=5

                    except Exception as e:
                        print(f'ggg:{e}')
                        response_messege(f'ERR:{e}')
                        hard_reset_count +=5

                else:
                    print('no mainfaucet',ip_required)
                    hard_reset_count +=5 

                    
            else:
                print('IP Changed',ip_required)
                hard_reset_count +=5

        if mainscript == 2:
            mainfaucet_window, sitekey,  ip_address, ip_required = open_faucets()
            reset_count = 0



        if mainscript == 5:
            for i in range(1,6):
                time.sleep(1)
                print('Pause...')

        if mainscript == 4:
            withdraw_bitbitzz(sb1) 

        if mainscript == 6:
            withdraw_feyorra(sb1) 
        if mainscript == 7:
            #withdraw_faucet(sb1, 3) 
            pass


    except Exception as e:
        print(f'ERR1:{e}')
        response_messege(f'ERR3:{e}')
        hard_reset_count +=5

        
 


 
