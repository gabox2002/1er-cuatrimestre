from data_stark import lista_personajes
from os import system

system("cls")

###B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
for personaje in lista_personajes:
    print(personaje["nombre"])

###C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto ala altura del mismo
for personaje in lista_personajes:
    altura_personaje = float(personaje['altura'])
    print(f"{personaje['nombre']} - {altura_personaje: .2f}")

###D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
maxima_altura = 0
bandera_mas_alta = False

for personaje in lista_personajes:
    if altura_personaje > maxima_altura or bandera_mas_alta == False:
        bandera_mas_alta = True
        maxima_altura = float(personaje['altura'])
        personaje_mas_alto = personaje['nombre']
    
print(f"El personaje mas alto es: {personaje_mas_alto} con: {maxima_altura}")
        

