

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
import easyocr

# Example usage

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
    facebook_cookies = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/Facebook_Logins/khabibmakanzie.json'
    fb_pass = 'uwuinsta2005'
    yt_api_key = 'AIzaSyCoAMmJOYzKhFdLO5oEmwI2Ne7C329jJtg'
    mysterium_raw = "https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/mysterium_cookie_mcnutt.json"
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

debug_mode = True

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


mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"

client = MongoClient(mongo_uri)
db = client['MoneyFarmV6'] 
collection = db[f'Farm{farm_id}']
ocr = PaddleOCR(use_angle_cls=True, lang='en',  drop_score=0)


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


def get_current_duration(sb):
    try:
        if sb.is_element_visible('.video-page-current-duration'):
            current_duration = sb.get_text('.video-page-current-duration')
            if debug_mode:
                print(f"Current video duration: {current_duration}")
            return int(current_duration)
        else:
            if debug_mode:
                print("Current duration element not found")
            return None
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
        try:
            continue_buttons = sb.find_elements(By.CSS_SELECTOR, 'h2.blnc')
            for button in continue_buttons:
                if 'You' in button.text:
                    print(f"Button found: {button.text}, clicking...")
                    gg = button.text
                    gg = int(float(gg.split()[2]))
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('left')
                    pyautogui.keyUp('ctrl')
                    time.sleep(2)
                    return None
                else:
                    print(button.text)
        except Exception as e:
            return None
        return None
    
def play_button(sb):
    current_duration = get_current_duration(sb)
    title1 = sb.get_title()
    if current_duration == 0:
        play_button_selector = '.ytp-large-play-button'
        try:
            if sb.is_element_visible('iframe'):
                sb.switch_to.frame(sb.find_element(By.TAG_NAME, "iframe"))
                if sb.is_element_visible(play_button_selector):
                    play_button_elements = sb.find_elements(By.CSS_SELECTOR, play_button_selector)
                    print("Play button found")
                    play_button = play_button_elements[0]
                    time.sleep(2)
                    play_button.click()
                    print("Play button Clicked")
                    sb.switch_to.default_content()
                    time.sleep(1)
                if sb.is_element_visible('button.ytp-ad-skip-button-modern'):
                    play_button_elements = sb.find_elements(By.CSS_SELECTOR, 'button.ytp-ad-skip-button-modern')
                    print("Play button found")
                    play_button = play_button_elements[0]
                    time.sleep(2)
                    play_button.click()
                    print("Play button Clicked")
                    sb.switch_to.default_content()
                    time.sleep(1)
                else:
                    print("Play button not found")
                    sb.switch_to.default_content()
            else:
                print("iframe not found")
                sb.switch_to.default_content()
        except Exception as e:
            if debug_mode:
                print(f"An error occurred: {e}")
            sb.switch_to.default_content()
    elif current_duration == 1 and title1 == 'Popmack':
        time.sleep(2)
        current_duration = get_current_duration(sb)
        if current_duration == 1:
            play_button_selector = '.ytp-large-play-button'
            try:
                if sb.is_element_visible('iframe'):
                    sb.switch_to.frame(sb.find_element(By.TAG_NAME, "iframe"))
                    if sb.is_element_visible(play_button_selector):
                        play_button_elements = sb.find_elements(By.CSS_SELECTOR, play_button_selector)
                        print("Play button found")
                        play_button = play_button_elements[0]
                        time.sleep(2)
                        play_button.click()
            except Exception as e:
                print(f'Issue{e}')



def playback_check(sb):
    try: 
        # Locate the <a> element by its id and click it
        if sb.is_element_visible('#replay_video'):
            #sb.highlight('#replay_video')
            sb.click('#replay_video')
            print("Clicked the 'replay_video' button.")
        else:
            if debug_mode:
                print("Not Found 'replay_video' button.")
    except (NoSuchElementException,Exception):
        if debug_mode:
            print("Element with id 'replay_video' is not present.")
    try:
        # Locate the <a> element by its id and click it
        if sb.is_element_present('.ytp-offline-slate-main-text'):
            #sb.highlight('.ytp-offline-slate-main-text')
            #sb.click('#replay_video')
            sb.refresh()
            print("Clicked the 'ytp-offline-slate-main-text' button.")
        else:
            if debug_mode:
                print("Not Found 'ytp-offline-slate-main-text' button.")
    except (NoSuchElementException,Exception):
        if debug_mode:
            print("Element with id 'ytp-offline-slate-main-text' is not present.")
    try: 
        # Locate the <a> element by its id and click it
        if sb.is_element_visible('button.ytp-ad-skip-button-modern'):
            #sb.highlight('#replay_video')
            sb.click('button.ytp-ad-skip-button-modern')
            print("Clicked the 'replay_video' button.")
        else:
            if debug_mode:
                print("Not Found 'replay_video' button.")
    except (NoSuchElementException,Exception):
        if debug_mode:
            print("Element with id 'replay_video' is not present.")


def reclick_button(sb):
    current_duration = get_current_duration(sb)
    if current_duration == 0:
        play_button_selector = '.ytp-large-play-button'
        try:
            sb.switch_to.frame(sb.find_element(By.TAG_NAME, "iframe"))
            play_button_elements = sb.find_elements(By.CSS_SELECTOR, play_button_selector)
            print("reclick_button found")
            play_button = play_button_elements[0]
            play_button.click()
            print("reclick_button Clicked")
            sb.switch_to.default_content()
            time.sleep(2)
            play_button.click()
            #time.sleep(2)
            print("reclick_button Clicked Again")

            print("Play button not found")
            sb.switch_to.default_content()
        except Exception as e:
            if debug_mode:
                print(f"An error occurred: {e}")
            sb.switch_to.default_content()

def remove_pink(sb):
    try:
        if sb.is_element_visible("div.pink_strip_homepage[style*='z-index: 20']"):
            element = sb.find_element("div.pink_strip_homepage[style*='z-index: 20']")
            #sb.highlight(element)
            sb.execute_script("arguments[0].remove();", element)
            print("Pink Element removed successfully.")
        else:
            if debug_mode:
                print("Pink Element not found.")
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
    try:
        # Check if the subscribe block container is visible based on its unique id
        if sb.is_element_visible("div#subscribe_block_container"):
            element = sb.find_element("div#subscribe_block_container")
            # Remove the subscribe block element
            sb.execute_script("arguments[0].remove();", element)
            print("Subscribe block removed successfully.")
        else:
            if debug_mode:
                print("Subscribe block not found.")
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
        return

headers = {
    'User-Agent': 'My User Agent 1.0',
}
def get_youtube_video_id(url):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*[/?]|(?:v|e(?:mbed)?|shorts|watch|playlist|embed|v/|embed/)|.*[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})|(?:shorts/([a-zA-Z0-9_-]{11}))'
    match = re.search(pattern, url)
    if match:
        return match.group(1) or match.group(2)
    else:
        return None
    
def yt_api_method(link):
    try:
        api_key = yt_api_key  # Replace with your API key
        pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*[/?]|(?:v|e(?:mbed)?|shorts|watch|playlist|embed|v/|embed/)|.*[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})|(?:shorts/([a-zA-Z0-9_-]{11}))'
        match = re.search(pattern, link)
        if match:
            video_id = match.group(1) or match.group(2)
            #video_id = '3KRBI8tNL00'  # The YouTube video ID
            category_mapping = {
                "1": "Film",
                "2": "Auto",
                "10": "Music",
                "15": "Pets",
                "17": "Sport",
                "19": "Travel",
                "20": "Gaming",
                "22": "People",
                "23": "Comedy",
                "24": "Entertainment",
                "25": "News",
                "26": "Howto",
                "27": "Education",
                "28": "Technology",
                "29": "Nonprofit",
                "34": "Comedy",
                "37": "Family",
                "40": "SciFi",

            }

            url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}'

            # Send the request to the YouTube Data API
            response = requests.get(url)
            data = response.json()

            # Extract the category ID and title from the response
            if 'items' in data and len(data['items']) > 0:
                category_id = data['items'][0]['snippet']['categoryId']
                title = data['items'][0]['snippet']['title']
                category_name = category_mapping.get(category_id, None)
                
                print(f"Video title: {title}")
                print(f"Category: {category_name}")
                return category_name
            else:
                print("Video details not found.")
                return None

        else:
            return None
    except Exception as e:
        print(e)

def get_video_infog(video_url, driver, timeout=8):
    if 'you' in video_url:
        category = yt_api_method(video_url)
        if category:
            return category
        original_window = driver.current_window_handle
        driver.open_new_window()
        try:
            # Set page timeout and open the view-source page
            driver.uc_open(f'view-source:{video_url}')
            print(f'view-source:{video_url}')

            # Wait for the page to load with a timeout of 8 seconds
            driver.wait_for_element_visible('body', timeout=timeout)
            
            # Get page source and parse it
            data = driver.get_text('body')
            html_content = str(data)
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract video category
            category_tag = soup.find('meta', itemprop='genre')
            category = category_tag['content'] if category_tag else None
            print(f"Category For This Video is {category}")

            # Close new window and switch back to original
            driver.close()
            driver.switch_to.window(original_window)

            # Return the category or 0 if not found
            if category:
                return category
            else:
                return 0

        except Exception as e:
            print(f"Error occurred: {e}")
            driver.close()
            driver.switch_to.window(original_window)
            return 0
    else:
        print("Youtube Link not valid")
        return 0
    

