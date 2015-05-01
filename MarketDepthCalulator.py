import urllib2
import json 
import sys
import time 

class MarketDepthCalulator:
	
	def __init__(self):
		self.okcoin_market_depth_url = "https://www.okcoin.cn/api/depth.do"
		self.btcchina_market_depth_url = "https://data.btcchina.com/data/orderbook?limit=200"
		self.price = 0
		self.quan = 1


	def pwd(self,sells):
		for x in range(199,189):
			print sells[x]

	def chinaExchangeBuyCoins(self,money):
		
		okCoinStart_time = time.time()
		okcoin_market_depth = json.loads(urllib2.urlopen(self.okcoin_market_depth_url).read())
		print "okCoin Execution Time = ",time.time() - okCoinStart_time
		self.pwd(okcoin_market_depth['asks']) ######################

		btcChinaStart_time = time.time()
		btcchina_market_depth = json.loads(urllib2.urlopen(self.btcchina_market_depth_url).read())
		print "btcChina Execution Time = ",time.time() - btcChinaStart_time
		self.pwd(btcchina_market_depth['asks'])########################

		totalMarcketBuyData = dict()
		totalMarcketBuyData['OKCoin'] = self.calculate_buy_bitcoins(money,okcoin_market_depth['asks'],okcoin_market_depth['bids'])
		totalMarcketBuyData['BTCChina'] = self.calculate_buy_bitcoins(money,btcchina_market_depth['asks'],btcchina_market_depth['bids'])
		return totalMarcketBuyData

	def calculate_buy_bitcoins(self,money,sells,buys):
		currMoney = money
		coinsExchanged = 0
		depth = 199

		try:
			while  currMoney > (sells[depth][self.price] * sells[depth][self.quan]) and currMoney > 0:
				currMoney = currMoney - (sells[depth][self.price] * sells[depth][self.quan])
				coinsExchanged = coinsExchanged + sells[depth][self.quan]
				depth = depth - 1
				print "while loop coins: ",coinsExchanged
				print "while loop money: ",currMoney
				print "while loop price: ",sells[depth][self.price]
				print "depth is ",depth
				print ""
		except:
			print "unable to calculate due to lack of sellers"
			print "depth reached was {0}".format(depth)
			sys.exit()

		print "Outside the ifstatmnet"
		if currMoney > 0:
			coinsExchanged = coinsExchanged + (currMoney / sells[depth][self.price])
			print "if stat coins: ",coinsExchanged
			print "if stat money: ",currMoney
			print "if stat price: ", sells[depth][self.price]
			print ""

		#testing accuracy 
		print "total bitcoins bought: {0}".format(coinsExchanged)
		print "total market depth reached: {0}".format(depth)
		print "total money spent: ${0}".format(money) 
		print "average price: ${0}".format(money/coinsExchanged)
		print " "


		return dict(coinsExchanged=coinsExchanged,depth=depth)




	#still a work in progross for the selling section 

	# def calulate_sell_bitcoins(self,coins):
	# 	currSellCoins = coins 
	# 	moneyEchanged = 0
	# 	depth = 0

	# 	try:
	# 		while currSellCoins > self.buys[depth][self.quan] and currSellCoins > 0:
	# 			moneyEchanged = moneyEchanged + (self.buys[depth][self.quan] * self.buys[depth][self.price])
	# 			currSellCoins = currSellCoins - self.buys[depth][self.quan]
	# 			depth = depth + 1 
	# 	except:
	# 		print "unable to calculate due to lack of buyers"
	# 		print "depth reached was {0}".format(depth)
	# 		print "coins sold reached {0}".format(currSellCoins)
	# 		sys.exit()

	# 	if currSellCoins < self.buys[depth][self.quan] and currSellCoins > 0:
	# 		moneyEchanged = moneyEchanged + (self.buys[depth][self.price] * currSellCoins)

	# 	print "total bitcoins sold: {0}".format(coins)
	# 	print "total market depth reached: {0}".format(depth)
	# 	print "total money exchanged for: ${0}".format(moneyEchanged) 


	










