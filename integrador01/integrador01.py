from data_stark import lista_personajes
from os import system

def mostrar_superheroes_masculinos():
    contador_superheroes_masculinos = 0
    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "M":
            contador_superheroes_masculinos += 1
            print(f"{personaje['nombre']} - {personaje['genero']} ")
    print(f"El numero de superheroes masculino es:  {contador_superheroes_masculinos}")

def mostrar_superheroes_femeninos():
    contador_superheroes_femeninos = 0
    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "F":
            contador_superheroes_femeninos += 1
            print(f"{personaje['nombre']} - {personaje['genero']} - {personaje['altura']}")
    print(f"El numero de superheroes femeninos es:  {contador_superheroes_femeninos}")

def mostrar_superheroe_masculino_mas_alto():
    mas_alto = ""
    bandera_mas_alto = False

    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "M":
            if bandera_mas_alto == False or float(personaje['altura']) > mas_alto:
                bandera_mas_alto = True
                mas_alto = float(personaje['altura'])
                masculino_mas_alto = personaje['nombre']

    print(f"El personaje masculino mas alto es {masculino_mas_alto} con {mas_alto}")

def mostrar_superheroe_femenino_mas_alta():
    mas_alta = ""
    bandera_mas_alta = False
    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "F":        
            if bandera_mas_alta == False or float(personaje['altura']) > mas_alta:
                mas_alta = float(personaje['altura'])
                femenino_mas_alta = personaje['nombre']
                bandera_mas_alta = True
            
    print(f"La personaje femenino mas alta es {femenino_mas_alta} con {mas_alta}")

def mostrar_superheroe_masculino_mas_bajo():
    mas_bajo = ""
    bandera_mas_bajo = False

    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if  personaje['genero'] == "M":
            if bandera_mas_bajo == False or float(personaje['altura']) < mas_bajo:
                bandera_mas_bajo = True
                mas_bajo = float(personaje['altura'])
                masculino_mas_bajo = personaje['nombre']

    print(f"El personaje masculino mas bajo es {masculino_mas_bajo} con {mas_bajo}")

def mostrar_superheroe_femenino_mas_baja():
    mas_baja = ""
    bandera_mas_baja = False
    
    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "F": # Si el genero del personaje es F
            if  bandera_mas_baja == False or float(personaje['altura']) < mas_baja: # Si cumple la bandera o la altura ingresada es la mas baja
                bandera_mas_baja = True
                mas_baja = float(personaje['altura'])
                femenino_mas_baja = personaje['nombre']

    print(f"La personaje femenino mas baja es {femenino_mas_baja} con {mas_baja}")

def mostrar_promedio_altura_masculino():
    altura_promedio_masculino = 0
    contador_masculino = 0

    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "M":
            altura_promedio_masculino += float(personaje['altura'])
            contador_masculino += 1

    promedio_altura_masculino = altura_promedio_masculino / contador_masculino

    print(f"La altura promedio de los superhéroes de género M es {promedio_altura_masculino: .2f}m")

def mostrar_promedio_altura_femenino():
    altura_promedio_femenino = 0
    contador_femenino = 0

    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "F":
            altura_promedio_femenino += float(personaje['altura'])
            contador_femenino += 1

    promedio_altura_femenino = altura_promedio_femenino / contador_femenino

    print(f"La altura promedio de los superhéroes de género F es {promedio_altura_femenino: .2f}m")

