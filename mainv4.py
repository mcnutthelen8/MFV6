from seleniumbase import Driver
import subprocess
import pyautogui
import time
import clipboard
import re
from selenium.webdriver.common.by import By
import numpy as np
from pymongo import MongoClient
import time
from datetime import datetime
import pytz
import datetime
import time
import numpy as np


mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"
client = MongoClient(mongo_uri)
db = client['CrashFarmV1'] 
collection = db['Results']

def get_current_window_id():
    result = subprocess.run(['xdotool', 'getactivewindow'], stdout=subprocess.PIPE)
    window_id = result.stdout.decode('utf-8').strip()
    print(f"Current Window ID: {window_id}")
    return window_id

def activate_window_by_id(window_id):
    #print(f"Activate Window ID: {window_id}")
    subprocess.run(['xdotool', 'windowactivate', window_id])

def copy_determine():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('left')
    pyautogui.press('a')
    pyautogui.keyUp('left')
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('left')
    pyautogui.press('c')
    pyautogui.keyUp('left')
    pyautogui.keyUp('ctrl')
    clip = clipboard.paste()
    return clip

def extract_number(input_text):

    input_text = input_text.strip()
    input_text = input_text.strip()
    bet_accepted_match = re.search(r'Bet accepted!\s+(\d+(\.\d+)?x?)', input_text, re.DOTALL)
    if bet_accepted_match:
        return bet_accepted_match.group(1)
    
    match_with_x = re.search(r'\b\d+(\.\d+)?x\b', input_text)
    if match_with_x:
        return match_with_x.group()

    return None
def add_messages(type_value, new_messages):
    try:
        query = {"type": type_value}
        existing_doc = collection.find_one(query)
        print("Existing document before update")
        new_message = new_messages
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



sb1 = Driver(uc=True, headed=True, undetectable=True, undetected=True)
sb1.maximize_window()
sb1.open("https://1xbet.com/en/allgamesentrance/crash")
xbet_window = get_current_window_id()
print(sb1.get_title())
time.sleep(10)

ongoing = '1.00x'
upload = True
while True:
    activate_window_by_id(xbet_window)
    clip = copy_determine()
    value = extract_number(clip)
    if value:
        if 'x'in value:
            upload = False
            ongoing = value
            print(f'Ongoing:{value}')
        else:
            if upload:
                print(f'Starting:{value}')
            else:
                numeric_value = float(ongoing.rstrip('x'))
                sri_lanka_tz = pytz.timezone('Asia/Colombo')
                utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                print(now, numeric_value)
                add_messages('results', {now: numeric_value})

                upload = True
    else:
        print('There are no VAluesERR', value)

