def percentDifference(self,buyData):
	difference = abs(buyData['OKCoin']['coinsExchanged'] - buyData['BTCChina']['coinsExchanged'])
	average = (buyData['OKCoin']['coinsExchanged'] + buyData['BTCChina']['coinsExchanged']) / 2
	print "difference is: ",difference
	print "average is : ",average
	return (difference / average) * 100

def findGreaterBuyCoins(self,buyData):
	if buyData['OKCoin']['coinsExchanged'] >= buyData['BTCChina']['coinsExchanged']:
		return 'OKCoin'
	else:
		return 'BTCChina'