#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import config,html
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
    query = "SELECT * from Installations where Commune='"+city+"'"
    cur = conn.cursor(buffered=True)
    cur.execute(query)
    for (pseudo) in cur:
        print(pseudo)


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


