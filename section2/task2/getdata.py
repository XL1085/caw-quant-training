
import json
import pandas as pd
from binance.client import Client
import time

def data():
    with open('binancekey.json') as f:
        api_key = json.load(f)

    client = Client(api_key['API_KEY'], api_key['API_SECRET'])

    candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1HOUR,"1 Jan, 2020","1 Apr, 2020")
    df = pd.DataFrame(candles)
    df = df.drop([6,7,8,10,11], axis=1)
    df.columns = ["datetime","open","high","low","close", "volume","baseVolume"]
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df = df[['close','high','low','open','volume','baseVolume','datetime']]
    df.to_csv('./BTC_USDT_1h.csv', index=False)
    

data()


