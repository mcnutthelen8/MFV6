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
import difflib
import cv2
import numpy as np
from PIL import Image
# Connect to the MySQL database
debug_mode = False

ip_required = 0
farm_id = 1
farm_id2 = 2
farm_id3 = 3
farm_id4 = 4
run_sb1 = True
run_sb2 = False
run_sb3 = False
run_sb4 = False
with_baymack = True
server_name1 = 'estonia'
server_name2 = 'romania'
server_name3 = 'poland'
server_name4 = 'hungary'

chrome_binary_path = '/opt/google/chrome/google-chrome'
chrome_user_data_dir = '/root/.config/google-chrome/'

chrome_user_data_dir2 = '/root/.config/google-chrome/second'
chrome_user_data_dir3 = '/root/.config/google-chrome/third'
chrome_user_data_dir4 = '/root/.config/google-chrome/four'


from pymongo import MongoClient


mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"
client = MongoClient(mongo_uri)
db = client['MoneyFarmV6'] 
collection = db[f'Farm{farm_id}']

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
        "Ip": ip
        
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
    original_window = driver.current_window_handle
    driver.open_new_window()
    #driver.switch_to.newest_window()
    driver.open('https://api.ipify.org/')
    ip_address = driver.get_text('body')
    print('IP =', ip_address)
    driver.close()
    driver.switch_to.window(original_window)
    return ip_address

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


def element_exists(sb, selector):
    try:
        return sb.is_element_visible(selector)
    except Exception:
        return False

def verify_success(sb):
    sb.assert_element('img[alt="Logo Assembly"]', timeout=5)
    sb.sleep(4)

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
        return None
    
def play_button(sb):
    current_duration = get_current_duration(sb)
    if current_duration == 0:
        play_button_selector = '.ytp-large-play-button'
        try:
            if sb.is_element_visible('iframe'):
                sb.switch_to.frame(sb.find_element(By.TAG_NAME, "iframe"))
                if sb.is_element_visible(play_button_selector):
                    play_button_elements = sb.find_elements(By.CSS_SELECTOR, play_button_selector)
                    print("Play button found")
                    play_button = play_button_elements[0]
                    time.sleep(1)
                    play_button.click()
                    print("Play button Clicked")
                    sb.switch_to.default_content()
                    #time.sleep(1)
                if sb.is_element_visible('button.ytp-ad-skip-button-modern'):
                    play_button_elements = sb.find_elements(By.CSS_SELECTOR, 'button.ytp-ad-skip-button-modern')
                    print("Play button found")
                    play_button = play_button_elements[0]
                    time.sleep(1)
                    play_button.click()
                    print("Play button Clicked")
                    sb.switch_to.default_content()
                    #time.sleep(1)
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

def get_video_infog(video_url, driver, timeout=8 ):
    original_window = driver.current_window_handle
    driver.open_new_window()
    #driver.switch_to.newest_window()
    driver.open(f'view-source:{video_url}')
    data = driver.get_text('body')
    html_content = str(data)
    soup = BeautifulSoup(html_content, 'html.parser')
    category_tag = soup.find('meta', itemprop='genre')
    category = category_tag['content'] if category_tag else None
    print(f"Category For This Video is {category}")
    driver.close()
    driver.switch_to.window(original_window)
    print(video_url)
    return category



def get_youtube_link(sb):
    page_source = sb.get_page_source()
    soup = BeautifulSoup(page_source, 'html.parser')
    a_tag = soup.find('a', class_='twitter')
        
    try:
        if a_tag:
            # Extract the href attribute
            href = a_tag.get('href')
            
            # Use regex to find the YouTube URL from the href
            youtube_url_match = re.search(r'https://www\.youtube\.com/watch\?v=[\w-]+', href)
            
            if youtube_url_match:
                #print(youtube_url_match.group(0))
                return youtube_url_match.group(0)
            else:
                return 0
        else:
            return 0

 
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
        return 0

