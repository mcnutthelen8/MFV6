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
# Connect to the MySQL database
debug_mode = False

ip_required = 0
farm_id = 3
farm_id2 = 1
farm_id3 = 2
farm_id4 = 4
server_name1 = 'poland'
server_name2 = 'estonia'
server_name3 = 'romania'
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
        return

headers = {
    'User-Agent': 'My User Agent 1.0',
}

def get_video_infog(video_url, timeout=8):
    print(video_url)
    try:
        response = requests.get(video_url, headers=headers, timeout=timeout)
        print("Response received")
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            category_tag = soup.find('meta', itemprop='genre')
            category = category_tag['content'] if category_tag else None
            print(f"Category For This Video is {category}")
            return category
    except requests.Timeout:
        print(f"Request timed out after {timeout} seconds")
        return '0'
    except Exception as e:
        print(f"Errorg: {e}")
        return '0'

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
                return "YouTube link not found."
        else:
            return "Anchor tag not found."
 
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
        return None

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
                    return True
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

def fix_ip(drive, name):
    ipscore = None
    proxycheck = None
    ip_address = 0
    while not (ipscore and proxycheck):
        ip_address = get_ip(drive)
        ipscore = get_ipscore(ip_address)
        proxycheck = get_proxycheck(ip_address, server_name= name)
        if ipscore and proxycheck:
            print(f'Good IP found: {ip_address}')
            return ip_address
        else:
            print(f'Bad IP detected: {ip_address}. Changing IP...')
            mysterium_vpn_connect(name)
            print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
            time.sleep(5)


    


def get_ocr_category(driver, links):
    title = driver.get_title()

    # Check if we are on the correct page, if not, open a new window
    if title != 'NopeCHA CAPTCHA Solver':
        driver.open_new_window()
        driver.open('https://mfv6-ocr4.tiiny.site/')
        title = driver.get_title()
        print(title)
    time.sleep(1)
    # Re-check title after navigation
    if title == 'NopeCHA CAPTCHA Solver':
        print(title)

        # Check if CAPTCHA is still loading
        if driver.is_text_visible('Submitting CAPTCHAs...'):
            print('Captcha still loading')
            return None
        
        # Check if the OCR element is present
        if driver.is_element_present("#ocr1"):
            print('OCR Loaded')
            return True
            # Get the text from the OCR fields
            answer1 = driver.get_text("#ocr1")
            answer2 = driver.get_text("#ocr2")
            answer3 = driver.get_text("#ocr3")
            answer4 = driver.get_text("#ocr4")
            
            # Store answers in a list
            answers = [answer1, answer2, answer3, answer4]
            
            # Close the new window and switch back to the original window
            driver.close()
            print(answers)
            return answers  # Return the list of answers
        else:
            # If the OCR elements aren't present, submit the links
            driver.type("input#image_urls[type='text']", links)
            driver.click("button")
            return None
    else:
        return None



def find_most_similar_word(word, word_list):
    most_similar_word = None
    highest_similarity = 0
    most_similar_index = -1
    
    # Loop through each word in the list and calculate the similarity
    for idx, candidate in enumerate(word_list):
        similarity = difflib.SequenceMatcher(None, word, candidate).ratio()
        
        # If similarity is higher than the current highest, update the result
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_word = candidate
            most_similar_index = idx  # Store the index
    
    return most_similar_word, most_similar_index


def fix_broken_words(word_list):
    reference_list = [
        "Comedy", "Education", "Gaming", "Music", "Science","Technology",
        "Auto","Family" ,"Entertainment", "News","Politics", "People","Blogs",
        "Travel", "Sports", "Beauty", "None","Nonprofit", "Howto", "Film",
    ]
    fixed_list = []
    
    for word in word_list:
        fixed_word = find_most_similar_word(word, reference_list)
        fixed_list.append(fixed_word)
    
    return fixed_list

API_KEY = 'd5ace46d229a8844061fed0df01de9d1'
IMG_PATHS = ['crop1.png', 'crop2.png', 'crop3.png', 'crop4.png']  # Output file paths

def capture_and_crop_regions(regions, output_paths):
    """
    Takes a screenshot of the entire screen, crops specified regions, and saves them as separate files.

    :param regions: List of tuples specifying the regions to crop. Each tuple should be in the format (x, y, width, height).
    :param output_paths: List of file paths where the cropped images will be saved.
    """
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

