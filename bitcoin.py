import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
API_KEY = "6775b7fc8b924802da9fc69e3ea28735969a28fa74289ba07d41b47d4773090d"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()

    if "data" in json_data and "priceUsd" in json_data["data"]:
        bitcoin_price = float(json_data["data"]["priceUsd"])
    elif "priceUsd" in json_data:
        bitcoin_price = float(json_data["priceUsd"])
    else:
        
        bitcoin_price = float(json_data["bpi"]["USD"]["rate_float"])

    total_cost = bitcoins * bitcoin_price
    print(f"${total_cost:,.4f}")

except (requests.RequestException, KeyError, ValueError):
    sys.exit("Request failed")