def cloudflare(id,sb):
    page_title = sb.get_title().strip()
    
    if page_title == 'Just a moment...':
        activate_window_by_id(id)
        print('tru')
        sb.uc_gui_handle_captcha()
        sb.uc_gui_click_captcha()
        sb.post_message("CouldFlare Found", duration=3)
    elif page_title == 'www.skylom.com | 502: Bad gateway' or page_title == 'www.skylom.com | 503: Bad gateway':
        print('www.skylom.com | 502: Bad gateway')
        sb.refresh()


def get_and_click_category(category, sb):
    try:
        # Wait for the category buttons to be present
        category_buttons = WebDriverWait(sb, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.link-btn-list.video-categ-options li a div'))
        )
        
        # Print the category buttons
        for button in category_buttons:
            print(button.text)
        
        # Find and click the assigned category
        for button in category_buttons:
            button_text = button.text.strip().lower()
            category_lower = category.lower()
            
            # Check for partial match
            if category_lower in button_text or button_text in category_lower:
                print(f"Found and clicked category: {button.text}")
                button.click()
                return True
        
        if debug_mode:
            print(f"Category '{category}' not found")
        return False
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {str(e)}")
        return False


    
    
def check_category_question(sb, debug_mode=False):
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

def click_next_video(sb):
    next_video_selector = 'a.retention-click.themeBtn.bluebtn#nextvideo'
    try:
        if sb.is_element_visible(next_video_selector):
            
            #sb.highlight(next_video_selector)
            sb.click(next_video_selector)
            print("Next Video button clicked")
            return True
    except (NoSuchElementException, TimeoutException, Exception):
        if debug_mode:
            print("Next Video button not found")
    next_video_selector = '#next-video'
    try:
        if sb.is_element_visible(next_video_selector):
            
            #sb.highlight(next_video_selector)
            sb.click(next_video_selector)
            print("Next Video button clicked")
            return True
    except (NoSuchElementException, TimeoutException, Exception):
        if debug_mode:
            print("Next Video button not found")
    next_video_selector = '#nextvideo'
    try:
        if sb.is_element_visible(next_video_selector):
            
            #sb.highlight(next_video_selector)
            sb.click(next_video_selector)
            print("Next Video button clicked")
            return True
    except (NoSuchElementException, TimeoutException, Exception):
        if debug_mode:
            print("Next Video button not found")

    next_video_selector = 'a.retention-click.themeBtn'
    try:
        if sb.is_element_visible(next_video_selector):
            
            #sb.highlight(next_video_selector)
            sb.click(next_video_selector)
            print("Next Video button clicked")
            return True
    except (NoSuchElementException, TimeoutException, Exception):
        if debug_mode:
            print("Next Video button not found")
    next_video_selector = 'a.themeBtn'
    try:
        if sb.is_element_visible(next_video_selector):
            
            #sb.highlight(next_video_selector)
            sb.click(next_video_selector)
            print("Next Video button clicked")
            return True
    except (NoSuchElementException, TimeoutException, Exception):
        if debug_mode:
            print("Next Video button not found")
        return False
    
def click_false_button(sb):
    try:
        if sb.is_element_visible("a.try_again"):
            sb.click("a.try_again")
            print("Clicked the 'a.try_again' button.")
            return True
        else:
            if debug_mode:
                print("'a.try_again' button is not visible.")
                
        if sb.is_element_visible("a.themeBtn.brdr-btn"):
            sb.click("a.themeBtn.brdr-btn")
            print("Clicked the 'False' button.")
            return True
        else:
            if debug_mode:
                print("'False' button is not visible.")
            return False
    except Exception as e:
        if debug_mode:
            print(f"False' button is not visible.NoSuchElementException")
    try:
        if sb.is_element_visible("a.themeBtn.brdr-btn"):
            sb.click("a.themeBtn.brdr-btn")
            print("Clicked the 'False' button.")
            return True
        else:
            if debug_mode:
                print("'False' button is not visible.")
            return False
    except Exception as e:
        if debug_mode:
            print(f"False' button is not visible.NoSuchElementException")
        return False

