from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

client.FUTURES_URL = "https://demo-fapi.binance.com"

try:
    balance = client.futures_account_balance()
    print("Connected Successfully!")
    print(balance)
except Exception as e:
    print("Error:", e)