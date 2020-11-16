import requests
import pandas as pd
import numpy as np
import backtrader as bt
import datetime
import sys  # To find out the script name (in argv[0])
import matplotlib.pyplot as plt



url = 'https://raw.githubusercontent.com/mementum/backtrader/master/datas/nvda-1999-2014.txt'

r = pd.read_csv(url, ',', parse_dates=['Date'])
#print(r)

class my_strategy1(bt.Strategy):
    # set strategy params
    params=(
        ('maperiod', 20),
        ('datetime', None)
           )
 
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose=self.datas[0].close
        # Initialization
        self.order = None
        self.buyprice = None
        self.buycomm = None
 
    def next(self):
        # Check if an order is pending
        if self.order:  
            return
        # Check if we are in the market  
        if not self.position: 
            #current close less than previous close
            if self.dataclose[0] < self.dataclose[-1]:
                # previous close less than the previous close
                if self.dataclose[-1] < self.dataclose[-2]:   
                    # Buy
                    self.order = self.buy(size=500)         
        else:
            # Already in the market ... we might sell
            if len(self) >= (self.bar_executed + 5):
                # sell
                self.order = self.sell(size=500)


data = bt.feeds.PandasData(
    dataname = r
    )

def main(com=0.002, startcash=10000,qts=500):

    # Create a cerebro entity                      
    cerebro = bt.Cerebro()  
    # Add the Data Feed to Cerebro
    cerebro.adddata(data) 
    # Add a strategy
    cerebro.optstrategy(my_strategy1, maperiod=range(3, 31)) 
    # set start cash
    cerebro.broker.setcash(startcash) 
    # set commission
    cerebro.broker.setcommission(commission=com)
    # Run and print
    cerebro.addsizer(bt.sizers.FixedSize, stake=qts)   
    print('Starting Portfolio Value: %.2f' %                    
    cerebro.broker.getvalue())    
    cerebro.run(maxcpus=1)    
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()

