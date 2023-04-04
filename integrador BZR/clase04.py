from data import lista_bzrp 
from os import system

def mostrar_temas():            
    print("Lista de temas: ") 
    for cancion in lista_bzrp:
        print(cancion["title"])

def mostrar_temas_mas_vistas():   
    maximo_reproducciones = 0   
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if cancion["views"] > maximo_reproducciones or bandera_primer_tema == False: 
            bandera_primer_tema = True
            maximo_reproducciones = cancion["views"]

    print("Temas con mayor cantidad de reproducciones")
    for cancion in lista_bzrp:
        if cancion["views"] == maximo_reproducciones:
            print(f"{cancion['title']}")

def mostrar_temas_menos_vistas():
    minimo_reproducciones = 0   #para buscar max y min
    bandera_primer_tema = False

    for cancion in lista_bzrp:
        if  cancion["views"] < minimo_reproducciones or bandera_primer_tema == False: #si scumple una cosa o la otra
            bandera_primer_tema = True
            minimo_reproducciones = cancion["views"]

    print(f"El minimo de vistas es: {minimo_reproducciones}")

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
    respuesta = int(input("\n1. Mostrar temas \n2. Mostrar temas mas vistos \n3. Mostrar temas menos vistos \n4. Mostrar suma de reproducciones \n5. mostrar el promedio de reproducciones \n10. Salir \nElija una opcion: "))
    match respuesta:
        case 1:
            mostrar_temas()
        case 2:
            mostrar_temas_mas_vistas()
        case 3:
            mostrar_temas_menos_vistas()
        case 4:
            mostrar_suma_de_reproducciones()
        case 5:
            mostrar_promedio_de_reproducciones()
        case 10:
            break
    

#print(lista_bzrp[0])
###B: Recorrer la lista imprimiendo por consola el título de cada video
#for cancion in lista_bzrp:  #extraer de lista
#    print(cancion["title"])

###C. Recorrer la lista imprimiendo por consola el título de cada video junto a la cantidad de reproducciones del mismo
#for cancion in lista_bzrp:  #extraer de lista
    #print((type(cancion["tittle"] )))   #str
    #print((type(cancion["views"] )))     #INT como son str + int no se pueden + 
    #print("%s - %d" % (cancion["title"], cancion ["views"]))    # mascaras de C en%s pegar una cadena str y %d decimal

#    print(f"{cancion['title']} - {cancion['views']}")



###D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)

# maximo_reproducciones = 0   #para buscar max, cuando busco minimo inicializarlo
# bandera_primer_tema = False

# for cancion in lista_bzrp:
#     if  cancion["views"] > maximo_reproducciones or bandera_primer_tema == False: #si se cumple una cosa o la otra
#         bandera_primer_tema = True
#         maximo_reproducciones = cancion["views"]

# print(f"El maximo de vistas es: {maximo_reproducciones}")

###E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones (MÍNIMO)
# minimo_reproducciones = 0   #para buscar max y min
# bandera_primer_tema = False

# for cancion in lista_bzrp:
#     if  cancion["views"] < minimo_reproducciones or bandera_primer_tema == False: #si se cumple una cosa o la otra
#         bandera_primer_tema = True
#         minimo_reproducciones = cancion["views"]

# print(f"El minimo de vistas es: {minimo_reproducciones}")

###F. Recorrer la lista y determinar la cantidad total de reproducciones del canal (ACUMULADOR)
# acumulador_reproducciones = 0
# for cancion in lista_bzrp:
#     acumulador_reproducciones += cancion["views"]

# print(f"La suma total de reproducciones del canal es: {acumulador_reproducciones}")

###G. Recorrer la lista y determinar la cantidad promedio de reproducciones que tiene un video (PROMEDIO)
# acumulador_reproducciones = 0
# contador_temas = 0

# for cancion in lista_bzrp:
#     acumulador_reproducciones += cancion["views"]  
#     contador_temas += 1

# promedio_reproducciones = acumulador_reproducciones/contador_temas

# print(f"El promedio de reproducciones del canal es: {(promedio_reproducciones/1000000):.2f} millones de reproducciones")

###H. Informar cual es el Título del vídeo asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO, ACUMULADOR y PROMEDIO)

# maximo_reproducciones = 0   #para buscar max, cuando busco minimo no inicializarlo
# bandera_primer_tema = False

# for cancion in lista_bzrp:
#     if cancion["views"] > maximo_reproducciones or bandera_primer_tema == False: #si se cumple una cosa o la otra
#         bandera_primer_tema = True
#         maximo_reproducciones = cancion["views"]

# print("Temas con mayor cantidad de reproducciones")
# for cancion in lista_bzrp:
#     if cancion["views"] == maximo_reproducciones:
#         print(f"{cancion['title']}")


# minimo_reproducciones = 0   
# bandera_primer_tema = False

# for cancion in lista_bzrp:
#     if  cancion["views"] < minimo_reproducciones or bandera_primer_tema == False: #si se cumple una cosa o la otra
#         bandera_primer_tema = True
#         minimo_reproducciones = cancion["views"]

# print("Temas con menor cantidad de reproducciones")
# for cancion in lista_bzrp:
#     if cancion["views"] == minimo_reproducciones:
#         print(f"{cancion['title']}")


### I. Calcular e informar cual es el video que más y el que menos dura.

### J. Ordenar el código implementando una función para cada uno de los valores informados