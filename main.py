from seleniumbase import Driver
import pyautogui
import requests
import time

chrome_binary_path = '/opt/google/chrome/google-chrome'
chrome_user_data_dir = '/root/.config/google-chrome/'

server_name1 = 'romania'


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
            mysterium_vpn_Recon_ip(name)
            time.sleep(5)
        else:
            print(f'Bad IP detected: {ip_address}. Changing IP...')
            mysterium_vpn_connect(name)
            print(f'Changing IP due to ipscore: {ipscore} and proxycheck: {proxycheck}')
            time.sleep(5)

dc = Driver(uc=False, headed= True,  user_data_dir=chrome_user_data_dir, binary_location=chrome_binary_path)
dc.maximize_window()
url = "chrome://extensions/"
dc.open(url)
print(dc.get_title())
ip = 0
preip = 0
while True:
    preip = get_ip(dc)
    if ip == preip:
        print(f'Good IP found: {ip}')
    else:
        ip = fix_ip(dc, server_name1)
