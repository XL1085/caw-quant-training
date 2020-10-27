
import etherscan.accounts as accounts
import json

with open('./key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b'
api = accounts.Account(address=address, api_key=key)

print(api.get_balance())

api.get_transaction_page(page=1, offset=10)

trans = api.get_all_transactions(offset=10)
print(trans)

api.get_blocks_mined_page(page=1, offset=10,)

blocks_mined = api.get_all_blocks_mined()


addresses = ['0xbb9bc244d798123fde783fcc1c72d3bb8c189413', '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a']
api = accounts.Account(address=addresses, api_key=key)
api.get_balance_multiple()