import json

json_data = '''
{
  "data": [
    {
      "deviceId": "10.10.1.1",
      "system-ip": "10.10.1.1",
      "host-name": "vmanage",
      "reachability": "reachable",
      "status": "normal",
      "personality": "vmanage",
      "device-type": "vmanage",
      "timezone": "UTC",
      "device-groups": [
        "No groups"
      ],
      "lastupdated": 1689620969357,
      "domain-id": "0",
      "board-serial": "F6963C4202C4B04C",
      "certificate-validity": "Valid",
      "max-controllers": "0",
      "uuid": "81ac6722-a226-4411-9d5d-45c0ca7d567b",
      "controlConnections": "6",
      "device-model": "vmanage",
      "version": "20.10.1",
      "connectedVManages": [
        "10.10.1.1"
      ],
      "site-id": "101",
      "latitude": "37.666684",
      "longitude": "-122.777023",
      "isDeviceGeoData": false,
      "platform": "x86_64",
      "uptime-date": 1689354060000,
      "statusOrder": 4,
      "device-os": "next",
      "validity": "valid",
      "state": "green",
      "state_description": "All daemons up",
      "model_sku": "None",
      "local-system-ip": "10.10.1.1",
      "total_cpu_count": "4",
      "testbed_mode": false,
      "layoutLevel": 1
    },
    {
      "deviceId": "10.10.1.5",
      "system-ip": "10.10.1.5",
      "host-name": "vsmart",
      "reachability": "reachable",
      "status": "normal",
      "personality": "vsmart",
      "device-type": "vsmart",
      "timezone": "UTC",
      "device-groups": [
        "No groups"
      ],
      "lastupdated": 1689355138938,
      "domain-id": "1",
      "board-serial": "F6963C4202C4B04E",
      "certificate-validity": "Valid",
      "uuid": "f7b49da3-383e-4cd5-abc1-c8e97d345a9f",
      "controlConnections": "11",
      "device-model": "vsmart",
      "version": "20.10.1",
      "connectedVManages": [
        "10.10.1.1"
      ],
      "site-id": "101",
      "ompPeers": "4",
      "latitude": "37.666684",
      "longitude": "-122.777023",
      "isDeviceGeoData": false,
      "platform": "x86_64",
      "uptime-date": 1682596920000,
      "statusOrder": 4,
      "device-os": "next",
      "validity": "valid",
      "state": "green",
      "state_description": "All daemons up",
      "model_sku": "None",
      "local-system-ip": "10.10.1.5",
      "total_cpu_count": "2",
      "testbed_mode": false,
      "layoutLevel": 2
    },
    {
      "deviceId": "10.10.1.3",
      "system-ip": "10.10.1.3",
      "host-name": "vbond",
      "reachability": "reachable",
      "status": "normal",
      "personality": "vbond",
      "device-type": "vbond",
      "timezone": "UTC",
      "device-groups": [
        "No groups"
      ],
      "lastupdated": 1689355128176,
      "board-serial": "F6963C4202C4B04D",
      "certificate-validity": "Valid",
      "uuid": "ed0863cb-83e7-496c-b118-068e2371b13c",
      "controlConnections": "--",
      "device-model": "vedge-cloud",
      "version": "20.10.1",
      "connectedVManages": [
        "10.10.1.1"
      ],
      "site-id": "101",
      "ompPeers": "--",
      "latitude": "37.666684",
      "longitude": "-122.777023",
      "isDeviceGeoData": false,
      "platform": "x86_64",
      "uptime-date": 1682596920000,
      "statusOrder": 4,
      "device-os": "next",
      "validity": "valid",
      "state": "green",
      "state_description": "All daemons up",
      "model_sku": "None",
      "local-system-ip": "10.10.1.3",
      "total_cpu_count": "4",
      "linux_cpu_count": "1",
      "testbed_mode": false,
      "layoutLevel": 3
    },
    {
      "deviceId": "10.10.1.11",
      "system-ip": "10.10.1.11",
      "host-name": "dc-cedge01",
      "reachability": "reachable",
      "status": "normal",
      "personality": "vedge",
      "device-type": "vedge",
      "timezone": "UTC +0000",
      "device-groups": [
        "No groups"
      ],
      "lastupdated": 1689634889181,
      "bfdSessionsUp": 12,
      "domain-id": "1",
      "board-serial": "756C5620",
      "certificate-validity": "Valid",
      "max-controllers": "0",
      "uuid": "C8K-E2D91A30-814B-F22D-4E7B-7D39BE74EE32",
      "bfdSessions": "12",
      "controlConnections": "3",
      "device-model": "vedge-C8000V",
      "version": "17.10.01.0.1479",
      "connectedVManages": [
        "10.10.1.1"
      ],
      "site-id": "100",
      "ompPeers": "1",
      "latitude": "37.411",
      "longitude": "-121.932",
      "isDeviceGeoData": true,
      "platform": "x86_64",
      "uptime-date": 1682599500000,
      "statusOrder": 4,
      "device-os": "next",
      "validity": "valid",
      "state": "green",
      "state_description": "All daemons up",
      "model_sku": "None",
      "local-system-ip": "10.10.1.11",
      "total_cpu_count": "2",
      "linux_cpu_count": "1",
      "testbed_mode": false,
      "layoutLevel": 4
    },
    {
      "deviceId": "10.10.1.13",
      "system-ip": "10.10.1.13",
      "host-name": "site1-cedge01",
      "reachability": "reachable",
      "status": "normal",
      "personality": "vedge",
      "device-type": "vedge",
      "timezone": "UTC +0000",
      "device-groups": [
        "No groups"
      ],
      "lastupdated": 1689634854580,
      "bfdSessionsUp": 4,
      "domain-id": "1",
      "board-serial": "1CD8DEDA",
      "certificate-validity": "Valid",
      "max-controllers": "0",
      "uuid": "C8K-7B7B98B0-4FF2-273A-D915-9CC9DC3B835C",
      "bfdSessions": "4",
      "controlConnections": "3",
      "device-model": "vedge-C8000V",
      "version": "17.10.01.0.1479",
      "connectedVManages": [
        "10.10.1.1"
      ],
      "site-id": "1001",
      "ompPeers": "1",
      "latitude": "35.852",
      "longitude": "-78.869",
      "isDeviceGeoData": true,
      "platform": "x86_64",
      "uptime-date": 1682599500000,
      "statusOrder": 4,
      "device-os": "next",
      "validity": "valid",
      "state": "green",
      "state_description": "All daemons up",
      "model_sku": "None",
      "local-system-ip": "10.10.1.13",
      "total_cpu_count": "2",
      "linux_cpu_count": "1",
      "testbed_mode": false,
      "layoutLevel": 4
    },
    {
      "deviceId": "10.10.1.15",
      "system-ip": "10.10.1.15",
      "host-name": "site2-cedge01",
      "reachability": "reachable",
      "status": "normal",
      "personality": "vedge",
      "device-type": "vedge",
      "timezone": "UTC +0000",
      "device-groups": [
        "No groups"
      ],
      "lastupdated": 1689355227090,
      "bfdSessionsUp": 4,
      "domain-id": "1",
      "board-serial": "6ED0F19A",
      "certificate-validity": "Valid",
      "max-controllers": "0",
      "uuid": "C8K-54A8601A-DFA6-9446-6E31-F06E42F1EFC6",
      "bfdSessions": "4",
      "controlConnections": "3",
      "device-model": "vedge-C8000V",
      "version": "17.10.01.0.1479",
      "connectedVManages": [
        "10.10.1.1"
      ],
      "site-id": "1002",
      "ompPeers": "1",
      "latitude": "53.277",
      "longitude": "-8.932",
      "isDeviceGeoData": true,
      "platform": "x86_64",
      "uptime-date": 1689168660000,
      "statusOrder": 4,
      "device-os": "next",
      "validity": "valid",
      "state": "green",
      "state_description": "All daemons up",
      "model_sku": "None",
      "local-system-ip": "10.10.1.15",
      "total_cpu_count": "2",
      "linux_cpu_count": "1",
      "testbed_mode": false,
      "layoutLevel": 4
    },
    {
      "deviceId": "10.10.1.17",
      "system-ip": "10.10.1.17",
      "host-name": "site3-vedge01",
      "reachability": "reachable",
      "status": "normal",
      "personality": "vedge",
      "device-type": "vedge",
      "timezone": "UTC",
      "device-groups": [
        "No groups"
      ],
      "lastupdated": 1689355176350,
      "bfdSessionsUp": 4,
      "domain-id": "1",
      "board-serial": "1701BB87",
      "certificate-validity": "Valid",
      "max-controllers": "0",
      "uuid": "dac3e7f5-b48f-d29b-0685-d3bb4b2ea991",
      "bfdSessions": "4",
      "controlConnections": "3",
      "device-model": "vedge-cloud",
      "version": "20.10.1",
      "connectedVManages": [
        "10.10.1.1"
      ],
      "site-id": "1003",
      "ompPeers": "1",
      "latitude": "53.408",
      "longitude": "-2.228",
      "isDeviceGeoData": true,
      "platform": "x86_64",
      "uptime-date": 1682599140000,
      "statusOrder": 4,
      "device-os": "next",
      "validity": "valid",
      "state": "green",
      "state_description": "All daemons up",
      "model_sku": "None",
      "local-system-ip": "10.10.1.17",
      "total_cpu_count": "2",
      "linux_cpu_count": "1",
      "testbed_mode": false,
      "layoutLevel": 4
    }
  ]
}
'''