def get_youtube_link_manual():
    try:
        pyautogui.moveTo(1316, 438)
        time.sleep(1)
        pyautogui.rightClick(1316, 438)

        for i in range(1,4):
            time.sleep(1)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/yt_copy_clip.png", region=(1041,404, 250, 244), confidence=0.8)
                pyautogui.click(x, y)
                link = clipboard.paste()
                link = link.replace('music.', '')
                return link
            except Exception as e:
                if debug_mode:
                    print(f'ERR:{e}') 
        return 0
        
    except Exception as e:
        if debug_mode:
            print(f'ERR:{e}')
        return 0



def get_youtube_link(sb):   
    try:
        # Find the iframe that contains "youtube.com/embed" in the src attribute
        iframe = sb.find_element("iframe[src*='youtube.com/embed']")

        # Switch to the iframe
        sb.switch_to_frame(iframe)

        # Get the page source after switching to the iframe
        page_source = sb.get_page_source()
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Locate the <a> tag inside <div class="ytp-title-text">
        a_tag = soup.find('a', class_='ytp-title-link')

        # Check if the <a> tag is found and extract the href attribute
        if a_tag:
            href = a_tag.get('href')

            # Use regex to find the YouTube URL from the href
            youtube_url_match = re.search(r'https://www\.youtube\.com/watch\?v=[\w-]+', href)

            if youtube_url_match:
                return youtube_url_match.group(0)
        print('Tring Pyauto Get LINK')
        link = get_youtube_link_manual()
        return link

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

    finally:
        # Switch back to the default content
        sb.switch_to.default_content()


    
def check_category_question(sb):
    category_question_selector = '.video-categ-question.video-question-answer'
    category_question_selector2 = '.video-categ-question'
    expected_text = "Guess What Category The Video Is?"
    expected_text2 = "Guess what category the video is?"
    
    try:
        # Check if the element is visible and has the expected text
        if sb.is_element_visible(category_question_selector2):
            actual_text = sb.get_text(category_question_selector2)
            print(actual_text)
            if actual_text.strip() == expected_text or actual_text.strip() == expected_text2:
                print("Category question exists and matches the expected text.")
                return True

            else:
                print(f"Category question found, but text does not match. Found: '{actual_text}'")
                if debug_mode:
                    print(f"Category question found, but text does not match. Found: '{actual_text}'")
                return False
        else:
            if debug_mode:
                print("Category question element does not exist or is not visible.")
            return False
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
        return False

def get_coin_value(driver):
    try:
        # Locate the <a> element containing the coin value
        element = driver.find_element("a.button.class-for-instant-baymack-videos.header-button")
        
        # Extract the text content
        text = element.text.strip()
        
        # Extract the numeric part from the text
        coin_value = text.split()[0]  # Assuming the first part is the numeric value
        
        print(f"Coin value: {coin_value}")
        return coin_value
    
    except Exception as e:
        print(f"Error: {e}")
        return None



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

#######Solve###############################################################
def simple_similarity(word1, word2):
    
    # Calculate character matches
    matches = sum(1 for a, b in zip(word1, word2) if a == b)
    return matches / max(len(word1), len(word2))

def find_most_similar_word2(word, word_list):
    normalized_word = word
    highest_similarity = 0
    most_similar_word = None
    
    for candidate in word_list:
        similarity = simple_similarity(normalized_word, candidate)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_word = candidate
    
    return most_similar_word

def find_most_similar_word(word, word_list):
    most_similar_word = None
    lowest_distance = float('inf')  # Start with an infinitely large distance
    most_similar_index = -1

    # Loop through each word in the list and calculate the Levenshtein distance
    for idx, candidate in enumerate(word_list):
        distance = Levenshtein.distance(word, candidate)
        
        # If distance is lower than the current lowest, update the result
        if distance < lowest_distance:
            lowest_distance = distance
            most_similar_word = candidate
            most_similar_index = idx  # Store the index
    
    return most_similar_word

def fix_broken_words(word_list):
    reference_list = [
        "comedy", "education", "gaming", "music", "science", "technology", "family",
        "entertainment", "none", "news", "politics", "people", "travel", "travel",
        "sports", "beauty", "nonprofit", "howto", "film", "pets", "food", "scifi", "people", 
        "news", "auto"
    ]
    
    replacements = {
        '0': 'o', '5': 's', '6': 's', '$': 's', '8': '&', '1': 'i', '4': 'a', '7': 'e', 
        '[': 'c', '{': 'c', '(': 'c', '<': 'c', '*': 'e'
    }
    
    special_cases = {
        'F-w': 'film',
        '1F()Ve': 'travel'
    }
    
    # Custom logic for edge cases after replacement
    category_fixes = {
        "politics": "news",
        "blogs": "people",
        "people & blogs": "people",
        "news & politics": "news",
        "family entertainment": "family"
    }
    
    fixed_list = []

    for word in word_list:
        # Apply basic replacements
        for old, new in replacements.items():
            word = word.replace(old, new)
        
        # Handle special cases explicitly
        if word in special_cases:
            word = special_cases[word]
        
        # Find the closest match to the reference list
        fixed_word = find_most_similar_word(word.lower(), reference_list)
        
        # Fix category-specific issues
        if fixed_word in category_fixes:
            fixed_word = category_fixes[fixed_word]
        
        # Handle short words
        letter_count = sum(1 for char in word if char.isalpha())
        if letter_count < 10:
            word = word.replace(' ', '')  # Compact short words if necessary
            if letter_count < 4:
                fixed_word = find_most_similar_word2(word.lower(), reference_list)
        
        # Default to 'none' if no match found
        if not fixed_word:
            fixed_word = "none"

        fixed_list.append(fixed_word)

    return fixed_list

def check_words(category, fixed_words):
    if category is None:
        print("Category is None aiyo.")
        return
    category = category.replace('-', '')
    category = category.replace('blog', 'people')
    category = category.replace('politics', 'news')
    #similar_word = find_most_similar_word(category, unfixed_words)
    print(f'Trying {category}')
    fixed_words_lower = [word.lower() for word in fixed_words if word is not None]
    for word in fixed_words:
        if word:
            word_lower = word.lower()
            category_lower = category.lower()
            if word_lower in category_lower:
                position = fixed_words_lower.index(word_lower)
                print(f'{word} is a match in {category}. Position: {position}')
                return position
        

    if category =='Sic-fi' or category =='Sicfi' or category =='Science' or category =='Technology':
            category = 'Science'
            for word in fixed_words:
                if word:
                    word_lower = word.lower()
                    category_lower = category.lower()
                    if word_lower in category_lower:
                        position = fixed_words_lower.index(word_lower)
                        print(f'{word} is a match in {category}. Position: {position}')
                        return position
            print(f'Failed {category} Tring Technology')            
            category = 'Technology'
            for word in fixed_words:
                if word:
                    word_lower = word.lower()
                    category_lower = category.lower()
                    if word_lower in category_lower:
                        position = fixed_words_lower.index(word_lower)
                        print(f'{word} is a match in {category}. Position: {position}')
                        return position
        

    print(f'Failed {category} Tring none')        
    category = 'none'
    for word in fixed_words:
        if word:
            word_lower = word.lower()
            category_lower = category.lower()
            if word_lower in category_lower:
                position = fixed_words_lower.index(word_lower)
                print(f'{word} is a match in {category}. Position: {position}')
                return position

            
    print(f'Failed {category} Tring People')   
             
    category = 'People'
    for word in fixed_words:
        if word:
            word_lower = word.lower()
            category_lower = category.lower()
            if word_lower in category_lower:
                position = fixed_words_lower.index(word_lower)
                print(f'{word} is a match in {category}. Position: {position}')
                return position
    print(f'Failed {category} Tring Music')    
    category = 'Music'
    for word in fixed_words:
        if word:
            word_lower = word.lower()
            category_lower = category.lower()
            if word_lower in category_lower:
                position = fixed_words_lower.index(word_lower)
                print(f'{word} is a match in {category}. Position: {position}')
                return position
    print(f'Failed {category} Tring Entertainment')          
        
    category = 'Entertainment'
    for word in fixed_words:
        if word:
            word_lower = word.lower()
            category_lower = category.lower()
            if word_lower in category_lower:
                position = fixed_words_lower.index(word_lower)
                print(f'{word} is a match in {category}. Position: {position}')
                return position


            
    return 4

