from bottle import route, run, template,static_file
import bottle


bottle.TEMPLATE_PATH.insert(0, '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/views')

@route('/')
def serve_homepage():
    print("res >>>",bottle.TEMPLATE_PATH)
    return template('index.html')


#Hosts html file which will be invoked from browser.
@route('/views/<staticFile>')
def serve_static_file(staticFile):
    filePath = '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/views/'
    return static_file(staticFile, filePath)

#host css files which will be invoked implicitly by your html files.
@route('/website/webapp/static/css/<cssFile>')
def serve_css_files(cssFile):
    filePath = '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/static/css/'
    return static_file(cssFile, filePath)

# host js files which will be invoked implicitly by your html files.
@route('/website/webapp/static/js/<jsFile>')
def serve_js_files(jsFile):
    filePath = '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/static/js/'
    return static_file(jsFile, filePath)


run(host='localhost', port=1337)
