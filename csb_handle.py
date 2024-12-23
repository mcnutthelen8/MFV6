from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from urllib.parse import urlparse, parse_qs
import time
import re
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import requests
from requests.exceptions import RequestException
from seleniumbase import SB
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
import pyperclip as clipboard
import pytz
import datetime
from datetime import datetime

#csb_handle.py --fresh 1 --vms 1 --layout 1 --csbid andyrogers468f23h
sri_lanka_tz = pytz.timezone('Asia/Colombo')
utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)  
sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser(description="Process some arguments.")
parser.add_argument('--fresh', type=int, help="Farm")
parser.add_argument('--vms', type=int, help="Fresh")
parser.add_argument('--layout', type=int, help="Fresh")

parser.add_argument('--csbid', type=str, help="Fresh")
args = parser.parse_args()
freshar = args.fresh
vmsar = args.vms
layoutar = args.layout
csbid = args.csbid

Layout = layoutar# 1

fresh = True
fresh_vms =True 
vm_count = 1 + 5
CSB_id = csbid
CSB_Script = f'CSB{Layout}'
waiting_sec = 3700

if freshar == 1:
    fresh = True
else:
    fresh = False

if vmsar == 1:
    fresh_vms = True
else:
    fresh_vms = False

#https://www.skylom.com/willem3
#https://www.zaptaps.com/willem
command_1 = '0'
command_2 = '0'
command_3 = '0'
command_4 = '0'
command_5 = '0'

if Layout == 1:
    command_1 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 1 --fresh 3'
    command_2 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 2 --fresh 3'
    command_3 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 3 --fresh 3'
    command_4 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 4 --fresh 3'
    command_5 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 5 --fresh 3'


elif Layout == 2:
    command_1 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 6 --fresh 3'
    command_2 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 7 --fresh 3'
    command_3 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 8 --fresh 3'
    command_4 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 9 --fresh 3'
    command_5 = 'git clone https://github.com/mcnutthelen8/MFV6.git && cd MFV6 && chmod +x install_dependencies.sh && ./install_dependencies.sh && python3 main.py --farm 10 --fresh 3'



chrome_binary_path = '/opt/google/chrome/google-chrome'
chrome_user_data_dir = f'/root/.config/google-chrome/{csbid}'

mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"
client = MongoClient(mongo_uri)
db = client['MoneyFarmV6'] 

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

    for i in range(1,5):
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

def are_extensions_exist():
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/extension_icon.png", region=(1700, 30, 300, 300), confidence=0.9)
        #pyautogui.click(x, y)
        print("extension_icon Button Found")
        return False

    except pyautogui.ImageNotFoundException:
        print("No extension_icon Button.")
        return True

def codesandbox_login(driver, codesandbox_id):
    driver.open('https://codesandbox.io/dashboard')
    time.sleep(5)
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
                    url = f'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/CBS_logins/{codesandbox_id}.json'
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
        #driver.close()

def are_codesand_logged(driver):
    driver.open('https://codesandbox.io/dashboard/recent')
    time.sleep(2)
    for i in range(1,9999):
        try:
            titile = driver.get_title()
            print(f'title is : {titile}')
            continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'h1.sc-bdnylx')
            for button in continue_buttons:
                if 'Sign in to CodeSandbox' in button.text:
                    print(f"H1 found: {button.text}, clicking...")
                    codesandbox_login(driver,CSB_id)
                    sb1.open('https://codesandbox.io/dashboard/recent')
            
            if 'Recent - CodeSandbox' in titile:
                return True

        except Exception as e:
            print(f' are_codesand_logged ERROR:{e}')

def create_devbox(driver):
    driver.open('https://codesandbox.io/dashboard')
    time.sleep(2)
    try:
        title = driver.get_title()
        print(f'Titile: {title},create_devbox wait for Recent')
        time.sleep(5)
        if title in title:
            print(f'Vm Has Loaded:{title}')

            for i in range(1, 20):
                time.sleep(2)
                continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.sc-bdnylx')
                for button in continue_buttons:
                    if 'Create' in button.text:
                        print(f"found: {button.text}, clicking...")
                        button.click()
                        time.sleep(3)
                        python_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[title="Python"]')
                        for button in python_buttons:
                            print(f"Found button with title: {button.get_attribute('title')}, clicking...")
                            button.click()
                            time.sleep(5)
                            python_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[type="submit"]')
                            for button in python_buttons:
                                print(f"Found button with title: {button.get_attribute('submit')}, clicking...")
                                button.click() 
                                while True:
                                    time.sleep(2)
                
                                    title = driver.get_title()
                                    print(f'Titile: {title}, create_devbox D')
                                    if 'README.md - workspace - CodeSandbox' in title:
                                        print(f'Vm Has Loaded:{title}')
                                        return True               
                                    if 'New Devtool - workspace - CodeSandbox' in title:
                                        print(f'Vm Has Loaded:{title}')
                                        return True  
                                    if 'workspace - CodeSandbox' in title:
                                        print(f'Vm Has Loaded:{title}')
                                        return True  
            print('Failed bruh...')
    except Exception as e:
        print(f'Create DevBox:{e}')
        return False
  
