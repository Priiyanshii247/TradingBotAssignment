import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

try:
    exchange_info = client.futures_exchange_info()

    print("Connected to Futures!")
    print("Number of symbols:",
          len(exchange_info["symbols"]))

except Exception as e:
    print("Error:", e)