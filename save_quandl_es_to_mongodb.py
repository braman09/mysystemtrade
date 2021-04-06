import pandas as pd
import quandl
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import date
from arctic import Arctic

# Connect to local MONGODB
store = Arctic('localhost')
# create the library
store.initialize_library('Futures')
# access the library
library = store['Futures']

es1 = quandl.get("CHRIS/CME_ES1", authtoken="",
                start_date="2010-01-01",end_date=date.today())
es2 = quandl.get("CHRIS/CME_ES2", authtoken="",
                start_date="2010-01-01",end_date=date.today())
es3 = quandl.get("CHRIS/CME_ES3", authtoken="",
                start_date="2010-01-01",end_date=date.today())
es4 = quandl.get("CHRIS/CME_ES4", authtoken="",
                start_date="2010-01-01",end_date=date.today())
es1.index.name = es2.index.name = es3.index.name = es4.index.name = 'Date'

# NQ contracts

nq1 = quandl.get("CHRIS/CME_NQ1", authtoken="",
                start_date="2010-01-01",end_date=date.today())
nq2 = quandl.get("CHRIS/CME_NQ2", authtoken="",
                start_date="2010-01-01",end_date=date.today())
nq1.index.name = nq2.index.name = 'Date'

# store all the data in the library
library.write('ES1',es1,metadata={'source':'Quandl'})
library.write('ES2',es2,metadata={'source':'Quandl'})
library.write('ES3',es3,metadata={'source':'Quandl'})
library.write('ES4',es4,metadata={'source':'Quandl'})
library.write('NQ1',nq1,metadata={'source':'Quandl'})
library.write('NQ2',nq2,metadata={'source':'Quandl'})
'''
# simple plot to make sense of data
es1['Settle'].plot(x = 'Date', y= 'Settle Price')
plt.show()

## various other plots like candle, bokeh, point-and-figure
# use of mplfinance
# replace column 'Settle' to 'Close' in case mplfinance barfs
#
es1.rename(columns = {'Settle':'Close'}, inplace = True)
es1.index.name = 'Date'
mpf.plot(es1)
mpf.plot(es1, type='candle')
mpf.plot(es1, type='line')
mpf.plot(es1, type='renko')
mpf.plot(es1, type='pnf')

mpf.plot(es1, type='candle', mav=(3,6,9), volume=True)
'''
