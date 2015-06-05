import urllib2 #making the api calls
import json #parseing the api calls to json
import time #testing the timing of the api calls

import Variables

class MarketDepthCalculator:
	
	#setting the url for the exhanges api
	def __init__(self):

		self.exchangeURLs = {"ChileBit":"https://api.blinktrade.com/api/v1/CLP/orderbook?crypto_currency=BTC",
							 "BTCChina":"https://data.btcchina.com/data/orderbook?limit=200",
							 "OKCoin":"https://www.okcoin.cn/api/depth.do",
							 "SurBitCoin":"https://api.blinktrade.com/api/v1/VEF/orderbook?crypto_currency=BTC",
							 "FoxBit":"https://api.blinktrade.com/api/v1/BRL/orderbook?crypto_currency=BTC"}

		self.exchangeReference = {"CLP":["ChileBit"],
								  "RMB":["BTCChina","OKCoin"],
								  "VEF":["SurBitCoin"],
								  "BRL":["FoxBit"]}
		self.exchangeDepth = {"ChileBit":0,
							  "BTCChina":199,
							  "OKCoin":199,
							  "SurBitCoin":0,
							  "FoxBit":0}

		self.open_exchange_rates_url = Variables.open_exchange_rates_url
		self.price = 0
		self.quan = 1


	def percentDifference(self,num1,num2):
		difference = num2 - num1
		average = (num2 + num1) / 2
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
	

	def bitnexoExchangeRate(self,base,exchange):
		return exchange[exchange['Best']]['moneyExchanged']/base['amount']


	def exchangeRate(self,baseCurrency,exchangeCurrency):
		if baseCurrency == 'RMB':
			baseCurrency = 'CNY' 
		if exchangeCurrency == 'RMB':
			exchangeCurrency = 'CNY' 
		data = self.exchangeRateDataSetup() 
		return 1/data['rates'][baseCurrency]*data['rates'][exchangeCurrency]



	def exchangeRateDataSetup(self):
		f = open("openExchangeRateData.txt")
		lastCallInfo = json.loads(f.read())
		f.close()


   		if time.time() - float(lastCallInfo['timestamp']) > 3600:
			print "making new api Exhcnage Data call"
			openExchangeRateData = json.loads(urllib2.urlopen(self.open_exchange_rates_url).read())
			openExchangeRateData['timestamp'] = time.time()
			with open("openExchangeRateData.txt",'w') as f:
				f.seek(0)
				json.dump(openExchangeRateData,f)
				f.truncate()
				f.close()
   		else:
   			print "using stored openExchange data"
   			openExchangeRateData = lastCallInfo

   		return openExchangeRateData


	#controling exchanges in the selling of coins 
	def ExchangeSellCoins(self,coins,name):
		market_depth = dict()
		totalMarketBuyData = dict()
		for exchange in self.exchangeReference[name]:
			Start_time = time.time()
			market_depth[exchange] = json.loads(urllib2.urlopen(self.exchangeURLs[exchange]).read())
			print exchange," Execution Time = ",time.time() - Start_time
			totalMarketBuyData[exchange] = self.calculate_sell_bitcoins(coins,market_depth[exchange]['bids'])
		
		totalMarketBuyData['Best'] = self.findBest(totalMarketBuyData)
		return totalMarketBuyData	

	#controling exchanges for the buying of coins 
	def ExchangeBuyCoins(self,money,name):
		market_depth = dict()
		totalMarketBuyData = dict()
		for exchange in self.exchangeReference[name]:
			#testing the time for each api call
			Start_time = time.time()
			market_depth[exchange] = json.loads(urllib2.urlopen(self.exchangeURLs[exchange]).read())
			print exchange," Execution Time = ",time.time() - Start_time
			totalMarketBuyData[exchange] = self.calculate_buy_bitcoins(money,market_depth[exchange]['asks'],self.exchangeDepth[exchange])
		
		totalMarketBuyData['Best'] = self.findBest(totalMarketBuyData)

		totalMarketBuyData['amount'] = money

		return totalMarketBuyData




	#use the api information to find the marketdepth for the money amount provided 
	#depth had to be passed in since the china exchange's asks array is in revese order of the other exchanges 
	#this allows for the use of the same function for all the exhcnages 
	def calculate_buy_bitcoins(self,money,sells,depth):
		currMoney = money
		coinsExchanged = 0
		varient = 1 if depth == 0 else -1

		try:
			while  currMoney > (sells[depth][self.price] * sells[depth][self.quan]) and currMoney > 0:
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

		if currSellCoins > 0:
			moneyExchanged = moneyExchanged + (buys[depth][self.price] * currSellCoins)

		print "total bitcoins sold: {0}".format(coins)
		print "total market depth reached: {0}".format(depth)
		print "total money exchanged for: ${0}".format(moneyExchanged) 

		return dict(moneyExchanged=moneyExchanged,depth=depth)


	










