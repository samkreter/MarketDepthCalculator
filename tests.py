from MarketDepthCalculator import MarketDepthCalculator
from urllib2 import Request, urlopen

import ExchangeInfo

for curr, exchanges in ExchangeInfo.exchangeReference.items():
	print curr
	print exchanges