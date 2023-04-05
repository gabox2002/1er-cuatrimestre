from data_stark import lista_personajes
from os import system

def mostrar_superheroes():
    for personaje in lista_personajes:
        print(personaje["nombre"])

def mostrar_alturas():
    for personaje in lista_personajes:
        altura_personaje = float(personaje['altura'])
        print(f"{personaje['nombre']} - {altura_personaje: .2f}m")

def mostrar_superheroe_mas_alto():
    maxima_altura = 0
    bandera_mas_alto = False

    for personaje in lista_personajes:
        if bandera_mas_alto == False or (float(personaje['altura'])) > maxima_altura:
            bandera_mas_alto = True
            maxima_altura = float(personaje['altura'])
            heroe_mas_alto = personaje['nombre']
                    
    print(f"El personaje mas alto es {heroe_mas_alto} y mide: {maxima_altura}m")

def mostrar_superheroe_mas_bajo():
    minima_altura = 0
    bandera_mas_bajo = False

    for personaje in lista_personajes:
        if bandera_mas_bajo == False or (float(personaje['altura'])) < minima_altura:
            bandera_mas_bajo = True
            minima_altura = float(personaje['altura'])   
            heroe_mas_bajo = personaje['nombre'] 

    print(f"El personaje mas bajo es {heroe_mas_bajo} y mide: {minima_altura}m")

def mostrar_promedio_alturas():
    acumulador_altura = 0
    contador_heroes = 0

    for personaje in lista_personajes:
        acumulador_altura += float(personaje['altura'])
        contador_heroes += 1
    print(f"La altura promedio de los superhéroes es: {acumulador_altura/contador_heroes:.2f}m")

def mostrar_superheroe_mas_pesado():
    maximo_peso = 0
    bandera_mas_pesado = False

    for personaje in lista_personajes:
        if bandera_mas_pesado == False or (float(personaje['peso'])) > maximo_peso:
            bandera_mas_pesado = True
            maximo_peso = float(personaje['peso'])
            heroe_mas_pesado = personaje['nombre']
    print(f"El superhéroe más pesado es {heroe_mas_pesado} y pesa: {maximo_peso}Kg")

def mostrar_superheroe_menos_pesado():
    minimo_peso = 0
    bandera_menos_pesado = False

    for personaje in lista_personajes:
        if bandera_menos_pesado == False or (float(personaje['peso'])) < minimo_peso:
            bandera_menos_pesado = True
            minimo_peso = float(personaje['peso'])
            heroe_menos_pesado = personaje['nombre']
    print(f"El superhéroe menos pesado es {heroe_menos_pesado} y pesa: {minimo_peso}Kg")

system("cls")
while True:
    respuesta = int(input("\n1. Mostrar superhéroes \n2. Mostrar sus alturas \n3. Mostrar al más alto \n4. Mostrar al más bajo \n5. Mostrar el promedio de altura \n6. Mostrar al más pesado \n7. Mostrar al menos pesado \n8. Salir \nElija una opción: "))
    match respuesta:
        case 1:
            mostrar_superheroes()
        case 2:
            mostrar_alturas()
        case 3:
            mostrar_superheroe_mas_alto()
        case 4:
            mostrar_superheroe_mas_bajo()
        case 5:
            mostrar_promedio_alturas()
        case 6:
            mostrar_superheroe_mas_pesado()
        case 7:
            mostrar_superheroe_menos_pesado()
        case 8:
            break




'''

###B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
for personaje in lista_personajes:
    print(personaje["nombre"])

###C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto ala altura del mismo
for personaje in lista_personajes:
    altura_personaje = float(personaje['altura'])
    print(f"{personaje['nombre']} - {altura_personaje: .2f}m")

###D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
maxima_altura = 0
bandera_mas_alto = False

for personaje in lista_personajes:
    if bandera_mas_alto == False or (float(personaje['altura'])) > maxima_altura:
        bandera_mas_alto = True
        maxima_altura = float(personaje['altura'])
        
            
print(f"El personaje mas alto mide: {maxima_altura}m")
        
###E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
minima_altura = 0
bandera_mas_bajo = False

for personaje in lista_personajes:
    if bandera_mas_bajo == False or (float(personaje['altura'])) < minima_altura:
        bandera_mas_bajo = True
        minima_altura = float(personaje['altura'])    
print(f"El personaje mas bajo mide: {minima_altura}m")

###F. Recorrer la lista y determinar la altura promedio de los superhéroes(PROMEDIO)
acumulador_altura = 0
contador_heroes = 0

for personaje in lista_personajes:
    acumulador_altura += float(personaje['altura'])
    contador_heroes += 1
print(f"La altura promedio de los superhéroes es: {acumulador_altura/contador_heroes:.2f}m")

###G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
for personaje in lista_personajes:
    if float(personaje['altura']) == maxima_altura:
        print(f"El nombre del superhéroe más alto es: {personaje['nombre']}")
    elif float(personaje['altura']) == minima_altura:
        print(f"El nombre del superhéroe más bajo es: {personaje['nombre']}")


###H. Calcular e informar cual es el superhéroe más y menos pesado.
for personaje in lista_personajes:
    peso_personaje = float(personaje['peso'])
    heroe_mas_pesado = personaje['nombre']
    print(f"{personaje['nombre']} - {peso_personaje: .2f}Kg")

maximo_peso = 0
bandera_mas_pesado = False

for personaje in lista_personajes:
    if bandera_mas_pesado == False or (float(personaje['peso'])) > maximo_peso:
        bandera_mas_pesado = True
        maximo_peso = float(personaje['peso'])
        heroe_mas_pesado = personaje['nombre']
print(f"El superhéroe más pesado es {heroe_mas_pesado} y pesa: {maximo_peso}Kg")

minimo_peso = 0
bandera_menos_pesado = False

for personaje in lista_personajes:
    if bandera_menos_pesado == False or (float(personaje['peso'])) < minimo_peso:
        bandera_menos_pesado = True
        minimo_peso = float(personaje['peso'])
        heroe_menos_pesado = personaje['nombre']
print(f"El superhéroe menos pesado es {heroe_menos_pesado} y pesa: {minimo_peso}Kg")

'''