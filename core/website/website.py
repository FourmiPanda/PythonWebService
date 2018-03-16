from bottle import route, run, template,static_file,get,request
import server,html

import bottle


bottle.TEMPLATE_PATH.insert(0, '/hometu/etudiants/j/o/E166294E/TechProd/TD2/PythonWebService/PythonWebService/core/website/webapp/views')

_HTML_BANNER_HEADER = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>" \
                                                           "\n<title>Recherche</title>\n<link rel='stylesheet' href='/website/webapp/static/css/style.css'>\n</head>\n<body>"

_HTML_BANNER_HEADER2 = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>" \
                                                           "\n<title>Recherche</title>\n<link rel='stylesheet' href='/website/webapp/static/css/liste.css'>\n</head>\n<body>"


_HTML_BANNER_FOOTER = "\n</body>\n</html>"

file = open("/hometu/etudiants/j/o/E166294E/TechProd/TD2/PythonWebService/core/website/webapp/views/google_map.html","r")
_HTML_MAP = file.read()
file.close()

# @route('/')
# def serve_homepage():
#     conn = server.__start();
#     print(server.__get_city(conn))
#     server.__close(conn)
#     return template('index.html')

@route('/')
def serve_homepage():
    conn = server.__start();
    liste_ville = server.__get_city(conn);
    liste_sport = server.__get_sport(conn);
    print(liste_sport)
    li_ville = ""
    li_ville+="\n<select name='li_ville'>"
    for val2 in liste_ville:
        li_ville+="\n<option>"+val2[0]+"</option>"
    li_ville+="\n</select>"

    li_Sport = ""
    li_Sport+="\n<select name='li_sport'>"
    for val2 in liste_sport:
        li_Sport+="\n<option>"+val2[0]+"</option>"
    li_Sport+="\n</select>"




    server.__close(conn)
    return _HTML_BANNER_HEADER + "<section class='webdesigntuts-workshop'><h1 id='title'>Bienvenue sur SportLooker !</h1><form action='/website/webapp/views/traitement/' method='GET'>" \
                                 +str(li_ville)+str(li_Sport)+"<br><button>Rechercher</button></form></section>" + _HTML_BANNER_FOOTER



#Hosts html file which will be invoked from browser.
@route('/website/webapp/views/<staticFile>')
def serve_static_file(staticFile):
    filePath = '/hometu/etudiants/j/o/E166294E/TechProd/TD2/PythonWebService/core/website/webapp/views/'
    return static_file(staticFile, filePath)

#host css files which will be invoked implicitly by your html files.
@route('/website/webapp/static/css/<cssFile>')
@route('/website/webapp/views/traitement/<cssFile>')
def serve_css_files(cssFile):
    print("load css")
    filePath = '/hometu/etudiants/j/o/E166294E/TechProd/TD2/PythonWebService/core/website/webapp/static/css/'
    return static_file(cssFile, filePath)

# host js files which will be invoked implicitly by your html files.
@route('/website/webapp/static/js/<jsFile>')
def serve_js_files(jsFile):
    filePath = '/hometu/etudiants/j/o/E166294E/TechProd/TD2/PythonWebService/core/website/webapp/static/js/'
    return static_file(jsFile, filePath)

@get('/website/webapp/views/traitement/')
def do_process():
    print(_HTML_MAP)
    li_ville = request.query["li_ville"]
    li_sport = request.query["li_sport"]

    conn = server.__start();
    if li_ville == "":
        res = server.__query_act(conn,html.escape(li_sport))
    else :
        if li_sport == "":
            res = server.__query_city(conn,html.escape(li_ville))
        else :
            res = server.__query_city_and_act(conn,html.escape(li_ville),html.escape(li_sport))

    server.__close(conn)
    li = ""
    for val in res:
        li+="<tr>"
        for val2 in val:
            li+="<td>"+val2+"<td>"
        li+="</tr>"


    return _HTML_BANNER_HEADER2+"<p id='title'>Vous avez recherché : "+str(li_ville)+" et "+str(li_sport)+"</p>"+"<div><table>"+str(li)+"</table></div>"+_HTML_MAP+_HTML_BANNER_FOOTER

run(host='localhost', port=1337)
