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


debug_mode = False

def get_ip(driver):
    original_window = driver.driver.current_window_handle
    driver.open_new_window()
    driver.switch_to_newest_window()
    driver.open('https://api.ipify.org/')
    ip_address = driver.get_text('body')
    print('IP =', ip_address)
    driver.driver.close()
    driver.switch_to_window(original_window)
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
                sb.switch_to_frame(sb.find_element(By.TAG_NAME, "iframe"))
                if sb.is_element_visible(play_button_selector):
                    play_button_elements = sb.find_elements(By.CSS_SELECTOR, play_button_selector)
                    print("Play button found")
                    play_button = play_button_elements[0]
                    play_button.click()
                    print("Play button Clicked")
                    sb.switch_to_default_content()
                    time.sleep(1)
                else:
                    print("Play button not found")
                    sb.switch_to_default_content()
            else:
                print("iframe not found")
                sb.switch_to_default_content()
        except Exception as e:
            if debug_mode:
                print(f"An error occurred: {e}")
            sb.switch_to_default_content()
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
            sb.switch_to_frame(sb.find_element(By.TAG_NAME, "iframe"))
            play_button_elements = sb.find_elements(By.CSS_SELECTOR, play_button_selector)
            print("reclick_button found")
            play_button = play_button_elements[0]
            play_button.click()
            print("reclick_button Clicked")
            sb.switch_to_default_content()
            time.sleep(2)
            play_button.click()
            #time.sleep(2)
            print("reclick_button Clicked Again")

            print("Play button not found")
            sb.switch_to_default_content()
        except Exception as e:
            if debug_mode:
                print(f"An error occurred: {e}")
            sb.switch_to_default_content()

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


def get_and_click_category(category,sb):
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
            if button.text.strip().lower() == category.lower():
                #sb.highlight(button)
                print(f"Found Clicked category: {button.text}")
                button.click()
                print(f"Found gClicked category: {button.text}")
                return True
        if debug_mode:
            print(f"Category '{category}' not found")
        return False
    
    except Exception as e:
        if debug_mode:
            print(f"An error occurred: {e}")
        return True
    
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
        if sb.is_element_visible(".//a[text()=' False ']"):
            sb.click(".//a[text()=' False ']")
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
        if sb.is_element_visible(".//a[text()=' False ']"):
            sb.click(".//a[text()=' False ']")
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


ip_required = '86.126.121.190' #'80.235.95.245' #'62.65.59.183'#Chrome /alisabro #'177.32.9.130' #'82.79.231.82'  #86.126.140.173'
ip_required_2 = '177.32.9.130' #186.213.222.230'
ip_required_2 = '88.196.211.168'

run_sb1 = True
run_sb2 = True

brave_user_data_dir = '/home/coder/.config/BraveSoftware/Brave-Browser/'
brave_binary_path = '/usr/bin/brave-browser'

#chrome_binary_path = '/opt/google/chrome/google-chrome'
#chrome_user_data_dir = '/home/user/.config/google-chrome/'
chrome_binary_path = '/opt/google/chrome/google-chrome'
chrome_user_data_dir = '/home/coder/.config/google-chrome'

with SB(uc=True, headed= True, undetectable=True, undetected=True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path) as sb1:

    sb1.driver.maximize_window()
    id1 = get_current_window_id()
    ip_address =get_ip(sb1)
    while ip_address != ip_required:
        print(f'IP is not Matched {ip_address}, Required: {ip_required}')

    print(f'IP Matched {ip_address}')
    if ip_address == ip_required:
        url = "https://www.skylom.com/videos"
        time.sleep(1)
        sb1.uc_open_with_tab(url)
        print(sb1.get_title())
        import img_captcha
        #import ocr_captcha
        def check_number_captcha_exists(sb, id):
            try:
                # Attempt to find the number captcha image
                try:
                    if sb.is_element_visible("#numberCaptcha"):
                        print("Number captcha exists.")
                        sb.driver.maximize_window()
                        activate_window_by_id(id)
                        #sb1.scroll_to_top()
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
                    sb.driver.maximize_window()
                    activate_window_by_id(id)
                    sb1.scroll_to_top()
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
        while True:
            #activate_window_by_id(id1)
            cloudflare(id1,sb1)
            sb1.switch_to_default_content()
            sb1.scroll_to_top()
            play_button(sb1)
            playback_check(sb1)
            remove_pink(sb1)
            previous_duration = current_duration
            current_duration = get_current_duration(sb=sb1)
            if current_duration == previous_duration and current_duration == 0 :
                print(f'reclick_waits:{reclick_waits}')
                reclick_waits +=1
                if reclick_waits > 25:
                    print(f'start reclick {reclick_waits}')
                    reclick_button(sb1)
                    reclick_waits = 0
            else:
                reclick_waits = 1

            if current_duration:
                if current_duration >= 10:
                    if ip_address == ip_required:
                        pass
                    else:
                        print('Getting IP at 10 sec..')
                        ip_address =get_ip(sb1)

                    if category == 0:
                        video_link = get_youtube_link(sb1) 
                        category = get_video_infog(video_link)
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
                if ip_address == ip_required:
                    ip_address = 0
                    print('starting to answer category')
                    if category != 0:
                        print('starting to answer category confirm')
                        if get_and_click_category(category,sb1) == False:
                            if debug_mode:
                                print("Issue Detect1")
                            if get_and_click_category('None',sb1) == False:
                                if debug_mode:
                                    print("Issue Detect2")
                                if get_and_click_category('Music',sb1) == False:
                                    if debug_mode:
                                        print("Issue Detect3")
                                    if get_and_click_category('Entertainment',sb1) == False:
                                        if debug_mode:
                                            print("Issue Detect4")
                                        if get_and_click_category('People & Blogs',sb1) == False:
                                            if debug_mode:
                                                print("Issue Detect5")
                                            if click_random_category(sb1) == False:
                                                if debug_mode:
                                                    print("Issue Detect6")
                    elif category == 0:
                        category = get_video_infog(video_link)
                        print(f"Category: {category}")
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
                    ip_address =get_ip(sb1)

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
            time.sleep(1)

    else:
        print(f'IP is not Matched in IF {ip_address}, Required: {ip_required}')