def capture_and_crop_regions(regions, output_paths):
    try:
        # Capture the entire screen
        screenshot = pyautogui.screenshot()
        
        if len(regions) != len(output_paths):
            raise ValueError("The number of regions must match the number of output paths.")

        # Process each region and save the cropped image
        for (x, y, width, height), output_path in zip(regions, output_paths):
            left = x
            top = y
            right = x + width
            bottom = y + height
            cropped_img = screenshot.crop((left, top, right, bottom))
            cropped_img.save(output_path)
            print(f"Saved cropped image to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def are_images_loaded(sb):
        # Find all image elements inside the ul
        images = sb.find_elements('ul.link-btn-list.video-categ-options img')
        # Iterate through the images and check if they are fully loaded
        for img in images:
            # Check if the image is loaded (complete) and has non-zero width and height
            is_loaded = sb.execute_script(
                "return arguments[0].complete && arguments[0].naturalWidth > 0 && arguments[0].naturalHeight > 0;", img
            )
            
            # If any image is not fully loaded, return False
            if not is_loaded:
                print(f"Image not loaded: {img.get_attribute('src')}")
                return False

        # If all images are loaded, return True
        return True

def get_category_images():
    # Define regions and paths
    regions = [
        #(622, 766, 320, 85),  # Example region 1 (x, y, width, height)
        #(960, 766, 320, 85),  # Example region 2
        #(622, 862, 320, 85),  # Example region 3
        #(960, 862, 320, 85)   # Example region 4
        (639,777, 320, 85),  # Example region 1 (x, y, width, height)
        (969,777, 320, 85),  # Example region 2
        (639,868, 320, 85),  # Example region 1 (x, y, width, height)
        (969,868, 320, 85),
    ]
    
    output_paths = [
        "crop1.png",  # Output file path for region 1
        "crop2.png",  # Output file path for region 2
        "crop3.png",  # Output file path for region 3
        "crop4.png"   # Output file path for region 4
    ]

    # Capture and crop regions
    capture_and_crop_regions(regions, output_paths)
    return True

def get_category_images_baymack():
        # Define regions and paths
    regions = [
        #(610,705, 300, 50),  # Example region 1 (x, y, width, height)
        #(1011,705, 300, 50),  # Example region 2
        #(610,767, 300, 50),  # Example region 3
        #(1011,767, 300, 50)   # Example region 4
        (591, 734, 300, 50),  # Example region 1 (x, y, width, height)
        (1016, 735, 300, 50),  # Example region 2
        (592, 794, 300, 50),  # Example region 3
        (1015, 793, 300, 50)   # Example region 4
    ]
    
    output_paths = [
        "crop1.png",  # Output file path for region 1
        "crop2.png",  # Output file path for region 2
        "crop3.png",  # Output file path for region 3
        "crop4.png"   # Output file path for region 4
    ]

    # Capture and crop regions
    capture_and_crop_regions(regions, output_paths)
    return True

def remove_lines_from_image(input_image_path, output_image_path, np1 = 2 , np2 = 1):
    image = cv2.imread(input_image_path, 0)
    kernel_dilation = np.ones((2, 1), np.uint8)
    kernel_erosion = np.ones((2, 2), np.uint8)
    dilation = cv2.dilate(image, kernel_dilation, iterations=1)
    erosion = cv2.erode(dilation, kernel_erosion, iterations=1)
    kernel_closing = np.ones((np1, np2), np.uint8)
    closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel_closing)
    cv2.imwrite(output_image_path, closing)

def grayscale_image_for_ocr(image_path, output_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, gray_image)

def captcha_to_text2(image_paths):
    temp_output = 'temp_output.png'
    list_img = []
    for image in image_paths:
        remove_lines_from_image(image, temp_output, np1 = 2 , np2 = 1)
        result = ocr.ocr(image)
        if result == [None]:
            print(f'try 3,3 for {image}')
            remove_lines_from_image(image, temp_output, np1 = 3 , np2 = 3)
            result = ocr.ocr(temp_output)
            if result == [None]:
                result = 'foo'
            else:
                result = ''.join([item[1][0] for item in result[0]])
        else:
            result = ''.join([item[1][0] for item in result[0]])
            result_back = result
            letter_count = sum(1 for char in result if char.isalpha())
            if letter_count <= 2:
                print(f'2 letter  for {image} letters are {result}')
                remove_lines_from_image(image, temp_output, np1 = 3 , np2 = 3)
                result = ocr.ocr(temp_output)
                if result == [None]:
                    result = result_back
                else:
                    result = ''.join([item[1][0] for item in result[0]])
        list_img.append(result)

    return list_img

def captcha_to_text(image_paths):
    temp_output = 'temp_output.png'
    list_img = []
    for image in image_paths:
        grayscale_image_for_ocr(image, temp_output)
        result = ocr.ocr(temp_output)
        if result == [None]:
            print(f'try 3,3 for {image}')
            
            result = ocr.ocr(image)
            if result == [None]:
                result = '555'
            else:
                result = ''.join([item[1][0] for item in result[0]])
        else:
            result = ''.join([item[1][0] for item in result[0]])
            #result_back = result
            #letter_count = sum(1 for char in result if char.isalpha())
        list_img.append(result)

    return list_img




def solve_image_category(drive, category, window):
    start_time = time.time()
    activate_window_by_id(window)
    titile =drive.get_title()
    print(titile)
    time.sleep(1)
    if titile == 'Popmack':
        #base = print_base64_images(drive)
        base = are_images_loaded(drive)
        if base == True:
            get_category_images()
            try:
                image = cv2.imread('crop3.png')
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                is_white = np.all(gray_image == gray_image[0, 0])
                if is_white:
                    print("The image is blank (all white).")
                else:
                    print("The image is not blank.")
                    image_paths = ['crop1.png', 'crop2.png', 'crop3.png', 'crop4.png']
                    captcha_ocr = captcha_to_text(image_paths)
                    print('Peddle Word list :', captcha_ocr)
                    fixword_list = fix_broken_words(captcha_ocr)
                    print('Fix Broken Word list :', fixword_list)
                    try:
                        if fixword_list:
                            position = check_words(category, fixword_list)
                            if position == 4:
                                print('position is None')
                                similar_word = find_most_similar_word(category, captcha_ocr)
                                position = captcha_ocr.index(similar_word)
                            print(f"The most similar word to '{category}' at index {position} : {fixword_list}")
                            title = drive.get_title()
                            if title == 'Popmack':
                                print(title,position)
                                if position == 0:
                                    pyautogui.click(749, 803)
                                if position == 1:
                                    pyautogui.click(1100, 803)
                                if position == 2:
                                    pyautogui.click(777, 896)
                                if position == 3:
                                    pyautogui.click(1094, 903)

                                end_time = time.time()
                                print(f"Completed in {end_time - start_time} seconds")

                    except Exception as e:
                        print(e)
                        pyautogui.click(1100, 803)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(base,'Base False')


    if titile == 'Baymack':
        #base = print_base64_images(drive)
        base = are_images_loaded(drive)
        if base == True:
            get_category_images_baymack()
            try:
                image = cv2.imread('crop3.png')
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                is_white = np.all(gray_image == gray_image[0, 0])
                if is_white:
                    print("The image is blank (all white).")
                else:
                    print("The image is not blank.")
                    image_paths = ['crop1.png', 'crop2.png', 'crop3.png', 'crop4.png']
                    captcha_ocr = captcha_to_text(image_paths)
                    print('Peddle Word list :', captcha_ocr)
                    fixword_list = fix_broken_words(captcha_ocr)
                    print('Fix Broken Word list :', fixword_list)

                    try:
                        if fixword_list:
                            position = check_words(category, fixword_list)
                            if position == 4:
                                print('position is None')
                                similar_word = find_most_similar_word(category, captcha_ocr)
                                position = captcha_ocr.index(similar_word)
                            print(f"The most similar word to '{category}' at index {position} : {fixword_list}")
                            title = drive.get_title()
                            if title == 'Baymack':
                                print(title,position)
                                if position == 0:
                                    pyautogui.click(749, 753)
                                if position == 1:
                                    pyautogui.click(1100, 753)
                                if position == 2:
                                    pyautogui.click(777, 828)
                                if position == 3:
                                    pyautogui.click(1094, 828)

                                end_time = time.time()
                                print(f"Completed in {end_time - start_time} seconds")

                    except Exception as e:
                        print(e)
                        pyautogui.click(1100, 803)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(base,'Base False')


################################################################################################################
skylom_window = 0
baymack_window = 0


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


def redeem(driver):
    try:    
        query = {"type": "main"}
        doc = collection.find_one(query)
        mail = doc["withdraw_mail"]

        # Locate all gift card names and values
        pyautogui.click(1166, 732)
        try:
                # Wait for the email input to appear
            driver.wait_for_element('input#userEmail', timeout=5)
            email_input = driver.find_element('input#userEmail')
            email_input.send_keys(mail)
            print(f"Filled the email input field with {mail}.")
            time.sleep(1)

            submit_button = driver.find_element('input#subGiftCard')
            submit_button.click()
            print("Clicked the submit button.")
            time.sleep(3)

        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


def redeem_1doller(driver):
    try:    
        query = {"type": "main"}
        doc = collection.find_one(query)
        mail = doc["withdraw_mail"]

        # Locate all gift card names and values
        pyautogui.click(1166, 617)
        try:
                # Wait for the email input to appear
            driver.wait_for_element('input#userEmail', timeout=5)
            email_input = driver.find_element('input#userEmail')
            email_input.send_keys(mail)
            print(f"Filled the email input field with {mail}.")
            time.sleep(1)

            submit_button = driver.find_element('input#subGiftCard')
            submit_button.click()
            print("Clicked the submit button.")
            time.sleep(3)

        except Exception as e:
            print(e)
    except Exception as e:
        print(e)

