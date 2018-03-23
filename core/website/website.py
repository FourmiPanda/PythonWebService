from bottle import route, run, template,static_file,get,request,view,post
import server,html,config


import bottle



conf = config.CONF()
bottle.TEMPLATE_PATH.insert(0,conf.CONST_PATH+'/PythonWebService/core/website/webapp/views')


file = open(conf.CONST_PATH+"/PythonWebService/core/website/webapp/views/google_map.html","r")


@route('/')
@view("index.html")
def serve_homepage():
    conn = server.__start();

    liste_ville = server.__get_city(conn);
    liste_sport = server.__get_sport(conn);

    print(liste_sport)

    server.__close(conn)

    my_dict = {'listeSport': liste_sport, 'listeVille': liste_ville}
    return template("index.html", my_dict)


#Hosts html file which will be invoked from browser.
@route('/website/webapp/views/<staticFile>')
def serve_static_file(staticFile):
    filePath = conf.CONST_PATH+'/PythonWebService/core/website/webapp/views/'
    return static_file(staticFile, filePath)

#host css files which will be invoked implicitly by your html files.
@route('/website/webapp/static/css/<cssFile>')
@route('/website/webapp/views/traitement/<cssFile>')
def serve_css_files(cssFile):
    print("load css")
    filePath = conf.CONST_PATH+'/PythonWebService/core/website/webapp/static/css/'
    return static_file(cssFile, filePath)

# host js files which will be invoked implicitly by your html files.
@route('/website/webapp/static/js/<jsFile>')
def serve_js_files(jsFile):
    filePath = conf.CONST_PATH+'/PythonWebService/core/website/webapp/static/js/'
    return static_file(jsFile, filePath)

@post('/website/webapp/views/traitement/')
@view('Template.html')
def do_process():
    print("TRAITEMENT")

    li_ville = request.forms.get("ville")
    li_sport = request.forms.get("sport")

    conn = server.__start()
    if li_ville == "":
        res = server.__query_act(conn,html.escape(li_sport))
    else :
        if li_sport == "":
            res = server.__query_city(conn,html.escape(li_ville))
        else :
            res = server.__query_city_and_act(conn,html.escape(li_ville),html.escape(li_sport))
    server.__close(conn)
    print(res)
    my_dict = {'res': res, 'nbRes': len(res)}
    return template("Template.html", my_dict)




run(host='localhost', port=1337)
