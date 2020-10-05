import requests
import pandas as pd
import json

ts=1585713600
while ts >= 1498219200:
    url='https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&e=binance&limit=2000&toTs='+str(ts)
    r=requests.get(url)
    jdata=r.json()
    d=pd.DataFrame(jdata["Data"]["Data"])
    data=d.to_csv()
    with open("/Users/xuanming/Documents/test3.csv","a") as f:
        result_data=f.write(data)
    ts-=7200000
   






