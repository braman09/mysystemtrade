from arctic import Arctic

import quandl
import quandlkey

# Connect to local MONGODB
store = Arctic('localhost')
# Create the library - defaults to VersionStore
store.initialize_library('NASDAQ')
# Access the library
library = store['NASDAQ']
# load some data - maybe from Quandl
#aapl = quandl.get("WIKI/AAPL", authtoken=quandlkey.KEY)
tsla = quandl.get("WIKI/TSLA", authtoken=quandlkey.KEY)
# store the data in the library
#library.write('AAPL',aapl,metadata={'source':'Quandl'})
library.write('TSLA',tsla,metadata={'source':'Quandl'})
# reading the data
item = library.read('AAPL')
aapl = item.data
metadata_aapl = item.metadata
item = library.read('TSLA')
tsla = item.data
metadata_tsla = item.metadata
              
