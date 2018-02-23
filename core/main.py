from core import server,parsing

print("Connexion a la DB")

conn = server.__start()

print("Connected")

# print("Création des matrices")
# mat1 = parsing.remplirInst()
# print("Fin mat1")
# mat2 = parsing.remplirEquip()
# print("Fin mat2")
# mat3 = parsing.remplirActi()
# print("Fin mat3")
#
#
# server.__createTable(conn,"Installations",mat1)
#
# server.__createTable(conn,"Equipements",mat2)
#
# server.__createTable(conn,"Activites",mat3)


server.__query_city(conn,"Châteaubriant")

server.__close(conn)

print("Disonnected")