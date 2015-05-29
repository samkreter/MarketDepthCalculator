from MarketDepthCalculator import MarketDepthCalculator

c = MarketDepthCalculator()

currency = 'BRL-VEF'
print currency[0:3]
print currency[4:7]
print c.exchangeRate(currency[0:2],currency[4:6])
