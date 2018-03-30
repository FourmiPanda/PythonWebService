from core import server,parsing

print("Connexion a la DB")

conn = server.start()

print("Connected")

print("Voulez vous rafraichir la base de donnée ? (o/n)")

m=input()

if m == "o" or m == "O":
    server.refresh_DB(conn)

server.close(conn)

print("Disonnected")