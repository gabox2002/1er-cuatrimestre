'''
La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.
'''

from os import system
system("cls") 

diccionario = {} # Creamos un diccionario vacío para almacenar las palabras y sus traducciones

while True:
    palabra_espanol = input("Ingrese una palabra en español: ")
    if palabra_espanol == "": # Si el usuario no ingresa nada, salimos del bucle
        break
    if palabra_espanol in diccionario: # Si la palabra ya existe, informamos al usuario
        print(f"La palabra '{palabra_espanol}' ya existe en el diccionario, su índice es {list(diccionario.keys()).index(palabra_espanol)}")
    else: # Si la palabra no existe, pedimos su traducción y la agregamos al diccionario
        palabra_ingles = input("Ingrese la traducción al inglés: ")
        diccionario[palabra_espanol] = palabra_ingles

print("Diccionario de Español a Inglés:")
for palabra_espanol, palabra_ingles in diccionario.items(): # Recorremos el diccionario y mostramos las palabras y sus traducciones
    print(f"{palabra_espanol} - {palabra_ingles}")