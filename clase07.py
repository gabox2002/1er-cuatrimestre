# texto = "hola"
# print(id(texto))
# texto = "chau"
# print(id(texto))
# print(type(texto))

#STRIP
cadena = "     Hola mundo    "
cadena = cadena.strip()
print(cadena)   # Hola mundo

#LOWER
cadena = "Hola Mundo"
cadena = cadena.lower()
print(cadena) # Hola Mundo

#UPPER
cadena = "Hola Mundo"
cadena = cadena.upper()
print(cadena) # HOLA MUNDO

#CAPITALIZE  (primer caracter en mayuscula)
cadena = "hola Mundo"
cadena = cadena.capitalize()
print(cadena) # Hola Mundo

#REPLACE (reemplaca un pedazo de la cadena)
cadena = "Hola Mundo"
cadena = cadena.replace("la", "@")
print(cadena)  #Ho@ Mundo

#SPLIT (divide cadena en subcadenas)
cadena = "Python, Java, C"
print(cadena.split(","))   #['Python', ' Java', ' C']

#JOIN (lo contrario al split) devuelve la primera cadena unida a cada uno
cadena = "+"
cadena = cadena.join(["A", "B", "C"])
print(cadena)  #A+B+C

#ZFILL (relena la adena con ceros a la izquierda hasta llegar a la longitud pasada como arametro)
cadena = "314"
print(cadena.zfill(6))  #000314

#ISALPHA (devuelve True si todos los caracteres son alfebeticos sin numeros ni espacios, False de lo contrario)

cadena = "HolaMundo"
print(cadena.isalpha()) #True

cadena = "Hola Mundo"
print(cadena.isalnum()) #False

#ISDIGIT

cadena = "123"
print(cadena.isdigit()) #True

cadena = "Hola Mundo"
print(cadena.isdecimal()) #False

#COUNT (permite contar las veces que otra cadena se encuentra dentro de la primera)

cadena = "Hola Mundo Hola"
print(cadena.count("la")) #2

cadena = "Hola Mundo"
print(cadena.count("la", 0, 2)) #2

#FORMAT

cadena = "Hola Mundo"
print(cadena.format("Hola {0} {1} {2}")) #Hola Hola Mundo Hola Mundo

cadena = "Hola Mundo"
print(cadena.format("Hola {0} {1} {2} {3}")) #Hola Hola Mundo Hola Mundo Hola Mundo

#LEN

cadena = "Hola Mundo"
print(len(cadena)) #10

cadena = "Hola Mundo"
print(len(cadena.strip())) #10

#SLICE corta en pedacito (rebanadas), el primer numero es donde comienza(inclusivo) y el segundo numero de indice es dnde termina (exclusivo)

cadena = "Hola Mundo"
print(cadena[0:5]) #Hola
print(cadena[0:5:2]) #Hl
print(cadena[5:10]) #Mundo
print(cadena[5:]) #Mundo
print(cadena[:5]) #Hola
