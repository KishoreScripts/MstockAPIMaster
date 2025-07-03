#login_manager.py

import requests
import json

def login_mstock(user_id, password, api_key):
    url = "https://mstockapi.miraeasset.com/api/v1/login"
    payload = {
        "userId": user_id,
        "password": password,
        "APIKey": api_key
    }
    response = requests.post(url, data=json.dumps(payload))
    return response.json()
