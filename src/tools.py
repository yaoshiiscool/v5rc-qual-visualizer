import requests
import json
from pathlib import Path
from config import get_api_key
#from pyvis.network import pyvis

API_KEY = get_api_key()
BASE_URL = "https://www.robotevents.com/api/v2"

def get_event_by_sku(sku: str) -> dict:
    """Gets an event via RECF SKU"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    params = {"sku[]": sku}

    r = requests.get(f"{BASE_URL}/events", headers=headers, params=params)
    r.raise_for_status()
    return r.json()

def get_team_by_number(team_number: str) -> dict:
    """Gets a team via RECF team number"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    params = {"number[]": team_number}

    r = requests.get(f"{BASE_URL}/teams", headers=headers, params=params)
    r.raise_for_status()
    return r.json()

def get_event_id(sku: str) -> int:
    """Gets an event ID via RECF SKU"""
    event = get_event_by_sku(sku)
    return event["data"][0]["id"]

def get_team_id(team_number: str) -> int:
    """Gets a team ID via RECF team number"""
    team = get_team_by_number(team_number)
    return team["data"][0]["id"]

def get_event_teams(event_id: int) -> dict:
    """Gets all teams in an event via RECF event ID"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    params = {"event_id": event_id}

    r = requests.get(f"{BASE_URL}/teams", headers=headers, params=params)
    r.raise_for_status()
    return r.json()

def save_json(data: dict, filename: str) -> None:
    """Saves a dictionary to a JSON file"""
    Path("data").mkdir(exist_ok=True)   # create /data if missing
    with open(f"data/{filename}", "w") as f:
        json.dump(data, f, indent=2)

sku = "RE-V5RC-26-4025"
event = get_event_by_sku(sku)
print(event)
save_json(event, f"{sku}.json")
