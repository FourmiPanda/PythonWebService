from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")


mat = parsing.remplirInst()
#server.__createTable(conn, "testCreation")

server.__query_city(conn)

server.__close(conn)

print("Disonnected")