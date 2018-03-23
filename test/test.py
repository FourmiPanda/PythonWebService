from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")

print("Voulez vous rafraichir la base de donnée ? (o/n)")

m=input()

if m == "o" or m == "O":
    server.__refresh_DB(conn)

server.__close(conn)

print("Disonnected")