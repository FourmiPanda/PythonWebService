from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

# print("Connected")
#
# print("Voulez vous rafraichir la base de donnée ? (o/n)")
#
# m=input()
#
# if m == "o" or m == "O":
#     server.__refresh_DB(conn)
#
# print("Taper le nom d'une ville : ")
# m = input()
#
# while m!="quit":
#     print("Taper le nom d'une ville : ")
#     server.__query_city(conn, m)
#     m=input()

query = "SELECT e.EquId, a.Commune from Equipements e, Activites a where a.Commune='Nantes' and a.TypeAct='Tennis' and e.EquId = a.EquId ORDER BY 1 ASC "
cur = conn.cursor(buffered=True)
cur.execute(query)
result = cur.fetchall()
print (result)

server.__close(conn)

print("Disonnected")