def upload_image(image_path):
    url = 'https://api.imgbb.com/1/upload'
    try:
        with open(image_path, 'rb') as file:
            response = requests.post(url, data={'key': API_KEY}, files={'image': file})
            response.raise_for_status()  # Raise an error for HTTP error responses
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during upload: {e}")
        return None

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
    
    # Upload images and print URLs
    image_urls = []
    for image_path in output_paths:
        result = upload_image(image_path)
        if result and 'data' in result and 'url' in result['data']:
            image_urls.append(result['data']['url'])
        else:
            image_urls.append(f"Failed to upload image: {image_path}")
    
    # Print image URLs
    urls =[]
    for url in image_urls:
        print(url)
        urls.append(url)

    # Join the list into a single string, separating URLs with commas
    url_string = ', '.join(urls) + ','  # Adding a trailing comma if you want it

    # Output the result
    print(url_string)
    return url_string


def check_words(category, fixed_words):

    if isinstance(fixed_words, list) and isinstance(fixed_words[0], tuple):
        fixed_words = [t[0] for t in fixed_words if isinstance(t, tuple) and len(t) > 0 and isinstance(t[0], str)]

    word_prefix = category[:4].lower() 

    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower() 
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
    category = 'None'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
    category = 'Music'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
        
    category = 'People'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
    category = 'Entertainment'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
    category = 'Science'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
        
    category = 'Technology'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
        

    category = 'News'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
        

    category = 'Politics'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
        

    category = 'Nonprofit'
    word_prefix = category[:4].lower() 
    for index, ref_word in enumerate(fixed_words):
        ref_word_prefix = ref_word[:4].lower()  
        if word_prefix in ref_word_prefix:
            print(f"Matching word for '{category}' at index {index}: {ref_word}")
            return index
    return 1

def solve_image_category(drive, category, window):
    title = drive.get_title()
    urls = "Fuckeup"
    if title == 'Skylom':

        print(title)
        urls = get_category_images()
    if get_ocr_category(drive, urls):
        answer1 = drive.get_text("#ocr1")
        answer2 = drive.get_text("#ocr2")
        answer3 = drive.get_text("#ocr3")
        answer4 = drive.get_text("#ocr4")
        answers = [answer1, answer2, answer3, answer4]
        if debug_mode:
            print(answers)
        drive.close()
        fix_answers= fix_broken_words(answers)
        if debug_mode:
            print(fix_answers)
        position = check_words(category, fix_answers)
        print(f"The most similar word to '{category}' at index {position} : {fix_answers}")
        drive.switch_to.window(window)
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

            






run_sb1 = True
run_sb2 = True
run_sb3 = False
run_sb4 = False

brave_user_data_dir = '/home/coder/.config/BraveSoftware/Brave-Browser/'
brave_binary_path = '/usr/bin/brave-browser'

#chrome_binary_path = '/opt/google/chrome/google-chrome'
#chrome_user_data_dir = '/home/user/.config/google-chrome/'

if run_sb1:
    sb1 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
    id1 = get_current_window_id()
    sb1.maximize_window()
    ip_required = fix_ip(sb1, server_name1)
    ip_address = get_ip(sb1)
    sb1.open("https://www.skylom.com/videos")
    print(sb1.get_title())

if run_sb2:
    sb2 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir2, binary_location=chrome_binary_path)
    id2 = get_current_window_id()
    sb2.maximize_window()
    ip_required2 = fix_ip(sb2, server_name2)
    ip_address2 = get_ip(sb2)
    sb2.open("https://www.skylom.com/videos")
    print(sb1.get_title())
if run_sb3:
    sb3 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir3, binary_location=chrome_binary_path)
    id3 = get_current_window_id()
    sb3.maximize_window()
    ip_required3 = fix_ip(sb3, server_name3)
    ip_address3 = get_ip(sb3)

if run_sb4:
    sb4 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir4, binary_location=chrome_binary_path)
    id4 = get_current_window_id()
    sb4.maximize_window()
    ip_required4 = fix_ip(sb4, server_name4)
    ip_address4 = get_ip(sb4)



    #print(f'IP Matched {ip_address}')
