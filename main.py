from seleniumbase import Driver
from PIL import Image
from PIL import Image
import os
import pyautogui
import time
import cv2
import numpy as np
import re
from selenium.webdriver.common.by import By
import numpy as np
from pymongo import MongoClient
import time
from datetime import datetime
import pytz
import datetime

mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"
client = MongoClient(mongo_uri)
db = client['CrashFarmV1'] 
collection = db['Results']


def extract_float(text):
    match = re.search(r'\d+\.\d+', text)
    if match:
        return float(match.group())
    return None

def current_state(driver):
    try:
        element = driver.find_element('h1#crash-payout-text')
        text = driver.get_text('h1#crash-payout-text')
        #print(text)
        if 'Starts' in text:
            val = extract_float(text)
            return 'Starting' , val
        elif 'Crash' in text:
            val = extract_float(text)
            return 'Crashed' , val 
        elif 'x' in text:
            val = extract_float(text)
            return 'Ongoing', val
        else:
            print(f'Unknown...{text}')
    except Exception as e:
        print(e)
    return


def get_last_ten(driver):
    container_selector = ".styles_row__3CzDv"  
    element_selector = ".styles_historyElement__3VTSn" 
    container = driver.find_element(By.CSS_SELECTOR, container_selector)
    elements = container.find_elements(By.CSS_SELECTOR, element_selector)
    values = [float(element.text.strip()) for element in elements if element.text.strip()]
    
    print('Last Values:', values)
    return values


def isacc_formula(list, sana):
    disura= 0
    for val in list:
        if val < sana:
            disura+= 1
    return disura


def determine_zone(results):
    first_five = results[:5]
    last_five = results[-5:]
    x  = isacc_formula(results, 2)
    y  = isacc_formula(first_five, 2)
    z  = isacc_formula(last_five, 2)
    if x >= 6:
        return 'Beta Zone Riskyy'
    return 'Omega Zone 50/50'
    


def analyze_results(results):
    # Calculate moving average
    moving_average = np.mean(results[-5:])  # Average of the last 5 results
    # Calculate standard deviation
    std_dev = np.std(results)
    
    return moving_average, std_dev

def should_enter(moving_average, std_dev, threshold=1.5):
    # Set a lower threshold for entering the game
    if moving_average < threshold * std_dev:
        return True  # Suggest entering
    return False  # Suggest not entering


def safe_betting_multiplier(results, zone):
    list = []
    for i in results:
        if i > 7:
            i = 5
        list.append(i)
    results = list

    avg_multiplier = np.mean(results)
    safe_multiplier = avg_multiplier * 0.55  
    val = round(safe_multiplier, 2)
    if 'Beta' in zone and val > 1.5:
        return 1.5
    if 'Omega' in zone and val > 3:
        return 3.00
    if val >= 5:
        val = 5.00
    return val

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

import numpy as np
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Function to predict next game metrics
def predict_next_game(data):
    window_size = 3
    X = []
    y_exit = []
    for i in range(len(data) - window_size):
        window = data[i:i + window_size]
        X.append(window)
        y_exit.append(data[i + window_size])  # Next value as the target

    X = np.array(X)
    y_exit = np.array(y_exit)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Define and train XGBoost model for safe exit prediction
    exit_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=3)
    exit_model.fit(X_scaled, y_exit)

    # Clustering to analyze trend zones based on historical patterns
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_scaled)

    latest_data = data[-window_size:]
    input_scaled = scaler.transform([latest_data])
    
    # Predict safe exit value for next round
    predicted_exit = exit_model.predict(input_scaled)[0]
    
    # Determine trend zone
    trend_zone = kmeans.predict(input_scaled)[0]
    
    # Entry decision based on safe exit prediction
    threshold = 2.5
    should_enter = 1 if predicted_exit > threshold else 0
    
    return should_enter, round(predicted_exit, 2), trend_zone



def get_previous_crash(number):
    sb1.open("https://faucetpayio.github.io/verify/#/crash")
    
# Usage example in your test:
sb1 = Driver(uc=True, headed=True, undetectable=True, undetected=True)
sb1.maximize_window()
sb1.open("https://faucetpay.io/crash")
print(sb1.get_title())
time.sleep(5)
# Capture screenshot of an element (for example, the calculator output)
#capture_element_screenshot(sb1, "img.captcha-image")
crash_val = 0
pre_prediction = None
prestate = 'Crashed'

while True:
    try:

        state, value = current_state(sb1)
        if state == 'Crashed':
            print(f'Crashed:{value}', end="\r")
            crash_val = value
            
            if prestate == 'Crashed':
                pass
            else:
                sri_lanka_tz = pytz.timezone('Asia/Colombo')
                utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)  # Corrected here
                sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
                now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
                add_messages('results', {now: crash_val})
                #Results_list.append(crash_val)
                prestate = 'Crashed'

        elif state == 'Ongoing':
            print(f'Ongoing:{value}', end="\r")
        elif state == 'Starting':
            #last_ten = get_last_ten(sb1)

            #last_results = get_last_ten(sb1)
            #print("Last Results:", last_results)
            Results_list = get_last_ten(sb1)
            if pre_prediction:
                if crash_val >= pre_prediction:
                    print(f'WON the Previous Bet Crashed:{crash_val} | Prediction:{pre_prediction}')
                else:
                    print(f'LOST the Previous Bet Crashed:{crash_val} | Prediction:{pre_prediction}')
            else:
                print('Not Enter the BET')

            print('History Values:',Results_list)
            #if Results_list:
            data = Results_list
            enter, safe_exit, zone = predict_next_game(data)
            prediction = safe_exit
                # Display predictions
            print("Should Enter:", "Yes" if enter == 1 else "No")
            print("Predicted Safe Exit Multiplier:", safe_exit)
            print("Trend Zone:", "Good" if zone == 0 else "Neutral" if zone == 1 else "Bad")


                #print("Weighted Moving Average of historical results:", round(weighted_avg, 2))
                #print("Standard Deviation:", round(std_dev, 2))
                #print("Suggested to exit:", safe_betting_multiplier(historical_results))
                #print("Should enter the game?", "Yes" if enter_game else "No")
                #print("Suggested :", prediction)
                #print("Current Zone:", zone)
            pre_prediction = prediction if enter == 1 else None

            for i in range(10):
                time.sleep(1)
                state, value = current_state(sb1)
                if state == 'Ongoing':
                    print(f'Ongoing:{value}')
                    break
    
        prestate = state
    
    
    except Exception as e:
        print(f"ERR:{e}")

#click_element_with_pyautogui(sb1, "div.output")

time.sleep(5)

