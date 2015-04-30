from bottle import route, run, template, static_file


# @get('/<filename:re:.*\.(jpg|png|gif|ico)>')
# def images(filename):
#     return static_file(filename, root='static/img')

# @get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
# def fonts(filename):
#     return static_file(filename, root='static/fonts')

#public routes
@route('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='public/js')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='public/css')


#bootstrap public 
@route('/bootstrap/css/<filename>')
def bootstrapCSS(filename):
	return static_file(filename,root='bootstrap/css')
@route('/bootstrap/js/<filename>')
def bootstrapJS(filename):
	return static_file(filename,root='bootstrap/js')



@route('/hello')
def hello():
    return template('hello')

run(host='localhost', port=8080, debug=True)