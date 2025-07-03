import requests

url = 'https://api.binance.com//api/v3/depth?symbol=BTCUSDT&limit=5'  # Replace with the URL you want to request

# Sending GET request
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Printing the response content (usually JSON or HTML)
    print(response.json())  # Use response.text for non-JSON content
else:
    print(f"Error {response.status_code}: {response.text}")