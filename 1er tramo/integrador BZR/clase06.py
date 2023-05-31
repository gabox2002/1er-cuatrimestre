from data import lista_bzrp 
#from funciones import   *  # el asterisco es para traer todo
from os import system

'''
{'title': 'QUEVEDO || BZRP Music Sessions #52', 
'views': 227192970, 
'length': 204, 
'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 
'date': '2022-07-06 00:00:00'}

'''

# en funciones.py
def mostrar_temas(lista_bzrp:list, clave:str = "", valor: int = 0):            #parametros opcionales
    print("Lista de temas: ") 

    if (clave != "" and valor != 0):
        for cancion in lista_bzrp:
            if cancion[clave] == valor:
                mostrar_video(cancion)
    else:                                                   #si los parametros vienen sin nada, muestro por default
        for cancion in lista_bzrp:   
            mostrar_video(cancion)


def mostrar_video(un_video:dict):
    print(f"Titulo: {un_video['title']}, - ",
          f"Vistas: {un_video['views']/1000000} - ",
          f"Tiempo: {un_video['length']/60}min")  #uso de interpolado

# def mostrar_algunos_temas(lista_bzrp:list, clave:str, valor:int):
#     for cancion in lista_bzrp:
#             if cancion[clave] == valor:
#                 mostrar_video(cancion)


def calcular_maximo(lista:list, clave:str)->int:
    maximo = 0   
    bandera_primer_tema = False

    if(type(lista) == list and len(lista) > 0 and type(clave) == str):
        for cancion in lista:
            if cancion[clave] > maximo or bandera_primer_tema == False:
                bandera_primer_tema = True
                maximo = cancion[clave]
    return maximo

def mostrar_temas_mas_vistas(lista:list):   
    maximo_reproducciones = calcular_maximo(lista, "views")
    
    if (maximo_reproducciones != 0):
        print("Temas con mayor cantidad de reproducciones")
        mostrar_temas(lista, "views", maximo_reproducciones)

    else:
        print("Ocurrio un error!")

def calcular_minimo(lista:list, clave:str)->int:
    minimo = 0   #para buscar max y min
    bandera_primer_tema = False

    for cancion in lista:
        if  cancion[clave] < minimo or bandera_primer_tema == False: #si scumple una cosa o la otra
            bandera_primer_tema = True
            minimo = cancion[clave]
    return minimo

def mostrar_temas_menos_vistas(lista:list):
    minimo_reproducciones = calcular_minimo(lista, "views")
    print("Temas con menor cantidad de reproducciones")

    mostrar_temas(lista, "views", minimo_reproducciones)

def mostrar_tema_mas_largo(lista:list):
    maximo_largo = calcular_maximo(lista, "length")   #reutilizando codigo
    print("Temas con mas duracion")

    mostrar_temas(lista, "length", maximo_largo) #reutilizando

def mostrar_suma_de_reproducciones():
    acumulador_reproducciones = 0
    for cancion in lista_bzrp:
            acumulador_reproducciones += cancion["views"]

    print(f"La suma total de reproducciones del canal es: {acumulador_reproducciones}")
    
def mostrar_promedio_de_reproducciones():
    acumulador_reproducciones = 0
    contador_temas = 0

    for cancion in lista_bzrp:
        acumulador_reproducciones += cancion["views"]  
        contador_temas += 1

    promedio_reproducciones = acumulador_reproducciones/contador_temas

    print(f"El promedio de reproducciones del canal es: {(promedio_reproducciones/1000000):.2f} millones de reproducciones")

system("cls") 
while True:      
    respuesta = int(input("""
        1. Mostrar temas
        2. Mostrar temas mas vistos
        3. Mostrar temas menos vistos
        4. Mostrar suma de reproducciones
        5. Mostrar el promedio de reproducciones
        6. Mostrar tema mas largo
        10. Salir
        Elija una opcion: """))
    match respuesta:
        case 1:
            mostrar_temas(lista_bzrp)
        case 2:
            mostrar_temas_mas_vistas(lista_bzrp)
        case 3:
            mostrar_temas_menos_vistas(lista_bzrp)
        case 4:
            mostrar_suma_de_reproducciones()
        case 5:
            mostrar_promedio_de_reproducciones()
        case 6:
            mostrar_tema_mas_largo(lista_bzrp)
        case 10:
            break
    