def handle_random_number_buttons(self):
    try:
        if self.is_element_visible("ul.link-btn-list.vid-category-options"):
            print('Numeric verification found')

            ul_element = self.find_element("ul.link-btn-list.vid-category-options")
            buttons = ul_element.find_elements(By.TAG_NAME, "a")
            
            values = []
            for button in buttons:
                text = button.text.strip()
                if text.isdigit():  # Check if the text is a digit
                    values.append(int(text))
                    print(f"Button value: {text}")
            
            if values:
                # Find the smallest value
                min_value = min(values)
                print(f"Smallest value: {min_value}")
                
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
                if debug_mode:
                    print("No numeric values found.")
                return False
        else:
            if debug_mode:
                 print("Numeric verification element is not visible.")
            return False
    except NoSuchElementException:
        if debug_mode:
            print("NoSuchElementException: Numeric verification element not found.")
        return False
    except Exception as e:
        if debug_mode:
               print(f"Exception: {e}")
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
    

def get_ipaddress():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        ip_info = response.json()
        ip_address = ip_info.get('ip', 'IP address not found')
        print(f"Public IP Address: {ip_address}")
        return ip_address
    except requests.RequestException as e:
        print(f"Error retrieving IP address: {e}")
        return None

def get_proxycheck(ip, server_name):
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
            print("Error: Status not OK")
            return None, None
    except requests.RequestException as e:
        print(f"Error retrieving IP address and proxy status: {e}")
        return None, None


def get_ipscore(ip):
    url = f'https://ipqualityscore.com/api/json/ip/Bfg1dzryVqbpSwtbxgWb1uVkXLrr1Nzr/{ip}?strictness=3&allow_public_access_points=false'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        result = response.json()
        #print(result)  # Print the raw response for debugging

        # Assign specific data fields to variables
        fraud_score = result.get('fraud_score', 'Unknown')
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
        if vpn == False and tor == False and active_vpn == False and active_tor == False and bot_status == False and recent_abuse == False:
            return True
        else:
            return None
    except requests.RequestException as e:
        print(f"Error retrieving IP data: {e}")
        return None, None, None, None, None, None, None, None

def mysterium_vpn_connect(server_name):
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

def mysterium_vpn_Recon_ip(server_name):
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
        proxycheck = get_proxycheck(ip_address, server_name= name)
        if ipscore and proxycheck == 200:
            print(f'Good IP found: {ip_address}')
            return ip_address
        elif proxycheck == 50 or proxycheck == 200:
            print(f'Country ok /Bad IP detected: {ip_address}. Changing IP...')
            #mysterium_vpn_Recon_ip(name)
            time.sleep(5)
        else:
            print(f'Bad IP detected: {ip_address}. Changing IP...')
            #mysterium_vpn_connect(name)
            print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
            time.sleep(5)

#######Solve###########
import Levenshtein

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
        "comedy", "education", "gaming", "music", "Music", "science","technology",
        "family" ,"entertainment","family entertainment", 'none', "news","politics", "people",
        "travel","travel & events", "sports", "beauty", "nonprofit", "howto", "film","pets", "food", "sic-fi","people & blogs","news & politics","auto",
    
    ]
    fixed_list = []
    
    for word in word_list:
        word = word.replace('0', 'o')
        word = word.replace('5', 's')
        word = word.replace('6', 's')
        word = word.replace('$', 's')
        word = word.replace('8', '&')
        word = word.replace('1', 'i')
        word = word.replace('[', 'c')
        word = word.replace('{', 'c')
        word = word.replace('(', 'c')
        word = word.replace('4', 'a')
        word = word.replace('7', 'e')
        word = word.replace('<', 'c')
        word = word.replace('*', 'e')
        if word == 'F-w':
            word = 'film'
        if word == '1F()Ve':
            print('travel')
            word = 'travel'
        letter_count = sum(1 for char in word if char.isalpha())
        fixed_word = find_most_similar_word(word.lower(), reference_list)

        if letter_count < 10:
            word = word.replace(' ', '')
            print(letter_count, word)
            if letter_count < 4:
                fixed_word = find_most_similar_word2(word.lower(), reference_list)
        else:
            fixed_word = find_most_similar_word(word.lower(), reference_list)
        if fixed_word == "politics":
            fixed_word ="news"
        if fixed_word == "blogs":
            fixed_word ="people"
        if fixed_word == "people & blogs":
            fixed_word ="people"
        if fixed_word == "news & politics":
            fixed_word ="news"
        if fixed_word == "family entertainment":
            fixed_word ="family"
        if fixed_word is None:
            fixed_word ="none"

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
        (622, 766, 320, 85),  # Example region 1 (x, y, width, height)
        (960, 766, 320, 85),  # Example region 2
        (622, 862, 320, 85),  # Example region 3
        (960, 862, 320, 85)   # Example region 4
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
        (610,705, 300, 50),  # Example region 1 (x, y, width, height)
        (1011,705, 300, 50),  # Example region 2
        (610,767, 300, 50),  # Example region 3
        (1011,767, 300, 50)   # Example region 4
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


