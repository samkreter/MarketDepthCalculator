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
@route('/is_ajax', method="POST")
def is_ajax():
	print "ajax called triggered"
	currency = request.forms.get('currency')
	amount = request.forms.get("amount-{0}".format(currency))
	calc = MarketDepthCalculator()
	totalMarketData = dict()
	return calc.chinaExchangeBuyCoins(float(amount))
	



@route('/')
def index():
    return template('index')

run(host='localhost', port=8080, debug=True)