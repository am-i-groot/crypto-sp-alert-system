import requests, json, time
from boltiot import boltiot

api_key="2a0c76b4-592f-45e8-ab2c-7ac89c60e14c"
device_id="BOLT5388904"

URL="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"

selling_price=44444.00

mybolt=Bolt(api_key, device_id)

while True:
    # Step 1
    print("Fetching the current price of Bitcoin in USD")
    response=response.request("GET", URL)
    response_text=json.loads(response.text)
    current_price=response_text["USD"]
    print("The current price of Bitcoin in USD is: ", current_price)

    # Step 2
    if current_price > selling_price:
        # Step 3
        response=mybolt.digitalWrite('0', 'HIGH')
        print(response)
        time.sleep(5)
        response=mybolt.digitalWrite('0', 'LOW')
        print("Enter new selling price: ", end = "")
        selling_price=int(input())
        print(response)
    time.sleep(30)