def deploy_docker(farmurl, driver):
    while True:
        currecto = False
        time.sleep(2)
        title = driver.get_title()
        print(f'Titile: {title}')
        if 'README.md - workspace - CodeSandbox' in title:
            print(f'Vm Has Loaded:{title}')
            currecto = True               
        if 'New Devtool - workspace - CodeSandbox' in title:
            print(f'Vm Has Loaded:{title}')
            currecto = True  
        if 'workspace - CodeSandbox' in title:
            print(f'Vm Has Loaded:{title}')
            currecto = True  
        if 'Recent - CodeSandbox' in title:
            print(f'going again create:{title} ')
            create_devbox(driver)

        if currecto:
            

            try:
                pyautogui.click(21, 303)
                time.sleep(3)
                pyautogui.click(319, 419)
                time.sleep(3)
                pyautogui.click(500, 840)
                time.sleep(3)
                pyautogui.press('enter')
                time.sleep(3)
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/workspace_git.png", region=(350, 780, 800, 800), confidence=0.9)
                if x and y:
                    pyautogui.click(x, y)
                    print("workspace git Found")
                    pyautogui.typewrite('docker run -i --platform=linux/amd64 -p 6080:6080 akarita/docker-ubuntu-desktop')
                    pyautogui.press('enter')
                    ggg2 = True
                    while ggg2 == True:
                        time.sleep(2)  
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/docker_deployed.png", region=(350, 780, 800, 800), confidence=0.9)
                            if x and y:
                                pyautogui.click(x, y)
                                print("docker_deployed git Found")
                                while True:
                                    pyautogui.click(23, 303)
                                    time.sleep(3)
                                    pyautogui.click(104, 345)
                                    time.sleep(5)
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/director_lister.png", region=(1120, 223, 1000, 1000), confidence=0.9)
                                        if x and y:
                                            pyautogui.click(x, y)
                                            print("director_lister git Found")
                                            pyautogui.click(1228,462)
                                            time.sleep(3)
                                            while True:
                                                time.sleep(2)
                                                pyautogui.rightClick(1467, 346)
                                                time.sleep(5)
                                                try:
                                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/open_terminal.png", region=(1120, 223, 1000, 1000), confidence=0.9)
                                                    if x and y:
                                                        pyautogui.click(x, y)
                                                        print("open_terminal git Found")
                                                        while True:
                                                            time.sleep(3)
                                                            try:
                                                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/desktop_terminal.png", region=(1120, 223, 1000, 1000), confidence=0.9)
                                                                if x and y:
                                                                    pyautogui.click(x, y)
                                                                    print("desktop_terminal git Found")
                                                                    pyautogui.typewrite(farmurl)
                                                                    pyautogui.press('enter')
                                                                    return True
                                                            except Exception as e:
                                                                print('desktop_terminal not found')


                                                except Exception as e:
                                                    print('open_terminal not found')
                                            
                                    except Exception as e:
                                        print('director_lister not found')

                        except Exception as e:
                            print('docker_deployed not found')
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/press_anykey_cbs.png", region=(350, 780, 1500, 800), confidence=0.9)
                            if x and y:
                                pyautogui.click(x, y)
                                print("press_anykey_cbs git Found")
                                pyautogui.press('enter')
                            
                        except Exception as e:
                            print('press_anykey_cbs not found')
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/docker_failed2.png", region=(320, 760, 1500, 900), confidence=0.9)
                            if x and y:
                                pyautogui.click(x, y)
                                print("Docker Failed Found")
                                create_devbox(driver)
                                return False
                        except Exception as e:
                            print('docker_failed2 not found')


            except Exception as e:
                print(f'Deploy:{e}')
        else:
            print("No correcto")