from paddleocr import PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en',  drop_score=0)

def remove_lines_from_image(input_image_path, output_image_path, np1 = 2 , np2 = 1):
    image = cv2.imread(input_image_path, 0)
    kernel_dilation = np.ones((2, 1), np.uint8)
    kernel_erosion = np.ones((2, 2), np.uint8)
    dilation = cv2.dilate(image, kernel_dilation, iterations=1)
    erosion = cv2.erode(dilation, kernel_erosion, iterations=1)
    kernel_closing = np.ones((np1, np2), np.uint8)
    closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel_closing)
    cv2.imwrite(output_image_path, closing)

def captcha_to_text(image_paths):
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


def solve_image_category(drive, category, window):
    start_time = time.time()
    activate_window_by_id(window)
    titile =drive.get_title()
    print(titile)
    time.sleep(1)
    if titile == 'Skylom':
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
                            if title == 'Skylom':
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
                                    pyautogui.click(749, 743)
                                if position == 1:
                                    pyautogui.click(1100, 743)
                                if position == 2:
                                    pyautogui.click(777, 788)
                                if position == 3:
                                    pyautogui.click(1094, 788)

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
brave_user_data_dir = '/home/coder/.config/BraveSoftware/Brave-Browser/'
brave_binary_path = '/usr/bin/brave-browser'

#chrome_binary_path = '/opt/google/chrome/google-chrome'
#chrome_user_data_dir = '/home/user/.config/google-chrome/'
skylom_window = 0
baymack_window = 0
if run_sb1:
    sb1 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
    id1 = get_current_window_id()
    sb1.maximize_window()
    ip_required = fix_ip(sb1, server_name1)
    ip_address = get_ip(sb1)
    sb1.open("https://www.skylom.com/videos")
    skylom_window = sb1.current_window_handle
    
    if with_baymack == True:
        sb1.open_new_window()
        sb1.open("https://www.baymack.com/videos")
        baymack_window = sb1.current_window_handle

    print(sb1.get_title())

if run_sb2:
    sb2 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir2, binary_location=chrome_binary_path)
    id2 = get_current_window_id()
    sb2.maximize_window()
    ip_required2 = fix_ip(sb2, server_name2)
    ip_address2 = get_ip(sb2)
    sb2.open("https://www.skylom.com/videos")
    print(sb1.get_title())

    #print(f'IP Matched {ip_address}')
