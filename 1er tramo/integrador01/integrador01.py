#Gabriel Quispe Integrador 01 Div C Grupo 3
from data_stark import lista_personajes
from os import system

def imprimir_heroes_genero(genero):
    '''
    Funcion que toma como parametro "genero" y recorre la lista_personaje,
    imprimiendo el nombre de cada superheroe cuyo genero coincida con el parametro "genero". 
    '''
    for heroe in lista_personajes:
        if heroe["genero"] == genero:
            print(f"{heroe['nombre']} - {heroe['identidad']}")

def encontrar_heroe_extremo(genero, extremo):
    '''
     Función que toma dos parametros: genero y extremo. El parametro "genero" especifica el genero del superheroe
     que se está buscando, y el parametro "extremo" para especificar "alto" o "bajo" para definir los extremos de las alturas. 
     Utiliza dos estructuras condicionales para determinar si la altura del heroe actual es mayor o menor que la altura maxima o mínima encontrada 
     hasta el momento y la función imprime el nombre y la altura del heroe extremos.
    '''
    
    altura_extrema = None    #inicializamos None para almacenar la info del del heroe con la altura mas extrema
    mas_alto = 0
    mas_bajo = 0    
    bandera_mas_bajo = False

    for heroe in lista_personajes:      #recorre la lista
        if heroe["genero"] == genero:    #verifica si el género del héroe coincide con el género que se está buscando
            altura = float(heroe["altura"])
            if altura > mas_alto and extremo == "alto":
                mas_alto = altura
                altura_extrema = heroe
                
            if bandera_mas_bajo == False or altura < mas_bajo and extremo == "bajo":
                bandera_mas_bajo = True
                mas_bajo = altura
                altura_extrema = heroe
                
    if altura_extrema is None:
        print(f"No se encontraron superheroes de genero {genero}")
    else:
        print(f"El heroe más {extremo} de genero {genero} es {altura_extrema['nombre']} con una altura de {altura_extrema['altura']}.")

def definir_altura_promedio(alturas):
    '''
    Funcion que toma como argumento las alturas, y devuelve el promedio de alturas 
    '''
    total_alturas = sum(alturas)
    promedio = total_alturas / len(alturas)
    return promedio

def promediar_altura_por_genero(genero):
    '''
    Funcion que toma como argumentos el género ("M" o "F"), crea una lista de alturas para ese genero y llama a la funcion "definir_altura_promedio" para calcular el promedio.
    '''
    alturas_genero = []
    for heroe in lista_personajes:
        if heroe["genero"] == genero:
            alturas_genero.append(float(heroe["altura"]))
    promedio = definir_altura_promedio(alturas_genero)
    print(f"El promedio de alturas de género {genero} es: {promedio:.2f}")
    
def contar_atributo(lista_personajes, atributo):
    '''
    Funcion que recibe una lista de diccionarios "lista_personajes" y un atributo "atributo"
    y devuelve un diccionario que cuenta cuantos personajes tienen cada valor para ese atributo en la lista. 
    Si el atributo no está presente en el diccionario del personaje o su valor es una cadena vacia, 
    se asigna la cadena 'No Tiene'.
    '''
    contador = {}
    #primero se verifica si el atributo está presente en el diccionario del personaje y si su valor no es una cadena vacía, utilizando el operador in y la comparación != ''. Si se cumple esta condición, se asigna el valor del atributo a la variable valor. De lo contrario, se asigna la cadena 'No Tiene'.
    for personaje in lista_personajes:
        if atributo in personaje and personaje[atributo] != '':
            valor = personaje[atributo]
        else:
            valor = 'No Tiene'
        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1
    return contador

def contar_por_color_ojos(lista_personajes):
    '''
    La función llama a "contar_atributo" con la lista de personajes y el atributo 'color_ojos' 
    y luego imprime el diccionario de resultados.
    '''
    resultados = contar_atributo(lista_personajes, 'color_ojos')
    print(resultados)

def contar_por_color_pelo(lista_personajes):
    '''
    La función llama a "contar_atributo" con la lista de personajes y el atributo 'color_pelo' 
    y luego imprime el diccionario de resultados.
    '''
    resultados = contar_atributo(lista_personajes, 'color_pelo')
    print(resultados)

def contar_por_inteligencia(lista_personajes):
    '''
    La función llama a "contar_atributo" con la lista de personajes y el atributo 'inteligencia' 
    y luego imprime el diccionario de resultados.
    '''
    resultados = contar_atributo(lista_personajes, 'inteligencia')
    print(resultados)

