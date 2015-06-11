from MarketDepthCalculator import MarketDepthCalculator
from urllib2 import Request, urlopen

values = """
  {
    "productPair": "BTCMXN"
  }
"""

headers = {
  'Content-Type': 'application/json'
}
request = Request('https://public-api.mexbt.com/v1/order-book', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body