def redeem_bay(driver):
    try:    
        query = {"type": "main"}
        doc = collection.find_one(query)
        mail = doc["withdraw_mail"]

        # Locate all gift card names and values
        pyautogui.click(1160, 594)
        try:
                # Wait for the email input to appear
            driver.wait_for_element('input#userEmail', timeout=5)
            email_input = driver.find_element('input#userEmail')
            email_input.send_keys(mail)
            print(f"Filled the email input field with {mail}.")
            time.sleep(1)

            submit_button = driver.find_element('input#subGiftCard')
            submit_button.click()
            print("Clicked the submit button.")
            time.sleep(3)

        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


def ipfixer():
    ip = 0
    preip = 0
    respo = 0
    gg2344 = 0
    query = {"type": "main"}
    update = {"$set": {"response": 'Fixing...🟠'}}
    result = collection.update_one(query, update)
    for i in CSB1_farms:
        collection_csb = db[f'Farm{i}']
        update = {"$set": {"request": 'ipfixer'}}
        result = collection_csb.update_one(query, update)
        print('Update Farm', i)

    while True:
        query = {"type": "main"}
        doc = collection.find_one(query)
        request = doc["request"]
        if request == 'ipfixer':
            preip = get_ip(sb1)
            if ip == preip:
                print(f'Good IP found: {ip}')
                if respo == 0:
                    update = {"$set": {"response": f'Ready IP🟢: {ip}'}}
                    result = collection.update_one(query, update)
                    if result.matched_count > 0:
                        print(f"Added new messages to existing document. Updated {result.modified_count} document(s).")
                        respo = 1
                    else:
                        print("No document found with the specified type.")
                else:
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
                        elif req == 'mainscript' and 'Running' in res:
                            res_farms.append(res)
                        elif req == 'mainscript' and 'Ready IP' in res:
                            res_farms.append(res)
                        else:
                            print('aiyo', i)
                    if len(res_farms) == len(CSB1_farms):
                        time.sleep(10)
                        if gg2344 > 4:

                            query = {"type": "main"}
                            update = {"$set": {"request": 'mainscript'}}
                            result = collection.update_one(query, update)
                        else:
                            gg2344 += 1
                    else:
                        gg2344 = 1
                        

                
            else:
                respo = 0
                update = {"$set": {"response": f'Changed IP🔴: {ip}'}}
                result = collection.update_one(query, update)
                ip = fix_ip(sb1, server_name1)
        else:
            return True


def get_coin_value_redeem(driver):
    try:
        continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'h2.blnc')
        for button in continue_buttons:
            if 'You' in button.text:
                print(f"Button found: {button.text}, clicking...")
                gg = button.text
                # Use regex to extract the numeric value
                #match = re.search(r'([\d,]+\.\d+)', gg)
                match = re.search(r'([\d,]+)', gg)
                if match:
                    gg = match.group(1).replace(',', '')  # Remove commas
                    gg = int(float(gg))  # Convert to integer
                    return gg
                else:
                    print("No coin value found in text.")
            else:
                print(button.text)
    except Exception as e:
        print(f"Error: {e}")
        pass
    return 0

                            
def control_panel():
    try:
        query = {"type": "main"}
        doc = collection.find_one(query)
        request = doc["request"]
        print(request)
        if request == 'ipfixer':
            ipfixer()
            return 2
        elif request == 'mainscript':
            print(request)
            return 1
        elif request == 'reset':
            print(request)
            return 3
        elif request == 'withdrawsky':
            print(request)
            return 4
        elif request == 'pause':
            print(request)
            return 5
        elif request == 'withdrawbay':
            print(request)
            return 6
        
        elif request == 'withdrawskydoller':
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


def click_random_category(sb):
    try:
        # Wait for the category buttons to be present
        category_buttons = WebDriverWait(sb, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.link-btn-list.video-categ-options li a div'))
        )
        
        # Print the category buttons
        for button in category_buttons:
            print(button.text)
        
        # Select a random button and click it
        random_button = random.choice(category_buttons)
        #sb.highlight(random_button)
        random_button.click()
        print(f"Clicked random category: {random_button.text}")
        return True
    
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
        return False
    

category_similarity_map = {
    'film': ['entertainment', 'none', 'music', 'people', 'gaming', 'nonprofit', 'news'],
    'auto': ['entertainment', 'none', 'sports', 'film', 'people', 'nonprofit', 'news'],
    'music': ['entertainment', 'people', 'film', 'none', 'gaming', 'nonprofit', 'news'],
    'pets': ['none', 'entertainment', 'people', 'film', 'nonprofit', 'howto', 'news'],
    'sports': ['none', 'entertainment', 'people', 'film', 'gaming', 'nonprofit', 'news'],
    'travel': ['none', 'people', 'film', 'entertainment', 'howto', 'nonprofit', 'news'],
    'gaming': ['entertainment', 'none', 'technology', 'people', 'film', 'howto', 'nonprofit', 'news'],
    'people': ['entertainment', 'none', 'music', 'film', 'nonprofit', 'technology', 'news', 'howto'],
    'comedy': ['entertainment', 'people', 'film', 'none', 'gaming', 'nonprofit', 'news'],
    'entertainment': ['people', 'none', 'film', 'gaming', 'nonprofit', 'howto', 'news', 'technology'],
    'news': ['nonprofit', 'education', 'nonprofit', 'none', 'people', 'film', 'entertainment', 'news'],
    'howto': ['education', 'science', 'nonprofit', 'none', 'people', 'film', 'news', 'entertainment'],
    'education': ['howto', 'science', 'nonprofit', 'none', 'people', 'film', 'entertainment', 'news'],
    'science': ['technology', 'education', 'none', 'entertainment', 'people', 'film', 'news'],
    'technology': ['science', 'gaming', 'education', 'none', 'entertainment', 'people', 'film', 'news'],
    'nonprofit': ['none', 'entertainment', 'people', 'film', 'gaming', 'education'],
    'family': ['entertainment', 'education', 'pets'],
    'scifi': ['film', 'gaming', 'none', 'entertainment', 'people', 'technology', 'gaming', 'nonprofit', 'news']
}

# Function to find the best matching category from a list
def get_best_matching_category(input_category, category_list):
    # Convert input category to lowercase
    input_category = input_category.lower()
    
    # Check if the input category is in the similarity map
    if input_category in category_similarity_map:
        # Get the list of similar categories for the input category
        similar_categories = [category.lower() for category in category_similarity_map[input_category]]
        
        # Find the first category in the provided list that matches the similar categories
        for category in category_list:
            if category.lower() in similar_categories:
                return category
    
    # If no match found, return False
    return False



def get_and_click_category(category, sb, selector_type='sky'):
    try:
        # Define CSS selectors based on selector_type
        if selector_type == 'sky':
            selector = 'ul.link-btn-list.video-categ-options li a div'
        elif selector_type == 'bay':
            selector = 'ul.link-btn-list.video-categ-options li a span'
        else:
            raise ValueError("Invalid selector_type specified")

        # Wait for the category buttons to be present
        category_buttons = WebDriverWait(sb, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
        )

        cateogry_options =[]
        # Print all category buttons for debugging
        for button in category_buttons:
            button_text = button.text.strip() if button.text else "No text"
            #print(f"Button text: {button_text}")
            cateogry_options2 = fix_broken_words([button_text])[0].lower()
            cateogry_options.append(cateogry_options2)
            print(f"Button text: {button_text}:{cateogry_options2}")

        # Fix the input category word
        fixed_category = fix_broken_words([category])[0].lower()

        # Try to find and click the matching category button
        for button in category_buttons:
            button_text = button.text.strip().lower() if button.text else ""
            fixed_button_text = fix_broken_words([button_text])[0].lower() if button_text else ""

            if fixed_category in fixed_button_text or fixed_button_text in fixed_category:
                print(f"Found and clicked category: {fixed_button_text} : Category:{fixed_category}")
                button.click()
                
                #cloudflare2(sb)  # Assuming this is your post-click function
                return True



        best_match = get_best_matching_category(fixed_category, cateogry_options)
        print(f"The best match for '{fixed_category}' is '{best_match}'.Category Options:{cateogry_options}")
        best_match = fix_broken_words([best_match])[0].lower()
        if best_match:
            # Try to find and click the matching category button
            for button in category_buttons:
                button_text = button.text.strip().lower() if button.text else ""
                fixed_button_text = fix_broken_words([button_text])[0].lower() if button_text else ""

                if best_match in fixed_button_text or fixed_button_text in best_match:
                    print(f"Found and clicked category2: {fixed_button_text} : Category:{best_match} and Btoon:{button_text}")
                    button.click()
                    #cloudflare2(sb)  # Assuming this is your post-click function
                    return True

        # List of fallback categories if the provided one is not found
        fallback_categories = ['Entertainment', 'None', 'People', 'Music', 'news', 'Technology', 'Science', 'Sci']
        fixed_fallback_categories = [fix_broken_words([cat])[0].lower() for cat in fallback_categories]

        # Try fallback categories
        for fallback_category in fixed_fallback_categories:
            for button in category_buttons:
                button_text = button.text.strip().lower() if button.text else ""
                fixed_button_text = fix_broken_words([button_text])[0].lower() if button_text else ""

                if fallback_category in fixed_button_text or fixed_button_text in fallback_category:
                    print(f"Found and clicked fallback category: {button.text}")
                    button.click()
                    #cloudflare2(sb)
                    return True

        # If no match is found, select a random button and click it
        random_button = random.choice(category_buttons)
        random_button.click()
        print(f"Clicked random category: {random_button.text}")
        return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def cal_ocr(sb, typetnf):
    try:
        title = sb.get_title()
        if 'Baymack' in title:
            if typetnf == True:
                capture_and_crop_regions([(871, 386, 247, 52)], ['captcha.png'])
                result = ocr.ocr('captcha.png')
                result = ''.join([item[1][0] for item in result[0]])
                result = ''.join(filter(str.isdigit, str(result)))
                print(result)
                if result:
                    gg_cleaned = result.replace('?', '')
                    if ' = ' in gg_cleaned:
                        calculation, expected_result = gg_cleaned.split(' = ')
                        calculated_value = eval(calculation)
                        expected_value = int(expected_result)
                        if calculated_value == expected_value:
                            print("True - The equation is correct.")
                            return 'True'
                        else:
                            print("False - The equation is incorrect.")
                            return 'False'
                    else:
                        print("False - The equation is incorrect.")
                        return 'False'

                else:
                    print("Error: Results Empty with new numCaptcha.")
            else:
                capture_and_crop_regions([(965, 379, 127, 62)], ['captcha.png'])
                result = ocr.ocr('captcha.png')
                result = ''.join([item[1][0] for item in result[0]])
                result = ''.join(filter(str.isdigit, str(result)))
                print(result)
                if result:
                    gg_cleaned = result.replace('?', '')
                    result = eval(gg_cleaned)
                    print(f"The result of {gg_cleaned} is: {result}")
                    return result
                else:
                    print("Error: Results Empty with new numCaptcha.")

        title = sb.get_title()
        if 'Popmack' in title:
            if typetnf == True:
                capture_and_crop_regions([(871, 393, 247, 52)], ['captcha.png'])
                result = ocr.ocr('captcha.png')
                result = ''.join([item[1][0] for item in result[0]])
                result = ''.join(filter(str.isdigit, str(result)))
                print(result)
                if result:
                    gg_cleaned = result.replace('?', '')
                    if ' = ' in gg_cleaned:
                        calculation, expected_result = gg_cleaned.split(' = ')
                        calculated_value = eval(calculation)
                        expected_value = int(expected_result)
                        if calculated_value == expected_value:
                            print("True - The equation is correct.")
                            return 'True'
                        else:
                            print("False - The equation is incorrect.")
                            return 'False'
                    else:
                        print("False - The equation is incorrect.")
                        return 'False'

                else:
                    print("Error: Results Empty with new numCaptcha.")
            else:
                capture_and_crop_regions([(965, 388, 127, 62)], ['captcha.png'])
                result = ocr.ocr('captcha.png')
                result = ''.join([item[1][0] for item in result[0]])
                result = ''.join(filter(str.isdigit, str(result)))
                print(result)
                if result:
                    gg_cleaned = result.replace('?', '')
                    result = eval(gg_cleaned)
                    print(f"The result of {gg_cleaned} is: {result}")
                    return result
                else:
                    print("Error: Results Empty with new numCaptcha.")




    except Exception as e:
        print(e)
    return None

