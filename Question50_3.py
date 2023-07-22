import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Define the vManage credentials
vmanage_host = "sandbox-sdwan-2.cisco.com"
vmanage_port = "443"
username = "devnetuser"
password = "RG!_Yw919_83"

# Construct the vManage API base URL
base_url = f"https://{vmanage_host}:{vmanage_port}/dataservice"

# Create a session and perform login
session = requests.Session()
login_url = f"{base_url}/j_security_check"
login_data = {"j_username": username, "j_password": password}
response = session.post(login_url, data=login_data, verify=False)

# Check if login was successful
if response.status_code != 200:
    print("Failed to log in to vManage. Status code:", response.status_code)
    print("Error message:", response.text)
    exit()

# Define the policy ID to deactivate
policy_id = "7f916737-02dc-4ff9-a14b-5da0737a0e8a"

# Deactivate the vSmart Policy D
# response = session.post("https://sandbox-sdwan-2.cisco.com:443/dataservice/template/policy/vsmart/activate/", data={"policyId": policy_id})
# Deactivate the vSmart Policy A
# response = session.post("https://sandbox-sdwan-2.cisco.com:443/dataservice/template/policy/vsmart/activate?policyId=%s" % policy_id)
# Deactivate the vSmart Policy B
response1 = session.post('https://sandbox-sdwan-2.cisco.com:443/dataservice/template/policy/vsmart/%s' % policy_id)

# Check the response status code to determine if the request was successful
if response1.status_code == 200:
    print("vSmart Policy deactivated successfully!")
else:
    print("Failed to deactivate vSmart Policy. Status code:", response.status_code)
    print("Error message:", response.text)
