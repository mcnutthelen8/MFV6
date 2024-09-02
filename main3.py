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
import mysql.connector
from mysql.connector import Error
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

def create_connection():
    """Create a database connection."""
    try:
        connection = mysql.connector.connect(
            host='ooy.h.filess.io',
            user='MFV6_herefooton',
            password='ded12e502693e0b05146dd9d6cf1b6d43f0fa5db',
            database='MFV6_herefooton',
            port=3307
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None



def insert_data(ip, amount, id):
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)

    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
    connection = create_connection()

    if connection:
        try:
            cursor = connection.cursor()

            # First, update the status_table
            sql_update = """
                UPDATE `status_table` 
                SET `ip_address` = %s, `status` = %s, `amount` = %s  
                WHERE `id` = %s;
            """
            values_update = (ip, str(now), amount, id)
            cursor.execute(sql_update, values_update)
            connection.commit()
            print("Status table updated successfully.")

            # Then, insert data into farm1_coins
            if id == 1:

                sql_insert = """
                    INSERT INTO farm1_coins (time, amount) 
                    VALUES (%s, %s)
                """
            if id == 2:

                sql_insert = """
                    INSERT INTO farm2_coins (time, amount) 
                    VALUES (%s, %s)
                """
            if id == 3:

                sql_insert = """
                    INSERT INTO farm3_coins (time, amount) 
                    VALUES (%s, %s)
                """
            if id == 4:

                sql_insert = """
                    INSERT INTO farm4_coins (time, amount) 
                    VALUES (%s, %s)
                """
            values_insert = (str(now), amount)
            cursor.execute(sql_insert, values_insert)  # Use execute instead of executemany
            connection.commit()
            print(f"Data inserted into {id}s successfully.")

            sql_query = "SELECT ip_address FROM status_table;"
            cursor.execute(sql_query)

            # Fetch all IP addresses
            rows = cursor.fetchall()
            ip_list = [row[0] for row in rows]
            if cursor:
                cursor.close()
            if connection:
                connection.close()
            return ip_list
        except Error as e:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
            print(f"Error: {e}")
            return None

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


    
def check_category_question(sb):
    category_question_selector = '.video-categ-question'
    try:
        if sb.is_element_visible(category_question_selector):
            print("Category question exists")
            return True
        else:
            if debug_mode:
                print("Category question does not exist")
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
            if proxy_status =='no':
                if country.lower() in server_name.lower():
                    return 200
                else:
                    print(f'{country} is not {server_name}')
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
            pyautogui.click(x, y)
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
        elif proxycheck == 50:
            print(f'Country ok /Bad IP detected: {ip_address}. Changing IP...')
            mysterium_vpn_Recon_ip(name)
            time.sleep(5)
        else:
            print(f'Bad IP detected: {ip_address}. Changing IP...')
            mysterium_vpn_connect(name)
            print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
            time.sleep(5)

#######Solve###########


def replace_white_with_limegreen(image_path, output_path, tolerance=30):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert("RGBA")  # Convert to RGBA to handle transparency if needed

        # Get the data of the image
        data = img.getdata()

        # Create a new list to store modified pixels
        new_data = []
        for item in data:
            # Calculate the difference between the pixel and white (255, 255, 255)
            r, g, b = item[:3]
            if abs(r - 255) <= tolerance and abs(g - 255) <= tolerance and abs(b - 255) <= tolerance:
                # Replace white (within the tolerance range) with limegreen
                new_data.append((0, 0, 0, item[3]))  # Keep original alpha value
            else:
                # Append other pixels unchanged
                new_data.append(item)

        # Update the image with the new pixel data
        img.putdata(new_data)

        # Save the image
        img.save(output_path, "PNG")
        print(f"Processed image saved as {output_path}")
        return output_path

    except Exception as e:
        print(f"Error: {e}")

def remove_noise(image_path, output_path):
    try:
        # Load the image
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply binary thresholding
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter out small contours (noise or lines)
        filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

        # Create a mask for the filtered contours
        mask = np.zeros_like(thresh)
        cv2.drawContours(mask, filtered_contours, -1, 255, thickness=cv2.FILLED)

        # Perform bitwise AND to keep only the large contours
        cleaned_img = cv2.bitwise_and(thresh, mask)

        # Invert the image to original binary style
        cleaned_img = cv2.bitwise_not(cleaned_img)

        # Save the cleaned image
        cv2.imwrite(output_path, cleaned_img)
        print(f"Cleaned image saved at {output_path}")

    except Exception as e:
        print(f"Error: {e}")