def solve_calculating_capcha(sb):
    try:
        if sb.is_element_visible("a.try_again"):
            sb.click("a.try_again")
            print("Clicked the 'a.try_again' button.")
            return True
        else:
            if debug_mode:
                print("'a.try_again' button is not visible.")
    except Exception as e:
        if debug_mode:
            print(f"False' button is not visible.NoSuchElementException")


    try:
        if sb.is_element_visible("ul.link-btn-list.vid-category-options"):
            print('Numeric verification found')

            ul_element = sb.find_element("ul.link-btn-list.vid-category-options")
            buttons = ul_element.find_elements(By.TAG_NAME, "a")
            
            values = []
            question_type_is_trueorfalse = None
            for button in buttons:
                text = button.text.strip()
                if text.isdigit():  # Check if the text is a digit
                    values.append(int(text))
                    print(f"Button value: {text}")
                    question_type_is_trueorfalse = False
                elif 'True' in text or 'False' in text:
                    print(f"Button value: {text}")
                    question_type_is_trueorfalse = True

            if question_type_is_trueorfalse == True:
                answer = cal_ocr(sb, typetnf= True)
                print('Cal Answer:',answer)
                if answer:
                    for button in buttons:
                        if answer in button.text.strip():
                            button.click()
                            print("Clicked the button with the smallest value.")
                            return True
            if values:
                if question_type_is_trueorfalse == False:

                    # Find the smallest value
                    min_value = min(values)
                    answer = cal_ocr(sb, typetnf= False)
                    print('Cal Answer:',answer)
                    if answer:
                        if answer in values:
                            min_value = answer
                    else:
                        min_value = min(values)
                    print(f"Answer value: {min_value} values are: {values}")
                    
                    # Find the button with the smallest value and click it
                    for button in buttons:
                        if button.text.strip() == str(min_value):
                            try:
                                button.click()
                                print("Clicked the button with the smallest value.")
                                return True
                            except Exception as click_exception:
                                print(f"Error clicking the button: {click_exception}")
                                return False
                else:
                    print('Something Wrong with question_type_is_trueorfalse:',question_type_is_trueorfalse)
            else:
                if debug_mode:
                    print("No numeric values found.")
                #return False
            pyautogui.press('f5')
        else:
            if debug_mode:
                 print("Numeric verification element is not visible.")
            return False

    except Exception as e:
        if debug_mode:
            print(f"False' button is not visible.NoSuchElementException")
    

#############Baymack_STUFF


def facebook_login():
    pyautogui.click(1613, 137)
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    urkg = clipboard.paste()
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.typewrite('https://web.facebook.com/')
    pyautogui.press('enter')
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
                    url = facebook_cookies
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
                            pyautogui.keyDown('ctrl')
                            pyautogui.press('l')
                            pyautogui.keyUp('ctrl')
                            time.sleep(2)
                            pyautogui.typewrite(urkg)
                            pyautogui.press('enter')
                            time.sleep(5)
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


def get_coin_value(driver):
    try:
        # Locate the <a> element containing the coin value
        element = driver.find_element("a.button.class-for-instant-baymack-videos.header-button")
        
        # Extract the text content
        text = element.text.strip()
        
        # Extract the numeric part from the text
        coin_value = text.split()[0]  # Assuming the first part is the numeric value
        
        print(f"Coin value: {coin_value}")
        return coin_value
    
    except Exception as e:
        print(f"Error: {e}")
        return None



def baymack_login(driver):
    
    coin_val = None
    start_time = 1
    while not coin_val:
        coin_val = get_coin_value(driver)  # Assuming get_coin_value() is defined elsewhere
        if coin_val:
            print(f'Baymack Coins: {coin_val}')
            return coin_val
        else:
            time.sleep(1)

            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/fb_somewentwrong.png", region=(615, 434, 800, 500), confidence=0.90)
                pyautogui.click(13, 81)

            except Exception as e:
                print(e)
            try:
                print(driver.get_title())
                # Look for '.quiz-btn' and click if visible
                if driver.is_element_visible('.quiz-btn'):
                    buttons = driver.find_elements(By.CSS_SELECTOR, '.quiz-btn')
                    if buttons:
                        print(".quiz-btn button found, clicking...")
                        buttons[0].click()
                    else:
                        print(".quiz-btn not found!")
                else:
                    print("Element .quiz-btn is not visible!")
                
                time.sleep(1)

                # Check for a button with specific class name and "Continue as" text
                continue_buttons = driver.find_elements(By.CSS_SELECTOR, 'span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft')
                for button in continue_buttons:
                    if 'Continue as' in button.text:
                        time.sleep(1)
                        print(f"Button found: {button.text}, clicking...")
                        pyautogui.click(791, 737)
                        start_time += 1
                        print(start_time)
                        if start_time > 3:
                            pyautogui.keyDown('ctrl')
                            pyautogui.press('left')
                            pyautogui.keyUp('ctrl')
                            time.sleep(2)
                            start_time  = 1
                        break

                # Check if password input is found
                if driver.is_element_visible('input[name="pass"][type="password"]') and driver.get_title() == 'Facebook':
                    password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"][type="password"]')
                    print("Password field found, typing password...")
                    password_field.send_keys(fb_pass)
                    
                    # Look for "Continue" button after entering the password
                    continue_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Continue"][data-testid="sec_ac_button"]')
                    if continue_button:
                        print("Continue button found, clicking...")
                        continue_button.click()
                    else:
                        print("Continue button not found!")
                
                if driver.get_title() == 'Log in to Facebook' or driver.get_title() == 'Log into Facebook':
                    print(driver.get_title())
                    query = {"type": "main"}
                    update = {"$set": {"response": 'Facebook Need Logins'}}
                    collection.update_one(query, update)
                    facebook_login()
                    

                if driver.is_element_visible('a.btn.btn-fb-social[href="/auth/facebook/callback"]'):
                    fb_login_button = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-fb-social[href="/auth/facebook/callback"]')
                    print("Facebook login button found, clicking...")
                    fb_login_button.click()
                else:
                    print("Facebook login button not found!")

            except Exception as e:
                print(f'Baymack Login Error: {e}')
                query = {"type": "main"}
                update = {"$set": {"response": ' Login Error:'}}
                collection.update_one(query, update)

        # Optionally, sleep to avoid excessive loop iteration speed
        driver.sleep(2)