if ip_address2 == ip_required2:
    if ip_address == ip_required:

        import img_captcha
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
                    time.sleep(5)
                    sb.maximize_window()
                    activate_window_by_id(id)
                    #sb1.scroll_to_top()
                    sb1.execute_script("window.scrollTo(0, 0);")
                    # Assuming img_captcha.solve_icon_captcha() is defined elsewhere
                    img_captcha.solve_image_skylom()
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
        reclick_waits = 1
        category = 0
        basic_info = True
        start_time = time.time()

        current_duration2 = 1
        reclick_waits2 = 1
        category2 = 0
        basic_info2 = True
        start_time2 = time.time()

        current_duration3 = 1
        reclick_waits3 = 1
        category3 = 0
        basic_info3 = True
        start_time3 = time.time()

        current_duration4 = 1
        reclick_waits4 = 1
        category4 = 0
        basic_info4 = True
        start_time4 = time.time()
        ip_address = 0
        ip_address2 = 0
        ip_address3 = 0
        ip_address4 = 0
        while True:
            #activate_window_by_id(id1)
            cloudflare(id1,sb1)
            sb1.switch_to.default_content()
            sb1.execute_script("window.scrollTo(0, 0);")
            play_button(sb1)
            playback_check(sb1)
            remove_pink(sb1)

            #SB2 
            if run_sb2:
                cloudflare(id2,sb2)
                sb2.switch_to.default_content()
                sb2.execute_script("window.scrollTo(0, 0);")
                play_button(sb2)
                playback_check(sb2)
                remove_pink(sb2)
            
            if run_sb3:
                cloudflare(id3,sb3)
                sb3.switch_to.default_content()
                sb3.execute_script("window.scrollTo(0, 0);")
                play_button(sb3)
                playback_check(sb3)
                remove_pink(sb3)
            
            if run_sb4:
                cloudflare(id4,sb4)
                sb4.switch_to.default_content()
                sb4.execute_script("window.scrollTo(0, 0);")
                play_button(sb4)
                playback_check(sb4)
                remove_pink(sb4)


            previous_duration = current_duration
            current_duration = get_current_duration(sb=sb1)
            
            if run_sb2:
                previous_duration2 = current_duration2
                current_duration2 = get_current_duration(sb=sb2)


            if run_sb3:
                previous_duration3 = current_duration3
                current_duration3 = get_current_duration(sb=sb3)


            if run_sb4:
                previous_duration4 = current_duration4
                current_duration4 = get_current_duration(sb=sb4)

##################################################################
##########################SB-1####################################
##################################################################

            if current_duration == previous_duration and current_duration == 0 :
                print(f'reclick_waits:{reclick_waits}')
                reclick_waits +=1
                if reclick_waits > 25:
                    print(f'reopenning reclick {reclick_waits}')
                    sb1.quit()
                    sb1 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
                    id1 = get_current_window_id()
                    sb1.maximize_window()
                    ip_required = fix_ip(sb1, server_name1)
                    ip_address = get_ip(sb1)
                    sb1.open("https://www.skylom.com/videos")
                    print(sb1.get_title())

                    reclick_waits = 0
                if reclick_waits > 20:
                    reclick_button(sb1)
                    pyautogui.click(990, 430)
                    time.sleep(3)
                    pyautogui.click(990, 430)
            else:
                reclick_waits = 1

            if current_duration:
                if current_duration >= 50:
                    if category == 0:
                        video_link = get_youtube_link(sb1) 
                        category = get_video_infog(video_link)
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
                        if basic_info:
                            #print("Category is ",category)
                            print(f"Video duration: {current_duration} and Category is {category}", end="\r")

 
                else:
                    category = 0
                    
                    if basic_info:
                        print(f"Video duration: {current_duration} and Category is {category}", end="\r")
                        #print('Video is Fresh')

            title = sb1.get_title()
            if title == 'Skylom':
                if debug_mode:
                    print(title)
                original_window = sb1.current_window_handle

            if check_category_question(sb1) == True:
                print('Getting IP at 10 sec..')
                ip_address =get_ip(sb1)
                if ip_address == ip_required:
                            if ip_address == ip_required:
                                ip_address = 0
                                print('starting to answer category')
                                if category != 0:
                                    print('starting to answer category confirm')
                                    title = sb1.get_title()
                                    if title == 'Skylom':
                                        print(title)
                                        original_window = sb1.current_window_handle
                                        activate_window_by_id(id1)
                                        solve_image_category(sb1, category, original_window)

                                elif category == 0:
                                    category = get_video_infog(video_link)

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

            title = sb1.get_title()
            if title == 'NopeCHA CAPTCHA Solver':
                activate_window_by_id(id1)
                solve_image_category(sb1, category, original_window)
                

            if click_next_video(sb1):
                elapsed_time = time.time() - start_time
                mins, secs = divmod(int(elapsed_time), 60)
                timer = f'{mins:02d}:{secs:02d}'
                seconds_only = int(elapsed_time)
                print(f'Next Click {timer}')
                print(f'Elapsed_time {seconds_only}')
                start_time = time.time()
                ip_address = 0

            click_false_button(sb1)
            handle_random_number_buttons(sb1)
            check_number_captcha_exists(sb1, id1)
            check_icon_captcha_exists(sb1, id1)

