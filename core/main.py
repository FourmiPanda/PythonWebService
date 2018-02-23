from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")

mat = parsing.remplirInst()

server.__createTable(conn,"Installations",mat)

server.__query_city(conn,"dadar")

server.__close(conn)

print("Disonnected")