
print('Version 9.7.4')
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

query = {"type": "main"}
# Example usage
pyautogui.moveTo(100, 100)
pyautogui.click(100, 200, duration=0.5)
# Initialize the argument parser
parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument('--farm', type=int, help="Farm")
parser.add_argument('--fresh', type=int, help="Fresh")
args = parser.parse_args()
farm_id = args.farm
fresh = args.fresh


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

Farm_list = [1, 2, 3, 4, 5]

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

    collection = db[f'Farm{farm_id}']
    quer2y = {"type": "main"}
    dochh2 = collection.find_one(quer2y)
    layout = dochh2["withdraw_mail"]
    print(f'Farm ID:{farm_id} | Layout: {layout}')

    if farm_id <= 5:
        mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
        CSB1_farms =Farm_list
    else:

        mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie.json"
        CSB1_farms =Farm_list



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
            earnpp_email = 'metroboom9106@gmail.com'
            earnpp_pass = 'metroboom9106'
            feyorra_email = 'metroboom9106@gmail.com'
            feyorra_pass = 'metroboom9106'
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
            earnpp_email = 'markshlld51@gmail.com'
            earnpp_pass = 'markshlld51'
            feyorra_email = 'markshlld51@gmail.com'
            feyorra_pass = 'markshlld51'

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
            earnpp_email = 'danielhenesy3@gmail.com'
            earnpp_pass = 'danielhenesy3'
            feyorra_email = 'danielhenesy3@gmail.com'
            feyorra_pass = 'danielhenesy3' 
            
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
            CSB1_farms = Farm_list
            earnpp_email = 'berendkalpana55@gmail.com'
            earnpp_pass = 'berendkalpana55'
            feyorra_email = 'berendkalpana55@gmail.com'
            feyorra_pass = 'berendkalpana55'
        elif '2' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list
            earnpp_email = 'yvonne6363@gmail.com'
            earnpp_pass = 'yvonne6363'
            feyorra_email = 'yvonne6363@gmail.com'
            feyorra_pass = 'yvonne6363'


        elif '3' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list
            earnpp_email = 'sheldnkumr86@gmail.com'
            earnpp_pass = 'sheldnkumr86'
            feyorra_email = 'sheldnkumr86@gmail.com'
            feyorra_pass = 'sheldnkumr86'

        elif '4' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list
            earnpp_email = 'andrewperera8@gmail.com'
            earnpp_pass = 'andrewperera8'
            feyorra_email = 'andrewperera8@gmail.com'
            feyorra_pass = 'andrewperera8'
        elif '5' in layout:
            server_name1 = 'canada' #'georgia'# 
            CSB1_farms = Farm_list
            earnpp_email = 'howard998@gmail.com'
            earnpp_pass = 'howard998'
            feyorra_email = 'howard998@gmail.com'
            feyorra_pass = 'howard998' 
            
        elif '6' in layout:
            server_name1 = 'canada'
            CSB1_farms = Farm_list
            earnpp_email = 'amberodum7@gmail.com'
            earnpp_pass = 'amberodum7'
            feyorra_email = 'amberodum7@gmail.com'
            feyorra_pass = 'amberodum7'


        else:
            print('Layout issue', layout)

    elif farm_id == 5:

        if '1' in layout:
            server_name1 = 'germany'
            CSB1_farms =Farm_list
            earnpp_email = 'ernestost5@gmail.com' 
            earnpp_pass = 'ernestost5'
            feyorra_email = 'ernestost5@gmail.com'
            feyorra_pass = 'ernestost5'

        elif '2' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms =Farm_list
            earnpp_email = 'rondolfapa9@gmail.com'
            earnpp_pass = 'rondolfapa9'
            feyorra_email = 'rondolfapa9@gmail.com'
            feyorra_pass = 'rondolfapa9'
        elif '3' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms = Farm_list
            earnpp_email = 'kevincharl3@gmail.com'
            earnpp_pass = 'kevincharl3'
            feyorra_email = 'kevincharl3@gmail.com'
            feyorra_pass = 'kevincharl3'

        elif '4' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms = Farm_list
            earnpp_email = 'kendleo4@gmail.com'
            earnpp_pass = 'kendleo4'
            feyorra_email = 'kendleo4@gmail.com'
            feyorra_pass = 'kendleo4'

        elif '5' in layout:
            server_name1 = 'germany' #'chile'
            CSB1_farms =Farm_list
            earnpp_email = 'willsmile31@gmail.com'
            earnpp_pass = 'willsmile31'
            feyorra_email = 'willsmile31@gmail.com'
            feyorra_pass = 'willsmile31' 
            
        elif '6' in layout:
            server_name1 = 'germany'
            CSB1_farms = Farm_list
            earnpp_email = 'adaavery5@gmail.com'
            earnpp_pass = 'adaavery5'
            feyorra_email = 'adaavery5@gmail.com'
            feyorra_pass = 'adaavery5'

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

