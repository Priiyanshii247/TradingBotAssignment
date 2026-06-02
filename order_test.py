import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://demo-fapi.binance.com"

timestamp = int(time.time() * 1000)

params = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": "0.001",
    "timestamp": timestamp
}

query_string = "&".join(
    [f"{k}={v}" for k, v in params.items()]
)

signature = hmac.new(
    API_SECRET.encode(),
    query_string.encode(),
    hashlib.sha256
).hexdigest()

params["signature"] = signature

headers = {
    "X-MBX-APIKEY": API_KEY
}

response = requests.post(
    f"{BASE_URL}/fapi/v1/order",
    headers=headers,
    params=params
)

print("Status:", response.status_code)
print(response.text)