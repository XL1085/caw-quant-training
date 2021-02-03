# all built-in libraries at the top
import os
import datetime

# all third-party libraries in the middle
import backtrader as bt
import pandas as pd
import matplotlib.pyplot as plt
import logging
import numpy as np

# all your own modules in the end
#from getdata import data


# declare all environment params / global variables. e.g:

'''
python
datadir = './data' # data path
logdir = './log' # log path
reportdir = './report' # report path
datafile = 'BTC_USDT_1h.csv' # data file
from_datetime = '2020-01-01 00:00:00' # start time 
to_datetime = '2020-04-01 00:00:00' # end time
'''

# define strategy class. e.g:

logging.basicConfig(filename='./logfile.log', filemode='a', level=logging.INFO)

class SMACross(bt.Strategy):
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = self.datas[0].datetime.date(0)
        return('%s, %s' % (dt.isoformat(), txt))

    params = (
        ('pfast', 10),
        ('pslow', 20)
    )

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose=self.datas[0].close
        # Initialization
        self.order = None
        sma_fast = self.p._movav(period=self.p.fast)
        sma_slow = self.p._movav(period=self.p.slow)
        self.buysig = btind.CrossOver(sma_fast, sma_slow)
    def next(self):
        logging.info(self.log('Close, %.2f' % self.dataclose[0]))

        if self.position.size:
            if self.buysig < 0:
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.sell()


        elif self.buysig > 0:
            self.log('BUY CREATE, %.2f' % self.dataclose[0])
            self.buy() 

if __name__ == '__main__':
    # initiate cerebro instance:
    cerebro = bt.Cerebro()
    # feed data:
    r = pd.read_csv('./BTC_USDT_1h.csv')
    r['datetime'] = pd.to_datetime(r['datetime'])
    r['openinterest'] = 0
    print(r)
    datafeed = bt.feeds.PandasData(dataname=r)
    
    cerebro.adddata(datafeed)
    # feed strategy:
    cerebro.addstrategy(SMACross)
    # additional backtest setting:
    # set start cash
    cerebro.broker.setcash(10000) 
    # set commission
    cerebro.broker.setcommission(commission=0.001)
    # Run and print
    cerebro.addsizer(bt.sizers.PercentSizer, percents=99)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue()) 
    cerebro.run() 
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()