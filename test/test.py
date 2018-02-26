from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")

print("Voulez vous rafraichir la base de donnée ? (o/n)")

m=input()

if m == "o" or m == "O":
    server.__refresh_DB(conn)

print("Taper le nom d'une ville : ")
m = input()

while m!="quit":
    print("Taper le nom d'une ville : ")
    server.__query_city(conn, m)
    m=input()

server.__close(conn)

print("Disonnected")