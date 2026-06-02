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

# Binance requires a timestamp
timestamp = int(time.time() * 1000)

query_string = f"timestamp={timestamp}"

# Generate signature
signature = hmac.new(
    API_SECRET.encode("utf-8"),
    query_string.encode("utf-8"),
    hashlib.sha256
).hexdigest()

# Signed endpoint
url = f"{BASE_URL}/fapi/v2/balance?{query_string}&signature={signature}"

headers = {
    "X-MBX-APIKEY": API_KEY
}

try:
    response = requests.get(url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:")
    print(response.text)

except Exception as e:
    print("Error:", e)