def CSB_credit_usage(driver):
    original_window = driver.current_window_handle
    driver.open_new_window()
    driver.open('https://codesandbox.io/dashboard/')
    time.sleep(3)
    usage_list = []
    ucredit = None
    try:
        continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'span.sc-bdnylx')

        for button in continue_buttons:
            if 'credits' in button.text:
                print(f"Found and processing: {button.text}")
                gg = button.text

                # Use regex to extract the numbers before and after the slash
                match = re.search(r'(\d+)\s*/\s*(\d+)', gg)
                if match:
                    current_credits = int(match.group(1))  # Extract current credits (e.g., 253)
                    total_credits = int(match.group(2))    # Extract total credits (e.g., 400)
                    
                    print(f"Current Credits: {current_credits}")
                    print(f"Total Credits: {total_credits}")
                    ucredit = current_credits  # Store the current credits if needed
                else:
                    print("No credit values found in text.")
    except Exception as e:
        print(e)
    driver.close()
    driver.switch_to.window(original_window)
    return ucredit
                    
def CSB_Usages(driver):
    original_window = driver.current_window_handle
    driver.open_new_window()
    driver.open('https://codesandbox.io/dashboard/')
    time.sleep(3)
    usage_list = []
    ucredit = 0
    
    try:

        continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.sc-bdnylx')
        for button in continue_buttons:
            if 'View usage' in button.text:
                print(f"Found and clicking: {button.text}")
                #button.click()
                pyautogui.click(217, 1042)
                
                time.sleep(5)
                continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'p.text-csb-green-5')
                for button in continue_buttons:
                    if 'free credits used' in button.text:
                        print(f"Found and clicking: {button.text}")
                        gg = button.text 
                        gg = gg.replace('free credits used', '').strip()
                        ucredit = gg

                rows = driver.find_elements(By.CSS_SELECTOR, "tbody#vm_usage tr")
                for row in rows:
                    row_id = row.get_attribute("id")
                    devbox_name = row.find_element(By.CSS_SELECTOR, "td:nth-of-type(1) a").text.strip()
                    credit = row.find_element(By.CSS_SELECTOR, "td:nth-of-type(2)").text.strip()
                    runtime = row.find_element(By.CSS_SELECTOR, "td:nth-of-type(3)").text.strip()
                    vm_tier = row.find_element(By.CSS_SELECTOR, "td:nth-of-type(4)").text.strip()
                    
                    print(f"ID_name: {row_id}")
                    print(f"Devbox: {devbox_name}")
                    print(f"Credit: {credit}")
                    print(f"Runtime: {runtime}")
                    print(f"Vm Tier: {vm_tier}\n")
                    
                    # Store the data in a Python dictionary
                    vm_usage_data = {
                        "ID_name": row_id,
                        "Devbox": devbox_name,
                        "Credit": credit,
                        "Runtime": runtime,
                        "Vm_Tier": vm_tier
                    }

                    # Add the data to the usage_list
                    usage_list.append(vm_usage_data)
            else:
                print(button.text)
                print('View usage Not Found')   

    except Exception as e:
        print(f'Error during usage extraction: {e}')
    
    # Close the new window and return to the original one
    driver.close()
    driver.switch_to.window(original_window)

    # Optionally convert usage_list to a JSON formatted string if needed
    json_usage_list = json.dumps(usage_list, indent=4)
    #print(json_usage_list)
    #print(usage_list)
    return ucredit, usage_list

def delete_csb(driver):
    driver.open('https://codesandbox.io/dashboard')
    time.sleep(2)
    for i in range(1,999):
        try:
            continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'span.sc-bdnylx')
            for button in continue_buttons:
                if 'You have no recent work' in button.text:
                    print(f"found: {button.text},You have no recent work clicking...")
                    return True
                
            continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'h3.sc-bdnylx')
            for button in continue_buttons:
                if 'Pick up where you left off' in button.text:
                    print(f"found: {button.text},Pick up where you left off clicking...")
                    pyautogui.rightClick(459, 624)
                    time.sleep(2)
                    pyautogui.click(504, 1026)
                    time.sleep(2)
        except Exception as e:
            print(f'Delete:{i}|{e}')

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
                    url = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie.json"
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
        #driver.close()

def mysterium_login(driver):
    for i in range(1,100):
        titile = sb1.get_title()
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



sb1 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
sb1.maximize_window()
url = "chrome://extensions/"
sb1.open(url)
print(sb1.get_title())
fresh = are_extensions_exist()

if fresh:
        mysterium = install_extensions('mysterium')
        nopecha = install_extensions('nopecha')
        cookie = install_extensions('cookie')
        fingerprint = install_extensions('fingerprint')
        mfhelper = install_extensions('mfhelper')
        if fingerprint and mysterium and nopecha and cookie and mfhelper:
            print('All Extensions are installed..')
            if pin_extensions():
                print('All Extensions are pinned')
                #mysterium_login(sb1)

