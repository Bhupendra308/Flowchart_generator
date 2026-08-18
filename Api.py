import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_active_api_config():
    active_api = os.getenv("ACTIVE_API", "api1").lower()
    api_num = active_api.replace("api", "")
    
    url = os.getenv(f"API{api_num}_URL")
    api_key = os.getenv(f"API{api_num}_KEY")
    api_host = os.getenv(f"API{api_num}_HOST")
    
    if not url or not api_key or not api_host:
        return None
    
    return {"url": url, "key": api_key, "host": api_host, "api": active_api}

def make_api_call(content):
    config = get_active_api_config()
    
    if not config:
        raise ValueError("No valid API configuration found. Check ACTIVE_API and API credentials in .env")
    
    payload = {
        "messages": [{"role": "user", "content": content}],
        "web_access": False
    }
    
    headers = {
        "content-type": "application/json",
        "x-rapidapi-key": config["key"],
        "x-rapidapi-host": config["host"]
    }
    
    response = requests.post(config["url"], json=payload, headers=headers)
    return response.json()
