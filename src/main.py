from config import get_api_key
#from pyvis.network import pyvis
import requests
import json
from pathlib import Path

API_KEY = get_api_key()
BASE_URL = "https://www.robotevents.com/api/v2"

def get_event_by_sku(sku: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    params = {"sku[]": sku}

    r = requests.get(f"{BASE_URL}/events", headers=headers, params=params)
    r.raise_for_status()
    return r.json()

def save_json(data: dict, filename: str):
    Path("data").mkdir(exist_ok=True)   # create /data if missing
    with open(f"data/{filename}", "w") as f:
        json.dump(data, f, indent=2)

event = get_event_by_sku("RE-VRC-23-1488")
save_json(event, "RE-VRC-23-1488.json")