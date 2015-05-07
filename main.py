from MarketDepthCalulator import MarketDepthCalulator

calc = MarketDepthCalulator()


calc.chileExchangeBuyCoins(140000.00)

# #testing the sell of bitcoins 
# while True:
# 	try:
# 		coins = float(raw_input('Enter the amount of bitcoin to convert to cash: '))
# 		break
# 	except:
# 		print "Not a number!"

# calc.calulate_sell_bitcoins(coins)

# print " "

# #testing the buying of bitcoins 
# while True:
# 	try:
# 	    money=float(raw_input('Enter the amount to convert to bitcoin: $'))
# 	    break
# 	except ValueError:
# 	    print "Not a number!"

# calc.calculate_buy_bitcoins(money)