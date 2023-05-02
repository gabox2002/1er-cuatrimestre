#Archivos

# "77" -> 00000111 
# 77 -> 

# 4 bytes

# import sys
# valor = 77

# print(sys.getsizeof(valor))   #28

# Modo de apertura
#"r" y "w" son las q mas vamos a usar

# crear un archivo
# path = "nombre.txt"
# archivo_texto = open(path, "w")= escribir / archivo_texto = open(path, "a") = apendizar
# archivo_texto.write("German")
# archivo_texto.close()

# leer un archivo
# path = "nombre.txt"
# archivo_texto = open(path, "r")
# print(archivo_texto)

#Intenta ingresar al arciho pero como no lo encuentra, muestra el mensaje de error
# path = "nombre.txt"      #path = "lalanombre.txt"
# try:
#     archivo_texto = open(path, "r")
#     lectura = archivo_texto.read()
#     print(lectura)
#     archivo_texto.close()
# except:
#     print("Error no se pudo abrir el archivo")   
# German
# German
# German
# gio


#READLINES = devuelve una lista, representado como una cadena
# path = "nombre.txt"      #path = "lalanombre.txt"

# archivo_texto = open(path, "r")
# lista = archivo_texto.readlines()
# archivo_texto.close()   #['German\n', 'German\n', 'German\n', 'gio']
# print(lista)
# for line in lista:
#     print(line, end = "")   # Para evitar el salto de linea


# lista = ["Gio", "Faus", "Gonza", "Marian"]
# archivo = open("nombres.txt", "w")   #para escritura
# for nombre in lista:
#     archivo.write(f"{nombre}\n")
# archivo.close()

#WRITElINE  

#WiTH   para que cierre el archivo automatico
# path = "nombres.txt"     
# with open(path, "r") as archivo:
#     lista = archivo.readlines()

# #Para ver si se cerro el archivo
# # print (archivo)  #<_io.TextIOWrapper name='nombres.txt' mode='r' encoding='cp1252'>
# # if archivo. closed:
# #       print("se cerro")
# # else:
# #       print("No se cerró")
#
# for line in lista:
#         print(line, end = "")   # Para evitar el salto de linea

#     # Gio
#     # Faus
#     # Gonza
#     # Marian

#####CSV####   archivo de texto, separado por comas, guiones, o etc, cada elemento esta separado por una coma, cada linea es item, y cada clave
# nombres = ["Jose", "Maria", "Franco"]
# apellidos = ["Gomez", "Ruiz", "Perez"]
# edades = [23, 36, 47]

# #crear archivo csv
# with open("agenda.csv", "w") as archivo:
#     for i in range(3):
#         line = "{0},{1},{2}\n".format(nombres[i], apellidos[i], edades[i])
#         archivo.write(line)

#leer el csg
# with open("agenda.csv", "r") as archivo:
#     for line in archivo:
#         print(line, end="")         #Jose,Gomez,23
#                                     #Maria,Ruiz,36
#                                     #Franco,Perez,47

#por cada registro
# with open("agenda.csv", "r") as file:
#     for line in file:
        # register = line.split(",")  #cortar cada registro por coma
        #print(register)

        # ['Jose', 'Gomez', '23\n']
        # ['Maria', 'Ruiz', '36\n']
        # ['Franco', 'Perez', '47\n']
        
        # print(f"{register[0]} - {register[1]} - {register[2]}", end="" ) #sacar el barra linea del salto de linea

        # Jose - Gomez - 23
        # Maria - Ruiz - 36
        # Franco - Perez - 47


# import re
# with open("agenda.csv", "r") as file:
#     for line in file:
#         register = re.split(",|\n", line)
#         # print(register)

#         # ['Jose', 'Gomez', '23', '']
#         # ['Maria', 'Ruiz', '36', '']
#         # ['Franco', 'Perez', '47', '']

#         print(f"{register[0]} - {register[1]} - {register[2]}", end="" ) #sacar el barra linea del salto de linea

#         #Jose - Gomez - 23Maria - Ruiz - 36Franco - Perez - 47

    
############JSON JavaScript Object Notation forma de un diccionario
# import json

# data = {}
# data["clientes"] = []
# data["clientes"].append({"nombre":"Juan", "edad":25})
# data["clientes"].append({"nombre":"Maria", "edad":32})                 
# data["clientes"].append({"nombre":"German", "edad":27})

# print(data)    #{'clientes': [{'nombre': 'Juan', 'edad': 25}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'German', 'edad': 27}]}

# with open("clientes.json", "w") as file:
#     json.dump(data, file, indent=4)               #data = origen del dat, archivo, y la identacion


# with open("clientes.json", "r") as archivo:
#     mi_data = json.load(archivo)

#     print(mi_data) 

#########PARSER CSV############################
# import re
# def parser_csv(path:str) -> list:
#     lista_temas = []

#     archivo = open(path, "r", enconding = "UTF-8")
#     for line in archivo:
#         register = re.split(",|\n",line)
#         tema = {}                           #corto en pedazos
#         tema["title"]= register[0]
#         tema["views"]= register[1]
#         tema["length"]= register[2]
#         tema["img_url"]= register[3]
#         tema["url"]= register[4]
#         tema["date"]= register[5]
#         lista_temas.append(tema)   #crea la lista
#     archivo.close()
#     return lista_temas
    
# def generar_csv(path:str, lista:list):
#     archivo = open(path, "w", encoding="UTF-8")
#     for tema in lista:
#         line = "{0},{1},{2},{3},{4},{5}"
#         line = line.format(tema["title"], 
#                            tema["views"], 
#                            tema["length"], 
#                            tema["img_url"],
#                            tema["url"],
#                            tema["date"])
#         archivo.write(line)
#     archivo.close()

   
# lista_biza = parser_csv("data.csv")
# for tema in lista_biza:
#     print(tema["title"])

# generar_csv("nueva_lista.csv", lista_biza)


#########PARSER JSON############################
import json

def parser_json(path:str)->list:
    with open(path,"r") as archivo:
        diccionario = json.load(archivo)

    return diccionario ["bzrp"]

def generar_json(path:str, lista):
    with open(path, "w") as archivo:
        json.dump(lista, archivo, indent=3)

lista = parser_json("data.json")
generar_json("nueva_lista.json", lista)



