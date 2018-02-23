#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import config
from mysql.connector import errorcode


def __start():
    conf = config.CONF()
    cnx = mysql.connector.connect(user=conf.CONST_USER, password=conf.CONST_PASSWORD,
                                  host=conf.CONST_HOST,
                                  database=conf.CONST_DATABASE)
    return cnx


def __close(conn):
    conn.close()


def __query_city(conn):
    query = "SELECT * from pseudonyme"
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

    TABLES[name] = ("CREATE TABLE "+name+" ( `arg1` int(12), `arg2` int(13))")
    print(mat)
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

    cursor.close()