def mostrar_superheroe_mas_alto_mas_bajo_por_genero():
    mas_alto = ""
    mas_bajo = ""
    mas_alta = ""
    mas_baja = ""
    bandera_mas_alto = False
    bandera_mas_bajo = False
    bandera_mas_alta = False
    bandera_mas_baja = False

    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "M":
                if bandera_mas_alto == False or float(personaje['altura']) > mas_alto:
                    bandera_mas_alto = True
                    mas_alto = float(personaje['altura'])
                    masculino_mas_alto = personaje['nombre']
                if bandera_mas_bajo == False or float(personaje['altura']) < mas_bajo:
                    bandera_mas_bajo = True
                    mas_bajo = float(personaje['altura'])
                    masculino_mas_bajo = personaje['nombre']

        if personaje['genero'] == "F":
            if bandera_mas_alta == False or float(personaje['altura']) > mas_alta:
                mas_alta = float(personaje['altura'])
                femenino_mas_alta = personaje['nombre']
                bandera_mas_alta = True
            if bandera_mas_baja == False or float(personaje['altura']) < mas_baja: 
                bandera_mas_baja = True
                mas_baja = float(personaje['altura'])
                femenino_mas_baja = personaje['nombre']
            
    print(f"El superheroe masculino mas alto es {masculino_mas_alto} con {mas_alto}")
    print(f"El superheroe masculino mas bajo es {masculino_mas_bajo} con {mas_bajo}")
    print(f"La superheroe femenina mas alta es {femenino_mas_alta} con {mas_alta}")
    print(f"La superheroe femenina mas baja es {femenino_mas_baja} con {mas_baja}")

def mostrar_superheroes_por_color_ojos():
    conteo_ojos = {} # Creamos un diccionario para almacenar el conteo de cada color de ojos

    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        color_ojos = personaje['color_ojos'] # Obtenemos el color de ojos del superhéroe actual
        if color_ojos not in conteo_ojos:    
            conteo_ojos[color_ojos] = 1     # Si el color de ojos no ha sido registrado en el diccionario, lo inicializamos con un conteo de 1
        else:                                
            conteo_ojos[color_ojos] += 1    # Si el color de ojos ya ha sido registrado, incrementamos su conteo en 1
            
    for (color, conteo) in conteo_ojos.items(): # Imprimimos el conteo de cada color de ojos (clave, valor)
        print(f"Hay {conteo} superhéroes con ojos de color {color}.")

def mostrar_superheroes_por_color_pelo():
    conteo_color_pelo = {} #creamos el diccionario para almacenar el conteo de cada tipo de color de pelo

    for personaje in lista_personajes:
        if  personaje["color_pelo"] == "":
            color = "No Tiene"
        else:        
            color = personaje["color_pelo"]

        if color in conteo_color_pelo:
            conteo_color_pelo[color] += 1 # Si el color_pelo no ha sido registrada en el diccionario, la inicializamos con una cantidad de 1
        else:
            conteo_color_pelo[color] = 1 # Si el color_pelo ya ha sido registrado, incrementamos su cantidad en 1
            
    for color, conteo in conteo_color_pelo.items():  #(clave, valor)(color es la clave, conteo el valor que toma con ese color de pelo) 
        print(f"Hay {conteo} superhéroes con el color de pelo {color}") # Se imprime el conteo para cada color de pelo.

def mostrar_superheroes_por_inteligencia():

    inteligencias = {}# Inicializar el diccionario de inteligencias

    for personaje in lista_personajes:
        if personaje['inteligencia'] == '':
            inteligencia = 'No Tiene'
        else:
            inteligencia = personaje['inteligencia']

        if inteligencia in inteligencias:
            inteligencias[inteligencia] += 1 # Si la inteligencia no ha sido registrada en el diccionario, la inicializamos con una cantidad de 1
        else:
            inteligencias[inteligencia] = 1 # Si la inteligencia ya ha sido registrado, incrementamos su cantidad en 1

    for inteligencia, cantidad in inteligencias.items():
        print(f"Hay {cantidad} superhéroes con inteligencia {inteligencia}")

def listado_superheroes_por_color_ojos():
    superheroes_por_color_ojos = {} # Crear diccionario vacío para almacenar héroes por color de ojos

    for superheroe in lista_personajes:  ## Recorrer la lista de héroes y agregarlos al diccionario correspondiente al color de ojos
        color_ojos = superheroe['color_ojos']
        if color_ojos not in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos] = []
        superheroes_por_color_ojos[color_ojos].append(superheroe['nombre'])

    for color_ojos, superheroes in superheroes_por_color_ojos.items():  # Imprimir el resultado (color_ojos, superheroe)
        print(f"Superhéroes con ojos de color {color_ojos}: {', '.join(superheroes)}")