baymack_coins = 0
vnc_url = 0
vnc_window = 0
start_vnc = 0

earnpp_cookie = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/earnpp.json'
feyorra_cookie = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/feyorra.json'
claimcoin_cookie = 'https://raw.githubusercontent.com/mcnutthelen8/MFV6/main/claimcoins.json'



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

def generate_transformations(image):
    """Generate rotated and flipped versions of the image."""
    transformations = []
    transformations.append(image)  # Original image
    transformations.append(cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE))  # 90 degrees clockwise
    transformations.append(cv2.rotate(image, cv2.ROTATE_180))  # 180 degrees
    transformations.append(cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE))  # 90 degrees counterclockwise
    transformations.append(cv2.flip(image, 0))  # Flip vertically
    transformations.append(cv2.flip(image, 1))  # Flip horizontally
    transformations.append(cv2.flip(image, -1))  # Flip both ways
    return transformations

def find_least_similar_image(image_dir):
    if not os.path.isdir(image_dir):
        print("Directory does not exist.")
        return False

    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    if len(image_files) == 0:
        print("No images found in the directory.")
        return False

    threshold = 0.7
    similarities = {}
    similarity_groups = {}

    # Load each image and generate transformations
    transformed_images = {}
    for img_file in image_files:
        img_path = os.path.join(image_dir, img_file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        transformed_images[img_file] = generate_transformations(img)

    # Compare images including transformations
    for i, (img_file, img_transforms) in enumerate(transformed_images.items()):
        for j in range(i + 1, len(image_files)):
            other_img_file = image_files[j]
            other_img_transforms = transformed_images[other_img_file]

            for img1 in img_transforms:
                for img2 in other_img_transforms:
                    # Check sizes before comparing
                    if img1.shape[0] <= img2.shape[0] and img1.shape[1] <= img2.shape[1]:
                        # Compute similarity
                        similarity = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)[0][0]
                        similarities[(img_file, other_img_file)] = similarity

                        if similarity >= threshold:
                            similarity_groups.setdefault(img_file, []).append(other_img_file)
                            similarity_groups.setdefault(other_img_file, []).append(img_file)

    if len(similarity_groups) == 0:
        print("No similar image combinations found.")
        return False

    least_similar_image = None
    min_similar_count = float('inf')
    for img_file, similar_imgs in similarity_groups.items():
        similar_count = len(similar_imgs)

        if similar_count < min_similar_count:
            min_similar_count = similar_count
            least_similar_image = img_file

    for img_file in image_files:
        if img_file not in similarity_groups:
            print(f"Image {img_file} has no similar combination and is unique.")
            return f'{image_dir}/{img_file}'

    print(f"Image {least_similar_image} has the least similar combinations.")
    return f'{image_dir}/{least_similar_image}'

def solve_least_captcha(image):
    split_image_by_width('element_screenshot.png', 5, output_dir="output_pieces")
    val = find_least_similar_image("output_pieces")
    if val:
        print('similar slot 5')
        return val
    split_image_by_width('element_screenshot.png', 6, output_dir="output_pieces")
    val = find_least_similar_image("output_pieces")
    if val:
        print('similar slot 6')
        return val
    split_image_by_width('element_screenshot.png', 7, output_dir="output_pieces")
    val = find_least_similar_image("output_pieces")
    if val:
        print('similar slot 7')
        return val
    split_image_by_width('element_screenshot.png', 8, output_dir="output_pieces")
    val = find_least_similar_image("output_pieces")
    if val:
        print('similar slot 8')
        return val

    return False



def solve_least_img(driver):
    for i in range(5):
        pyautogui.moveTo(400, 400)
        time.sleep(1)
        driver.switch_to.default_content()
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        print(scroll_height, 'height')
        driver.execute_script(f"window.scrollTo(0, {scroll_height});")
        time.sleep(1)
        
        if driver.is_element_visible('img#rscaptcha_img'):
            print('rscaptcha Found')
            capture_element_screenshot(sb1, "img#rscaptcha_img")
            val = solve_least_captcha("element_screenshot.png")
            print('val', val)
            if val:
                try:
                    x, y = pyautogui.locateCenterOnScreen(val, confidence=0.85)
                    if x and y:
                        pyautogui.click(x, y)

                        return True
                except Exception as e:
                    print(e)
            else:
                return None

            
        #time.sleep(3)
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
            return True

    #time.sleep(1)

    print("No matching icon found.")

def cloudflare(sb, login = True):
    try:
        page_title = sb.get_title()
        gg = False
        while gg == False:
            try:

                if page_title != sb.get_title():
                    return
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.9)
                print("verify_cloudflare git Found")
                if x and y:
                    sb.disconnect() 
                    for i in range(1, 300):
                        
                        try:
                            time.sleep(1)
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare.png", confidence=0.9)
                            print("verify_cloudflare git Found")
                            try:
                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_box.png", confidence=0.9)
                                pyautogui.click(x, y)
                                time.sleep(5)
                                if login == False: 
                                    sb.connect()
                                    return True

                            except Exception as e:
                                print(e)
                                
                            try:
                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cloudflare_success.png", confidence=0.9)
                                pyautogui.click(x, y)
                                time.sleep(1)
                                if login == True: 
                                    sb.connect()
                                    return True

                            except Exception as e:
                                print(e)

                        except Exception as e:
                                print('cloudflare not found keep trying')

                    sb.connect()
                else:
                    gg = True
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
            
            sb1.execute_script("window.scrollTo(0, 1000);")
            #time.sleep(1)
            #sb1.disconnect()

            #    for i in range(1, 3):
            #        try:
            #            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/collect_your_reward.png", region=(507,156, 965, 919), confidence=0.9)
            #            #pyautogui.moveTo(random.randint(700, 1700), random.randint(300, 500), duration= 1)
            #            #pyautogui.moveTo(x, y, duration= 1)
            #            pyautogui.click(x, y)
            #            print("Collect button clicked.")
            #            time.sleep(2)
            #            pyautogui.press('f5')
            #            time.sleep(2)
            #            sb1.connect()
            #            return True
            #        except Exception as e:
            #            print(e)
            sb1.uc_click(button_selector)
            print("Collect button Not clicked.")
            #sb1.connect()
            return None
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
            solve_least_img(sb1)
        else:
            for i in range(1, 10):
                time.sleep(1)
                sb1.execute_script("window.scrollTo(0, 1000);")
                cloudflare(driver, True)
                try:
                    x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{captcha_image}.png", confidence=0.85)
                    if x and y: 

                        login_button = driver.find_element(By.CSS_SELECTOR, submit_button)
                        #click_element_with_pyautogui(driver, login_button)
                        #click_element_with_pyautogui(sb1, 'button[type="submit"]')
                        pyautogui.press('enter')
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
    pyautogui.press('enter')
    sb1.uc_click(submit_button)
    
    time.sleep(3)
    print("🚀 Login attempt made!")

def logging_bitmoon(url, driver, email, password, captcha_image, restrict_pages, submit_button):
    driver.uc_open(url)
    time.sleep(2)

    all_windows = driver.window_handles
    for window in all_windows:
        if window not in restrict_pages:
            driver.switch_to.window(window)
    while True:
        if driver.is_element_visible('a.nav-link.btn.btn-success'):
            try:
                # Locate and click the login button
                button = driver.find_element('a.nav-link.btn.btn-success')
                button.click()
                time.sleep(2)
                print('gggg')
                email_input = driver.find_element( 'input[type="text"]')
                email_input.send_keys(email)

                # Locate the password input by type attribute
                password_input = driver.find_element('input[type="password"]')
                password_input.send_keys(password)
                # Find the dropdown element by its id and select "Cloudflare" by value
                select_element = Select(driver.find_element('select.form-control.custom-select.mb-2'))
                select_element.select_by_value("2")  # Selects "Cloudflare"
                # Step 3: Wait for the CAPTCHA checkbox to be validated
                print("CAPTCHA Check")
                if captcha_image:
                    for i in range(1, 200):
                        time.sleep(1)
                        sb1.execute_script("window.scrollTo(0, 1000);")
                        cloudflare(driver, True)
                        try:
                            x, y = pyautogui.locateCenterOnScreen(f"/root/Desktop/MFV6/images/{captcha_image}.png", confidence=0.85)
                            if x and y: 

                                login_button = driver.find_element(By.CSS_SELECTOR, submit_button)
                                #click_element_with_pyautogui(driver, login_button)
                                #click_element_with_pyautogui(sb1, 'button[type="submit"]')
                                sb1.uc_click(submit_button)
                                #sb1.uc_click('button[type="submit"]')
                                pyautogui.press('enter')
                                #driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                                login_button.click(login_button)
                                time.sleep(5)
                                break
                        except Exception as e:
                            print(f'ERR:{e}') 

                print("✅ CAPTCHA validated")
                #click_element_with_pyautogui(sb1, 'button[type="submit"]')
                pyautogui.press('enter')
                time.sleep(5)
                
                print("🚀 Login attempt made!")
                
            except Exception as e:
                print(f'ERR: {e}')
        else:
            return

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
    driver.switch_to.window(current_window)

def handle_captcha_and_cloudflare(driver):
    cloudflare(driver, login = False)

