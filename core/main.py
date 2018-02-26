from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")



server.__close(conn)

print("Disonnected")