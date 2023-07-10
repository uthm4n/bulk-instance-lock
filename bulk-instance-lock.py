import requests
import json 


url = "https://<YOUR-MORPHEUS-APPLIANCE-URL>/api/instances?max=25&offset=0&showDeleted=false&details=false"  # change the appliance URL 

headers = {
    "accept": "application/json",
    "authorization": "Bearer <YOUR-MORPHEUS-API-TOKEN>"                           # add your Morpheus API token 
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()
instanceIDs = []
for IDs in data['instances']:
    IDs = IDs['id']
    instanceIDs.append(IDs)


for h in instanceIDs: 
    url = f"https://<YOUR-MORPHEUS-APPLIANCE-URL>/api/instances/{h}/lock"          # change the appliance URL 
    headers = {
    "accept": "application/json",
    "authorization": "Bearer <YOUR-MORPHEUS-API-TOKEN>"                            # add your Morpheus API token 
    }
    response = requests.put(url, headers=headers, verify=False)
    print(response.text)