def handle_site(driver, url, expected_title, not_expected_title , function, window_list ,captcha_handling=True):
    driver.uc_open(url)
    ready = False
    while not ready:
        time.sleep(1)
        all_windows = driver.window_handles
        for window in all_windows:
            if window not in window_list:
                driver.switch_to.window(window)
        current_title = driver.get_title()
        print(f"Current title: {current_title}")


            
            

        if not_expected_title == current_title:
            if function == 1:
                login_to_faucet('https://earn-pepe.com/login', sb1, 'khabibmakanzie@gmail.com', 'CQ2pNwi3zsFgat@', 'cloudflare_success', window_list, 'button#loginBtn')
            elif function == 2:
                login_to_faucet('https://feyorra.site/login', sb1, 'khabibmakanzie@gmail.com', 'D6.6fz9r5QVyziT', 'cloudflare_success', window_list, 'button#loginBtn')
            elif function == 3:
                login_to_faucet('https://claimcoin.in/login', sb1, 'khabibmakanzie@gmail.com', '@$uiJjkFfZU3K@e', None, window_list, 'button[type="submit"]') #'not_a_robot'
            elif function == 6:
                login_to_faucet('https://feyorra.top/login', sb1, 'khabibmakanzie@gmail.com', '%aYYcsSfcYjN%5x', 'rscaptcha', window_list, 'button[type="submit"]') #'not_a_robot'


        elif expected_title in current_title:
            if driver.current_window_handle not in window_list:
                if function == 4:
                    baymack_login(driver)
                elif function == 5:
                    logging_bitmoon('https://earnbitmoon.club/', sb1, 'ddilakshi232', 'p~Q18oQjmp}nv6g', 'cloudflare_success', window_list, 'button[type="submit"]') #'not_a_robot'

                ready = True

        elif 'Just' in current_title:
            if captcha_handling:
                handle_captcha_and_cloudflare(driver)
        
        else:
            print(f"{current_title} is not the expected title. Reconnecting...")
            all_windows = driver.window_handles
            for window in all_windows:
                if window not in window_list:
                    driver.switch_to.window(window)
            driver.uc_open(url)
            if captcha_handling:
                handle_captcha_and_cloudflare(driver)

    return driver.current_window_handle


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

#import easyocr
#reader = easyocr.Reader(['en'], gpu= False)
# Iterate over each image and extract text
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

# Example usage:



def feyorratop_claim(driver):
    try:
        original_window = driver.current_window_handle
        all_windows_before_click = driver.window_handles.copy()
        pyautogui.click(300, 200)

        all_windows = driver.window_handles
        for window in all_windows:
            if window not in all_windows_before_click:
                print(f"Closing new tab: {window}")
                driver.switch_to.window(window)
                driver.close()
        driver.switch_to.window(original_window)
        time.sleep(1)
        if 'Faucet | Feyorra' in driver.get_title():
            driver.execute_script("window.scrollTo(0, 1000);")

            if driver.is_element_visible('img#Imageid'):        
                
                capture_element_screenshot(driver, "img#Imageid")
                remove_border("element_screenshot.png", "element_screenshot.png")
                result = ocr.ocr('element_screenshot.png')
                try:
                    result = ''.join([item[1][0] for item in result[0]])
                    result = ''.join(filter(str.isdigit, str(result)))
                    print(result)
                    if result:
                        password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
                        password_input.send_keys(result)  
                        time.sleep(1)
                        sb1.uc_click('button[type="submit"]')
                    else:
                        pyautogui.press('f5')
                except Exception as e:
                    pyautogui.press('f5')
        else:
            driver.uc_open('https://feyorra.top/faucet')
    except Exception as e:
        print(f'ERR:{e}')

# Main logic
if run_sb1:
    sb1 = Driver(uc=True, headed=True, undetectable=True, undetected=True, user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path,  page_load_strategy='none')
    sb1.maximize_window()
    sb1.uc_open("chrome://extensions/")
    print(sb1.get_title())
    
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
    


def open_faucets():
    current_window = sb1.current_window_handle
    all_windows = sb1.window_handles
    for window in all_windows:
        if window != current_window:
            sb1.switch_to.window(window)
            sb1.close()  # Close the tab
    sb1.switch_to.window(current_window)
    time.sleep(1)
    #ipfixer()
    ip_required = fix_ip(sb1, server_name1)
    ip_address = get_ip(sb1)

    if earnpp:
        earnpp_window = handle_site(sb1, "https://earn-pepe.com/member/faucet","Faucet | Earn-pepe" , "Home | Earn-pepe", 1, [])
        print(f"EarnPP window handle: {earnpp_window}")
    else:
        earnpp_window = None
    if feyorra:
        sb1.open_new_window()
        feyorra_window = handle_site(sb1, "https://feyorra.site/member/faucet", "Faucet | Feyorra" , "Home | Feyorra", 2, [earnpp_window])
        print(f"Feyorra window handle: {feyorra_window}")
    else:
        feyorra_window = None
    if claimcoin:
        sb1.open_new_window()
        claimcoin_window = handle_site(sb1, "https://claimcoin.in/faucet", "Faucet | ClaimCoin - ClaimCoin Faucet", "ClaimCoin - MultiCurrency Crypto Earning Platform", 3, [earnpp_window, feyorra_window])
        print(f"ClaimCoin window handle: {claimcoin_window}")
    else:
        claimcoin_window = None

    if baymack:
        sb1.open_new_window()
        #baymack_login(sb1)
        baymack_window = handle_site(sb1, "https://www.baymack.com/videos", "Baymack", "Baymack", 4, [earnpp_window, feyorra_window, claimcoin_window])
        print(f"Baymack window handle: {claimcoin_window}")
    else:
        baymack_window = None

    if bitmoon:
        sb1.open_new_window()
        #baymack_login(sb1)
        bitmoon_window = handle_site(sb1, "https://earnbitmoon.club/", "Earnbitmoon - ultimate faucet !", "Earnbitmoon - ultimate faucet !", 5, [earnpp_window, feyorra_window, claimcoin_window,baymack_window])
        print(f"bitmoon_window window handle: {bitmoon_window}")
    else:
        bitmoon_window = None
    if feyorratop:
        sb1.open_new_window()
        #baymack_login(sb1)
        feyorratop_window = handle_site(sb1, "https://feyorra.top/faucet", "Faucet | Feyorra", "Home | Feyorra", 6, [earnpp_window, feyorra_window, claimcoin_window,baymack_window, bitmoon_window])
        print(f"feyorratop_window window handle: {feyorratop_window}")
    else:
        feyorratop_window = None

    all_window_handles = [earnpp_window, feyorra_window, claimcoin_window, baymack_window, bitmoon_window, feyorratop_window]
    close_extra_windows(sb1, all_window_handles)

    print(f"Windows: EarnPP: {earnpp_window}, Feyorra: {feyorra_window}, ClaimCoin: {claimcoin_window}, Baymack:{baymack_window}")
    return earnpp_window, feyorra_window, claimcoin_window,baymack_window,bitmoon_window, feyorratop_window,  ip_address, ip_required


def debug_messages(messages):
    if debug_mode:
        print(messages)

earnpp_count = 0 
feyorra_count = 0
claimcoin_count = 0

earnpp_window, feyorra_window, claimcoin_window,baymack_window,bitmoon_window, feyorratop_window,  ip_address, ip_required = open_faucets()
reset_count = 0
previous_reset_count = 0
time.sleep(2)
start_time = time.time()
import img_captcha
import img_captcha_bay
#pyautogui.scroll(2000)
def check_icon_captcha_exists(sb):
            try:
                if sb.is_element_visible(".captcha-modal__icons .captcha-image"):
                    print("Icon captcha exists.")
                    #time.sleep(2)
                    sb.maximize_window()
                    #activate_window_by_id(id)
                    title =  sb.get_title()
                    if title == 'Popmack':
                        #sb1.scroll_to_top()
                        sb.execute_script("window.scrollTo(0, 0);")
                        # Assuming img_captcha.solve_icon_captcha() is defined elsewhere
                        img_captcha.solve_image_skylom()
                        time.sleep(1)
                        return True
                    if title == 'Baymack':
                        #sb1.scroll_to_top()
                        sb.execute_script("window.scrollTo(0, 0);")
                        # Assuming img_captcha.solve_icon_captcha() is defined elsewhere
                        img_captcha_bay.solve_image_skylom()
                        time.sleep(2)
                        return True
                else:
                    if debug_mode:
                        print("Icon captcha does not exist.")
                    return False
            except Exception as e:
                if debug_mode:
                # Handle the case where the container or images are not found
                    print("Exception: Icon captcha container not found.")
                return False



current_duration = 1
current_duration_bay = 1
reclick_waits = 1
category = 0
category_bay = 0
basic_info = True

current_duration2 = 1
reclick_waits2 = 1
category2 = 0

basic_info2 = True
start_time2 = time.time()

