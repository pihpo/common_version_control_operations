import json
# Function to send the message to the external messaging application
def send_to_application(message):
    # Replace this line with code to send the message to the application
    # For this example, we'll simply print the message
    print(message)

# JSON data received from the application
return_val = {
    "alertData": {
        "countNode": 1,
        "bssids": [
            "aa:bb:cc:dd:ee:ff",
            "11:22:33:44:55:66"
        ],
        "minFirstSeen": 1548512334,
        "maxLastSeen": 1548512802,
        "countIsContained": 0,
        "reason": "Seen on LAN",
        "wiredMac": "aa:bb:cc:dd:ee:f0"
    },
    "alertId": "629378047939282802",
    "alertType": "Air Marshal - Roque AP detected",
    "occuredAt": "2019-01-26T14:18:54.000000Z",
    "organizationId": "123456",
    "organizationName": "Organization",
    "organizationUrl": "https://nl.meraki.com/o/.../manage/organization/overview",
    "networkId": "L 123456789012345678",
    "networkName": "Network",
    "networkUrl": "https://nl.meraki.com/.../manage/nodes/list",
    "version": "0.1",
    "SharedSecret": "supersecret",
    "sentAt": "2019-01-26T14:35:20.442869Z"
}
#=====================================================================================
#D Extract the "bssids" list from the "alertData" section of the JSON data
bssids = return_val["alertData"]["bssids"]
alert = return_val["alertType"]
# Send a message to the external messaging application for each broadcast SSID detected
for value in bssids:
    send_to_application("ALERT: detected a bssid on the network: " + value + " AlertType" + alert)
#=====================================================================================
#A
# bssids = return_val["bssids"]
# for number in range (return_val["alertData"]["countNode"]):
# 	send_to_application ("ALERT: detected a bssid on the network: "+ return_val ["alertData"] [bssids] [number])
#=====================================================================================
#B. 
# bssids = return_val["bssids"]
# for value in bssids: 
# 	 send_to_application ("ALERT: detected a bssid on the network: "+value)
#=====================================================================================
#C
# count = retutn_val ["alertData"]["countNode"]
# bssids =return_val ["alertData"] [count] ["bssids"]
# for value in bssids:
#     send_to_application ("ALERT: detected a bssid on the network: "+value)
#=====================================================================================
#D Extract the "bssids" list from the "alertData" section of the JSON data
bssids = return_val["alertData"]["bssids"]
# Send a message to the external messaging application for each broadcast SSID detected
for value in bssids:
    send_to_application("ALERT: detected a bssid on the network: " + value)
#=====================================================================================
# Function to print the index of all key-value pairs
def print_index_and_value(data, prefix=""):
    if isinstance(data, dict):
        for key, value in data.items():
            new_prefix = f"{prefix}['{key}']"
            print(new_prefix)
            print_index_and_value(value, new_prefix)
    elif isinstance(data, list):
        for i, value in enumerate(data):
            new_prefix = f"{prefix}[{i}]"
            print(new_prefix)
            print_index_and_value(value, new_prefix)

# Print the index of all key-value pairs in the JSON data
print_index_and_value(return_val)