chrome_binary_path = '/opt/google/chrome/google-chrome'
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

def insert_data(ip, amount1, amount2, amount3, amount4,emailg):
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
    for i in range(8):
        try:
            original_window = driver.current_window_handle
            driver.open_new_window()
            try:
                #driver.switch_to.newest_window()
                #driver.get('https://api.ipify.org/')
                driver.get('https://checkip.amazonaws.com/')
                
                ip_address = driver.get_text('body')
                print('IP =', ip_address)
                driver.close()
                driver.connect()
                driver.switch_to.window(original_window)
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
                val = get_proxycheck_inbrowser(driver, ip, server_name)
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

def mysterium_vpn_connect(server_name, driver):
    try:
        query = {"type": "main"}
        for i in CSB1_farms:
            collection_csb = db[f'Farm{i}']
            sample_document = {
                "response": f'Changed IP🔴: Farm {farm_id} |fix_ip',
                "request": 'ipfixer'
                
            }
            update = {"$set": sample_document}
            result = collection_csb.update_one(query, update)
            print('Update Farm fix_ip', i)
    except Exception as e:
        print(e)

    mysterium_reinstaller()
    sweet_enable()
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
        ip_address = extract_valid_ipv4(ip_address)
        if ip_address:

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
                    blacklistedIP = other_blacklists + blacklistedIP 
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
                ip_address = extract_valid_ipv4(ip_address)
                if ip_address:
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
        time.sleep(10)
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
    ready_count = 0
    query = {"type": "main"}
    update = {"$set": {"response": 'Fixing...🟠'}}
    result = collection.update_one(query, update)
    for i in CSB1_farms:
        collection_csb = db[f'Farm{i}']
        
        update = {"$set": {"request": 'ipfixer'}}
        result = collection_csb.update_one(query, update)
        print('Update Farm', i)

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
                            if gg2344 > 6:
                                return
                                reff_farm = farm_id
                                if farm_id == 1:
                                    
                                    #clear_browser_cache_history(sb1)
                                    #sb1.uc_open("chrome://extensions/")
                                    return
                                elif farm_id == 2:
                                    reff_farm = 1
                                elif farm_id == 3:
                                    reff_farm = 2
                                elif farm_id == 4:
                                    reff_farm = 3
                                elif farm_id == 5:
                                    reff_farm = 4

                                collection_csb = db[f'Farm{reff_farm}']
                                query = {"type": "main"}
                                doc = collection_csb.find_one(query)
                                #res = doc["response"]
                                req = doc["request"]
                                if req == 'mainscript': #and 'Loging' not in res:
                                    #clear_browser_cache_history(sb1)
                                    #sb1.uc_open("chrome://extensions/")
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
model = tf.keras.models.load_model('captcha_model_v12.keras')

