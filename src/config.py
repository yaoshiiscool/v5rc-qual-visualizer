import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key() -> str:
    key = os.getenv("ROBOTEVENTS_API_KEY")
    if not key:
        raise RuntimeError("Missing API Key")
    return key 