def listado_superheroes_por_color_pelo():

    heroes_por_pelo = {} # Crear diccionario vacío para almacenar héroes por color de pelo

    for superheroe in lista_personajes: # Recorrer la lista de héroes y agregarlos al diccionario correspondiente al color de pelo
        pelo = superheroe['color_pelo'] or 'No Tiene'
        if pelo not in heroes_por_pelo:
            heroes_por_pelo[pelo] = []
        heroes_por_pelo[pelo].append(superheroe['nombre'])


    for pelo, heroes in heroes_por_pelo.items():    # Imprimir el resultado
        print(f"Superhéroes con pelo de color {pelo}: {', '.join(heroes)}")

def listado_superheroes_por_inteligencia():
    
#O. Listar todos los superhéroes agrupados por tipo de inteligencia.

    heroes_por_inteligencia = {}    # Crear diccionario vacío para almacenar héroes por tipo de inteligencia

    for heroe in lista_personajes:  # Recorrer la lista de héroes y agregarlos al diccionario correspondiente al tipo de inteligencia
        inteligencia = heroe['inteligencia'] or 'No Tiene'
        if inteligencia not in heroes_por_inteligencia:
            heroes_por_inteligencia[inteligencia] = []
        heroes_por_inteligencia[inteligencia].append(heroe['nombre'])


    for inteligencia, heroes in heroes_por_inteligencia.items(): # Imprimir el resultado
        print(f"Superhéroes con inteligencia {inteligencia}: {', '.join(heroes)}")

system("cls")
while True:
    respuesta = int(input("Informacion Superheroes:\n1. Superhéroes de género masculino.\n2. Superhéroes de género femenino.\n3. Superhéroe más alto de género Masculino.\n4. Superhéroe más alto de género Femenino.\n5. Superhéroe más bajo de género Masculino.\n6. Superhéroe más baja de género Femenino.\n7. Altura promedio de los superhéroes de género Masculino.\n8. Altura promedio de los superhéroes de género Fmenino.\n9. Nombre del superhéroe asociado a cada uno de los indicadores de altura por género.\n10. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n11. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n12. Determinar cuántos superhéroes tienen cada tipo de inteligencia.\n13. Listado de superhéroes agrupados por color de ojos.\n14. Listado de superhéroes agrupados por color de pelo.\n15. Listado de superhéroes agrupados por tipo de inteligencia.\n16. Salir \nElija una opción: "))
    match respuesta:
        case 1:
            mostrar_superheroes_masculinos()
        case 2:
            mostrar_superheroes_femeninos()
        case 3:
            mostrar_superheroe_masculino_mas_alto()
        case 4:
            mostrar_superheroe_femenino_mas_alta()
        case 5:
            mostrar_superheroe_masculino_mas_bajo()
        case 6:
            mostrar_superheroe_femenino_mas_baja()
        case 7:
            mostrar_promedio_altura_masculino()
        case 8:
            mostrar_promedio_altura_femenino()
        case 9:
            mostrar_superheroe_mas_alto_mas_bajo_por_genero()
        case 10:
            mostrar_superheroes_por_color_ojos()
        case 11:
            mostrar_superheroes_por_color_pelo()
        case 12:
            mostrar_superheroes_por_inteligencia()
        case 13:
            listado_superheroes_por_color_ojos()
        case 14:
            listado_superheroes_por_color_pelo()
        case 15:
            listado_superheroes_por_inteligencia()
        case 16:
            break
        






# ###A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if personaje['genero'] == "M":
#         print(f"{personaje['nombre']} - {personaje['genero']} ")


