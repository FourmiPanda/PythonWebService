import core.parsing

from core import server

print("Connexion a la DB")

conn = server.__start()

print("Connected")

mat = core.parsing.remplirInst()

server.__createTable(conn, "testCreation")

server.__query_city(conn)

server.__close(conn)

print("Disonnected")