# Parse the JSON data
data = json.loads(json_data)

A = data['data'][0]['deviceId']
B = data['data'][0]['status']

C = data['data'][1]['deviceId']
D = data['data'][1]['status']

E = data['data'][2]['deviceId']
F = data['data'][2]['status']

G = data['data'][3]['deviceId']
K = data['data'][3]['status']

print("device 1 : "+A +" have : ",B)  # Output: up
print("device 2 : "+C +" have : ",D)
print("device 1 : "+E +" have : ",F)  # Output: up
print("device 2 : "+G +" have : ",K)
# Retrieve deviceId and status values for each item in the "data" list
device_statuses = [(item["deviceId"], item["status"]) for item in data["data"]]

# # Print the deviceId and status values
for device_id, status in device_statuses:
    print("Device ID:", device_id)
    print("Status:", status)
    print()

#==========================================================================================
import json

json_data = '''
{
    "data": [
        {
            "count": 4,
            "detailsURL": "",
            "name": "VEdge Hardware Health",
            "status": "error",
            "statusList": [
                {
                    "count": 4,
                    "detailsURL": "/dataservice/device/hardwarehealth/detail?state-normal",
                    "message": "4 (normal=4, warning=0, error=0)",
                    "name": "normal",
                    "status": "up"
                }
            ]
            
        }
    ]
}
'''