category_classes_list =  ['award', 'bell', 'broom', 'bug', 'bullhorn', 'camera', 'cannabis', 'capsules', 'car-crash', 'car', 'carrot', 'cat', 'certificate', 'charging-station', 'chart-line', 'check', 'chess-knight', 'times-circle', 'history', 'couch', 'crow', 'democrat', 'dice', 'dog', 'dove', 'dragon', 'tint', 'envelope', 'surprise', 'tired', 'feather-alt', 'cog', 'gem', 'gift', 'gopuram', 'graduation-cap', 'guitar', 'hammer', 'hat-wizard', 'heart', 'helicopter', 'home', 'image', 'key', 'kiwi-bird', 'laptop', 'leaf', 'lightbulb', 'link', 'lock', 'marker', 'microchip', 'microphone', 'money-bill-wave', 'moon', 'coffee', 'coffee', 'music', 'oil-can', 'paw', 'piggy-bank', 'pizza-slice', 'plug', 'puzzle-piece', 'republican', 'ribbon', 'robot', 'rocket', 'sync-alt', 'satellite', 'cut', 'tools', 'ship', 'space-shuttle', 'signal', 'sim-card', 'sitemap', 'skull-crossbones', 'smoking', 'snowman', 'spa', 'spider', 'star-of-david', 'star', 'sun', 'syringe', 'tablets', 'tag', 'thermometer-half', 'thermometer', 'thumbs-up', 'thumbtack', 'tooth', 'tractor', 'traffic-light', 'subway', 'tree', 'truck-monster', 'truck-pickup', 'umbrella', 'user', 'utensil-spoon', 'shuttle-van', 'vector-square', 'vial', 'vials', 'video', 'volleyball-ball', 'times', 'yin-yang']
def predict_image(image_path, category_options):
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
    y_center += offset_y + 15

    # Move the mouse to the exact center and click
    pyautogui.moveTo(x_center - 3, y_center, duration=duration)
    pyautogui.click()

captcha_basetring = ''
#V3
#Steps to solve the captcha:
#1. Get the captcha 
def solve_icon_captcha(sb1):
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
    
                            if 'Login' in page_title or 'Faucet' in page_title:
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



def login_to_faucet(url, driver, email, password, captcha_image, restrict_pages, submit_button, ip_required):

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
                    ip_address = get_ip(driver)
                    if ip_required != ip_address:
                        print("IP address mismatch, login")
                        return False
                    all_windows = driver.window_handles
                    for window in all_windows:
                        if window not in restrict_pages:
                            driver.switch_to.window(window)
                    try:
                        x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{captcha_image}.png", confidence=0.85)
                        if x and y: 
                            if 'Feyorra' in current_title:

                                mouse_moveclick(cropped_path="/root/Desktop/MFV6/images/feyorra_loginbt.png")
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
    





earnpp_window = None
claimcoin_window = None
feyorra_window = None
baymack_window = None
feyorratop_window = None
earntrump_window = None
earnbonk_window = None

def close_extra_windows(driver, keep_window_handles):
    gg = False
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window not in keep_window_handles:
            driver.switch_to.window(window)
            driver.close()
            driver.connect()
            gg = True
    driver.switch_to.window(current_window)
    return gg

def handle_captcha_and_cloudflare(driver):
    cloudflare(driver, login = False)