# ###B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if personaje['genero'] == "F":
#         print(f"{personaje['nombre']} - {personaje['genero']} ")

# ###C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# mas_alto = 0
# bandera_mas_alto = False

# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if personaje['genero'] == "M":
#         if bandera_mas_alto == False or float(personaje['altura']) > mas_alto:
#             bandera_mas_alto = True
#             mas_alto = float(personaje['altura'])
#             masculino_mas_alto = personaje['nombre']

# print(f"El personaje masculino mas alto es {masculino_mas_alto} con {mas_alto}m")

# ###D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# mas_alta = 0
# bandera_mas_alta = False
# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if personaje['genero'] == "F":        
#         if bandera_mas_alta == False or float(personaje['altura']) > mas_alta:
#             mas_alta = float(personaje['altura'])
#             femenino_mas_alta = personaje['nombre']
#             bandera_mas_alta = True
        
# print(f"La personaje femenino mas alta es {femenino_mas_alta} con {mas_alta}m")

# ###E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# mas_bajo = 0
# bandera_mas_bajo = False

# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if  personaje['genero'] == "M":
#         if bandera_mas_bajo == False or float(personaje['altura']) < mas_bajo:
#             bandera_mas_bajo = True
#             mas_bajo = float(personaje['altura'])
#             masculino_mas_bajo = personaje['nombre']

# print(f"El personaje masculino mas bajo es {masculino_mas_bajo} con {mas_bajo}m")

# ###F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# mas_baja = 0
# bandera_mas_baja = False

# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if personaje['genero'] == "F": # Si el genero del personaje es F
#         if bandera_mas_baja == False or float(personaje['altura']) < mas_baja: # Si cumple la bandera o la altura ingresada es la mas baja
#             bandera_mas_baja = True
#             mas_baja = float(personaje['altura'])
#             femenino_mas_baja = personaje['nombre']

# print(f"La personaje femenino mas baja es {femenino_mas_baja} con {mas_baja}m")

# ###G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# altura_promedio_masculino = 0
# contador_masculino = 0

# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if personaje['genero'] == "M":
#         altura_promedio_masculino += float(personaje['altura'])
#         contador_masculino += 1

# promedio_altura_masculino = altura_promedio_masculino / contador_masculino

# print(f"La altura promedio de los superhéroes de género M es {promedio_altura_masculino: .2f}m")

# ###H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
# altura_promedio_femenino = 0
# contador_femenino = 0

# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if personaje['genero'] == "F":
#         altura_promedio_femenino += float(personaje['altura'])
#         contador_femenino += 1

# promedio_altura_femenino = altura_promedio_femenino / contador_femenino

# print(f"La altura promedio de los superhéroes de género F es {promedio_altura_femenino: .2f}m")

# ###I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     if float(personaje['altura']) == mas_alto:
#         print(f"El superheroe masculino mas alto es {personaje['nombre']} con {float(personaje['altura'])}m")

#     if float(personaje['altura']) == mas_alta:
#         print(f"El superheroe femenino mas alta es {personaje['nombre']} con {float(personaje['altura'])}m")

# ###J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# conteo_ojos = {} # Creamos un diccionario para almacenar el conteo de cada color de ojos

# for personaje in lista_personajes: # Recorremos la lista de superhéroes
#     color_ojos = personaje['color_ojos'] # Obtenemos el color de ojos del superhéroe actual
#     if color_ojos not in conteo_ojos:    
#         conteo_ojos[color_ojos] = 1     # Si el color de ojos no ha sido registrado en el diccionario, lo inicializamos con un conteo de 1
#     else:                                
#         conteo_ojos[color_ojos] += 1    # Si el color de ojos ya ha sido registrado, incrementamos su conteo en 1
        
# for (color, conteo) in conteo_ojos.items(): # Imprimimos el conteo de cada color de ojos (clave, valor)
#     print(f"Hay {conteo} superhéroes con ojos de color {color}.")

