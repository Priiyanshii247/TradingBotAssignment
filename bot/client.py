import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

# Demo Futures endpoint
client.FUTURES_URL = "https://demo-fapi.binance.com"