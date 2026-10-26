import requests
from epita_govind_manu_geolocation.config import config

def fetch_live_data() -> dict:
    url = "https://ipinfo.io/json"
    
    # If a token is provided and isn't a placeholder, use query params
    params = {}
    if config.api_key and not config.api_key.startswith("your_"):
        params = {"token": config.api_key}

    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return {
        "status": "LIVE_SUCCESS",
        "ip": data.get("ip"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "org": data.get("org")
    }