# ###K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# conteo_color_pelo = {} #creamos el diccionario para almacenar el conteo de cada tipo de color de pelo

# for personaje in lista_personajes:
#     if  personaje["color_pelo"] == "":
#         color = "No Tiene"
#     else:        
#         color = personaje["color_pelo"]

#     if color in conteo_color_pelo:
#         conteo_color_pelo[color] += 1 # Si el color_pelo no ha sido registrada en el diccionario, la inicializamos con una cantidad de 1
#     else:
#         conteo_color_pelo[color] = 1 # Si el color_pelo ya ha sido registrado, incrementamos su cantidad en 1
        
# for color, conteo in conteo_color_pelo.items():  #(clave, valor)(color es la clave, conteo el valor que toma con ese color de pelo) 
#     print(f"Hay {conteo} superhéroes con el color de pelo {color}") # Se imprime el conteo para cada color de pelo.

# ###L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).

# inteligencias = {}# Inicializar el diccionario de inteligencias

# for personaje in lista_personajes:
#     if personaje['inteligencia'] == '':
#         inteligencia = 'No Tiene'
#     else:
#         inteligencia = personaje['inteligencia']

#     if inteligencia in inteligencias:
#         inteligencias[inteligencia] += 1 # Si la inteligencia no ha sido registrada en el diccionario, la inicializamos con una cantidad de 1
#     else:
#         inteligencias[inteligencia] = 1 # Si la inteligencia ya ha sido registrado, incrementamos su cantidad en 1

# for inteligencia, cantidad in inteligencias.items():
#     print(f"Hay {cantidad} superhéroes con inteligencia {inteligencia}")

# ###M. Listar todos los superhéroes agrupados por color de ojos.
# superheroes_por_color_ojos = {} # Crear diccionario vacío para almacenar héroes por color de ojos

# for superheroe in lista_personajes:  ## Recorrer la lista de héroes y agregarlos al diccionario correspondiente al color de ojos
#     color_ojos = superheroe['color_ojos']
#     if color_ojos not in superheroes_por_color_ojos:
#         superheroes_por_color_ojos[color_ojos] = []
#     superheroes_por_color_ojos[color_ojos].append(superheroe['nombre'])

# for color_ojos, superheroes in superheroes_por_color_ojos.items():  # Imprimir el resultado (color_ojos, superheroe)
#     print(f"Superhéroes con ojos de color {color_ojos}: {', '.join(superheroes)}")


# ###N. Listar todos los superhéroes agrupados por color de pelo.

# heroes_por_pelo = {} # Crear diccionario vacío para almacenar héroes por color de pelo

# for superheroe in lista_personajes: # Recorrer la lista de héroes y agregarlos al diccionario correspondiente al color de pelo
#     pelo = superheroe['color_pelo'] or 'No Tiene'
#     if pelo not in heroes_por_pelo:
#         heroes_por_pelo[pelo] = []
#     heroes_por_pelo[pelo].append(superheroe['nombre'])


# for pelo, heroes in heroes_por_pelo.items():    # Imprimir el resultado
#     print(f"Superhéroes con pelo de color {pelo}: {', '.join(heroes)}")

# #O. Listar todos los superhéroes agrupados por tipo de inteligencia.

# heroes_por_inteligencia = {}    # Crear diccionario vacío para almacenar héroes por tipo de inteligencia

# for heroe in lista_personajes:  # Recorrer la lista de héroes y agregarlos al diccionario correspondiente al tipo de inteligencia
#     inteligencia = heroe['inteligencia'] or 'No Tiene'
#     if inteligencia not in heroes_por_inteligencia:
#         heroes_por_inteligencia[inteligencia] = []
#     heroes_por_inteligencia[inteligencia].append(heroe['nombre'])


# for inteligencia, heroes in heroes_por_inteligencia.items(): # Imprimir el resultado
#     print(f"Superhéroes con inteligencia {inteligencia}: {', '.join(heroes)}")