def handle_site(driver, url, expected_title, not_expected_title , function, window_list ,ip_required, ip_check = False):
    driver.uc_open(url)
    ready = False
    while not ready:
        time.sleep(1)
        pyautogui.moveTo(100, 200)
        pyautogui.moveTo(200, 400)
        ip_address = get_ip(driver)
        if ip_check:
            if ip_required != ip_address:
                return 404
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

        all_windows = driver.window_handles
        for window in all_windows:
            if window not in window_list:
                driver.switch_to.window(window)
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
                login_to_faucet('https://earn-pepe.com/login', sb1, earnpp_email, earnpp_pass, 'cloudflare_success', window_list, 'button#ClaimBtn', ip_required = ip_required)
                #login_to_faucet('https://earn-pepe.com/login', sb1, earnpp_email, earnpp_pass, 'rscaptcha', window_list, 'button#loginBtn')
            elif function == 2:
                login_to_faucet('https://feyorra.site/login', sb1, feyorra_email, feyorra_pass, 'cloudflare_success', window_list, 'button#ClaimBtn',ip_required = ip_required)
            elif function == 3:
                login_to_faucet('https://earn-trump.com/login', sb1, earnpp_email, earnpp_pass,  'cloudflare_success', window_list, 'button#ClaimBtn', ip_required = ip_required) #'not_a_robot'
            elif function == 4:
                login_to_faucet('https://earn-bonk.com/login', sb1, feyorra_email, feyorra_pass,  'cloudflare_success', window_list, 'button#ClaimBtn', ip_required = ip_required)  #'not_a_robot'


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
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/extension_icon.png", region=(1234, 30, 683, 522), confidence=0.9)
        pyautogui.click(x, y)
        print("extension_icon Button Found")

        for i in range(1,50):
            time.sleep(1)
            pyautogui.moveTo(1700, 30)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/pin.png", region=(1234, 30, 683, 522), confidence=0.9)
                pyautogui.click(x, y)
                pyautogui.moveTo(1700, 30)
                print("pin Button Found")
                time.sleep(1)    
            except pyautogui.ImageNotFoundException:
                print("No pin Button.")
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/all_pinned.png", region=(1234, 30, 683, 522), confidence=0.99)
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
        all_windows = driver.window_handles
        for window in all_windows:
            if window != current_window:
                driver.switch_to.window(window)
                driver.close()  # Close the tab
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
sb1 = None
def are_extensions_exist():
    for i in range(3):
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cookie_icon.png", region=(1225, 33, 755, 400), confidence=0.9)
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
    for x in range(5):
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/sweet_dis_icon.png",  region=(1625, 43, 700, 300), confidence=0.98)
            pyautogui.click(x, y)
            for i in range(5):
                time.sleep(3)
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/sweet_connect.png", confidence=0.8)
                    pyautogui.click(x, y)
                    time.sleep(5)
                    #pyautogui.click(300, 300)
                    time.sleep(8)
                except pyautogui.ImageNotFoundException:
                    print("Waiting for Sweet to pop")
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/sweet_sg2.png", confidence=0.8)
                    pyautogui.click(x, y)
                    time.sleep(5)
                    pyautogui.click(300, 300)
                    time.sleep(5)
                    return
                    
                except pyautogui.ImageNotFoundException:
                    print("Waiting for Sweet to pop")
        except pyautogui.ImageNotFoundException:
            print("No icon_image_loaded Human.")
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/sg_sweet_icon.png",  region=(1625, 43, 700, 300), confidence=0.99)
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

def mysterium_reinstaller():
    response_messege('Changed IP🔴 :Mys Reinstaller')
    global sb1
    global chrome_user_data_dir
    global layout
    global browser_proxy
    for i in range(4):
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_connected.png", region=(1625, 43, 400, 300), confidence=0.99)
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




def mysterium_reinstaller_old():
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
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/pepe_limit.png", confidence=0.95)
            print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Earn-Trump12' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/trump_limit.png", confidence=0.95)
            print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Feyorra' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/feyorra_limit.png", confidence=0.95)
            print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Earn-Bonk' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/bonk_limit.png", confidence=0.95)
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
    if 'Earn-pepe1' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/pepe_limit.png", confidence=0.95)
            #print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Earn-Trump12' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/trump_limit.png", confidence=0.95)
            #print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Feyorra' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/feyorra_understand.png", confidence=0.9)
            pyautogui.click(x, y, duration = 0.2)
            #print('Limit Reached')
            return True
        except Exception as e:    
            #print("No icon_image_loaded Human.")
            return False
    elif 'Earn-Bonk' in title:
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/bonk_understand.png", confidence=0.9)
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
def clear_browser_cache_history(driver):
    try:
        global sb1
        response_messege(f'Clearing Cahe')
        driver.open("chrome://settings/clearBrowserData")
        time.sleep(8)
        pyautogui.click(869, 468)
        time.sleep(2)
        pyautogui.click(869, 585)
        time.sleep(2)
        pyautogui.click(1161, 797)
        time.sleep(5)
        try:
            sb1.quit()
            time.sleep(1)
        except Exception as e:
            print(f"sb1.quit() failed: {e}")

        # Fallback kill
        for proc_name in ['chrome', 'chromium']:
            try:
                subprocess.run(['pkill', '-f', proc_name], check=False, stderr=subprocess.DEVNULL)
                print(f"All {proc_name} processes killed (if any).")
            except Exception as e:
                print(f"Failed to kill {proc_name} processes: {e}")
        time.sleep(2)
        sb1 = open_browsers()
    except Exception as e:
        print(f"Error clearing browser cache: {e}")

