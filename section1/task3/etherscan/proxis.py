
from etherscan.proxies import Proxies
import json

with open('./key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

api = Proxies(api_key=key)

# get price
price = api.GAS_PRICE()
print(price)

# get blocks by number
block = api.get_block_by_number(5747732)
print(block['number'])

# get block transaction count by number
tx_count = api.get_block_transaction_count_by_number(block_number='0x10FB78')
print(int(tx_count, 16))

# get most recent block
block = api.get_most_recent_block()
print(int(block, 16))

# get transactions
transaction = api.get_transaction_by_blocknumber_index(block_number='0x57b2cc',
                                                       index='0x2')
print(transaction['transactionIndex'])

# get transactions by hash
TX_HASH = '0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1'
transaction = api.get_transaction_by_hash(
    tx_hash=TX_HASH)
print(transaction['hash'])

# get transaction count
count = api.get_transaction_count('0x6E2446aCfcec11CC4a60f36aFA061a9ba81aF7e0')
print(int(count, 16))

# get transaction receipt
receipt = api.get_transaction_receipt(
    '0xb03d4625fd433ad05f036abdc895a1837a7d838ed39f970db69e7d832e41205d')
print(receipt)

# get uncle by blocknumber index
uncles = api.get_uncle_by_blocknumber_index(block_number='0x210A9B',
                                            index='0x0')
print(uncles['uncles'])

