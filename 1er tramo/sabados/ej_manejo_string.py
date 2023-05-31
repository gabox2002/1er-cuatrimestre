'''
1.Contar letras: Crea una función que tome una cadena
de texto como argumento y
cuente el número de letras que contiene.
2.Eliminar caracteres: Crea una función que tome una
cadena de texto y un carácter como argumentos, y
elimine todas las ocurrencias de ese carácter en la
cadena.
3.Contar palabras: Crea una función que tome una
cadena de texto como argumento y
cuente el número de palabras que contiene.
Suponga que las palabras están separadas por un
espacio.
4.Reemplazar palabras: Crea una función que tome una
cadena de texto, una palabra y otra palabra como
argumentos, y reemplace todas las ocurrencias de la
primera palabra por la segunda en la cadena.
5.Buscar patrón: Crea una función que tome dos cadenas
de texto como argumentos: una cadena principal y un
patrón. La función debe encontrar todas las ocurrencias
del patrón en la cadena principal y devolver una lista con
las posiciones donde se encontró el patrón.
'''

# Para contar el número de letras en una cadena de texto, podemos utilizar un bucle for para iterar sobre cada caracter de la cadena y aumentar un contador si el caracter es una letra:
def contar_letras(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isalpha():
            contador += 1
    return contador

# Para eliminar todas las ocurrencias de un carácter en una cadena de texto, podemos utilizar el método replace():
def eliminar_caracter(cadena, caracter):
    return cadena.replace(caracter, "")

# Para contar el número de palabras en una cadena de texto, podemos utilizar el método split() para separar la cadena en una lista de palabras y luego contar el número de elementos en esa lista:
def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

# Para reemplazar todas las ocurrencias de una palabra por otra en una cadena de texto, podemos utilizar el método replace():
def reemplazar_palabra(cadena, palabra_original, palabra_nueva):
    return cadena.replace(palabra_original, palabra_nueva)



# Para buscar un patrón en una cadena de texto y devolver una lista con las posiciones donde se encontró el patrón, podemos utilizar el método find() en un bucle while para buscar el patrón en la cadena, guardando la posición donde se encontró y continuando la búsqueda desde la posición siguiente:
def buscar_patron(cadena, patron):
    posiciones = []
    posicion = cadena.find(patron)
    while posicion != -1:
        posiciones.append(posicion)
        posicion = cadena.find(patron, posicion + 1)
    return posiciones