##################################################################
##########################SB-2####################################
##################################################################
            if run_sb2:
                if current_duration2 == previous_duration2 and current_duration2 == 0 :
                    print(f'reclick_waits:{reclick_waits2}')
                    reclick_waits2 +=1
                    if reclick_waits2 > 25:
                        print(f'reopenning reclick {reclick_waits2}')
                        sb2.quit()
                        sb2 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir2, binary_location=chrome_binary_path)
                        id2 = get_current_window_id()
                        sb2.maximize_window()
                        ip_required2 = fix_ip(sb2, server_name2)
                        ip_address2 = get_ip(sb2)
                        sb2.open("https://www.skylom.com/videos")
                        print(sb2.get_title())

                        reclick_waits2 = 0
                    if reclick_waits2 > 20:
                        reclick_button(sb2)
                        pyautogui.click(990, 430)
                        time.sleep(3)
                        pyautogui.click(990, 430)
                else:
                    reclick_waits2 = 1

                if current_duration2:
                    if current_duration2 >= 50:
                        if category2 == 0:
                            video_link2 = get_youtube_link(sb2) 
                            category2 = get_video_infog(video_link2)
                            if category2:
                                if debug_mode:
                                    print(f"Category: {category2}")
                                if "Howto" in category2:
                                    category2 = "How-To"
                                elif "Science" in category2:
                                    category2 = "Sic-fi"
                                elif "Beauty" in category2:
                                    category2 = "Beauty"
                                elif "Nonprofit" in category2:
                                    category2 = "Nonprofit"    
                                elif "Film" in category2:
                                    category2 = "Film"        
                                elif "Auto" in category2:
                                    category2 = "Auto"    
                                elif "Technology" in category2:
                                    category2 = "Technology"        
                                ip_address2 =get_ip(sb2)
                                proxycheck2 = get_proxycheck(ip_address2, server_name= server_name2)
                                coins2 = get_coin_value(sb2)
                                if ip_address2 == ip_required2 and proxycheck2:
                                    if coins2:
                                        ip_list2 = insert_data(ip= ip_address2,amount= coins2, id= farm_id2)
                                        if ip_list2:
                                            duplicates_ip2 = set([ip2 for ip2 in ip_list2 if ip_list2.count(ip2) > 1])
                                            if ip_address2 in duplicates_ip2:
                                                print(f'{duplicates_ip2} same ip2 detect {ip_address2}')
                                                ip_required2 = fix_ip(sb2, server_name1)
                                                ip_address2 = get_ip(sb2)
                                            else:
                                                print('no 2 duplicate on 1st')  
                        else:
                            if basic_info:
                                #print("Category is ",category)
                                print(f"Video duration2: {current_duration2} and Category2 is {category2}", end="\r")

    
                    else:
                        category2 = 0
                        
                        if basic_info:
                            print(f"Video duration2: {current_duration2} and Category2 is {category2}", end="\r")
                            #print('Video is Fresh')

                title2 = sb2.get_title()
                if title2 == 'Skylom':
                    if debug_mode:
                        print(title2)
                    original_window2 = sb2.current_window_handle

                if check_category_question(sb2) == True:
                    print('Getting 2 IP at 10 sec..')
                    ip_address2 =get_ip(sb2)
                    if ip_address2 == ip_required2:
                                if ip_address2 == ip_required2:
                                    ip_address2 = 0
                                    print('starting 2 to answer category')
                                    if category != 0:
                                        print('starting 2 to answer category confirm')
                                        title2 = sb2.get_title()
                                        if title2 == 'Skylom':
                                            print(title2)
                                            original_window2 = sb2.current_window_handle
                                            activate_window_by_id(id2)
                                            solve_image_category(sb2, category2, original_window2)

                                    elif category2 == 0:
                                        category2 = get_video_infog(video_link2)

                                        print(f"Category: {category2}")
                                        if category2:
                                            if "Howto" in category2:
                                                category2 = "How-To"
                                            elif "Science" in category2:
                                                category2 = "Sic-fi"
                                            elif "Nonprofit" in category2:
                                                category2 = "Nonprofit"    
                                            elif "Film" in category2:
                                                category2 = "Film"        
                                            elif "Auto" in category2:
                                                category2 = "Auto"    
                                            elif "Technology" in category2:
                                                category2 = "Technology"        
                        
                    else:
                        #ip_address =get_ip(sb)
                        print(f'IP 2 is not Matched in IF category {ip_address2}, Required: {ip_required2}')
                        print('Getting 2 IP at after found category...')
                        ip_required = fix_ip(sb2, server_name2)
                        ip_address = get_ip(sb2)

                title2 = sb2.get_title()
                if title2 == 'NopeCHA CAPTCHA Solver':
                    activate_window_by_id(id2)
                    solve_image_category(sb2, category, original_window2)
                  



                if click_next_video(sb2):
                    elapsed_time2 = time.time() - start_time2
                    mins2, secs2 = divmod(int(elapsed_time2), 60)
                    timer2 = f'{mins2:02d}:{secs2:02d}'
                    seconds_only2 = int(elapsed_time2)
                    print(f'Next Click {timer2}')
                    print(f'Elapsed_time {seconds_only2}')
                    start_time2 = time.time()
                    ip_address2 = 0

                click_false_button(sb2)
                handle_random_number_buttons(sb2)
                check_number_captcha_exists(sb2, id2)
                check_icon_captcha_exists(sb2, id2)
                time.sleep(1)

