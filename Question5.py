import json

# Given JSON data
json_data = '''
{
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
'''

# Convert JSON data to Python dictionary
data = json.loads(json_data)

# Extract the broadcast SSID from the alertData
broadcast_ssid = data["alertData"]["bssids"][0]

# Function to send the message to the external messaging application
def send_to_application(message):
    # Replace this part with the actual implementation to send the message
    # For example, you could use an API call or a messaging library to send the message
    print("Sending message to external application: ", message)

# Call the send_to_application function with the broadcast SSID as the message
send_to_application(broadcast_ssid)