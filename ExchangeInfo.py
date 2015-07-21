#exchnages api urls
exchangeURLs = {"ChileBit":"https://api.blinktrade.com/api/v1/CLP/orderbook?crypto_currency=BTC",
                 "BTCChina":"https://data.btcchina.com/data/orderbook?limit=200",
                 "OKCoin":"https://www.okcoin.cn/api/depth.do",
                 "SurBitCoin":"https://api.blinktrade.com/api/v1/VEF/orderbook?crypto_currency=BTC",
                 "FoxBit":"https://api.blinktrade.com/api/v1/BRL/orderbook?crypto_currency=BTC",
                 "MexBT":"https://data.mexbt.com/order-book/btcmxn",
                 "SurBTC":"https://www.surbtc.com/api/v1/markets/btc-clp/order_book.json"}

#tell the exchanges for each country
exchangeReference = {"CLP":["ChileBit","SurBTC"],
                     "RMB":["BTCChina","OKCoin"],
                     "VEF":["SurBitCoin"],
                     "BRL":["FoxBit"],
                     "MXN":["MexBT"]}
#tell the market depth needed for accurate functions
exchangeDepth = {"ChileBit":0,
                 "BTCChina":199,
                 "OKCoin":199,
                 "SurBitCoin":0,
                 "FoxBit":0,
                 "MexBT":0,
                 "SurBTC":0}