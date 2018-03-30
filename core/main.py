from core import server,parsing

print("Connexion a la DB")

conn = server.start()

print("Connected")

server.refresh_DB(conn)

mat = parsing.remplirActi()
print(mat)

res = server.get_sport(conn)
print(res)

server.close(conn)

print("Disonnected")