codesandlogged = are_codesand_logged(sb1)
urls_dev = []
page_windows = []

if fresh_vms:
    delete_csb(sb1)
    for i in range(1, vm_count):
        sb1.maximize_window()
        command = command_1
        if   i == 1: command = command_1
        elif i == 2: command = command_2
        elif i == 3: command = command_3
        elif i == 4: command = command_4
        elif i == 5: command = command_5

        sb1.open_new_window()
        create_devbox(sb1)
        ggt = False
        while ggt == False:
            ggt = deploy_docker(command,sb1)
            time.sleep(5)
        
        time.sleep(5)
        pyautogui.click(942, 65)
        time.sleep(1)
        pyautogui.click(942, 65)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.keyUp('ctrl')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        page_url = clipboard.paste()
        page_window = sb1.current_window_handle
        urls_dev.append(page_url)
        page_windows.append(page_window)
else:
    collection = db[CSB_Script]
    data = collection.find_one({"csb_script_id": CSB_Script})
    devboxes = data['devboxes']
    devboxes_id = [item.strip() for item in devboxes.split('<br>') if item.strip()]
    urls_dev = [f'https://codesandbox.io/p/{item}' for item in devboxes_id]
    for url in urls_dev:
        sb1.maximize_window()
        sb1.open_new_window()
        sb1.open(url)
        window = sb1.current_window_handle
        page_windows.append(window)


while True:
    #Wating
    gg = True
    start_time = time.time()
    while gg == True:
        urls =[]
        for i, page in enumerate(page_windows):
            collection = db[CSB_Script]                
            #######################################
            ucredit = CSB_credit_usage(sb1)
            sri_lanka_tz = pytz.timezone('Asia/Colombo')
            utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)  
            sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
            now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
            query = {"type": "main"}
            sample_document = {
                "ucredit": ucredit,
                "status": now
            }
            update = {"$set": sample_document}
            result = collection.update_one(query, update)    
            ############################################
            i += 1
            sb1.switch_to.window(page)
            time.sleep(1)
            time.sleep(2)
            pyautogui.click(942, 69)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.keyUp('ctrl')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.keyUp('ctrl')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.keyUp('ctrl')
            pyautogui.click(1220 ,208)
            page_url = clipboard.paste()
                    #page_url = sb1.get_current_url()
            urls.append(page_url)
            print(f'List URLS:{urls} page:{page_url}')
            query = {"type": "main"}
            doc = collection.find_one(query)
            request = doc["request"]
            if 's' in request:
                x = ''
                for z in range(1,6):
                    y = str(z)
                    if y in request:
                        x = z - 1
                        break
                page = page_windows[x]
                sb1.switch_to.window(page)
                time.sleep(2)
                command = command_1
                if   i == 1: command = command_1
                elif i == 2: command = command_2
                elif i == 3: command = command_3
                elif i == 4: command = command_4
                elif i == 5: command = command_5
            
                create_devbox(sb1)
                deploy_docker(command, sb1)
                pyautogui.click(942, 65)
                collection = db[CSB_Script]
                query = {"type": "main"}
                doc = collection.find_one(query)
                update = {"$set": {"request": 'None'}}
                result = collection.update_one(query, update)      
                if result.modified_count > 0:
                    print(f"Updated {result.modified_count} document(s).")
                else:
                    print("No document was updated.")
            
            elif 'wait' in request:
                for i in range(3000):
                    query = {"type": "main"}
                    doc = collection.find_one(query)
                    request = doc["request"]
                    if 'wait' in request:
                        print(f'Waiting{request} | {i}')
                        time.sleep(5)
                    else:
                        break
                    
            time.sleep(5)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/reload_window.png", region=(144, 118, 1700, 1000), confidence=0.9)
                pyautogui.click(242, 85)
                pyautogui.press('f5')

            except Exception as e:
                print(f'Waiting For Find Directior Listener{i}')

            title =  sb1.get_title()
            if 'Unable to start the microVM' in title:
                command = command_1
                if   i == 1: command = command_1
                elif i == 2: command = command_2
                elif i == 3: command = command_3
                elif i == 4: command = command_4
                elif i == 5: command = command_5
                query = {"type": "main"}
                doc = collection.find_one(query)
                update = {"$set": {"request": f'Resetting DEV{i}'}}
                result = collection.update_one(query, update) 
                create_devbox(sb1)
                deploy_docker(command , sb1)
                pyautogui.click(942, 65)
                query = {"type": "main"}
                doc = collection.find_one(query)
                update = {"$set": {"request": 'None'}}
                result = collection.update_one(query, update)  
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/505-screen.png", region=(1120, 223, 1000, 1000), confidence=0.9)
                if x and y:
                    command = command_1
                    if   i == 1: command = command_1
                    elif i == 2: command = command_2
                    elif i == 3: command = command_3
                    elif i == 4: command = command_4
                    elif i == 5: command = command_5
                    query = {"type": "main"}
                    doc = collection.find_one(query)
                    update = {"$set": {"request": f'Resetting DEV{i}'}}
                    result = collection.update_one(query, update) 
                    create_devbox(sb1)
                    deploy_docker(command , sb1)
                    pyautogui.click(942, 65)
                    query = {"type": "main"}
                    doc = collection.find_one(query)
                    update = {"$set": {"request": 'None'}}
                    result = collection.update_one(query, update)  
            except Exception as e:
                print(f'ERR{e}')
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/502.png", region=(1120, 223, 1000, 1000), confidence=0.9)
                if x and y:
                    command = command_1
                    if   i == 1: command = command_1
                    elif i == 2: command = command_2
                    elif i == 3: command = command_3
                    elif i == 4: command = command_4
                    elif i == 5: command = command_5
                    query = {"type": "main"}
                    doc = collection.find_one(query)
                    update = {"$set": {"request": f'Resetting DEV{i}'}}
                    result = collection.update_one(query, update) 
                    create_devbox(sb1)
                    deploy_docker(command , sb1)
                    pyautogui.click(942, 65)
                    query = {"type": "main"}
                    doc = collection.find_one(query)
                    update = {"$set": {"request": 'None'}}
                    result = collection.update_one(query, update)  
            except Exception as e:
                print(f'ERR{e}')
            time.sleep(35)
            
        if len(urls) == 5:
            devbox_string = "<br>\n".join([url.replace('https://codesandbox.io/p/', '') for url in urls])
            query = {"type": "main"}
            sample_document = {
                "devboxes": devbox_string
            }
            update = {"$set": sample_document}
            result = collection.update_one(query, update) 
        elapsed_time = time.time() - start_time
        mins, secs = divmod(int(elapsed_time), 60)
        timer = f'{mins:02d}:{secs:02d}'
        seconds_only = int(elapsed_time)
        print(f'Next Click {timer}')
        print(f'Elapsed_time {seconds_only}')
        if seconds_only > waiting_sec:
            gg = False

