from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")

res = server.__query_city(conn, "Nantes")
print(res)


server.__close(conn)

print("Disonnected")