if ip_address == ip_required:
    if ip_address == ip_required:

        import img_captcha
        import img_captcha_bay
        #import ocr_captcha

        def check_number_captcha_exists(sb, id):

            try:
                # Attempt to find the number captcha image
                try:
                    if sb.is_element_visible("#numberCaptcha"):
                        print("Number captcha exists.")
                        sb.maximize_window()
                        activate_window_by_id(id)
                        #sb1.scroll_to_top()
                        sb1.execute_script("window.scrollTo(0, 0);")
                        #answer = ocr_captcha.solve_ocr()
                        try:
                            #sb.type("input.captcha[type='text']", str(answer))
                            answer = sb.get_text("input.captcha[type='text']")
                            str_value = str(answer)
                            str_value.isdigit()
                            if answer:
                                if str_value.isdigit():
                                    sb.click("input.btn.btn-info")
                                else:
                                    sb.type("input.captcha[type='text']", '1000')
                                    print(f'answer contain string{answer} {str(str_value.isdigit())}')

                            print(f"Captcha filled and form submitted. {answer}")
                            return True
                        except Exception:
                            if debug_mode:
                                print(f"Error finding input box or submit button: {e}")
                            return False
                    else:
                        if debug_mode:
                            print("Number captcha exists but is not displayed.")
                        return False
                except Exception:
                    if debug_mode:
                        print("Number captcha does not exist.")
                    return False

            except Exception as e:
                if debug_mode:
                    print(f"An unexpected error occurred: {e}")
                return False
            
        def check_icon_captcha_exists(sb, id):
            try:
                if sb.is_element_visible(".captcha-modal__icons .captcha-image"):
                    print("Icon captcha exists.")
                    time.sleep(2)
                    sb.maximize_window()
                    activate_window_by_id(id)
                    title =  sb.get_title()
                    if title == 'Skylom':
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
                        time.sleep(1)
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
        start_time = time.time()

        current_duration2 = 1
        reclick_waits2 = 1
        category2 = 0

        basic_info2 = True
        start_time2 = time.time()


        ip_address = 0
        ip_address2 = 0
        ip_address3 = 0
        ip_address4 = 0
        previous_duration_bay = 0
        baymack_coins = 0
        previous_duration = 0
        while True:
            time.sleep(1)
            cloudflare(id1,sb1)
            sb1.switch_to.default_content()
            sb1.execute_script("window.scrollTo(0, 0);")
            play_button(sb1)
            playback_check(sb1)
            remove_pink(sb1)
            title = sb1.get_title()


