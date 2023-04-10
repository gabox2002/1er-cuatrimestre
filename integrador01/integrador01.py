from data_stark import lista_personajes
from os import system





system("cls")
#while True:

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

####K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
#conteo_color_pelo = {} #creamos el diccionario para almacenar el conteo de cada tipo de color de pelo

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

###M. Listar todos los superhéroes agrupados por color de ojos.
superheroes_por_color_ojos = {}

for personaje in lista_personajes:
    color_ojos = personaje['color_ojos']
    print(f"Superhéroes con ojos de color {color_ojos}:")
    if color_ojos not in superheroes_por_color_ojos:
        superheroes_por_color_ojos[color_ojos] = []
    superheroes_por_color_ojos[color_ojos].append(personaje)

    print("- " + personaje["nombre"])

# for color in superheroes_por_color_ojos:
#     print(f"Superhéroes con ojos de color {color}:")
#     for personaje in lista_personajes:
#         if personaje["color_ojos"] == color:
#             print("- " + personaje["nombre"])
#     print("\n") # salto de línea para separar cada grupo de superhéroes