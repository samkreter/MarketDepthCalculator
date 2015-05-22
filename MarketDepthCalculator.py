import urllib2 #making the api calls
import json #parseing the api calls to json
import time #testing the timing of the api calls

class MarketDepthCalculator:
	
	#setting the url for the exhanges api
	def __init__(self):
		self.okcoin_market_depth_url = "https://www.okcoin.cn/api/depth.do"
		self.btcchina_market_depth_url = "https://data.btcchina.com/data/orderbook?limit=200"
		self.chileBit_market_depth_url = "https://api.blinktrade.com/api/v1/CLP/orderbook?crypto_currency=BTC"
		self.price = 0
		self.quan = 1

	#test fundtion, delete before production
	def pwd(self,sells):
		for x in range(199,189):
			print sells[x]

	def percentDifference(self,buyData):
		difference = abs(buyData['OKCoin']['coinsExchanged'] - buyData['BTCChina']['coinsExchanged'])
		average = (buyData['OKCoin']['coinsExchanged'] + buyData['BTCChina']['coinsExchanged']) / 2
		print "difference is: ",difference
		print "average is : ",average
		return (difference / average) * 100

	def findBest(self,data):
		best = ''
		amount = 0
		for key, value in data.iteritems():
			if value > amount:
				amount = value
				best = key 
		return best 


	#controling chile's exchanges in the selling of coins 
	def chileExchangeSellCoins(self,coins):

		chileBitStart_time = time.time()
		chileBit_market_depth = json.loads(urllib2.urlopen(self.chileBit_market_depth_url).read())
		print "chileBit Execution Time = ",time.time() - chileBitStart_time

		totalMarketBuyData = dict()
		totalMarketBuyData['ChileBit'] = self.calculate_sell_bitcoins(coins,chileBit_market_depth['bids'])
		totalMarketBuyData['Best'] = self.findBest(totalMarketBuyData)
		return totalMarketBuyData

	#controling chile's exchanges for the buying of coins 
	def chileExchangeBuyCoins(self,money):
		#testing the time for each api call
		chileBitStart_time = time.time()
		chileBit_market_depth = json.loads(urllib2.urlopen(self.chileBit_market_depth_url).read())
		print "chileBit Execution Time = ",time.time() - chileBitStart_time

		totalMarketBuyData = dict()
		totalMarketBuyData['ChileBit'] = self.calculate_buy_bitcoins(money,chileBit_market_depth['asks'],0)

		totalMarketBuyData['Best'] = self.findBest(totalMarketBuyData)

		#totalMarketBuyData['PercentDifference'] = self.percentDifference(totalMarketBuyData)

	#use both chinas exchanges to set up the dict, main funtion to be called outside the class
	def chinaExchangeBuyCoins(self,money):
		#testing the time for each api call
		okCoinStart_time = time.time()
		okcoin_market_depth = json.loads(urllib2.urlopen(self.okcoin_market_depth_url).read())
		print "okCoin Execution Time = ",time.time() - okCoinStart_time

		btcChinaStart_time = time.time()
		btcchina_market_depth = json.loads(urllib2.urlopen(self.btcchina_market_depth_url).read())
		print "btcChina Execution Time = ",time.time() - btcChinaStart_time

		totalMarketBuyData = dict()
		totalMarketBuyData['OKCoin'] = self.calculate_buy_bitcoins(money,okcoin_market_depth['asks'],len(okcoin_market_depth['asks']) - 1 )
		totalMarketBuyData['BTCChina'] = self.calculate_buy_bitcoins(money,btcchina_market_depth['asks'],len(btcchina_market_depth['asks']) - 1)

		totalMarketBuyData['Best'] = self.findBest(totalMarketBuyData)

		totalMarketBuyData['PercentDifference'] = self.percentDifference(totalMarketBuyData)

		return totalMarketBuyData

	#use the api information to find the marketdepth for the money amount provided 
	#depth had to be passed in since the china exchange's asks array is in revese order of the other exchanges 
	#this allows for the use of the same function for all the exhcnages 
	def calculate_buy_bitcoins(self,money,sells,depth):
		currMoney = money
		coinsExchanged = 0
		varient = 1 if depth == 0 else -1
		print "depth is ",depth

		try:
			while  currMoney > (sells[depth][self.price] * sells[depth][self.quan]) and currMoney > 0:
				print "pq:",sells[depth][self.price],",",sells[depth][self.quan]," depth: ",depth
				currMoney = currMoney - (sells[depth][self.price] * sells[depth][self.quan])
				coinsExchanged = coinsExchanged + sells[depth][self.quan]
				depth = depth + varient
		#if the exception is thrown, the amount exceeded the limit that the api gives out
		except Exception:
			print "unable to calculate due to lack of sellers"
			print "depth reached was {0}".format(len(sells) - depth)
			return

		#catch the final seller and add the correct amount of bitcoins to the coinsExchanged var
		if currMoney > 0:
			coinsExchanged = coinsExchanged + (currMoney / sells[depth][self.price])

		#testing accuracy 
		print "total bitcoins bought: {0}".format(coinsExchanged)
		print "total market depth reached: {0}".format(len(sells) - depth)
		print "total money spent: ${0}".format(money) 
		print "average price: ${0}".format(money/coinsExchanged)
		print " "

		#return the necssary data
		return dict(coinsExchanged=coinsExchanged,depth=(len(sells) - depth))


	def calculate_sell_bitcoins(self,coins,buys):
		currSellCoins = coins 
		moneyExchanged = 0
		depth = 0

		try:
			while currSellCoins > buys[depth][self.quan] and currSellCoins > 0:
				moneyExchanged = moneyExchanged + (buys[depth][self.quan] * buys[depth][self.price])
				currSellCoins = currSellCoins - buys[depth][self.quan]
				depth = depth + 1 
		except:
			print "unable to calculate due to lack of buyers"
			print "depth reached was {0}".format(depth)
			print "coins sold reached {0}".format(currSellCoins)
			sys.exit()

		if currSellCoins > 0:
			moneyExchanged = moneyExchanged + (buys[depth][self.price] * currSellCoins)

		print "total bitcoins sold: {0}".format(coins)
		print "total market depth reached: {0}".format(depth)
		print "total money exchanged for: ${0}".format(moneyExchanged) 

		return dict(moneyExchanged=moneyExchanged,depth=depth)


	










