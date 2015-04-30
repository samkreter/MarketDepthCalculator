import urllib2
import json 
import sys

class MarketDepthCalulator:
	
	def __init__(self):
		btcchina_market_depth_url = "https://data.btcchina.com/data/orderbook?limit=200"
		okcoin_market_depth_url = "https://www.okcoin.cn/api/depth.do"

		okcoin_market_depth = json.loads(urllib2.urlopen(btcchina_market_depth_url).read())

		self.sells = okcoin_market_depth['asks']
		self.buys = okcoin_market_depth['bids']
		self.price = 0
		self.quan = 1



	def calulate_sell_bitcoins(self,coins):
		currSellCoins = coins 
		moneyEchanged = 0
		depth = 0

		try:
			while currSellCoins > self.buys[depth][self.quan] and currSellCoins > 0:
				moneyEchanged = moneyEchanged + (self.buys[depth][self.quan] * self.buys[depth][self.price])
				currSellCoins = currSellCoins - self.buys[depth][self.quan]
				depth = depth + 1 
		except:
			print "unable to calculate due to lack of buyers"
			print "depth reached was {0}".format(depth)
			print "coins sold reached {0}".format(currSellCoins)
			sys.exit()

		if currSellCoins < self.buys[depth][self.quan] and currSellCoins > 0:
			moneyEchanged = moneyEchanged + (self.buys[depth][self.price] * currSellCoins)

		print "total bitcoins sold: {0}".format(coins)
		print "total market depth reached: {0}".format(depth)
		print "total money exchanged for: ${0}".format(moneyEchanged) 


	def calculate_buy_bitcoins(self,money):
		currMoney = money
		coinsExchanged = 0
		depth = 0

		try:
			while  currMoney > (self.sells[depth][self.price] * self.sells[depth][self.quan]) and currMoney > 0:
				currMoney = currMoney - (self.sells[depth][self.price] * self.sells[depth][self.quan])
				coinsExchanged = coinsExchanged + self.sells[depth][self.quan]
				depth = depth + 1
		except:
			print "unable to calculate due to lack of sellers"
			print "depth reached was {0}".format(depth)
			sys.exit()

		if currMoney < self.sells[depth][self.price] and currMoney > 0:
			coinsExchanged = coinsExchanged + (currMoney / self.sells[depth][self.price])

		#testing accuracy 
		print "total bitcoins bought: {0}".format(coinsExchanged)
		print "total market depth reached: {0}".format(depth)
		print "total money spent: ${0}".format(money) 









