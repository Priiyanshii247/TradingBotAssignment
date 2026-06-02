from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

client.FUTURES_URL = "https://demo-fapi.binance.com"

try:
    print(client.futures_account_balance())
except Exception as e:
    print("ERROR:", e)