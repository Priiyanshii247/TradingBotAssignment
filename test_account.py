import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

print("API Key Found:", bool(api_key))
print("Secret Found:", bool(api_secret))

client = Client(api_key, api_secret)

try:
    print(client.ping())
except Exception as e:
    print("Error:", e)
    