fresh_start_faucet = True
login_faucet_detect = True
def open_browsers():
    global sb1
    global chrome_user_data_dir
    global layout
    global browser_proxy
    pyautogui.moveTo(100, 100)
    pyautogui.click(100, 200, duration=0.5)
    browser_proxy  =get_browser_proxy()

    quer2y = {"type": "main"}
    dochh2 = collection.find_one(quer2y)
    layout = dochh2["withdraw_mail"]
    print(f'Farm ID:{farm_id} | Layout: {layout}')
    chrome_user_data_dir = f'/root/.config/google-chrome/{browser_proxy}{layout}'
    sb1 = Driver(
        uc=True,
        headed=True,
        undetectable=True,
        undetected= True,
        no_sandbox=True,  # --no-sandbox
        disable_gpu=True,  # --disable-gpu
        user_data_dir=chrome_user_data_dir,
        binary_location=chrome_binary_path,
        page_load_strategy="eager",
        extension_dir="/root/Desktop/MFV6/mysterium,/root/Desktop/MFV6/fingerprint,/root/Desktop/MFV6/cookie,/root/Desktop/MFV6/mfhelper,/root/Desktop/MFV6/sweet",
        chromium_arg=[
            "--disable-dev-shm-usage",
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
    time.sleep(8)
    #sb1.execute_script("window.scrollTo(0, 300);")
    print(sb1.get_title())
    gggv = are_extensions_exist()
    get_mails_passowrds(farm_id)
    if gggv:
        if fresh >= 4:
            pass
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
            pyautogui.moveTo(100, 200)
            pyautogui.moveTo(200, 400)
            global faucetlayout
            global fresh_start_faucet
            global login_faucet_detect
            quer2y = {"type": "main"}
            dochh2 = collection.find_one(quer2y)
            layout2 = dochh2["withdraw_mail"]
            print(f'Farm ID:{farm_id} | Layout: {layout2}')
            browser_proxy2  =get_browser_proxy()
            chrome_user_data_dir2 = f'/root/.config/google-chrome/{browser_proxy2}{layout2}'
            if chrome_user_data_dir == chrome_user_data_dir2 and layout == layout2 and browser_proxy2 == browser_proxy:
                response_messege(f'Same Browser | L {layout2}')
            else:
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
                        print(f"All {proc_name} processes killed (if any).")
                    except Exception as e:
                        print(f"Failed to kill {proc_name} processes: {e}")
                time.sleep(6)
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
                        if req == 'ipfixer':
                            if 'Ready' in res:
                                print('IP is ready')

                            else:
                                ipfixer()
                                ip_required = fix_ip(sb1, server_name1)
                                ip_address = get_ip(sb1)

            else:
                ipfixer()
                ip_required = fix_ip(sb1, server_name1)
                ip_address = get_ip(sb1)

            ip_address = get_ip(sb1)
            pyautogui.moveTo(100, 200)
            pyautogui.moveTo(200, 400)
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

                ipscore = get_ipscore(ip_address)
                proxycheck = get_proxycheck(sb1, ip_address, server_name= server_name1)
                if ipscore and proxycheck == 200:
                    print(f'Good IP found: {ip_address}')
                    update_ip(ip_address, config_path="mfhelper/config.json")
                else:
                    raise Exception(" earnpp_window == 404")
                fresh_start_faucet = True
                pyautogui.moveTo(100, 200)
                pyautogui.moveTo(200, 400)
                if fresh_start_faucet == True:
                    ip_address = get_ip(sb1)
                    if ip_required == ip_address:
                        response_messege('EarnPP Loging Fresh')
                        if earnpp:
                            if faucetlayout == 1:
                                earnpp_window = handle_site(sb1, "https://earn-pepe.com/member/faucet","Faucet | Earn-pepe" , "Home | Earn-pepe", 1, [], ip_required, ip_check = True)
                                if earnpp_window == 404:
                                    raise Exception(" earnpp_window == 404")
                                print(f"EarnPP window handle: {earnpp_window}")

                        else:
                            earnpp_window = None
                    else:
                        raise Exception("Ip changed")

                    ip_address = get_ip(sb1)
                    if ip_required == ip_address:
                        response_messege('Feyorra Loging Fresh')
                        if feyorra:
                            #sb1.open_new_window()
                            if faucetlayout == 1:
                                feyorra_window = handle_site(sb1, "https://feyorra.site/member/faucet", "Faucet | Feyorra" , "Best - Meme Coins Faucet", 2, [], ip_required, ip_check = True)
                                if feyorra_window == 404:
                                    raise Exception(" feyorra_window == 404")
                                print(f"Feyorra window handle: {feyorra_window}")
                                time.sleep(2)
                                Click_Understand()



                        else:
                            feyorra_window = None
                    else:
                        raise Exception("Ip changed")
                    
                    ip_address = get_ip(sb1)
                    if ip_required == ip_address:
                        response_messege('trump Loging Fresh')
                        if earntrump:
                            #sb1.open_new_window()
                            if faucetlayout == 1:
                                earntrump_window = handle_site(sb1, "https://earn-trump.com/member/faucet","Faucet | Earn-Trump" , "Free $Trump Coin Faucet | Earn $Trump Crypto Instantly", 3, [], ip_required, ip_check = True)
                                if earntrump_window == 404:
                                    raise Exception(" earntrump_window == 404")
                                print(f"earntrump window handle: {earntrump_window}")


                        else:
                            earntrump_window = None
                    else:
                        raise Exception("Ip changed")
                    
                    ip_address = get_ip(sb1)
                    if ip_required == ip_address:
                        response_messege('earnbonk Loging Fresh')
                        if earnbonk:
                            #sb1.open_new_window()
                            if faucetlayout == 1:
                                earnbonk_window = handle_site(sb1, "https://earn-bonk.com/member/faucet", "Faucet | Earn-Bonk" , "Earn Bonk", 4, [], ip_required,ip_check =  True)
                                if earnbonk_window == 404:
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
                
                
                ip_address = get_ip(sb1)
                if ip_required == ip_address:
                    response_messege('Started')
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

                    return earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required
        except Exception as e:
                response_messege(f'Resetting Browser{e}')
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
previous_script_seconds_only = 0
while True:
    try:
        mainscript = control_panel()
        print('control_panel', mainscript)
        if mainscript == 1:
            
            debug_messages(f'Ip address Found:{ip_address}')
            cc_faucet = None
            script_elapsed_time = time.time() - Script_Started
            script_seconds_only = int(script_elapsed_time)
            debug_messages(f'script_elapsed_time Seconds:{script_seconds_only}')
            if script_seconds_only > 1200:
                Script_Started = time.time()
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

                earnpp_window,feyorra_window,earntrump_window,earnbonk_window,  ip_address, ip_required = open_faucets()
                previous_script_seconds_only = script_seconds_only
                Script_Started = time.time()

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
            if reset_count >= 20:
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
                previous_script_seconds_only = script_seconds_only

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
                            reset_count +=7
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
                        pyautogui.press('enter')
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
                            reset_count +=7
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
                        pyautogui.press('enter')
                        title =sb1.get_title()

                        if 'Faucet | Earn-Trump' in title:
                            debug_messages(f'Solving Icon Captcha on Earn-Trump')

                            val = get_coins(sb1, 1)
                            if val:
                                earntrump_coins = val
                            gg = solve_icon_captcha(sb1)
                            if gg:
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
                            reset_count +=5
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
                        pyautogui.press('enter')
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
                            reset_count +=5
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
                if seconds_only > 20:
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
                    print(f'EarnPP:{earnpp_coins} | Feyorra:{feyorra_coins} | Trump:{earntrump_coins}|BONK:{earnbonk_coins} ')
                    if earnpp_coins and feyorra_coins and earnbonk_coins and earntrump_coins: 
                        start_time3 = time.time()
                        emailgg = f'{earnpp_email} <br>country: {server_name1} <br>Current Layout:{layout} <br>Farm:{farm_id} <br>Pre-Session Reset:{previous_script_seconds_only} <br>Session Reset:{script_seconds_only}'
                        insert_data(ip_address, earnpp_coins, feyorra_coins, earntrump_coins, earnbonk_coins, emailgg)
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
            previous_script_seconds_only = script_seconds_only
        reset_count +=2
     