def agrupar_por_atributo(lista_personajes, atributo):
    '''
    La función recibe una lista de personajes lista_personajes y un atributo atributo. Crea un diccionario agrupados donde se almacenará el grupo de personajes por atributo. 
    Luego, itera por cada personaje en la lista lista_personajes y verifica si el atributo existe en el diccionario del personaje y si su valor no es una cadena vacía. 
    Si se cumple esta condición, se asigna el valor del atributo a la variable valor. De lo contrario, se asigna la cadena 'No Tiene'. 
    A continuación, verifica si valor ya existe en agrupados. Si es así, agrega el personaje a la lista de personajes agrupados bajo ese valor. 
    De lo contrario, crea una nueva entrada en el diccionario agrupados para el valor valor y agrega el personaje a la lista de personajes agrupados bajo ese valor. 
    Finalmente, devuelve el diccionario agrupados.
    '''
    agrupados = {}
    for personaje in lista_personajes:
        if atributo in personaje and personaje[atributo] != '':
            valor = personaje[atributo]
        else:
            valor = 'No Tiene'
        if valor in agrupados:
            agrupados[valor].append(personaje)
        else:
            agrupados[valor] = [personaje]
    return agrupados

def listar_heroes_por_color_ojos(lista_personajes):
    '''
    La función recibe una lista de personajes lista_personajes. 
    Utiliza la función agrupar_por_atributo() para agrupar los personajes por color de ojos y luego itera sobre el diccionario resultante. 
    Imprime cada color de ojos y luego itera sobre la lista de personajes para ese color de ojos e imprime el nombre del héroe.
    '''
    agrupados = agrupar_por_atributo(lista_personajes, 'color_ojos')
    for color, heroes in agrupados.items():
        print(f"Color de ojos: {color}")
        for heroe in heroes:
            print(f"\t{heroe['nombre']}")

def listar_heroes_por_color_pelo(lista_personajes):
    '''
    La función recibe una lista de personajes lista_personajes. 
    Utiliza la función agrupar_por_atributo() para agrupar los personajes por color de pelo y luego itera sobre el diccionario resultante. 
    Imprime cada color de pelo y luego itera sobre la lista de personajes para ese color de pelo e imprime el nombre del héroe.
    '''
    agrupados = agrupar_por_atributo(lista_personajes, 'color_pelo')
    for color, heroes in agrupados.items():
        print(f"Color de pelo: {color}")
        for heroe in heroes:
            print(f"\t{heroe['nombre']}")

def listar_heroes_por_inteligencia(lista_personajes):
    '''
    La función recibe una lista de personajes lista_personajes. 
    Utiliza la función agrupar_por_atributo() para agrupar los personajes por tipo de inteligencia y luego itera sobre el diccionario resultante. 
    Imprime cada tipo de inteligencia y luego itera sobre la lista de personajes para ese tipo de inteligencia e imprime el nombre del héroe.
    '''
    agrupados = agrupar_por_atributo(lista_personajes, 'inteligencia')
    for tipo, heroes in agrupados.items():
        print(f"Tipo de inteligencia: {tipo}")
        for heroe in heroes:
            print(f"\t{heroe['nombre']}")

system("cls")
while True:
    respuesta = int(input('''Menu de superheroes:
    1. Imprimir héroes de género M
    2. Imprimir héroes de género F
    3. Encontrar héroe más alto de género M
    4. Encontrar héroe más alto de género F
    5. Encontrar héroe más bajo de género M
    6. Encontrar héroe más bajo de género F
    7. Promedio de alturas genero Masculino
    8. Promedio de alturas genero Femenino
    9. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    10. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    11. Determinar cuántos superhéroes tienen cada tipo de inteligencia
    12. Listar todos los superhéroes agrupados por color de ojos.
    13. Listar todos los superhéroes agrupados por color de pelo.
    14. Listar todos los superhéroes agrupados por tipo de inteligencia
    15. Salir \nEscoja una opcion: '''))
    match respuesta:
        case 1:
            imprimir_heroes_genero("M")
        case 2:
            imprimir_heroes_genero("F")
        case 3:
            encontrar_heroe_extremo("M", "alto")
        case 4:
            encontrar_heroe_extremo("F", "alto")
        case 5:
            encontrar_heroe_extremo("M", "bajo")
        case 6:
            encontrar_heroe_extremo("F", "bajo")
        case 7:
            promediar_altura_por_genero("M")
        case 8:
            promediar_altura_por_genero("F")
        case 9: 
            contar_por_color_ojos(lista_personajes)
        case 10:
            contar_por_color_pelo(lista_personajes)
        case 11:
            contar_por_inteligencia(lista_personajes)
        case 12:
            listar_heroes_por_color_ojos(lista_personajes)
        case 13:
            listar_heroes_por_color_pelo(lista_personajes)
        case 14:
            listar_heroes_por_inteligencia(lista_personajes)
        case 15:
            break
          

