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
		tmd['currency'] = 'CLP-RMB'
		tmd['Chile'] = calc.chileExchangeBuyCoins(amount)
		tmd['China'] = calc.chinaExchangeSellCoins(tmd['Chile'][tmd['Chile']['Best']]['coinsExchanged'])
	elif currency == 'RMB-CLP':
		print "RMB-CLP ajax"
		tmd['currency'] = 'RMB-CLP'
		tmd['China'] = calc.chinaExchangeBuyCoins(float(amount))
		tmd['Chile'] = calc.chileExchangeSellCoins(tmd['China'][tmd['China']['Best']]['coinsExchanged'])
	#RMB-BRL tab 
	elif currency == 'RMB-BRL':
		print "RMB-BRL ajax"
		tmd['currency'] = 'RMB-BRL'
		tmd['China'] = calc.chinaExchangeBuyCoins(float(amount))
		tmd['Brazil'] = calc.brazilExchangeSellCoins(tmd['China'][tmd['China']['Best']]['coinsExchanged'])
	elif currency == 'BRL-RMB':
		print "BRL-RMB ajax"
		tmd['currency'] = 'BRL-RMB'
		tmd['Brazil'] = calc.brazilExchangeBuyCoins(amount)
		tmd['China'] = calc.chinaExchangeSellCoins(tmd['Brazil'][tmd['Brazil']['Best']]['coinsExchanged'])
	#RMB-VEF tab
	elif currency == 'RMB-VEF':
		print "RMB-VEF ajax"
		tmd['currency'] = 'RMB-VEF'
		tmd['China'] = calc.chinaExchangeBuyCoins(float(amount))
		tmd['Venezuela'] = calc.venezuelaExchangeSellCoins(tmd['China'][tmd['China']['Best']]['coinsExchanged'])
	elif currency == 'VEF-RMB':
		print "VEF-RMB ajax"
		tmd['currency'] = 'VEF-RMB'
		tmd['Venezuela'] = calc.venezuelaExchangeBuyCoins(amount)
		tmd['China'] = calc.chinaExchangeSellCoins(tmd['Venezuela'][tmd['Venezuela']['Best']]['coinsExchanged'])

	return tmd
	



@route('/')
def index():
    return template('index')

run(host='localhost', port=8080, debug=True)