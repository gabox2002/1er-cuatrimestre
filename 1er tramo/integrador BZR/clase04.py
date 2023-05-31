from data import lista_bzrp 
from os import system

def mostrar_temas():            #desarrollo de la funcion
    print("Lista de temas: ") 
    for cancion in lista_bzrp:
        print(cancion["title"])

def mostrar_temas_mas_vistas():   
    maximo_vistas = 0   
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if cancion["views"] > maximo_vistas or bandera_primer_tema == False: 
            bandera_primer_tema = True
            maximo_vistas = cancion["views"]

    print("Temas con mayor cantidad de reproducciones")
    for cancion in lista_bzrp:
        if cancion["views"] == maximo_vistas:
            print(f"{cancion['title']} con {maximo_vistas} vistas")

def mostrar_temas_menos_vistas():
    minimo_reproducciones = 0   #para buscar max y min
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if  cancion["views"] < minimo_reproducciones or bandera_primer_tema == False: #si scumple una cosa o la otra
            bandera_primer_tema = True
            minimo_reproducciones = cancion["views"]

    print(f"El minimo de vistas es: {cancion['title']} con {minimo_reproducciones} vistas")

def mostrar_temas_mas_largo():
    maximo_duracion = 0   #para buscar max, cuando busco minimo no inicializarlo
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if cancion["length"] > maximo_duracion or bandera_primer_tema == False: #si se cumple una cosa o la otra
            bandera_primer_tema = True
            maximo_duracion = cancion["length"]

    print("Temas con mayor tiempo de duracion:")
    for cancion in lista_bzrp:
        if cancion["length"] == maximo_duracion:
            print(f"{cancion['title']} - {cancion['length']} seg")

def mostrar_temas_mas_corto():
    minimo_duracion = 0   
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if  cancion["length"] < minimo_duracion or bandera_primer_tema == False: #si se cumple una cosa o la otra
            bandera_primer_tema = True
            minimo_duracion = cancion["length"]

    print("Temas con menor tiempo de duracion:")
    for cancion in lista_bzrp:
        if cancion["length"] == minimo_duracion:
            print(f"{cancion['title']} - {cancion['length']} seg")

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
    6. Mostrar el tema mas largo
    7. Mostrar el tema mas corto
    10. Salir
    Elija una opcion: """))
    match respuesta:
        case 1:
            mostrar_temas()     #llamada de la funcion
        case 2:
            mostrar_temas_mas_vistas()
        case 3:
            mostrar_temas_menos_vistas()
        case 4:
            mostrar_suma_de_reproducciones()
        case 5:
            mostrar_promedio_de_reproducciones()
        case 6:
            mostrar_temas_mas_largo()
        case 7:
            mostrar_temas_mas_corto()
        case 10:
            break
    
