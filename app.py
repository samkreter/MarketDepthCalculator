from bottle import route,request, response, run, template, static_file
from MarketDepthCalculator import MarketDepthCalculator
import ExchangeInfo
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
#font awsome routes
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
	print("ajax called triggered")
	currency = request.forms.get('currency')
	#get the amount from the form
	amount = float(request.forms.get("amount-{0}".format(currency)))
	
	#create instance of the class
	calc = MarketDepthCalculator()
	#total Market data
	tmd = dict()

	#split the cuurency to get the indiviual curr names 
	curr1 = currency[0:3]
	curr2 = currency[4:7]

	tmd['currency'] = currency
	tmd['exhangeRate'] = calc.exchangeRate(curr1,curr2)
	tmd[curr1] = calc.ExchangeBuyCoins(amount,curr1)
	#check for errors and return if they are found
	if 'errors' in tmd[curr1]:
		return tmd[curr1]
	tmd[curr2] = calc.ExchangeSellCoins(tmd[curr1]['exchanges'][tmd[curr1]['Best']]['coinsExchanged'],curr2)
	if 'errors' in tmd[curr2]:
		return tmd[curr1]
	
	tmd['bitnexoExchangeRate'] = calc.bitnexoExchangeRate(tmd[curr1],tmd[curr2])
	tmd['percentDifference'] = calc.percentDifference(tmd['exhangeRate'],tmd['bitnexoExchangeRate'])
	
	return tmd
	
@route('/test')
def test():
	currencies = {"RMB","CLP","VEF","BRL","MXN"}
	return template('test',exhangeData=currencies)
#create the index route for the main page 
@route('/')
def index():
    return template('index')

run(host='localhost', port=8080, debug=True)