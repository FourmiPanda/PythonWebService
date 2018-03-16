from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")

server.__refresh_DB(conn)

mat = parsing.remplirActi()
print(mat)

res = server.__get_sport(conn)
print(res)

server.__close(conn)

print("Disonnected")