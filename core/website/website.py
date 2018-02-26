from bottle import route, run, template,static_file,get,request
import server

import bottle


bottle.TEMPLATE_PATH.insert(0, '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/views')

_HTML_BANNER_HEADER = "<!DOCTYPE html><html><head><meta charset='utf-8'>" \
                                                           "<title>Recherche</title><link rel='stylesheet' href='liste.css'></head><body>"
_HTML_BANNER_FOOTER = "</body></html>"

@route('/')
def serve_homepage():
    return template('index.html')


#Hosts html file which will be invoked from browser.
@route('/website/webapp/views/<staticFile>')
def serve_static_file(staticFile):
    filePath = '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/views/'
    return static_file(staticFile, filePath)

#host css files which will be invoked implicitly by your html files.
@route('/website/webapp/static/css/<cssFile>')
@route('/website/webapp/views/traitement/<cssFile>')
def serve_css_files(cssFile):
    print("load css")
    filePath = '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/static/css/'
    return static_file(cssFile, filePath)

# host js files which will be invoked implicitly by your html files.
@route('/website/webapp/static/js/<jsFile>')
def serve_js_files(jsFile):
    filePath = '/hometu/etudiants/e/l/E168076R/PycharmProjects/PythonWebService/core/website/webapp/static/js/'
    return static_file(jsFile, filePath)

@get('/website/webapp/views/traitement/')
def do_process():
    search = request.query["search"]

    conn = server.__start();
    res = server.__query_city(conn, search)
    li = ""
    for val in res:
        li+="<tr>"
        for val2 in val:
            li+="<td>"+val2+"<td>"
        li+="</tr>"

    return _HTML_BANNER_HEADER+"<p id='title'>Vous avez rechercher : "+str(search)+"</p>"+"<div><table>"+str(li)+"</table></div>"+_HTML_BANNER_FOOTER

run(host='localhost', port=1337)
