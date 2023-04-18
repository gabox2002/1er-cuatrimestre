from data_stark import lista_personajes
from os import system

'''
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''
def listar_superheroes(lista_personajes:list, clave:str = "", valor: int = 0):
    print("Lista de superheroes: ") 

    if (clave != "" and valor != ""):
        for personaje in lista_personajes: # Recorremos la lista de superhéroes
            if personaje[clave] == valor:
                mostrar_superheroe(personaje)
    else: 
        for personaje in lista_personajes: 
            mostrar_superheroe(personaje)

def mostrar_superheroe(superheroe:dict):
        print(f"Nombre: {superheroe['nombre']}, -",
              f"Genero: {superheroe['genero']} -",
              f"Altura: {float(superheroe['altura'])}m, -",
              f"Peso: {float(superheroe['peso'])}kg") 

       

def calcular_maximo(lista:list, clave:str)->int:
    maximo = 0
    bandera_mas_alto = False
    
    if(type(lista) == list and len(lista) > 0 and type(clave) == str):
        for personaje in lista:                              # Recorremos la lista de superhéroes
            if personaje[clave] > maximo or bandera_mas_alto == False:
                bandera_mas_alto = True
                maximo = personaje[clave]
                
        return maximo


def mostrar_superheroes_masculinos():
    print(f"Los superheroes masculinos son: ")
    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "M":
            mostrar_superheroe(personaje)

def mostrar_superheroes_femeninos():
    print(f"Los superheroes femeninos son: ")
    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "F":
            mostrar_superheroe(personaje)

def mostrar_superheroe_masculino_mas_alto(lista:list):    
    # for personaje in lista_personajes: # Recorremos la lista de superhéroes
    #     if personaje['genero'] == "M":  
    masculino_mas_alto = calcular_maximo(lista, "altura")
    
    if (masculino_mas_alto != 0):
        print("El personaje masculino mas alto es: ")
        listar_superheroes(lista, "altura", masculino_mas_alto)
    else:
        print("Ocurrio un error!")


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

    print(f"La altura promedio de los superhéroes masculinos es {promedio_altura_masculino: .2f}")

def mostrar_promedio_altura_femenino():
    altura_promedio_femenino = 0
    contador_femenino = 0

    for personaje in lista_personajes: # Recorremos la lista de superhéroes
        if personaje['genero'] == "F":
            altura_promedio_femenino += float(personaje['altura'])
            contador_femenino += 1

    promedio_altura_femenino = altura_promedio_femenino / contador_femenino

    print(f"La altura promedio de los superhéroes femeninos es {promedio_altura_femenino: .2f}")

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
    print(f"y el mas bajo es {masculino_mas_bajo} con {mas_bajo}")
    print(f"La superheroe femenina mas alta es {femenino_mas_alta} con {mas_alta}")
    print(f"y la mas baja es {femenino_mas_baja} con {mas_baja}")

def mostrar_cantidad_superheroes_por_color_ojos():  
    contador_ojos_brown = 0
    contador_ojos_blue = 0  
    contador_ojos_green = 0
    contador_ojos_yellow_sin_irises = 0
    contador_ojos_yellow = 0      
    contador_ojos_hazel = 0
    contador_ojos_silver = 0
    contador_ojos_red = 0
    
    for personaje in lista_personajes:
        if personaje['color_ojos'] == "Brown":
            contador_ojos_brown += 1
        elif personaje['color_ojos'] == "Blue" or personaje['color_ojos'] == "blue":
            contador_ojos_blue += 1
        elif personaje['color_ojos'] == "Green":
            contador_ojos_green += 1
        elif personaje['color_ojos'] == "Yellow (without irises)":
            contador_ojos_yellow_sin_irises += 1
        elif personaje['color_ojos'] == "Yellow":
            contador_ojos_yellow += 1
        elif personaje['color_ojos'] == "Hazel":
            contador_ojos_hazel += 1
        elif personaje['color_ojos'] == "Silver":
            contador_ojos_silver += 1
        elif personaje['color_ojos'] == "Red":
            contador_ojos_red += 1

    print(f"La cantidad de superheroes por tipo de color de ojos es:")
    print(f"- Brown: {contador_ojos_brown}")
    print(f"- Blue: {contador_ojos_blue}")
    print(f"- Green: {contador_ojos_green}")
    print(f"- Yellow (without irises): {contador_ojos_yellow_sin_irises}")
    print(f"- Yellow: {contador_ojos_yellow}")
    print(f"- Hazel: {contador_ojos_hazel}")
    print(f"- Silver: {contador_ojos_silver}")
    print(f"- Red: {contador_ojos_red}")

def mostrar_cantidad_superheroes_por_color_pelo():
    contador_pelo_yellow = 0
    contador_pelo_brown = 0
    contador_pelo_black = 0
    contador_pelo_auburn = 0
    contador_pelo_red_orange = 0
    contador_pelo_white = 0
    contador_pelo_no_hair = 0
    contador_pelo_blond = 0
    contador_pelo_green = 0
    contador_pelo_red = 0
    contador_pelo_brown_white = 0
    
    for personaje in lista_personajes:
        if personaje['color_pelo'] == "Yellow":
            contador_pelo_yellow += 1
        elif personaje['color_pelo'] == "Brown":
            contador_pelo_brown += 1
        elif personaje['color_pelo'] == "Black": 
            contador_pelo_black += 1
        elif personaje['color_pelo'] == "Auburn":
            contador_pelo_auburn += 1
        elif personaje['color_pelo'] == "Red / Orange":
            contador_pelo_red_orange += 1
        elif personaje['color_pelo'] == "White":
            contador_pelo_white += 1
        elif personaje['color_pelo'] == "No Hair" or personaje['color_pelo'] == "":
            contador_pelo_no_hair += 1
        elif personaje['color_pelo'] == "Blond" or personaje['color_pelo'] == "blond":
            contador_pelo_blond += 1
        elif personaje['color_pelo'] == "Green":
            contador_pelo_green += 1
        elif personaje['color_pelo'] == "Red":
            contador_pelo_red += 1
        elif personaje['color_pelo'] == "Brown / White":
            contador_pelo_brown_white += 1

    print(f"La cantidad de superheroes por tipo de color de pelo es: ")
    print(f"- Yellow: {contador_pelo_yellow}")
    print(f"- Brown: {contador_pelo_brown}")
    print(f"- Black: {contador_pelo_black}")
    print(f"- Auburn: {contador_pelo_auburn}")
    print(f"- Red / Orange: {contador_pelo_red_orange}")
    print(f"- White: {contador_pelo_white}")
    print(f"- No Hair: {contador_pelo_no_hair}")
    print(f"- Blond: {contador_pelo_blond}")
    print(f"- Green: {contador_pelo_green}")
    print(f"- Red: {contador_pelo_red}")
    print(f"- Brown / White: {contador_pelo_brown_white}")

def mostrar_cantidad_superheroes_por_inteligencia():
    contador_inteligencia_good = 0
    contador_inteligencia_high = 0
    contador_inteligencia_average = 0
    contador_inteligencia_no_tiene = 0
    
    for personaje in lista_personajes:
        if personaje['inteligencia'] == "good":
            contador_inteligencia_good += 1
        if personaje['inteligencia'] == "high":
            contador_inteligencia_high += 1
        if personaje['inteligencia'] == "average":
            contador_inteligencia_average += 1
        if personaje['inteligencia'] == "":
            contador_inteligencia_no_tiene += 1

    print(f"La cantidad de superheroes por nivel de inteligencia es: ")
    print(f"- Good: {contador_inteligencia_good}")
    print(f"- High: {contador_inteligencia_high}")
    print(f"- Average: {contador_inteligencia_average}")
    print(f"- No tiene nivel de Inteligencia : {contador_inteligencia_no_tiene}")

def listar_superheroes_por_color_ojos():
    #crear un diccionario para mostrar superheroes por color de ojos
    lista_color_ojos = {"Brown": [], "Blue": [], "Green": [], "Yellow (without irises)": [], 
                        "Yellow": [], "Hazel": [], "Silver": [], "Red": []} 
    ## Iterar a través de la lista de personajes y agregar a la lista correspondiente al color de ojos
    for personaje in lista_personajes:    
        if personaje['color_ojos'] == "Brown":
            lista_color_ojos["Brown"].append(personaje)
        elif personaje["color_ojos"] == "Blue" or personaje["color_ojos"] == "blue":
            lista_color_ojos["Blue"].append(personaje)
        elif personaje["color_ojos"] == "Green":
            lista_color_ojos["Green"].append(personaje)
        elif personaje["color_ojos"] == "Yellow (without irises)":
            lista_color_ojos["Yellow (without irises)"].append(personaje)
        elif personaje['color_ojos'] == "Yellow":
            lista_color_ojos["Yellow"].append(personaje)
        elif personaje["color_ojos"] == "Hazel":
            lista_color_ojos["Hazel"].append(personaje)
        elif personaje["color_ojos"] == "Silver":
            lista_color_ojos["Silver"].append(personaje)
        elif personaje["color_ojos"] == "Red":
            lista_color_ojos["Red"].append(personaje)
    
    print("Listado de superheroes agrupados por color de ojos: ")        
    for color in lista_color_ojos:        
        print("-" + color + ":")
        for personaje in lista_color_ojos[color]:
            print("    " + personaje["nombre"])
        
def listar_superheroes_por_color_pelo():

    # Crear diccionario vacío para almacenar héroes por color de pelo
    lista_color_pelo = {"Yellow": [], "Brown": [], "White": [], "Auburn": [], "Red / Orange": [], "Red": [],
                        "Black": [], "Green": [], "No Hair": [], "Blond": [], "Brown / White": []} 
    ## Iterar a través de la lista de personajes y agregar a la lista correspondiente al color de ojos
    for personaje in lista_personajes:    
        if personaje['color_pelo'] == "Yellow":
            lista_color_pelo["Yellow"].append(personaje)
        elif personaje['color_pelo'] == "Brown":
            lista_color_pelo["Brown"].append(personaje)
        elif personaje['color_pelo'] == "Auburn":
            lista_color_pelo["Auburn"].append(personaje)
        elif personaje['color_pelo'] == "Red / Orange":
            lista_color_pelo["Red / Orange"].append(personaje)
        elif personaje["color_pelo"] == "White":
            lista_color_pelo["White"].append(personaje)
        elif personaje["color_pelo"] == "Black":
            lista_color_pelo["Black"].append(personaje)
        elif personaje["color_pelo"] == "Green":
            lista_color_pelo["Green"].append(personaje)
        elif personaje["color_pelo"] == "Brown / White":
            lista_color_pelo["Brown / White"].append(personaje)
        elif personaje["color_pelo"] == "No Hair" or personaje["color_pelo"] == "":
            lista_color_pelo["No Hair"].append(personaje)
        elif personaje['color_pelo'] == "Blond" or personaje['color_pelo'] == "blond":
            lista_color_pelo["Blond"].append(personaje)
        elif personaje["color_pelo"] == "Red":
            lista_color_pelo["Red"].append(personaje)
    
    print("Listado de superheroes agrupados por color de pelo: ")        
    for color in lista_color_pelo:        
        print("-" + color + ":")
        for personaje in lista_color_pelo[color]:
            print("    " + personaje["nombre"])

def listar_superheroes_por_inteligencia():
    #Crear diccionario vacío para almacenar héroes por tipo de inteligencia
    lista_inteligencia = {"High": [], "Good": [], "Average": [], "No tiene": []} 
    ## Iterar a través de la lista de personajes y agregar a la lista correspondiente a la inteligencia
    for personaje in lista_personajes:  
        if personaje['inteligencia'] == "high":
            lista_inteligencia["High"].append(personaje)
        elif personaje['inteligencia'] == "good":
            lista_inteligencia["Good"].append(personaje)
        elif personaje['inteligencia'] == "average":
            lista_inteligencia["Average"].append(personaje)
        elif personaje['inteligencia'] == "":
            lista_inteligencia["No tiene"].append(personaje)
    
    print("Listado de superheroes agrupados por nivel de inteligencia: ")        
    for inteligencia in lista_inteligencia:        
        print("-" + inteligencia + ":")
        for personaje in lista_inteligencia[inteligencia]:
            print("    " + personaje["nombre"])

system("cls")
while True:
    respuesta = int(input("""Informacion Superheroes:
    0. Mostrar superheroes
    1. Superhéroes de género masculino.
    2. Superhéroes de género femenino.
    3. Superhéroe más alto de género Masculino.
    4. Superhéroe más alto de género Femenino.
    5. Superhéroe más bajo de género Masculino.
    6. Superhéroe más baja de género Femenino.
    7. Altura promedio de los superhéroes de género Masculino.
    8. Altura promedio de los superhéroes de género Fmenino.
    9. Nombre del superhéroe asociado a cada uno de los indicadores de altura por género.
    10. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    11. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    12. Determinar cuántos superhéroes tienen cada tipo de inteligencia.
    13. Listado de superhéroes agrupados por color de ojos.
    14. Listado de superhéroes agrupados por color de pelo.
    15. Listado de superhéroes agrupados por tipo de inteligencia.
    16. Salir \nElija una opción: """))
    match respuesta:
        case 0:
            listar_superheroes(lista_personajes)
        case 1:
            mostrar_superheroes_masculinos()
        case 2:
            mostrar_superheroes_femeninos()
        case 3:
            mostrar_superheroe_masculino_mas_alto(lista_personajes)
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
            mostrar_cantidad_superheroes_por_color_ojos()
        case 11:
            mostrar_cantidad_superheroes_por_color_pelo()
        case 12:
            mostrar_cantidad_superheroes_por_inteligencia()
        case 13:
            listar_superheroes_por_color_ojos()
        case 14:
            listar_superheroes_por_color_pelo()
        case 15:
            listar_superheroes_por_inteligencia()
        case 16:
            break
        
