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
# Convert JSON data to Python dictionary
d = json.loads(json_data)
# W = d[data][0][statusList][0][status]
# Y = d["data"]["statusList"]["status"]
# Z = d{"data"}[0]{"statusList"}[0]{"status"}
U = d["data"][0]["statusList"][0]["status"]

print(U)  # Output: up

