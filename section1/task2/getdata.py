
import config
import csv
from binance.client import Client

client=Client(config.API_KEY,config.API_SECRET)

candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1HOUR,"1 Apr, 2017","1 Apr, 2020")

csvfile=open('klines.csv','w', newline='')
candlestick_writer=csv.writer(csvfile, delimiter=',')

for candlestick in candles:
    candlestick_writer.writerow(candlestick)


trades = client.get_recent_trades(symbol='BTCUSDT')
csvfile2=open('trades.csv','w',newline='')
tradestick_writer=csv.writer(csvfile2, delimiter=',')

for tradestick in trades:
    tradestick_writer.writerow(tradestick)


orderbook = client.get_orderbook_tickers()
csvfile3=open('orderbook.csv','w',newline='')
orderbook_writer=csv.writer(csvfile3, delimiter=',')

for tricker in orderbook:
    orderbook_writer.writerow(tricker)

