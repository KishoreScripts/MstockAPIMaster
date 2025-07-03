#secrets_manager.py 

import os
import json

CRED_FILE = "mstock_credentials.json"

def save_credentials(data):
    with open(CRED_FILE, "w") as f:
        json.dump(data, f)

def load_credentials():
    if os.path.exists(CRED_FILE):
        with open(CRED_FILE) as f:
            return json.load(f)
    return None
