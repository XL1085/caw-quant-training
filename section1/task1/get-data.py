
import requests
import json
import time
import pandas as pd

def getdata(fsym, tsym, limit, e, enddate, startdate):

    ts = int(time.mktime(time.strptime(enddate, '%Y-%m-%d %H:%M:%S')))

    y17 = int(time.mktime(time.strptime(startdate, '%Y-%m-%d %H:%M:%S')))
    while ts >= y17:
        url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym='+fsym+'&tsym='+tsym+'&limit='+limit+'&e='+e+'&toTs='+str(ts)
        r = requests.get(url)
        jdata = r.json()
        d = pd.DataFrame(jdata["Data"]["Data"])
        d['date'] = pd.to_datetime(d['time'].values, unit='s')
        data = d.drop(['conversionType', 'conversionSymbol', 'time'], axis=1)
        data.to_csv('./test.csv', header=0, mode='a', index=0)
    
        ts -= 7200000
   


getdata('BTC', 'USDT', '2000', 'binance', '2020-04-01 00:00:00', '2017-04-01 00:00:00')


#sort the date, remove duplicate data, add the column names
newdata = pd.read_csv('test.csv')
print(newdata.head())

newdata.columns = ['close', 'high', 'low', 'open', 'volume', 'baseVolume', 'datetime']
sv = newdata.sort_values(by='datetime', ascending=True)
sv['datetime'] = pd.to_datetime(sv['datetime'])
ssv = sv[(sv['datetime'] >= '2017-04-01 00:00:00') & (sv['datetime'] <= '2020-04-01 00:00:00')]
ssvv = ssv.drop_duplicates()
print(ssvv.head())

ssvv.to_csv('./BTC_USDT.csv', index=False)

