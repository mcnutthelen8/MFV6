from flask import Flask, jsonify, render_template, request, Response
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta
import pytz
import random
import requests


app = Flask(__name__)
refaccset = [1,3,4]
# MongoDB connection URI
mongo_uri = "mongodb+srv://redgta36:J6n7Hoz2ribHmMmx@moneyfarm.wwzcs.mongodb.net/?retryWrites=true&w=majority&appName=moneyfarm"

# Connect to the MongoDB cluster
client = MongoClient(mongo_uri)

# Specify the database and collection
db = client['MoneyFarmV6']  # Replace with your database name
#collection = db['Farm1']  # Replace with your collection name
def rpm_cal(results):
    messages2 = []
    
    for document in results:  # Iterate over each document
        if isinstance(document, dict) and 'messages' in document:  # Check if 'messages' field exists in the document
            messages = document['messages']
            messages2.append(messages)
        else:
            print("No 'messages' field found in this document or document is not a dictionary")
    
    if not messages2:
        print("No valid documents found.")
        return 0 

    data_dict = messages2[0]
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)  # Current UTC time
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)
    now = sri_lanka_time.strftime('%Y-%m-%d %H:%M:%S')
    sorted_data = dict(sorted(data_dict.items(), key=lambda item: datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S")))
    current_time = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    one_hour_ago = current_time - timedelta(hours=1)
    filtered_messages = {k: v for k, v in sorted_data.items() if one_hour_ago <= datetime.strptime(k, "%Y-%m-%d %H:%M:%S") <= current_time}
    
    if len(filtered_messages) > 0:
        first_timestamp = list(filtered_messages.keys())[0]
        last_timestamp = list(filtered_messages.keys())[-1]

        first_amount = filtered_messages[first_timestamp]
        last_amount = filtered_messages[last_timestamp]

        try:
            # Check if the amount is a string and remove commas if needed
            if first_amount:
                if isinstance(first_amount, str):
                    first_amount = float(first_amount.replace(',', ''))
                else:
                    first_amount = float(first_amount)  # If already a number, convert to float
            if last_amount:
                if isinstance(last_amount, str):
                    last_amount = float(last_amount.replace(',', ''))
                else:
                    if last_amount:
                        last_amount = float(last_amount)
                    else:
                        last_amount = 0  # If already a number, convert to float
        except ValueError:
            print(f"Invalid amount data: first_amount={first_amount}, last_amount={last_amount}")
            return 0
        if first_amount and last_amount:
            amount_difference = last_amount - first_amount
            return amount_difference
        return 0
    else:
        return 0


def calculate_hourly_earnings(results):
    messages2 = []
    
    for document in results:  # Iterate over each document
        if isinstance(document, dict) and 'messages' in document:  # Check if 'messages' field exists in the document
            messages = document['messages']
            messages2.append(messages)
        else:
            print("No 'messages' field found in this document or document is not a dictionary")
    
    
    if not messages2:
        print("No valid documents found. Cal")
        return {}

    # Combine all message dictionaries into one (if there are multiple)
    data_dict = {}
    for message_set in messages2:
        data_dict.update(message_set)
    
    # Setup timezone for Sri Lanka
    sri_lanka_tz = pytz.timezone('Asia/Colombo')
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    sri_lanka_time = utc_now.astimezone(sri_lanka_tz)

    # Make sure all timestamps are aware datetime objects
    sorted_data = dict(sorted(data_dict.items(), key=lambda item: datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S").replace(tzinfo=sri_lanka_tz)))

    # Prepare results to store earnings per hour
    earnings_per_hour = {}
    
    # Get current hour to use for ordering
    current_hour = sri_lanka_time.replace(minute=0, second=0, microsecond=0)

    # Iterate through the last 24 hours
    for i in range(24):
        # Calculate start and end times for each hour interval
        end_time = current_hour - timedelta(hours=i)
        start_time = end_time - timedelta(hours=1)

        # Filter messages within this hour window
        filtered_messages = {k: v for k, v in sorted_data.items() 
                             if start_time <= datetime.strptime(k, "%Y-%m-%d %H:%M:%S").replace(tzinfo=sri_lanka_tz) < end_time}
        
        if len(filtered_messages) > 0:
            # Get the first and last message of this hour
            first_timestamp = list(filtered_messages.keys())[0]
            last_timestamp = list(filtered_messages.keys())[-1]

            first_amount = filtered_messages[first_timestamp]
            last_amount = filtered_messages[last_timestamp]

            # Convert amounts to float and calculate the difference
            try:
                if isinstance(first_amount, str):
                    first_amount = float(first_amount.replace(',', ''))
                else:
                    first_amount = float(first_amount)

                if isinstance(last_amount, str):
                    last_amount = float(last_amount.replace(',', ''))
                else:
                    if last_amount:
                        last_amount = float(last_amount)
                    else:
                        last_amount = 0  #
            except ValueError:
                print(f"Invalid amount data: first_amount={first_amount}, last_amount={last_amount}")
                earnings_per_hour[end_time.strftime('%H:00')] = 0
                continue

            # Calculate the difference and store the result
            earnings_per_hour[end_time.strftime('%H:00')] = last_amount - first_amount
        else:
            # If no messages in this hour, set earnings to 0
            earnings_per_hour[end_time.strftime('%H:00')] = 0

    # Sort the earnings from the current hour to the last hour (24 hours back)
    ordered_earnings = {}
    for i in range(24):
        hour = (current_hour - timedelta(hours=i)).strftime('%H:00')
        if hour in earnings_per_hour:
            ordered_earnings[hour] = earnings_per_hour[hour]
        else:
            ordered_earnings[hour] = 0
    
    return ordered_earnings

def send_discord_message(webhook_url, message):
    data = {
        "content": message
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")


@app.route('/get-data')
def get_data():
    query = {"type": "main"}
    all_sources = """<table id="maintable">
                            <tr>
                                <th>FarmID</th>
                                <th>Email</th>
                                <th>IP Address</th>
                                <th>Status</th>
                                <th colspan="3">Plants</th>
                                <th colspan="2">Control Panel</th>
                            </tr>"""
    runningfarmstat = 0
    runningcsbstat = 0
    earnstat = 0
    all_charts = []
    all_charts_time = []
    all_charts_feyorra = []
    all_charts_time_feyorra = []
    csb_source = ""
    for i in range(1, 11): 
        farm_name = f'Farm{i}'
        collection = db[farm_name]
        document = collection.find_one(query)
        message_pepe = collection.find({"type": "pepelom"})
        message_feyorra = collection.find({"type": "feyorramack"})
        message_claimc = collection.find({"type": "claimcoins"})
        #message_bitmoon = collection.find({"type": "bitmoon"})
        
        if document: #and message_pepe:
            rpm_pepe1 = rpm_cal(message_pepe)
            rpm_feyorra1 = rpm_cal(message_feyorra)
            rpm_claimc1 = rpm_cal(message_claimc)
            #rpm_bitmo1 = rpm_cal(message_bitmoon)
            #print(rpm_pepe1)
            #rpm_feyorra = int(float(rpm_feyorra1))
            rpm_feyorra = f'<b style="color:limegreen;">{round(rpm_feyorra1, 5)} </b>' if round(rpm_feyorra1, 5) > 0.01  else f'<b style="color:red;">{round(rpm_feyorra1, 5)} </b>'

            rpm_pepe = f'<b style="color:limegreen;">{round(rpm_pepe1, 5)} </b>' if round(rpm_pepe1, 5) > 0.03  else f'<b style="color:red;">{round(rpm_pepe1, 5)} </b>'
            rpm_claimc = f'<b style="color:limegreen;">{abs(int(rpm_claimc1))} </b>' if abs(int(rpm_claimc1)) > 60  else f'<b style="color:red;">{abs(int(rpm_claimc1))} </b>'
            #rpm_bitmo = f'<b style="color:limegreen;">{abs(int(rpm_bitmo1))} </b>' if abs(int(rpm_bitmo1)) > 40  else f'<b style="color:red;">{abs(int(rpm_bitmo1))} </b>'
            
            
            #print(rpm_pepe)

            current_time = datetime.now()
            given_time_str = document['Status']
            given_time = datetime.strptime(given_time_str, "%Y-%m-%d %H:%M:%S")
            time_difference = current_time - given_time
            status = f'<b style="color:limegreen;">{given_time_str}🟢 </b>' if time_difference <= timedelta(minutes=5) else f'<b style="color:red;">{given_time_str}🔴 </b>'

            # Prepare the table content for this farm
            email = document['Email']
            withdraw_mail = document['withdraw_mail']
            mails = f'<b>Account:</b> {email} <br><b>Layout:</b> {withdraw_mail}'
            ip_address = document['Ip']
            pepelom = document['pepelom']
            feyorramack = document['feyorramack']
            claimc = document['claimcoins']

            vals = pepelom + feyorramack
            earnstat +=vals
            #bitmon = document['bitmoon']
            # Convert the string values to floats
            #pepe_valuex = float(pepelom.replace(',', ''))
            #feyorra_valuex = float(feyorramack.replace(',', ''))
            #claimc_valuex = float(claimc.replace(',', ''))
            pepe_dollarsx = 0
            # Perform the calculations

            req = document['request']
            res = document['response']



            if res == 'Running':
                if time_difference >= timedelta(minutes=5):
                    res = f'Offline🔴'
                else:
                    res = f'Running🟢'
                    runningfarmstat += 1

            # Append this farm's data to the combined source string
            farm_source = f"""
                <tr>
                    <td rowspan="6">{farm_name}</td>
                    <td rowspan="6">{mails}</td>
                    <td rowspan="6">{ip_address}</td>
                    <td rowspan="6">{status}</td>
                    <td rowspan="2">Pepe</td>
                    <th>Amount</th>
                    <th>RPH</th>
                    <td rowspan="2" colspan="1">{req}</td>
                    
                    <td rowspan="2" colspan="1">{res}</td>
                </tr>
                <tr>
                    <td>{pepelom}</td>
                    <td>{rpm_pepe}</td>
                    
                </tr>
                <tr>
                    <td rowspan="2">Feyorra</td>
                    <th>Amount</th>
                    <th>RPH</th>

                <td rowspan="4" colspan="3">
                    <button type="submit" name="button" value="ipfixer-{farm_name}" class="button-control-panel">IP Fixer</button>
                    <button type="submit" name="button" value="mainscript-{farm_name}" class="button-control-panel">Main Script</button>
                    <button type="submit" name="button" value="reset-{farm_name}" class="button-control-panel">Reset</button>
                    <button type="submit" name="button" value="pause-{farm_name}" class="button-control-panel">Pause</button>
                    <button type="submit" name="button" value="kill-{farm_name}" class="button-control-panel">Kill</button>
                    <br>
                    <button type="submit" name="button" value="withdrawpepe-{farm_name}" class="button-control-panel">Pepe Withdraw</button>
                    <button type="submit" name="button" value="withdrawfeyorra-{farm_name}" class="button-control-panel">Feyorra Withdraw</button>
                    <button type="submit" name="button" value="withdrawclaimc-{farm_name}" class="button-control-panel">ClaimC Withdraw</button>
                    <br>
                    <button type="submit" name="button" value="Layout1-{farm_name}" class="button-control-panel">Layout 1</button>
                    <button type="submit" name="button" value="Layout2-{farm_name}" class="button-control-panel">Layout 2</button>
                    <button type="submit" name="button" value="Layout3-{farm_name}" class="button-control-panel">Layout 3</button>
                    <button type="submit" name="button" value="Layout4-{farm_name}" class="button-control-panel">Layout 4</button>
                </td>
                </tr>
                <tr>
                    <td>{feyorramack}</td>
                    <td>{rpm_feyorra}</td>
                </tr>
                <tr>
                    <td rowspan="2">ClaimC</td>
                    <th>Amount</th>
                    <th>RPH</th>
                </tr>
                <tr>
                    <td>{claimc}</td>
                    <td>{rpm_claimc}</td>
                </tr>

            """
            all_sources += farm_source

            message_pepe = collection.find({"type": "pepelom"})
            chart_pepe = calculate_hourly_earnings(message_pepe)
            chart_pepe_times = list(chart_pepe.keys())
            chart_pepe_amounts = list(chart_pepe.values())
            char_pepe = []
            for amount in chart_pepe_amounts:
                if amount > 40:
                    amount = 40
                if amount < 0:
                    amount = 0
                char_pepe.append(amount)
            chart_pepe_amounts = char_pepe
            chart_pepe_times.reverse()
            chart_pepe_amounts.reverse()

            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            if farm_name == 'Farm1':
                all_charts_time = chart_pepe_times
            chart_ex1 ={
                        'label': farm_name, 
                        'data': chart_pepe_amounts, 
                        'borderColor': f'rgba({red}, {green}, {blue}, 1)', 
                        'backgroundColor': f'rgba({red}, {green}, {blue}, 0.2)',
                        'fill': True, 
                        'tension': 0.4 
            }
            all_charts.append(chart_ex1)

            #feyorramack
            message_feyorra = collection.find({"type": "feyorramack"})
            chart_feyorra = calculate_hourly_earnings(message_feyorra)
            chart_feyorra_times = list(chart_feyorra.keys())
            chart_feyorra_amounts = list(chart_feyorra.values())
            char_feyorra = []
            for amount in chart_feyorra_amounts:
                if amount > 800:
                    amount = 800
                if amount < 0:
                    amount = 0
                char_feyorra.append(amount)
            chart_feyorra_amounts = char_feyorra
            chart_feyorra_times.reverse()
            chart_feyorra_amounts.reverse()
            if farm_name == 'Farm1':
                all_charts_time_feyorra = chart_feyorra_times
            chart_ex2 ={
                        'label': farm_name, 
                        'data': chart_feyorra_amounts, 
                        'borderColor': f'rgba({red}, {green}, {blue}, 1)', 
                        'backgroundColor': f'rgba({red}, {green}, {blue}, 0.2)',
                        'fill': True, 
                        'tension': 0.4 
            }
            all_charts_feyorra.append(chart_ex2)

            #message = f"<@{545070510367834133}> Farm{i} has Offline🔴. Last Activity:{given_time_str} | Req:{req} / Res:{res}"
            #if req == 'mainscript' and res == 'Offline🔴': #and time_difference >= timedelta(minutes=5):
            #    send_discord_message(webhook_url, message)


        else:
            all_sources += f"<tr><td colspan='7'>No data found for {farm_name}</td></tr>"

        if i % 5 == 0:
            farm_source = f"""
                                </table><br>
                    """
            quotient = i // 5
            collection = db[f'CSB{quotient}']
            document = collection.find()
            document2 = collection.find_one({"csb_script_id": f"CSB{quotient}"})

            csb_script_id = document2['csb_script_id']
            csb_logins = document2['csb_logins']
            devboxes = document2['devboxes']
            ucredit = document2['ucredit']
            rq = document2['request']
            rs = document2['response']
            hello = f'{rq} | {rs}'

            devbox_list = devboxes.split('<br>\n')
            devbox_withbutton = """ """

            #devbox_withbutton += f'<button type="submit" name="button" value="CSB{quotient}-s1" class="button-control-panel">SandBox 1</button><br>'
            #devbox_withbutton += f'<button type="submit" name="button" value="CSB{quotient}-s2" class="button-control-panel">SandBox 2</button><br>'
            #devbox_withbutton += f'<button type="submit" name="button" value="CSB{quotient}-s3" class="button-control-panel">SandBox 3</button><br>'
            #devbox_withbutton += f'<button type="submit" name="button" value="CSB{quotient}-s4" class="button-control-panel">SandBox 4</button><br>'
            #devbox_withbutton += f'<button type="submit" name="button" value="CSB{quotient}-s5" class="button-control-panel">SandBox 5</button><br>'
            #devbox_withbutton += f'''<button type="submit" name="button" value="CSB{quotient}-pause" class="button-control-panel">Pause</button>
            #                        <button type="submit" name="button" value="CSB{quotient}-kill" class="button-control-panel">Kill</button>
            #                        <button type="submit" name="button" value="CSB{quotient}-None" class="button-control-panel">None</button><br>'''
            devbox_withbutton += f'''<button type="submit" name="button" value="CSB{quotient}-ipfixer" class="button-control-panel">IP Fixer</button><br>
                                    <button type="submit" name="button" value="CSB{quotient}-Layout1" class="button-control-panel">Layout 1</button><br>
                                    <button type="submit" name="button" value="CSB{quotient}-Layout2" class="button-control-panel">Layout 2</button><br>
                                    <button type="submit" name="button" value="CSB{quotient}-Layout3" class="button-control-panel">Layout 3</button><br>
                                    <button type="submit" name="button" value="CSB{quotient}-Layout4" class="button-control-panel">Layout 4</button><br>'''
            

            current_time = datetime.now()

            given_time_str = document2['status']
            given_time = datetime.strptime(given_time_str, "%Y-%m-%d %H:%M:%S")
            time_difference = current_time - given_time
            status = f'<b style="color:limegreen;">{given_time_str}🟢 </b>' if time_difference <= timedelta(minutes=30) else f'<b style="color:red;">{given_time_str}🔴 </b>'
            if time_difference <= timedelta(minutes=30):
                runningcsbstat += 1


            new_data = f"""                        <table id="CSB-table">
                            <thead>
                                <tr>
                                    <th>CSB Script ID</th>
                                    <th>CSB Login</th>
                                    <th>URL ID</th>
                                    <th>Used Credits</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
            <tr class="expandable">
                <td>{csb_script_id}</td>
                <td>{csb_logins}</td>
                <td>{devboxes}</td>

                <td>{ucredit}</td>

                <td>{status}</td>
                <td>{devbox_withbutton}</td>
                <td>{hello}</td>
            </tr>
            <tr class="details">
                <td colspan="5">
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Devbox</th>
                                <th>Credit</th>
                                <th>Runtime</th>
                                <th>VM Tier</th>
                            </tr>
                        </thead>
                        <tbody> """
            all_sources += new_data
            for doc in document:
                if 'ID_name' in doc:
                    ID_name = doc['ID_name']
                    Devbox = doc['Devbox']
                    Credit = doc['Credit']
                    Runtime = doc['Runtime']
                    Vm_Tier = doc['Vm_Tier']

                    new_data = f"""
                                            <table id="CSB-table">
                                <thead>
                                    <tr>
                                        <th>CSB Script ID</th>
                                        <th>CSB Login</th>
                                        <th>URL ID</th>
                                        <th>Used Credits</th>
                                        <th>Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                            <tr>
                                <td>{ID_name}</td>
                                <td>{Devbox}</td>
                                <td>{Credit}</td>
                                <td>{Runtime}</td>
                                <td>{Vm_Tier}</td>
                            </tr>"""
                            
                    all_sources += new_data
            new_data ="""
                        </tbody>
                    </table>
                </td>
            </tr>                            </tbody>
                            </table>"""
            all_sources += new_data


            all_sources += farm_source

        if i % 5 == 0 and i != 12:
            all_sources += """<table id="maintable">
                                    <tr>
                                        <th>FarmID</th>
                                        <th>Email</th>
                                        <th>IP Address</th>
                                        <th>Status</th>
                                        <th colspan="3">Plants</th>
                                        <th colspan="2">Control Panel</th>
                                    </tr>"""



    collection = db[f'LocalCSB']
    document2 = collection.find_one({"csb_script_id": f"LocalCSB"})

    csb_script_id = document2['csb_script_id']
    csb_logins = document2['csb_logins']
    devboxes = document2['devboxes']
    ucredit = document2['ucredit']
    rq = document2['request']
    rs = document2['response']
    hello = f'{rq} | {rs}'

    devbox_list = devboxes.split('<br>\n')
    devbox_withbutton = """ """

    devbox_withbutton += f'<button type="submit" name="button" value="Local-s1" class="button-control-panel">SandBox 1</button><br>'
    devbox_withbutton += f'<button type="submit" name="button" value="Local-s2" class="button-control-panel">SandBox 2</button><br>'
    devbox_withbutton += f'<button type="submit" name="button" value="Local-s3" class="button-control-panel">SandBox 3</button><br>'
    devbox_withbutton += f'<button type="submit" name="button" value="Local-s4" class="button-control-panel">SandBox 4</button><br>'
    devbox_withbutton += f'<button type="submit" name="button" value="Local-s5" class="button-control-panel">SandBox 5</button><br>'

    devbox_withbutton += f'''<button type="submit" name="button" value="Local-ipfixer" class="button-control-panel">IP Fixer</button>
                            <button type="submit" name="button" value="Local-Layout1" class="button-control-panel">Layout1</button>
                            <button type="submit" name="button" value="Local-Layout2" class="button-control-panel">Layout2</button>
                            <button type="submit" name="button" value="Local-Layout3" class="button-control-panel">Layout3</button>
                            <button type="submit" name="button" value="Local-Layout4" class="button-control-panel">Layout4</button>'''

    current_time = datetime.now()

    given_time_str = document2['status']
    given_time = datetime.strptime(given_time_str, "%Y-%m-%d %H:%M:%S")
    time_difference = current_time - given_time
    status = f'<b style="color:limegreen;">{given_time_str}🟢 </b>' if time_difference <= timedelta(minutes=30) else f'<b style="color:red;">{given_time_str}🔴 </b>'

    earnstat *= 0.25
    runningfarmstat = f"🟢 {runningfarmstat}" if runningfarmstat == 10 or runningfarmstat==5 else f"🔴 {runningfarmstat}"

    mainpanel = f"""
    
    <div class="main-panel">
        <div class="main-panel-box" id="farm-running">
            <p id="runningfarmstat" style="font-size: 40px;font-style: italic;">{runningfarmstat}/12</p>
            <p style="font-size: 20px;font-style:oblique;">Farm Status</p>
        </div>
        <div class="main-panel-box" id="farm-running">
            <p id="runningcsbstat" style="font-size: 40px;font-style: italic;">{runningcsbstat}/3</p>
            <p style="font-size: 20px;font-style:oblique;">CSB Status</p>
        </div>
        <div class="main-panel-box" id="earning">
            <p id="earningstat" style="font-size: 40px;font-style: italic;">{earnstat:.2f}$</p>
            <p style="font-size: 20px;font-style:oblique;">Earn Status</p>
        </div>
    </div>
    <!-- <table id="CSB-table">
                            <thead>
                                <tr>
                                    <th>CSB Script ID</th>
                                    <th>CSB Login</th>
                                    <th>URL ID</th>
                                    <th>Used Credits</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
            <tr class="expandable" >
                <td>{csb_script_id}</td>
                <td>{csb_logins}</td>
                <td>{devboxes}</td>

                <td>{ucredit}</td>

                <td>{status}</td>
                <td>{devbox_withbutton}</td>
                <td>{hello}</td>
            </tr>

            </tbody>
                            </table>-->
                            <br><br>
    """
    return jsonify({"earnstat":earnstat,"runningfarmstat":runningfarmstat,"mainpanel": mainpanel, "source": all_sources, "chartamout": all_charts, "charttime": all_charts_time, "chartamoutfeyorra": all_charts_feyorra, "charttimefeyorra": all_charts_time_feyorra, "csb_source": csb_source})


@app.route('/button-control-panel', methods=['POST'])
def button_control_panel():
    button_value = request.form.get('button')
    print(button_value)
    if 'Local' in button_value:
        query = {"type": "main"}
        farm, func = button_value.split('-')
        print(farm, func)

        collection = db['LocalCSB']
        #doc = collection.find_one(query)
        sample = {
            "request": func,
            "response": 'None',
            
        }
        result = collection.update_one(query, {"$set": sample})  
        if result.modified_count > 0:
            print(f"Updated {result.modified_count} document(s).")
        else:
            print("No document was updated.", farm, func)
        return Response(status=200)
    
    elif 'CSB' in button_value and 'ipfixer'  in button_value:
        farm, func = button_value.split('-')
        print(farm, func,'hellow')
        query = {"type": "main"}
        if farm == 'CSB1':
            for i in range(1,6):
                collection = db[f'Farm{i}']
                #doc = collection.find_one(query)
                sample = {
                    "request": func,
                    "response": 'None',
                    
                }
                result = collection.update_one(query, {"$set": sample})  
                if result.modified_count > 0:
                    print(f"Updated {result.modified_count} document(s).")
                else:
                    print("No document was updated. CP")
        elif farm == 'CSB2':
            for i in range(6,11):
                collection = db[f'Farm{i}']
                #doc = collection.find_one(query)
                sample = {
                    "request": func,
                    "response": 'None',
                    
                }
                result = collection.update_one(query, {"$set": sample})  
                if result.modified_count > 0:
                    print(f"Updated {result.modified_count} document(s).")
                else:
                    print("No document was updated. CP")
        return Response(status=200)
    

    elif 'CSB' in button_value and 'Layout'  in button_value:
        farm, func = button_value.split('-')
        print(farm, func,'hellow')
        query = {"type": "main"}
        if farm == 'CSB1':
            for i in range(1,6):
                collection = db[f'Farm{i}']
                #doc = collection.find_one(query)
                sample = {
                    "withdraw_mail": func,
                    
                }
                result = collection.update_one(query, {"$set": sample})  
                if result.modified_count > 0:
                    print(f"Updated {result.modified_count} document(s).")
                else:
                    print("No document was updated. CP")
        elif farm == 'CSB2':
            for i in range(6,11):
                collection = db[f'Farm{i}']
                #doc = collection.find_one(query)
                sample = {
                    "withdraw_mail": func,
                    
                }
                result = collection.update_one(query, {"$set": sample})  
                if result.modified_count > 0:
                    print(f"Updated {result.modified_count} document(s).")
                else:
                    print("No document was updated. CP")
        return Response(status=200)
    

    elif 'Layout' in button_value and 'CSB' not in button_value:
        query = {"type": "main"}
        layout, farm = button_value.split('-')

        collection = db[farm]
        #doc = collection.find_one(query)
        sample = {
            "withdraw_mail": layout,
            
        }
        result = collection.update_one(query, {"$set": sample})  
        if result.modified_count > 0:
            print(f"Updated {result.modified_count} document(s).")
        else:
            print("No document was updated. CP")
        return Response(status=200)


    elif 'CSB' in button_value:
        query = {"type": "main"}
        farm, func = button_value.split('-')
        print(farm, func)

        collection = db[farm]
        #doc = collection.find_one(query)
        sample = {
            "request": func,
            "response": 'None',
            
        }
        result = collection.update_one(query, {"$set": sample})  
        if result.modified_count > 0:
            print(f"Updated {result.modified_count} document(s).")
        else:
            print("No document was updated.", farm, func)
        return Response(status=200)
    
    
    else:
        query = {"type": "main"}
        func, farm = button_value.split('-')

        collection = db[farm]
        #doc = collection.find_one(query)
        sample = {
            "request": func,
            "response": 'None',
            
        }
        result = collection.update_one(query, {"$set": sample})  
        if result.modified_count > 0:
            print(f"Updated {result.modified_count} document(s).")
        else:
            print("No document was updated. CP")
        return Response(status=200)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
#https://www.pepelom.com/dilu62
#https://www.zaptaps.com/dilu
#mcnutthelen8@gmail.com
#andyrogers468@gmail.com
#khabibmakanzie@gmail.com
