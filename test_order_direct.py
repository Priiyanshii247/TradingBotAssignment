from bot.client import client

try:
    print("Checking Futures Balance...")
    print(client.futures_account_balance())
except Exception as e:
    print("BALANCE ERROR:", e)

try:
    print("\nChecking Futures Account...")
    print(client.futures_account())
except Exception as e:
    print("ACCOUNT ERROR:", e)