from data import lista_bzrp 
from funciones import *
from os import system
'''
{
    'title': 'QUEVEDO || BZRP Music Sessions #52', 
'views': 227192970, 
'length': 204, 
'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 
'date': '2022-07-06 00:00:00'
}
'''

def calcular_maximo(lista:list, clave:str)->int:
    maximo = 0   
    bandera_primer_tema = False

    if(type(lista) == list and len(lista) > 0 and type(clave) == str):
        for cancion in lista:
            if cancion[clave] > maximo or bandera_primer_tema == False: 
                bandera_primer_tema = True
                maximo= cancion[clave]

    return maximo



def mostrar_temas_mas_vistas(lista:list):   
    maximo_reproducciones = calcular_maximo(lista, "views")

    if(maximo_reproducciones != 0):
        print("Temas con mayor cantidad de reproducciones")
        for cancion in lista:
            if cancion["views"] == maximo_reproducciones:
                mostrar_video(cancion)

    else:
        print("Error, no hay temas con mayor cantidad de reproducciones")

def mostrar_tema_mas_largo(lista:list):
    maximo_largo = calcular_maximo(lista, "length")

    print(f"Tema con mayor duración")
    for cancion in lista:
        if cancion["length"] == maximo_largo:
            mostrar_video(cancion)








def mostrar_temas_menos_vistas():
    minimo_reproducciones = 0   #para buscar max y min
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if  cancion["views"] < minimo_reproducciones or bandera_primer_tema == False: #si scumple una cosa o la otra
            bandera_primer_tema = True
            minimo_reproducciones = cancion["views"]

    print(f"El minimo de vistas es: {minimo_reproducciones}")
    for cancion in lista_bzrp:
        if  cancion["views"] == minimo_reproducciones:
            # print(f"{cancion['title']}")
            mostrar_video(cancion)

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
    respuesta = int(input("\n1. Mostrar temas \n2. Mostrar temas mas vistos \n3. Mostrar temas menos vistos \n4. Mostrar suma de reproducciones \n5. Mostrar el promedio de reproducciones \n6. Mostrar el tema mas largo\n10. Salir \nElija una opcion: "))
    match respuesta:
        case 1:
            mostrar_temas(lista_bzrp)
        case 2:
            mostrar_temas_mas_vistas(lista_bzrp)
        case 3:
            mostrar_temas_menos_vistas()
        case 4:
            mostrar_suma_de_reproducciones()
        case 5:
            mostrar_promedio_de_reproducciones()
        case 6:
            mostrar_tema_mas_largo(lista_bzrp)
        case 10:
            break
    