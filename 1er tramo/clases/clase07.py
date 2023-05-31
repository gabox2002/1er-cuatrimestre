# texto = "hola"
# print(id(texto))
# texto = "chau"
# print(id(texto))
# print(type(texto))

#Metodos para validar 
#STRIP                  elimina caracteres vacios que pueda contener, al principio y final 
cadena = "     Hola mundo    "
cadena = cadena.strip()
print(cadena)   # Hola mundo

#LOWER                  convierte en minusculas todo el texto
cadena = "Hola Mundo"
cadena = cadena.lower()
print(cadena) # Hola Mundo

#UPPER          convierte todo el text en Mayuscula
cadena = "Hola Mundo"
cadena = cadena.upper()
print(cadena) # HOLA MUNDO

#CAPITALIZE     primer caracter dentro de la cadena en mayuscula, y si  tengo mayuscula convierte en minuscula
cadena = "hola Mundo"
cadena = cadena.capitalize()
print(cadena) # Hola mundo

#REPLACE        reemplaza un pedazo de la cadena por otro
cadena = "Hola Mundo"
cadena = cadena.replace("la", "@")
print(cadena)  #Ho@ Mundo

#SPLIT          divide cadena en subcadenas y las devuelve almacenadas en una lista
cadena = "Python, Java, C"
print(cadena.split(","))   #['Python', ' Java', ' C']

#JOIN (lo contrario al split) devuelve la primera cadena unida a cada uno con el delimitador establecido
cadena = "+"
cadena = cadena.join(["A", "B", "C"])
print(cadena)  #A+B+C

#ZFILL (rellena la cadena con ceros a la izquierda hasta llegar a la longitud pasada como parametro)
cadena = "314"
print(cadena.zfill(6))  #000314  "Por si quiero darle un ancho fijo a todos, completo con ceros"

                    #Todos los que comienzan con IS.... devuelve un booleano

#ISALPHA (devuelve un booleano-> True si todos los caracteres son alfebeticos sin numeros ni espacios, False de lo contrario)
cadena = "HolaMundo"
print(cadena.isalpha()) #True

cadena = "Hola Mundo"
print(cadena.isalpha()) #False                   "uso este metodo por si quiero validar un nombre"


#ISALNUM (devuelve un booleano-> True si todos los caracteres son alfanumericos, False lo contrario)
cadena = "Hola Mundo 123"
print(cadena.isalnum()) #False -> por el espacio

cadena = "HolaMundo123"
print(cadena.isalnum()) #True



#ISDIGIT
cadena = "123"
print(cadena.isdigit()) #True

cadena = "Hola Mundo"
print(cadena.isdecimal()) #False


#COUNT (permite contar las veces que se repite dentro de la primera)
cadena = "Hola Mundo Hola"
print(cadena.count("la")) #2                   devolviendo cantidad de incidencias dentro de una cadena

cadena = "Hola Mundo"
print(cadena.count("la", 0, 2)) #2


#FORMAT             (las llaves son reemplazadas con los  valores de las variables pasadas)
nombre_usuario = "Juan"
edad_usuario = 35
cadena = "Nombre: {1}, Edad: {0}"
print(cadena.format(edad_usuario, nombre_usuario))    #Nombre: Juan, Edad: 35

cadena = "Hola Mundo"
print(cadena.format("Hola {0} {1} {2}")) #Hola Hola Mundo Hola Mundo


cadena = "Hola Mundo"
print(cadena.format("Hola {0} {1} {2} {3}")) #Hola Hola Mundo Hola Mundo Hola Mundo


#F-STRING       (uso del interpolado)
n_usuario = "Juan"
e_usuario = 35
cadena = f"Nombre: {n_usuario}, Edad: {e_usuario}"
print(cadena)    #Nombre: Juan, Edad: 35



#LEN            (indica la longitud de la cadena de texto de la variable en ese momento)
cadena = "Hola Mundo"
print(len(cadena)) #10                Incluyendo espacios

cadena = "  Hola Mundo  "
print(len(cadena.strip())) #10



#SLICE corta en pedacito (rebanadas), el primer numero es donde comienza(inclusivo) 
                                        # y el segundo numero de indice es donde termina (exclusivo)

cadena = "Hola Mundo"
#         0123456789
print(cadena[0:5]) #Hola
print(cadena[0:5:2]) #Hl
print(cadena[5:10]) #Mundo
print(cadena[5:]) #Mundo
print(cadena[:5]) #Hola
