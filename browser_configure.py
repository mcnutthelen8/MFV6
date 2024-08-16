import pyautogui
import time
import requests
from seleniumbase import Driver




def mysterium_vpn_connect(server_name):
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.95)
        pyautogui.click(x, y)
        print("mysterium_icon_empty Found")
        time.sleep(5)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/search_mysterium.png", region=(1325, 494, 800, 400), confidence=0.95)
            pyautogui.click(x, y)
            print("search_mysterium Found")
            time.sleep(2)
            pyautogui.typewrite(server_name)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.scroll(-500)
            time.sleep(2)
            pyautogui.click(1627, 568)
            return True
        except pyautogui.ImageNotFoundException:
            print("No search_mysterium .")

    except pyautogui.ImageNotFoundException:
        print("No mysterium_icon_empty .")
    return None

def mysterium_login():
    pyautogui.click(1613, 137)
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.typewrite('https://app.mysteriumvpn.com/')
    pyautogui.press('enter')
    time.sleep(5)
    for i in range(1,100):
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/cookie_icon.png", region=(1625, 43, 400, 300), confidence=0.95)
            pyautogui.click(x, y)
            print("cookie_icon Found")
            time.sleep(3)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/all_site.png", region=(1300, 212, 600, 300), confidence=0.95)
                pyautogui.click(x, y)
                print("all_site Found")
            except pyautogui.ImageNotFoundException:
                print("No all_site .")
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.95)
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
                        text_content = ""
                    if text_content:
                        pyautogui.click(1385, 310)
                        time.sleep(1)
                        pyautogui.typewrite(text_content)
                        time.sleep(1)
                        try:
                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/import_icon.png", region=(1300, 212, 900, 900), confidence=0.95)
                            pyautogui.click(x, y)
                            print("import_icon Found")
                            pyautogui.click(313, 147)
                            time.sleep(3)
                            pyautogui.press('f5')
                            time.sleep(3)
                            try:
                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.95)
                                pyautogui.click(x, y)
                                print("mysterium_icon_empty Found")
                                i = 1
                                for i in range(1, 100):
                                    try:
                                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_login.png", region=(1375, 543, 600, 300), confidence=0.95)
                                        pyautogui.click(x, y)
                                        print("mysterium_login Found")
                                        for i in range(1, 100):
                                            try:
                                                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_allow.png", region=(842, 750, 400, 300), confidence=0.95)
                                                pyautogui.click(x, y)
                                                print("mysterium_allow Found")
                                                time.sleep(3)
                                                try:
                                                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/mysterium_icon_empty.png", region=(1625, 43, 400, 300), confidence=0.95)
                                                    pyautogui.click(x, y)
                                                    print("mysterium_icon_empty 2 Found")
                                                    time.sleep(3)
                                                    for i in range(1,100):
                                                        time.sleep(1)
                                                        try:
                                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/settings_mysterium.png", region=(1445, 630, 400, 300), confidence=0.95)
                                                            pyautogui.click(x, y)
                                                            print("settings_mysterium 2 Found")
                                                            time.sleep(1)
                                                        except pyautogui.ImageNotFoundException:
                                                            print("No settings_mysterium 2.")

                                                        try:
                                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/connection_mysterium_option.png", region=(1325, 109, 800, 900), confidence=0.95)
                                                            pyautogui.click(x, y)
                                                            print("connection_mysterium_option Found")
                                                            time.sleep(1)
                                                        except pyautogui.ImageNotFoundException:
                                                            print("No connection_mysterium_option.")

                                                        try:
                                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/refresh_ip_off.png", region=(1325, 109, 800, 900), confidence=0.95)
                                                            pyautogui.click(1640, 300)
                                                            pyautogui.click(1668, 300)
                                                            print("refresh_ip_off Found")
                                                            time.sleep(1)
                                                        except pyautogui.ImageNotFoundException:
                                                            print("No refresh_ip_off.")

                                                        try:
                                                            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/refresh_ip_on.png", region=(1325, 109, 800, 900), confidence=0.95)
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
                        
                        except pyautogui.ImageNotFoundException:
                            print(f"No import_icon .{i}")
                    time.sleep(1)


            except pyautogui.ImageNotFoundException:
                print("No import_icon .")

        except pyautogui.ImageNotFoundException:
            print("No cookie_icon .")

        try:
            x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/allow_button.png", region=(1080, 247, 400, 300), confidence=0.95)
            pyautogui.click(x, y)
            print("allow_button Found")
                    
        except pyautogui.ImageNotFoundException:
            print("No allow_button .")

def nopecha_elements():
    try:
        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/nopecha_error.png", region=(1625, 43, 400, 300), confidence=0.95)
        pyautogui.click(x, y)
        print("nopecha_error Button Found")
        for i in range(1,1000):
            time.sleep(1)
            try:
                x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/text_captcha_option.png", region=(1430, 475, 300, 300), confidence=0.97)
                pyautogui.click(x, y)
                print("text_captcha_option Button Found")
                time.sleep(2)

            except pyautogui.ImageNotFoundException:
                print(f"No text_captcha_option Button.{i}")
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/auto_solve_off.png", region=(1412, 152, 800, 800), confidence=0.9)
                    pyautogui.click(1693, 193)
                    pyautogui.click(1735, 193)
                    print("auto_solve_off Button Found")
                    time.sleep(2)
                except pyautogui.ImageNotFoundException:
                    print(f"No auto_solve_off Button.{i}")
                try:
                    x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/auto_solve_on.png", region=(1412, 152, 800, 800), confidence=0.9)
                    print("auto_solve_on Button Found")
                    try:
                        x, y = pyautogui.locateCenterOnScreen("/root/Desktop/MFV6/images/elements_filled.png", region=(1412, 152, 800, 800), confidence=0.95)
                        print("elements_filled Button Found")
                        return True
                    except pyautogui.ImageNotFoundException:
                        print(f"No elements_filled Button.{i}")
                        print('Adding the Elements..')
                        pyautogui.click(1705, 509)
                        time.sleep(1)
                        pyautogui.click(1705, 509)
                        pyautogui.click(1705, 509)
                        pyautogui.click(1705, 509)
                        pyautogui.press('delete')
                        pyautogui.typewrite('#numberCaptcha')

                        time.sleep(1)
                        pyautogui.click(1705, 612)
                        time.sleep(1)
                        pyautogui.click(1705, 612)
                        pyautogui.click(1705, 612)
                        pyautogui.click(1705, 612)
                        pyautogui.press('delete')
                        pyautogui.typewrite('#captcha')
                        pyautogui.click(1613, 137)
                        print(' Elements Added')
                    
                except pyautogui.ImageNotFoundException:
                    print(f"No auto_solve_on Button.{i}")
                    
    except pyautogui.ImageNotFoundException:
        print("No nopecha_error Button.")
    return None

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


chrome_binary_path = '/opt/google/chrome/google-chrome'
chrome_user_data_dir = '/root/.config/google-chrome/'
dc = Driver(uc=False, headed= True)
dc.maximize_window()
url = "chrome://extensions/"
dc.open(url)
print(dc.get_title())

mysterium = install_extensions('mysterium')
nopecha = install_extensions('nopecha')
cookie = install_extensions('cookie')
fingerprint = install_extensions('fingerprint')
if fingerprint and mysterium and nopecha and cookie:
    print('All Extensions are installed..')
    if pin_extensions():
        print('All Extensions are pinned')
        if nopecha_elements():
            print('Nopecha Elements Added')
            if mysterium_login():
                print('Mysterium Login Done...')
                #mysterium_vpn_connect('estonia')
                time.sleep(100000)
time.sleep(100000)
