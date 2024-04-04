# import requests
import uuid
import json
import os

new_token = "123"
print(new_token)

print(os.getcwd())

parent_dir = r'C:\Users\dsimonov\Documents\Scripts\django\russpass_chat'

filename = 'token1.txt'


full_path = os.path.join(parent_dir, filename)
with open(full_path, 'w') as f:
    f.writelines(new_token)