##################################################################
##########################SB-3####################################
##################################################################
            if run_sb3:
                if current_duration3 == previous_duration3 and current_duration3 == 0 :
                    print(f'reclick_waits:{reclick_waits3}')
                    reclick_waits3 +=1
                    if reclick_waits3 > 25:
                        print(f'reopenning reclick {reclick_waits3}')
                        sb3.quit()
                        sb3 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir3, binary_location=chrome_binary_path)
                        id3 = get_current_window_id()
                        sb3.maximize_window()
                        ip_required3 = fix_ip(sb3, server_name3)
                        ip_address3 = get_ip(sb3)
                        sb3.open("https://www.skylom.com/videos")
                        print(sb3.get_title())

                        
                        reclick_waits3 = 0
                    if reclick_waits3 > 20:
                        reclick_button(sb3)
                        activate_window_by_id(id3)
                        pyautogui.click(990, 430)
                        time.sleep(3)
                        pyautogui.click(990, 430)
                else:
                    reclick_waits3 = 1

                if current_duration3:
                    if current_duration3 >= 10:
                        if ip_address3 == ip_required3:
                            pass
                        else:
                            print('Getting3 IP at 10 sec..')
                            ip_address3 =get_ip(sb3)
                            coins3 = get_coin_value(sb3)
                            if coins3:
                                ip_list3 = insert_data(ip= ip_address3,amount= coins3, id= farm_id3)
                                if ip_list3:
                                    duplicates_ip3 = set([ip for ip in ip_list3 if ip_list3.count(ip) > 1])
                                    if ip_address3 in duplicates_ip3:
                                        print(f'{duplicates_ip3} same 3 ip detect {ip_address3}')
                                        ip_required3 = fix_ip(sb3, server_name3)
                                        ip_address3 = get_ip(sb3)

                        if category3 == 0:
                            video_link3 = get_youtube_link(sb3) 
                            category3 = get_video_infog(video_link3)
                            if debug_mode:
                                print(f"Category3: {category3}")
                            if "Howto" in category3:
                                category3 = "How-To"
                            elif "Science" in category3:
                                category3 = "Sic-fi"
                            elif "Beauty" in category3:
                                category3 = "Beauty"
                            elif "Nonprofit" in category3:
                                category3 = "Nonprofit"    
                            elif "Film" in category3:
                                category3 = "Film"        
                            elif "Auto" in category3:
                                category3 = "Auto"    
                            elif "Technology" in category3:
                                category3 = "Technology"        
                        
                        else:
                            if basic_info3:
                                #print("Category is ",category)
                                print(f"Video duration3: {current_duration3} and Category3 is {category3}", end="\r")
                    
                    else:
                        category3 = 0
                        
                        if basic_info:
                            print(f"Video duration3: {current_duration2} and Category3 is {category3}", end="\r")
                            #print('Video is Fresh')

                if check_category_question(sb3) == True:
                    if ip_address3 == ip_required3:
                        ip_address3 = 0
                        print('starting to answer category')
                        if category3 != 0:
                            print('starting to answer category confirm')
                            if get_and_click_category(category3,sb3) == False:
                                if debug_mode:
                                    print("Issue Detect1")
                                if get_and_click_category('None',sb3) == False:
                                    if debug_mode:
                                        print("Issue Detect2")
                                    if get_and_click_category('Music',sb3) == False:
                                        if debug_mode:
                                            print("Issue Detect3")
                                        if get_and_click_category('Entertainment',sb3) == False:
                                            if debug_mode:
                                                print("Issue Detect4")
                                            if get_and_click_category('People & Blogs',sb3) == False:
                                                if debug_mode:
                                                    print("Issue Detect5")
                                                if get_and_click_category('Science',sb3) == False:
                                                    if debug_mode:
                                                        print("Issue Detect7")
                                                    if get_and_click_category('Technology',sb3) == False:
                                                        if debug_mode:
                                                            print("Issue Detect6")
                                                        if get_and_click_category('News',sb3) == False:
                                                            if debug_mode:
                                                                print("Issue Detect8")
                                                            if click_random_category(sb3) == False:
                                                                print('random3')
                                                                if debug_mode:
                                                                    print("Issue Detect9")
                        elif category3 == 0:
                            category3 = get_video_infog(video_link3)
                            print(f"Category: {category3}")
                            if "Howto" in category3:
                                category3 = "How-To"
                            elif "Science" in category3:
                                category3 = "Sic-fi"
                            elif "Nonprofit" in category3:
                                category3 = "Nonprofit"    
                            elif "Film" in category3:
                                category3 = "Film"        
                            elif "Auto" in category3:
                                category3 = "Auto"    
                            elif "Technology" in category3:
                                category3 = "Technology"        
                    
                    else:
                        #ip_address =get_ip(sb)
                        print(f'IP2 is not Matched in IF category {ip_address3}, Required: {ip_required3}')
                        print('Getting2 IP at after found category...')
                        ip_address3 =get_ip(sb3)

                if click_next_video(sb3):
                    elapsed_time3 = time.time() - start_time3
                    mins3, secs3 = divmod(int(elapsed_time3), 60)
                    timer3 = f'{mins3:02d}:{secs3:02d}'
                    seconds_only3 = int(elapsed_time3)
                    print(f'Next Click {timer3}')
                    print(f'Elapsed_time {seconds_only3}')
                    start_time3 = time.time()
                    ip_address3 = 0

                click_false_button(sb3)
                handle_random_number_buttons(sb3)
                check_number_captcha_exists(sb3, id3)
                check_icon_captcha_exists(sb3, id3)
                time.sleep(1)