##################################################################
##########################SB-1####################################
##################################################################
            if title == 'Skylom':
                previous_duration = current_duration
                current_duration = get_current_duration(sb=sb1)
                if current_duration == previous_duration and current_duration == 0 :
                    print(f'reclick_waits:{reclick_waits}')
                    reclick_waits +=1
                    if reclick_waits > 155:
                        print(f'reopenning reclick {reclick_waits}')
                        sb1.quit()
                        sb1 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
                        id1 = get_current_window_id()
                        sb1.maximize_window()
                        ip_required = fix_ip(sb1, server_name1)
                        ip_address = get_ip(sb1)
                        sb1.open("https://www.skylom.com/videos")
                        skylom_window = sb1.current_window_handle
                        
                        if with_baymack == True:
                            sb1.open_new_window()
                            sb1.open("https://www.baymack.com/videos")
                            baymack_window = sb1.current_window_handle

                        print(sb1.get_title())

                        reclick_waits = 0
                    if reclick_waits > 50:
                        reclick_button(sb1)
                        pyautogui.click(990, 430)
                        time.sleep(3)
                        pyautogui.click(990, 430)
                else:
                    reclick_waits = 1
                
                if current_duration:
                    if current_duration >= 20:
                        if category == 0:
                            video_link = get_youtube_link(sb1) 
                            category = get_video_infog(video_link, sb1)
                            if category:
                                if debug_mode:
                                    print(f"Category: {category}")
                                if "Howto" in category:
                                    category = "How-To"
                                elif "Science" in category:
                                    category = "Sic-fi"
                                elif "Beauty" in category:
                                    category = "Beauty"
                                elif "Nonprofit" in category:
                                    category = "Nonprofit"    
                                elif "Film" in category:
                                    category = "Film"        
                                elif "Auto" in category:
                                    category = "Auto"    
                                elif "Technology" in category:
                                    category = "Technology"
                                title = sb1.get_title()
                                if title == 'Skylom':        
                                    ip_address =get_ip(sb1)
                                    proxycheck = get_proxycheck(ip_address, server_name= server_name1)
                                    coins = get_coin_value(sb1)
                                    if ip_address == ip_required and proxycheck:
                                        if coins and baymack_coins != 0:
                                            insert_data(ip= ip_address,amount1=coins, amount2=baymack_coins)
                                            print('insert Data')


                            else:
                                print(f'category is not defined{category}')
                        else:
                            if basic_info:
                                #print("Category is ",category)
                                print(f"Video duration: {current_duration} and Category is {category}", end="\r")

    
                    else:
                        category = 0
                        
                        if basic_info:
                            print(f"Video duration: {current_duration} and Category is {category}", end="\r")
                            #print('Video is Fresh')



                if check_category_question(sb1) == True:
                    print('Getting IP at 10 sec..')
                    #ip_address =get_ip(sb1)
                    if ip_address == ip_required:
                                if ip_address == ip_required:
                                    title = sb1.get_title()
                                    print('starting to answer category')
                                    if category != 0 and title == 'Skylom':
                                        print(title)
                                        solve_image_category(sb1, category, id1)

                                    elif category == 0:
                                        video_link = get_youtube_link(sb1) 
                                        category = get_video_infog(video_link, sb1)

                                        print(f"Category: {category}")
                                        if category:
                                            if "Howto" in category:
                                                category = "How-To"
                                            elif "Science" in category:
                                                category = "Sic-fi"
                                            elif "Nonprofit" in category:
                                                category = "Nonprofit"    
                                            elif "Film" in category:
                                                category = "Film"        
                                            elif "Auto" in category:
                                                category = "Auto"    
                                            elif "Technology" in category:
                                                category = "Technology"        
                    
                    else:
                        #ip_address =get_ip(sb)
                        print(f'IP is not Matched in IF category {ip_address}, Required: {ip_required}')
                        print('Getting IP at after found category...')
                        break
                        ip_required = fix_ip(sb1, server_name1)
                        ip_address = get_ip(sb1)

                    
            if title == 'Baymack':
                previous_duration_bay = current_duration_bay
                current_duration_bay = get_current_duration(sb=sb1)
                if current_duration_bay == previous_duration_bay and current_duration_bay == 0 :
                    print(f'reclick_waits:{reclick_waits}')
                    reclick_waits +=1
                    if reclick_waits > 155:
                        print(f'reopenning reclick {reclick_waits}')
                        sb1.quit()
                        sb1 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
                        id1 = get_current_window_id()
                        sb1.maximize_window()
                        ip_required = fix_ip(sb1, server_name1)
                        ip_address = get_ip(sb1)
                        sb1.open("https://www.skylom.com/videos")
                        skylom_window = sb1.current_window_handle
                        
                        if with_baymack == True:
                            sb1.open_new_window()
                            sb1.open("https://www.baymack.com/videos")
                            baymack_window = sb1.current_window_handle

                        print(sb1.get_title())

                        reclick_waits = 0
                    if reclick_waits > 50:
                        reclick_button(sb1)
                        pyautogui.click(990, 430)
                        time.sleep(3)
                        pyautogui.click(990, 430)
                else:
                    reclick_waits = 1
                
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
                                    #proxycheck = get_proxycheck(ip_address, server_name= server_name1)
                                    coins = get_coin_value(sb1)
                                    if coins:
                                        baymack_coins = coins
                                    else:
                                        print('Bymack Coins not availible')

 
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
                                            print(title)
                                            solve_image_category(sb1, category_bay, id1)

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
                    
                    else:
                        #ip_address =get_ip(sb)
                        print(f'IP _bays not Matched in IF category {ip_address}, Required: {ip_required}')
                        print('Getting IP at after found category...')
                        break
                        ip_required = fix_ip(sb1, server_name1)
                        ip_address = get_ip(sb1)





            #check_number_captcha_exists(sb1, id1)
            check_icon_captcha_exists(sb1, id1)
            #click_false_button(sb1)
            #handle_random_number_buttons(sb1)



            if with_baymack == True:
                title = sb1.get_title()
                if title == 'Skylom':
                    sb1.switch_to.window(baymack_window)
                elif title == 'Baymack':
                    sb1.switch_to.window(skylom_window)
                else:
                    print(f'no title was sky or bay {title}')
                
