from etherscan.stats import Stats
import json

with open('./key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Stats(api_key=key)

# get ether last price
last_price = api.get_ether_last_price()
print(last_price)

# get total ether supply
# call with default address, The DAO
supply = api.get_total_ether_supply()
print(supply)