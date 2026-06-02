import requests

url = "https://demo-fapi.binance.com/fapi/v1/ping"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:", response.text)