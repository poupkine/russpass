import requests
import uuid
import json
import os

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
 
payload='scope=GIGACHAT_API_PERS'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': str(uuid.uuid4()),
  'Authorization': 'Basic M2JiMTRlODgtZmM3OS00NDVmLThkZWQtODhlYWUzNzI5M2ViOjhmMGRhZjQ5LTBhNGItNDBiMy04YmI0LThmMzJlODhlYzk3Nw=='
}

response = requests.request("POST", url, headers=headers, data=payload, verify='ca.cer')

print(response.text)
new_token = dict(json.loads(response.text))["access_token"]
print(new_token)


parent_dir = r'C:\Users\dsimonov\Documents\Scripts\django\russpass_chat'

filename = 'token.txt'


full_path = os.path.join(parent_dir, filename)
with open(full_path, 'w') as f:
    f.writelines(new_token)