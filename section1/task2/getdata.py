

import json
import pandas as pd
from binance.client import Client


with open('./key.json') as f:
    api_key = json.load(f)


client = Client(api_key['API_KEY'], api_key['API_SECRET'])


candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1HOUR,"1 Apr, 2017","1 Apr, 2020")
df = pd.DataFrame(candles)
df.to_csv('klines.csv')


trades = client.get_recent_trades(symbol='BTCUSDT')
df2 = pd.DataFrame(trades)
df2.to_csv('trades.csv')


orderbook = client.get_orderbook_tickers()
df3 = pd.DataFrame(orderbook)
df3.to_csv('orderbook.csv')
