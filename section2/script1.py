import requests
import pandas as pd
import numpy as np
import backtrader as bt
import datetime
import sys  # To find out the script name (in argv[0])
import matplotlib.pyplot as plt
import logging

logging.basicConfig(filename='./log/logfile.log', filemode='a', level=logging.INFO)

class mystrategy(bt.Strategy):
        
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        return ('%s, %s' % (dt.isoformat(), txt))
        
        
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose=self.datas[0].close
        # Initialization
        self.order = None
        self.buyprice = None
        self.buycomm = None
 
    def next(self):
        # Simply log the closing price of the series from the reference
        logging.info(self.log('Close, %.2f' % self.dataclose[0]))
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




if __name__ == "__main__":

    # Create a cerebro entity                      
    cerebro = bt.Cerebro()  
    # Add a strategy
    cerebro.addstrategy(mystrategy) 
    #Create data feeds
    r = pd.read_csv('nvda-1999-2014.txt', sep=',', index_col=0, parse_dates=True)
    r['openinterest'] = 0
    data = bt.feeds.PandasData(dataname=r)
    # Add the Data Feed to Cerebro
    cerebro.adddata(data)
    # set start cash
    cerebro.broker.setcash(10000) 
    # set commission
    cerebro.broker.setcommission(commission=0.002)
    # Run and print
    cerebro.addsizer(bt.sizers.FixedSize, stake=500)   
    print('Starting Portfolio Value: %.2f' %                    
    cerebro.broker.getvalue())    
    cerebro.run()    
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()
    

