#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import config,html
import parsing,server
from mysql.connector import errorcode


def __start():
    conf = config.CONF()
    cnx = mysql.connector.connect(user=conf.CONST_USER, password=conf.CONST_PASSWORD,
                                  host=conf.CONST_HOST,
                                  database=conf.CONST_DATABASE)
    return cnx


def __close(conn):
    conn.close()


def __query_city(conn,city):
    print("QueryCity")
    query = "SELECT * from Installations where Commune='"+html.escape(city)+"' ORDER BY 1 ASC"
    cur = conn.cursor(buffered=True)
    cur.execute(query)
    result = cur.fetchall()
    return result


def __query_act(conn,act):
    print("QueryAct")
    query = "SELECT * from Installations where TypeAct='"+html.escape(act)+"' ORDER BY 1 ASC"
    cur = conn.cursor(buffered=True)
    cur.execute(query)
    result = cur.fetchall()
    return result


def __query_city_and_act(conn,city,act):
    print("QueryCity&Act")
    query = "SELECT * from Installations where Commune='"+html.escape(city)+"' and TypeAct='"+html.escape(act)+"' ORDER BY 1 ASC"
    cur = conn.cursor(buffered=True)
    cur.execute(query)
    result = cur.fetchall()
    return result


def __query_all(conn):
    print("QueryAll")
    query = "SELECT * from Installations ORDER BY 1 ASC"
    cur = conn.cursor(buffered=True)
    cur.execute(query)
    result = cur.fetchall()
    return result


def __get_city(conn):
    query = "SELECT DISTINCT Commune from Installations ORDER BY 1 ASC"
    cur = conn.cursor(buffered=True)
    cur.execute(query)
    result = cur.fetchall()
    return result


def __get_sport(conn):
    query = "SELECT DISTINCT TypeAct from Installations ORDER BY 1 ASC"
    cur = conn.cursor(buffered=True)
    cur.execute(query)
    result = cur.fetchall()
    return result



def __refresh_DB(conn):
    print("Création des matrices")
    mat1 = parsing.remplirInst()
    print("Fin mat1 remplirInst()")
    mat2 = parsing.remplirEquip()
    print("Fin mat2 remplirEquip()")
    mat3 = parsing.remplirActi()
    print("Fin mat3 remplirActi()")
    server.__createTable(conn, "Installations", mat1)
    server.__createTable(conn, "Equipements", mat2)
    server.__createTable(conn, "Activites", mat3)


def __createTable(conn,name,mat):

    try:
        query = ("DROP TABLE "+name+";")
        cur = conn.cursor(buffered=True)
        cur.execute(query)
    except mysql.connector.Error as err:
            print(err.msg+" cannot drop.")
    else:
        print("OK. Drop table "+name)

    TABLES = {}

    newlist = list()
    for i in mat[str(0)].keys():
        newlist.append(i)


    table_string = ""
    table_string = "CREATE TABLE "+name+" ("
    for val in newlist:
        if val == newlist[len(newlist)-1]:
            table_string += "`" + val + "` varchar(255) DEFAULT NULL"
        else:
            table_string += "`" + val + "` varchar(255) DEFAULT NULL,"
    table_string+=")"

    print(table_string)

    TABLES[name] = (table_string)

    cursor = conn.cursor(buffered=True)

    for name, ddl in TABLES.items():
        try:
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    print("*-*-*-* Insertion des données *-*-*-*")
    for ens in range(0,len(mat)):
        query = "INSERT INTO "+name+" values("
        for type in newlist:
            if type == newlist[len(newlist) - 1]:
                query += '"' +html.escape(str(mat[str(ens)][type])) + '"'
            else:
                query += '"' + html.escape(str(mat[str(ens)][type])) + '",'
        query+=")"
        print(query)
        cur.execute(query)
    cursor.close()


