from arctic import Arctic

import quandl
import quandlkey
'''
# Connect to local MONGODB
store = Arctic('localhost')
# Create the library - defaults to VersionStore
store.initialize_library('NASDAQ')
# Access the library
library = store['NASDAQ']
# load some data - maybe from Quandl
aapl = quandl.get("WIKI/AAPL", authtoken=quandlkey.KEY)
# store the data in the library
library.write('AAPL',aapl,metadata={'source':'Quandl'})
# reading the data
item = library.read('AAPL')
aapl = item.data
metadata = item.metadata
'''
# connect to mongodb
store = Arctic('localhost')

store.initialize_library('NASDAQ')
library = store['NASDAQ']
item = library.read('AAPL')
aapl = item.data

store.initialize_library('Futures')
library = store['Futures']
item = library.read('ES1')
es1 = item.data
item = library.read('ES2')
es2 = item.data
item = library.read('ES3')
es3 = item.data
item = library.read('ES4')
es4 = item.data
item = library.read('NQ1')
nq1 = item.data
item = library.read('NQ2')
nq2 = item.data
                    
