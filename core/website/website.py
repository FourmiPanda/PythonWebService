from bottle import route, run, template,static_file,get,request,view,post
import server,html,config


import bottle



conf = config.CONF()
bottle.TEMPLATE_PATH.insert(0,conf.CONST_PATH+'/PythonWebService/core/website/webapp/views')


file = open(conf.CONST_PATH+"/PythonWebService/core/website/webapp/views/google_map.html","r")


@route('/')
@view("index.html")
def serve_homepage():
    conn = server.start();

    liste_ville = server.get_city(conn);
    liste_sport = server.get_sport(conn);
    liste_niveau = server.getNiveau(conn);

    print(liste_niveau)

    server.close(conn)

    my_dict = {'listeSport': liste_sport, 'listeVille': liste_ville, 'listeNiveau' : liste_niveau}
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


def do_process():
    print("TRAITEMENT")

    li_ville = request.forms.ville
    li_sport = request.forms.sport
    li_niv = request.forms.niveau

    conn = server.start()

    if li_ville == "":
        res = server.query_act(conn,li_sport)
    else :
        if li_sport == "":
            res = server.query_city(conn,li_ville)
        else :
            if li_niv == "":
                res = server.query_city_and_act(conn,li_ville,li_sport)
            else:
                res = server.query_city_and_act_and_niv(conn, li_ville,li_sport,li_niv)

    server.close(conn)
    print(res)
    my_dict = {'res': res, 'nbRes': len(res)}
    return template("Template.html", my_dict)

@post('/website/webapp/views/traitement/')
@view('Template.html')
def mainProcess():

    x = request.forms.posLat
    y = request.forms.posLng

    print(x)

    if (x != "" and y != ""):
        print("normal")
    else:
        res = do_process()

    return res

run(host='localhost', port=1337)