##############################################

    collection = db[CSB_Script]
    query = {"type": "main"}
    doc = collection.find_one(query)
    #request = doc["request"]
    #print(request)
    update = {"$set": {"request": 'None'}}
    result = collection.update_one(query, update)      
    if result.modified_count > 0:
        print(f"Updated {result.modified_count} document(s).")
    else:
        print("No document was updated.")

    update = {"$set": {"response": 'None'}}
    result = collection.update_one(query, update)      
    if result.modified_count > 0:
        print(f"Updated {result.modified_count} document(s).")
    else:
        print("No document was updated.")


    urls =[]
    for page in page_windows:
        sb1.switch_to.window(page)
        sb1.refresh()
        time.sleep(2)
        pyautogui.click(942, 69)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.keyUp('ctrl')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.keyUp('ctrl')
        page_url = clipboard.paste()
                #page_url = sb1.get_current_url()
        urls.append(page_url)
            
    #after each Refresh
    if len(urls) == 5:
        collection = db[CSB_Script]
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} documents.")
        devbox_string = "<br>\n".join([url.replace('https://codesandbox.io/p/', '') for url in urls])
        sri_lanka_tz = pytz.timezone('Asia/Colombo')
        utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)  
        sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
        now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
        ucredit, usage_list = CSB_Usages(sb1)
        
        csb_panel =     {"csb_script_id": CSB_Script,
                        "csb_logins": CSB_id,
                        "devboxes": devbox_string,
                        "ucredit" : ucredit,
                        "status": now,
                        "request": "None",
                        "response": "None",
                        "type": "main"}
        
        csb_panel_collection = db[CSB_Script]
        csb_panel_result = csb_panel_collection.insert_one(csb_panel)
        print(f"Inserted csb_panel with ID: {csb_panel_result.inserted_id}")

        if usage_list:
            usage_collection = db[CSB_Script]
            usage_result = usage_collection.insert_many(usage_list)
            print(f"Inserted usage documents with IDs: {usage_result.inserted_ids}")