json_data2 = '''
{
  "data": [
    {
      "count": 4,
      "detailsURL": "",
      "name": "VEdge Hardware Health",
      "status": "error",
      "statusList": [
        {
          "count": 4,
          "detailsURL": "/dataservice/device/hardwarehealth/detail?state-normal",
          "message": "4 (normal=4, warning=0, error=0)",
          "name": "normal",
          "status": "up"
        }
      ]
    }
  ],
  "cisco": [
    {
      "count": 4,
      "detailsURL": "",
      "name": "cisco Hardware Health",
      "status": "error",
      "statusList": [
        {
          "count": 4,
          "detailsURL": "/dataservice/device/hardwarehealth/detail?state-abnormal",
          "message": "40 (normal=10, warning=10, error=10)",
          "name": "abnormal",
          "status": "up"
        }
      ]
    }
  ]
}
'''
json_data3 = '''
{
  "data": [
    {
      "count": 4,
      "detailsURL": "",
      "name": "VEdge Hardware Health",
      "status": "error",
      "statusList": [
        {
          "count": 4,
          "detailsURL": "/dataservice/device/hardwarehealth/detail?state-normal",
          "message": "4 (normal=4, warning=0, error=0)",
          "name": "normal",
          "status": "up"
        }
      ]
    }
  ],
  "cisco": [
    {
      "count": 4,
      "detailsURL": "",
      "name": "cisco Hardware Health",
      "status": "error",
      "statusList": [
        {
          "count": 4,
          "detailsURL": "/dataservice/device/hardwarehealth/detail?state-abnormal",
          "message": "40 (normal=10, warning=10, error=10)",
          "name": "abnormal",
          "status": "up"
        }
      ]
    }
  ]
}
'''
# Convert JSON data to Python dictionary
data = json.loads(json_data)
A = data['data'][0]['name']
B = data['data'][0]['statusList'][0]['message']

C = data['cisco'][0]['name']
D = data['cisco'][0]['statusList'][0]['message']

print("device 1 : "+A +" have : ",B)  # Output: up
print("device 2 : "+C +" have : ",D)

# def print_json_indexes(data, index=''):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             new_index = f'{index}/{key}' if index else key
#             print_json_indexes(value, new_index)
#     elif isinstance(data, list):
#         for i, value in enumerate(data):
#             new_index = f'{index}/{i}' if index else str(i)
#             print_json_indexes(value, new_index)
#     else:
#         print(f'Index: {index}, Value: {data}')

# json_data = json.loads(json_data)
# print_json_indexes(json_data)