##################################################################
##########################SB-4####################################
##################################################################
            if run_sb4:
                if current_duration4 == previous_duration4 and current_duration4 == 0 :
                    print(f'reclick_waits:{reclick_waits4}')
                    reclick_waits4 +=1
                    if reclick_waits4 > 25:
                        print(f'reopenning reclick {reclick_waits4}')
                        sb4.quit()
                        sb4 = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir4, binary_location=chrome_binary_path)
                        id4 = get_current_window_id()
                        sb4.maximize_window()
                        ip_required4 = fix_ip(sb4, server_name4)
                        ip_address4 = get_ip(sb4)
                        sb4.open("https://www.skylom.com/videos")
                        print(sb4.get_title())

                        
                        reclick_waits4 = 0
                    if reclick_waits4 > 20:
                        reclick_button(sb4)
                        activate_window_by_id(id4)
                        pyautogui.click(990, 430)
                        time.sleep(3)
                        pyautogui.click(990, 430)
                else:
                    reclick_waits4 = 1

                if current_duration4:
                    if current_duration4 >= 10:
                        if ip_address4 == ip_required4:
                            pass
                        else:
                            print('Getting4 IP at 10 sec..')
                            ip_address4 =get_ip(sb4)
                            coins4 = get_coin_value(sb4)
                            if coins4:
                                ip_list4 = insert_data(ip= ip_address4,amount= coins4, id= farm_id4)
                                if ip_list4:
                                    duplicates_ip4 = set([ip for ip in ip_list4 if ip_list4.count(ip) > 1])
                                    if ip_address4 in duplicates_ip4:
                                        print(f'{duplicates_ip4} same 4 ip detect {ip_address4}')
                                        ip_required4 = fix_ip(sb4, server_name4)
                                        ip_address4 = get_ip(sb4)


                        if category4 == 0:
                            video_link4 = get_youtube_link(sb4) 
                            category4 = get_video_infog(video_link4)
                            if debug_mode:
                                print(f"Category4: {category4}")
                            if "Howto" in category4:
                                category4 = "How-To"
                            elif "Science" in category4:
                                category4 = "Sic-fi"
                            elif "Beauty" in category4:
                                category4 = "Beauty"
                            elif "Nonprofit" in category4:
                                category4 = "Nonprofit"    
                            elif "Film" in category4:
                                category4 = "Film"        
                            elif "Auto" in category4:
                                category4 = "Auto"    
                            elif "Technology" in category4:
                                category4 = "Technology"        
                        
                        else:
                            if basic_info4:
                                #print("Category is ",category)
                                print(f"Video duration4: {current_duration4} and Category4 is {category4}", end="\r")
                    
                    else:
                        category4 = 0
                        
                        if basic_info:
                            print(f"Video duration4: {current_duration4} and Category4 is {category4}", end="\r")
                            #print('Video is Fresh')

                if check_category_question(sb4) == True:
                    if ip_address4 == ip_required4:
                        ip_address4 = 0
                        print('starting to answer category')
                        if category4 != 0:
                            print('starting to answer category confirm')
                            if get_and_click_category(category4,sb4) == False:
                                if debug_mode:
                                    print("Issue Detect1")
                                if get_and_click_category('None',sb4) == False:
                                    if debug_mode:
                                        print("Issue Detect2")
                                    if get_and_click_category('Music',sb4) == False:
                                        if debug_mode:
                                            print("Issue Detect3")
                                        if get_and_click_category('Entertainment',sb4) == False:
                                            if debug_mode:
                                                print("Issue Detect4")
                                            if get_and_click_category('People & Blogs',sb4) == False:
                                                if debug_mode:
                                                    print("Issue Detect5")
                                                if get_and_click_category('Science',sb4) == False:
                                                    if debug_mode:
                                                        print("Issue Detect7")
                                                    if get_and_click_category('Technology',sb4) == False:
                                                        if debug_mode:
                                                            print("Issue Detect6")
                                                        if get_and_click_category('News',sb4) == False:
                                                            if debug_mode:
                                                                print("Issue Detect8")
                                                            if click_random_category(sb4) == False:
                                                                print('random4')
                                                                if debug_mode:
                                                                    print("Issue Detect9")
                        elif category4 == 0:
                            category4 = get_video_infog(video_link4)
                            print(f"Category: {category4}")
                            if "Howto" in category4:
                                category4 = "How-To"
                            elif "Science" in category4:
                                category4 = "Sic-fi"
                            elif "Nonprofit" in category4:
                                category4 = "Nonprofit"    
                            elif "Film" in category4:
                                category4 = "Film"        
                            elif "Auto" in category4:
                                category4 = "Auto"    
                            elif "Technology" in category4:
                                category4 = "Technology"        
                    
                    else:
                        #ip_address =get_ip(sb)
                        print(f'IP2 is not Matched in IF category {ip_address4}, Required: {ip_required4}')
                        print('Getting2 IP at after found category...')
                        ip_address4 =get_ip(sb4)

                if click_next_video(sb4):
                    elapsed_time4 = time.time() - start_time4
                    mins4, secs4 = divmod(int(elapsed_time4), 60)
                    timer4 = f'{mins4:02d}:{secs4:02d}'
                    seconds_only4 = int(elapsed_time4)
                    print(f'Next Click {timer4}')
                    print(f'Elapsed_time {seconds_only4}')
                    start_time4 = time.time()
                    ip_address4 = 0

                click_false_button(sb3)
                handle_random_number_buttons(sb4)
                check_number_captcha_exists(sb4, id4)
                check_icon_captcha_exists(sb4, id4)
 

    else:
        print(f'IP is not Matched in IF {ip_address}, Required: {ip_required}')
