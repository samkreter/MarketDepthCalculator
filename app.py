from bottle import route,request, response, run, template, static_file
from MarketDepthCalculator import MarketDepthCalculator

# @get('/<filename:re:.*\.(jpg|png|gif|ico)>')
# def images(filename):
#     return static_file(filename, root='static/img')

# @get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
# def fonts(filename):
#     return static_file(filename, root='static/fonts')


#bootstrap public 
@route('/bootstrap/css/<filename>')
def bootstrapCSS(filename):
	return static_file(filename,root='bootstrap/css')
@route('/bootstrap/js/<filename>')
def bootstrapJS(filename):
	return static_file(filename,root='bootstrap/js')

@route('/font-awesome/css/<filename>')
def fontawesomeCSS(filename):
	return static_file(filename,root='font-awesome-4.3.0/css')
@route('/font-awesome/fonts/<filename>')
def fontawesomeFonts(filename):
	return static_file(filename,root='font-awesome-4.3.0/fonts')




#public routes
@route('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='public/js')
@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='public/css')



#App routes
@route('/amount_form_ajax', method="POST")
def amount_form_ajax():
	print "ajax called triggered"
	currency = request.forms.get('currency')
	amount = float(request.forms.get("amount-{0}".format(currency)))
	calc = MarketDepthCalculator()
	#total Market data
	tmd = dict()
	if currency == 'CLP-RMB':
		print "CLP-RMB ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Chile'] = calc.chileExchangeBuyCoins(amount)
		tmd['China'] = calc.chinaExchangeSellCoins(tmd['Chile'][tmd['Chile']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Chile'],tmd['China'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	elif currency == 'RMB-CLP':
		print "RMB-CLP ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['China'] = calc.chinaExchangeBuyCoins(float(amount))
		tmd['Chile'] = calc.chileExchangeSellCoins(tmd['China'][tmd['China']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['China'],tmd['Chile'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	#RMB-BRL tab 
	elif currency == 'RMB-BRL':
		print "RMB-BRL ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['China'] = calc.chinaExchangeBuyCoins(float(amount))
		tmd['Brazil'] = calc.brazilExchangeSellCoins(tmd['China'][tmd['China']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['China'],tmd['Brazil'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	elif currency == 'BRL-RMB':
		print "BRL-RMB ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Brazil'] = calc.brazilExchangeBuyCoins(amount)
		tmd['China'] = calc.chinaExchangeSellCoins(tmd['Brazil'][tmd['Brazil']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Brazil'],tmd['China'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	#RMB-VEF tab
	elif currency == 'RMB-VEF':
		print "RMB-VEF ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['China'] = calc.chinaExchangeBuyCoins(float(amount))
		tmd['Venezuela'] = calc.venezuelaExchangeSellCoins(tmd['China'][tmd['China']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['China'],tmd['Venezuela'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	elif currency == 'VEF-RMB':
		print "VEF-RMB ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Venezuela'] = calc.venezuelaExchangeBuyCoins(amount)
		tmd['China'] = calc.chinaExchangeSellCoins(tmd['Venezuela'][tmd['Venezuela']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Venezuela'],tmd['China'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	#CLP-VEF tab
	elif currency == 'CLP-VEF':
		print "CLP-VEF ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Chile'] = calc.chileExchangeBuyCoins(amount)
		tmd['Venezuela'] = calc.venezuelaExchangeSellCoins(tmd['Chile'][tmd['Chile']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Chile'],tmd['Venezuela'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	elif currency == 'VEF-CLP':
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Venezuela'] = calc.venezuelaExchangeBuyCoins(amount)
		tmd['Chile'] = calc.chileExchangeSellCoins(tmd['Venezuela'][tmd['Venezuela']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Venezuela'],tmd['Chile'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	#CLP-BRL tab
	elif currency == 'CLP-BRL':
		print 'CLP-BRL ajax'
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Chile'] = calc.chileExchangeBuyCoins(amount)
		tmd['Brazil'] = calc.brazilExchangeSellCoins(tmd['Chile'][tmd['Chile']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Chile'],tmd['Brazil'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	elif currency == 'BRL-CLP':
		print 'BRL-CLP'
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Brazil'] = calc.brazilExchangeBuyCoins(amount)
		tmd['Chile'] = calc.chileExchangeSellCoins(tmd['Brazil'][tmd['Brazil']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Brazil'],tmd['Chile'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	#BRL-VEF tab
	elif currency == 'BRL-VEF':
		print "BRL-VEF ajax"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Brazil'] = calc.brazilExchangeBuyCoins(amount)
		tmd['Venezuela'] = calc.venezuelaExchangeSellCoins(tmd['Brazil'][tmd['Brazil']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Brazil'],tmd['Venezuela'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	elif currency == 'VEF-BRL':
		print "VEF-BRL"
		tmd['currency'] = currency
		tmd['exhangeRate'] = calc.exchangeRate(currency[0:3],currency[4:7])
		tmd['Venezuela'] = calc.venezuelaExchangeBuyCoins(amount)
		tmd['Brazil'] = calc.brazilExchangeSellCoins(tmd['Venezuela'][tmd['Venezuela']['Best']]['coinsExchanged'])
		tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd['Venezuela'],tmd['Brazil'])
		tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	return tmd
	



@route('/')
def index():
    return template('index')

run(host='localhost', port=8080, debug=True)