def remove_random_lines(image_path, output_path):


    # Read the image
    image = cv2.imread(image_path)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("original", img)

    img = cv2.bitwise_not(img)

    kernel = np.ones((14, 14), np.uint8)
    close = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    newkernel = np.ones((5, 5), np.uint8)
    inv = cv2.erode(close, newkernel, iterations=1)

    inv = cv2.bitwise_not(inv)

    cv2.imshow("inverted", inv)
    cv2.imwrite(output_path, inv)

    # Save the cleaned image
    #cv2.imwrite(output_path, cleaned_image)

def decaptcha(image_path, output_path):
    # Load the image
    src = cv2.imread(image_path)

    # Convert image to HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    # Define the line color range in HSV (fine-tune these values as needed)
    lower_color = np.array([0, 0, 110], dtype="uint8")   # Slightly darker shade for gray
    upper_color = np.array([180, 30, 135], dtype="uint8") # Capturing grey variations

    # Create mask for grey lines
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Slightly increase dilation to remove remaining lines
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    mask_dilated = cv2.dilate(mask, kernel, iterations=2)  # Increase iterations if necessary

    # Apply inpainting to remove the lines
    dst = cv2.inpaint(src, mask_dilated, 2 , cv2.INPAINT_TELEA)

    # Convert the result to grayscale for further processing
    gray_dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to smooth out noise
    blurred_dst = cv2.GaussianBlur(gray_dst, (5,5), 0)

    # Apply Otsu's threshold to binarize the image (make it black and white)
    _, final_dst = cv2.threshold(blurred_dst, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    cv2.imwrite(output_path, final_dst)

def sharp_image(image_path, output_path):
        # Load the image
            image = cv2.imread(image_path)

            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Define a stronger sharpening kernel
            kernel = np.array([[0, -1, 0],
                            [-1, 171,-1],
                            [0, -1, 0]])

            # Apply the kernel to the image
            sharpened = cv2.filter2D(gray, -1, kernel)


            # Save the sharpened image
            cv2.imwrite(output_path, sharpened)

def Filter_images(output_path):
    replace_white_with_limegreen(output_path, output_path, tolerance=50)
    sharp_image(output_path, output_path)

    remove_noise(output_path, output_path)
    sharp_image(output_path, output_path)

    decaptcha(output_path, output_path)
    sharp_image(output_path, output_path)

import Levenshtein

def simple_similarity(word1, word2):
    
    # Calculate character matches
    matches = sum(1 for a, b in zip(word1, word2) if a == b)
    return matches / max(len(word1), len(word2))

# Function to find the most similar word from the reference list
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
        letter_count = sum(1 for char in word if char.isalpha())
        if letter_count < 4:
            if word[0] == 'm' or word[0] == 'M':
                word = 'music'
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


import easyocr
reader = easyocr.Reader(['en'], gpu= False)
def ez_ocr(path):
    results = reader.readtext(path, detail = 0)
    cleaned_text = ''
    for text in results:
        text = text.lower()
        cleaned_text += text

    cleaned_text = cleaned_text.replace('0', 'o')
    cleaned_text = cleaned_text.replace('5', 's')
    cleaned_text = cleaned_text.replace('6', 's')
    cleaned_text = cleaned_text.replace('$', 's')
    cleaned_text = cleaned_text.replace('8', '&')
    cleaned_text = cleaned_text.replace('1', 'i')
    cleaned_text = cleaned_text.replace('[', 'c')
    cleaned_text = cleaned_text.replace('(', 'c')
    cleaned_text = cleaned_text.replace('4', 'a')
    cleaned_text = cleaned_text.replace('7', 'e')
    cleaned_text = cleaned_text.replace('<', 'c')
    cleaned_text = cleaned_text.replace('*', 'e')
    letter_count = sum(1 for char in cleaned_text if char.isalpha())
    if letter_count < 10:
        cleaned_text = cleaned_text.replace(' ', '')
        print(letter_count, cleaned_text)
    if cleaned_text == '':
        cleaned_text = 'food'

    return cleaned_text


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
        
    if category =='Music':
            category = 'auto'
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
            
    return 4



import os
import shutil

def copy_images_to_folder(images_list, destination_folder):
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Loop through each image path in the list and copy it to the destination folder
    for image_path in images_list:
        # Check if the image exists
        if os.path.exists(image_path):
            try:
                # Copy the image to the destination folder
                shutil.copy(image_path, destination_folder)
                print(f'Copied: {image_path} to {destination_folder}')
            except Exception as e:
                print(f'Error copying {image_path}: {e}')
        else:
            print(f'Image not found: {image_path}')


import base64
from io import BytesIO


def print_base64_images(drive):
    strings = []
    seen = set()  # To track seen base64 strings
    
    try:
        page_source = drive.get_page_source()
        base64_images = re.findall(r'data:image/[^;]+;base64,([^"]+)', page_source)

        for idx, image_data in enumerate(base64_images):
            if image_data not in seen:  # Check for duplicates
                print(f"Base64 Image {idx+1}: {image_data[:10]}...")
                strings.append(image_data)
                seen.add(image_data)  # Mark as seen to avoid duplicates

        print(f"\nTotal unique base64 strings: {len(strings)}")

        # Save each unique image
        for idx, image_data in enumerate(strings):
            image_bytes = base64.b64decode(image_data)  # Decode base64
            image = Image.open(BytesIO(image_bytes))  # Convert to PIL image
            image.save(f"crop{idx+1}.png")  # Save image as PNG
            print(f"crop{idx+1} saved as image_{idx+1}.png")

        return True
    except Exception as e:
        print(e)
    return False


def list_fixer(list1, list2):
    for i in range(len(list1)):
        if list1[i] == 'food':
            list1[i] = list2[i]
        elif list2[i] == 'food':
            list2[i] = list1[i]
    for i in range(min(len(list1), len(list2))): 
        count1 = len([char for char in list1[i] if char.isalpha()])
        count2 = len([char for char in list2[i] if char.isalpha()])
        if count1 < count2:
            list1[i] = list2[i]
        elif count1 > count2:
            list2[i] = list1[i]

    return list1


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
                    image_paths_back = ['crop1.png', 'crop2.png', 'crop3.png', 'crop4.png']
                    copy_images_to_folder(image_paths_back, 'Backup')
                    image_path = "crop1.png"
                    Filter_images(image_path)
                    image_path = "crop2.png"
                    Filter_images(image_path)
                    image_path = "crop3.png"
                    Filter_images(image_path)
                    image_path = "crop4.png"
                    Filter_images(image_path)
                    print('Images Filtered...')
                    image_paths = ['crop1.png', 'crop2.png', 'crop3.png', 'crop4.png']
                    Filtered_words = []
                    for image in image_paths:
                        word = ez_ocr(image)
                        #print("Ezocr Text:", word)
                        Filtered_words.append(word)

                    print('Filtered Ez list :', Filtered_words)

                    image_paths = ['Backup/crop1.png', 'Backup/crop2.png', 'Backup/crop3.png', 'Backup/crop4.png']
                    NoFiltered_words = []
                    for image in image_paths:
                        word = ez_ocr(image)
                        #print("Ezocr Text:", word)
                        NoFiltered_words.append(word)
                    print('None Filtered Ez list :', NoFiltered_words)


                    fixed_list = list_fixer(Filtered_words, NoFiltered_words)
                    print('fixedlist list :', fixed_list)
                    similar_word = find_most_similar_word(category, fixed_list)
    
                    fixword_list = fix_broken_words(fixed_list)
                    print('Fix Broken Word list :', fixword_list)
                    try:
                        if fixword_list:

                            position = check_words(category, fixword_list)
                            if position == 4:
                                print('position is None')
                                print(f'{similar_word} is similar with {category}')
                                position = fixed_list.index(similar_word)
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
                    image_paths_back = ['crop1.png', 'crop2.png', 'crop3.png', 'crop4.png']
                    copy_images_to_folder(image_paths_back, 'Backup')
                    image_path = "crop1.png"
                    Filter_images(image_path)
                    image_path = "crop2.png"
                    Filter_images(image_path)
                    image_path = "crop3.png"
                    Filter_images(image_path)
                    image_path = "crop4.png"
                    Filter_images(image_path)
                    print('Images Filtered...')
                    image_paths = ['crop1.png', 'crop2.png', 'crop3.png', 'crop4.png']
                    Filtered_words = []
                    for image in image_paths:
                        word = ez_ocr(image)
                        #print("Ezocr Text:", word)
                        Filtered_words.append(word)

                    print('Filtered Ez list :', Filtered_words)

                    image_paths = ['Backup/crop1.png', 'Backup/crop2.png', 'Backup/crop3.png', 'Backup/crop4.png']
                    NoFiltered_words = []
                    for image in image_paths:
                        word = ez_ocr(image)
                        #print("Ezocr Text:", word)
                        NoFiltered_words.append(word)
                    print('None Filtered Ez list :', NoFiltered_words)


                    fixed_list = list_fixer(Filtered_words, NoFiltered_words)
                    print('fixedlist list :', fixed_list)
                    similar_word = find_most_similar_word(category, fixed_list)
    
                    fixword_list = fix_broken_words(fixed_list)
                    print('Fix Broken Word list :', fixword_list)
                    try:
                        if fixword_list:
                            position = check_words(category, fixword_list)
                            if position == 4:
                                print('position is None')
                                print(f'{similar_word} is similar with {category}')
                                position = fixed_list.index(similar_word)
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
                                        if coins:
                                            ip_list = insert_data(ip= ip_address,amount= coins, id= farm_id)
                                            if ip_list:
                                                duplicates_ip = set([ip for ip in ip_list if ip_list.count(ip) > 1])
                                                if ip_address in duplicates_ip:
                                                    print(f'{duplicates_ip} same ip detect {ip_address}')
                                                    ip_required = fix_ip(sb1, server_name1)
                                                    ip_address = get_ip(sb1)
                                                else:
                                                    print('no duplicate on 1st')  
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
                                    if title == 'Skylom':
                                        sb1.switch_to.window(baymack_window)
                                        if click_next_video(sb1):
                                            elapsed_time = time.time() - start_time
                                            mins, secs = divmod(int(elapsed_time), 60)
                                            timer = f'{mins:02d}:{secs:02d}'
                                            seconds_only = int(elapsed_time)
                                            print(f'Next Click {timer}')
                                            print(f'Elapsed_time {seconds_only}')
                                            start_time = time.time()
                                            ip_address = 0
                                        sb1.switch_to.window(skylom_window)
                                    print('starting to answer category')
                                    if category != 0:
                                        print('starting to answer category confirm')
                                        title = sb1.get_title()
                                        if title:
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
                                if title == 'Skylom':        
                                    ip_address =get_ip(sb1)
                                    proxycheck = get_proxycheck(ip_address, server_name= server_name1)
                                    coins = get_coin_value(sb1)
                                    if ip_address == ip_required and proxycheck:
                                        if coins:
                                            ip_list = insert_data(ip= ip_address,amount= coins, id= farm_id)
                                            if ip_list:
                                                duplicates_ip = set([ip for ip in ip_list if ip_list.count(ip) > 1])
                                                if ip_address in duplicates_ip:
                                                    print(f'{duplicates_ip} same ip detect {ip_address}')
                                                    ip_required = fix_ip(sb1, server_name1)
                                                    ip_address = get_ip(sb1)
                                                else:
                                                    print('no duplicate on 1st')  
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
                                    if title == 'Baymack':
                                        sb1.switch_to.window(skylom_window)
                                        if click_next_video(sb1):
                                            elapsed_time = time.time() - start_time
                                            mins, secs = divmod(int(elapsed_time), 60)
                                            timer = f'{mins:02d}:{secs:02d}'
                                            seconds_only = int(elapsed_time)
                                            print(f'Next Click {timer}')
                                            print(f'Elapsed_time {seconds_only}')
                                            start_time = time.time()
                                            #ip_address = 0
                                        sb1.switch_to.window(baymack_window)
                                    print('starting to answer category')
                                    if category_bay != 0:
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
                        ip_required = fix_ip(sb1, server_name1)
                        ip_address = get_ip(sb1)


            if click_next_video(sb1):

                elapsed_time = time.time() - start_time
                mins, secs = divmod(int(elapsed_time), 60)
                timer = f'{mins:02d}:{secs:02d}'
                seconds_only = int(elapsed_time)
                print(f'Next Click {timer}')
                print(f'Elapsed_time {seconds_only}')
                start_time = time.time()
                title = sb1.get_title()
                if title == 'Skylom':
                    ip_address = 0



            check_number_captcha_exists(sb1, id1)
            check_icon_captcha_exists(sb1, id1)


            calc_captcha = click_false_button(sb1)
            if calc_captcha == False:
                calc_captcha = handle_random_number_buttons(sb1)

            while calc_captcha == True:
                calc_captcha = click_false_button(sb1)
                if calc_captcha == False:
                    calc_captcha = handle_random_number_buttons(sb1)
                time.sleep(1)


            if with_baymack == True:
                title = sb1.get_title()
                if title == 'Skylom':
                    sb1.switch_to.window(baymack_window)
                elif title == 'Baymack':
                    sb1.switch_to.window(skylom_window)
                else:
                    print(f'no title was sky or bay {title}')
                