previous_duration_bay = 0
#baymack_coins = 0
previous_duration = 0
print('Starting Loop')
while True:
    try:
        ip_address = get_ip(sb1)
        debug_messages(f'Ip address Found:{ip_address}')
        if ip_address == ip_required:
            debug_messages(f'Ip address Match:{ip_address}')

            all_window_handles = [earnpp_window, feyorra_window, claimcoin_window,baymack_window,bitmoon_window, feyorratop_window]
            close_extra_windows(sb1, all_window_handles)


            if reset_count > 5:
                earnpp_window, feyorra_window, claimcoin_window,baymack_window,bitmoon_window, feyorratop_window,  ip_address, ip_required = open_faucets()

            if previous_reset_count == reset_count:
                reset_count = 0
            else:
                previous_reset_count = reset_count
            if earnpp:
                try:
                    debug_messages(f'Switching Pages to EarnPP')
                    sb1.switch_to.window(earnpp_window)
                    debug_messages(f'Getting Pages Titile:EarnPP')
                    title =sb1.get_title()
                    if 'Faucet | Earn-pepe' in title:
                        debug_messages(f'Solving Icon Captcha on EarnPP')
                        solve_icon_captcha(sb1)
                        debug_messages(f'Solved Icon Captcha on EarnPP')

                    elif 'Just' in title:
                        debug_messages(f'Just.. Found on EarnPP')

                        cloudflare(sb1, login = False)
                        debug_messages(f'Just Fixed EarnPP')
                    else:
                        debug_messages(f'EarnPP not Found:{title} | reset:{reset_count}')
                        reset_count +=1

                except Exception as e:
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
                        solve_icon_captcha(sb1)
                            
                    elif 'Just' in title:
                        debug_messages(f'Just.. Found on Feyorra')
                        cloudflare(sb1, login = False)
                        debug_messages(f'Just Fixed Feyorra')
                    else:
                        debug_messages(f'Feyorra not Found:{title} | reset:{reset_count}')
                        reset_count +=1
                except Exception as e:
                    debug_messages(f'ERR on Feyorra:{e}')
                    reset_count +=1

            if claimcoin:
                try:
                    debug_messages(f'Time capture in ClaimCoins')
                    elapsed_time = time.time() - start_time
                    seconds_only = int(elapsed_time)
                    debug_messages(f'ClaimCoins Seconds:{seconds_only}')
                    if seconds_only > 12:
                        debug_messages(f'Switching Pages to ClaimCoins:{seconds_only}')
                        sb1.switch_to.window(claimcoin_window)
                        debug_messages(f'Getting Pages Titile:ClaimCoins')
                        title =sb1.get_title()
                        if 'Faucet | ClaimCoin' in title:
                            debug_messages(f'Solving Icon Captcha on ClaimCoins')
                            cc_faucet =  find_and_click_collect_button(sb1)
                            if cc_faucet:
                                debug_messages(f'Solved Icon Captcha on Claimcoins')
                                claimcoin_count = 1 
                                start_time = time.time()
                            sb1.switch_to.window(claimcoin_window)
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on Claimcoins')

                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed Claimcoins')
                        else:
                            debug_messages(f'ClamCoim not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                    
                except Exception as e:
                    debug_messages(f'ERR on ClamCoim:{e}')
                    reset_count +=1


            if baymack:

                try:
                    debug_messages(f'Switching Pages to baymack')
                    sb1.switch_to.window(baymack_window)
                    debug_messages(f'Getting Pages Titile:baymack')
                    play_button(sb1)
                    playback_check(sb1)
                    remove_pink(sb1)
                    check_icon_captcha_exists(sb1)

                    cloudflare(sb1)
                    solve_calculating_capcha(sb1)
                    title =sb1.get_title()

                    if 'Baymack' in title:
                        previous_duration_bay = current_duration_bay
                        current_duration_bay = get_current_duration(sb=sb1)
                        if current_duration_bay == previous_duration_bay:
                            time.sleep(2) #and current_duration_bay == 0 :
                            print(f'reclick_waits2:{reclick_waits2}')
                            reclick_waits2 +=1
                            if reclick_waits2 > 40:
                                print(f'reopenning reclick {reclick_waits2}')
                                query = {"type": "main"}
                                update = {"$set": {"request": 'reset'}}
                                result = collection.update_one(query, update)

                                print(sb1.get_title())
                                reclick_waits2 = 0

                            if reclick_waits2 == 15 or reclick_waits2 == 20 or reclick_waits2 == 26 or reclick_waits2 == 30:
                                #reclick_button(sb1)
                                pyautogui.click(990, 430)
                                pyautogui.press('f5')
                                time.sleep(3)

                        else:
                            reclick_waits2 = 1
                        
                        if current_duration_bay:
                            if current_duration_bay >= 20:
                                if category_bay == 0:
                                    video_link = get_youtube_link(sb1) 
                                    category_bay = get_video_infog(video_link, sb1)
                                    if category_bay:
                                        if debug_mode:
                                            print(f"Category: {category_bay}")
                                        if "Howto" in category_bay:
                                            category_bay = "How-To"
                                        elif "Science" in category_bay:
                                            category_bay = "Sic-fi"
                                        elif "Beauty" in category_bay:
                                            category_bay = "Beauty"
                                        elif "Nonprofit" in category_bay:
                                            category_bay = "Nonprofit"    
                                        elif "Film" in category_bay:
                                            category_bay = "Film"        
                                        elif "Auto" in category_bay:
                                            category_bay = "Auto"    
                                        elif "Technology" in category_bay:
                                            category_bay = "Technology"
                                        title = sb1.get_title()
                                        if title == 'Baymack':        
                                            #ip_address =get_ip(sb1)
                                            #proxycheck = get_proxycheck(sb1, ip_address, server_name= server_name1)
                                            coins = get_coin_value(sb1)
                                            if coins:
                                                baymack_coins = coins
                                            else:
                                                print('Bymack Coins not availible')
                                    if category_bay == 0 or category_bay == None:
                                        pyautogui.press('f5')
        
                                    else:
                                        print(f'category_bay is not defined{category_bay}')
                                else:
                                    if basic_info:
                                        #print("Category is ",category)
                                        print(f"Video duration_bay: {current_duration_bay} and Category is {category_bay}", end="\r")

            
                            else:
                                category_bay = 0
                                
                                if basic_info:
                                    print(f"Video duration_bay: {current_duration_bay} and Category is {category_bay}", end="\r")
                                    #print('Video is Fresh')

                        #else:
                            #cloudflare(id1,sb1)

                        if check_category_question(sb1) == True:
                            print('Getting IP at 10 sec..')
                            #ip_address =get_ip(sb1)
                            if ip_address == ip_address:
                                        if ip_address == ip_address:
                                            title = sb1.get_title()
                                            if category_bay != 0 and title == 'Baymack':
                                                print('starting to answer category confirm')
                                                title = sb1.get_title()
                                                if title:
                                                    print(title,'Category_bay:',category_bay)
                                                    get_and_click_category(category_bay, sb1, selector_type='bay')
                                                    #solve_image_category(sb1, category_bay, id1)

                                            elif category_bay == 0:
                                                video_link = get_youtube_link(sb1) 
                                                category_bay = get_video_infog(video_link, sb1)

                                                print(f"Category: {category_bay}")
                                                if category_bay:
                                                    if "Howto" in category_bay:
                                                        category_bay = "How-To"
                                                    elif "Science" in category_bay:
                                                        category_bay = "Sic-fi"
                                                    elif "Nonprofit" in category_bay:
                                                        category_bay = "Nonprofit"    
                                                    elif "Film" in category_bay:
                                                        category_bay = "Film"        
                                                    elif "Auto" in category_bay:
                                                        category_bay = "Auto"    
                                                    elif "Technology" in category_bay:
                                                        category_bay = "Technology"        
                                                if category_bay == 0 or category_bay == None:
                                                    pyautogui.press('f5')
                            else:
                                #ip_address =get_ip(sb)
                                print(f'IP _bays not Matched in IF category {ip_address}, Required: {ip_required}')
                                print('Getting IP at after found category...')
                                query = {"type": "main"}
                                update = {"$set": {"response": f'IP is not Matched{ip_address}, Required: {ip_required}'}}
                                result = collection.update_one(query, update)

                                update2 = {"$set": {"request": 'ipfixer'}}
                                result = collection.update_one(query, update2)
                                time.sleep(3)


                    elif 'Just' in title:
                        debug_messages(f'Just.. Found on baymack')

                        cloudflare(sb1, login = False)
                        debug_messages(f'Just Fixed baymack')
                    else:
                        debug_messages(f'baymack not Found:{title} | reset:{reset_count}')
                        reset_count +=1
                except Exception as e:
                    debug_messages(f'ERR on baymack:{e}')
                    reset_count +=1

            if feyorratop:
                try:
                        debug_messages(f'Time capture in feyorratop')
                        sb1.switch_to.window(feyorratop_window)
                        debug_messages(f'Getting Pages Titile:feyorratop')
                        title =sb1.get_title()
                        if 'Faucet | Feyorra' in title:
                            debug_messages(f'Solving Icon Captcha on feyorratop')
                            feyorratop_claim(sb1)
                        elif 'Just' in title:
                            debug_messages(f'Just.. Found on feyorratop')

                            cloudflare(sb1, login = False)
                            debug_messages(f'Just Fixed feyorratop')
                        else:
                            
                            debug_messages(f'feyorratop not Found:{title} | reset:{reset_count}')
                            reset_count +=1
                    
                except Exception as e:
                    debug_messages(f'ERR on feyorratop:{e}')
                    reset_count +=1

        else:
            print('Ip fucked')
            #ip_required = fix_ip(sb1, server_name1)
            #ip_address = get_ip(sb1)
    except Exception as e:
        print(f'Oh Hell No{e}')
