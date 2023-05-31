from data import lista_bzrp 
from funciones import *
from os import system
'''
    'title': 'Bizarrap x Duki x Nicki Nicole - YaMeFui'
{
    'title': 'QUEVEDO || BZRP Music Sessions #52', 
    'title': 'Bizarrap x Duki x Nicki Nicole - YaMeFui'
    'title': 'ECKO || BZRP Freestyle & Music Session'
    'views': 227192970, 
    'length': 204, 
    'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
    'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 
    'date': '2022-07-06 00:00:00'
}
'''
# Necesitamos que tenga la lista este nuevo Formato:

# Tipo : BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duración: 204 segundos
# Codigo: A_g3lMcWVy0
# Fecha de carga: 6/7/2022
# Hora de carga: 00:00



#normalizar cadena
def prueba():    #PARSER DE UNA CADENA
    titulo = "QUEVEDO || BZRP Music Sessions #52"
    parte1 = titulo.split('||')   #['QUEVEDO ', ' BZRP Music Sessions #52']
    artista = parte1[0].strip()
    parte2 = parte1[1].split('#')  #[' BZRP Music Sessions ', '52']
    tipo = parte2[0].strip()
    tipo = tipo.upper()
    numero = parte2[1]
       
    print(f"out: {artista}-{numero}-{tipo}")     #out: QUEVEDO-52-BZRP MUSIC SESSIONS


'''
'title': 'QUEVEDO || BZRP Music Sessions #52'
'title': 'Bizarrap x Duki x Nicki Nicole - YaMeFui'
'title': 'ECKO || BZRP Freestyle & Music Session'
'''
def prueba1(titulo:str):    #PARAMETRIZANDO EL TITULO formateo por sessiones
    parte1 = titulo.split('||')   #['QUEVEDO ', ' BZRP Music Sessions #52']
    if(len(parte1) >1):                 #si se puede dividir en mas de 1
        artista = parte1[0].strip()
        parte2 = parte1[1].split('#')  #[' BZRP Music Sessions ', '52']
        if(len(parte2) >1):
            tipo = parte2[0].strip()
            tipo = tipo.upper()
            numero = parte2[1]
    
            print(f"out: {artista}-{numero}-{tipo}")  

'''
'title': 'QUEVEDO || BZRP Music Sessions #52'
'title': 'Bizarrap x Duki x Nicki Nicole - YaMeFui'
'title': 'ECKO || BZRP Freestyle & Music Session'
'''
#otra forma de obtener las sesiones
def prueba2(titulo:str): #Formateo por sesiones
    parte1 = titulo.split('BZRP Music Sessions')
    if(len(parte1) == 2):                                #si lo pudo separar en 2
        artista = parte1[0].replace("||", "").strip()
        tipo = "BZRP MUSIC SESSIONS"
        numero = parte1[1].replace("#", "").strip()
        print(f"{artista} - {numero} - {tipo}")

# NICKI NICOLE - 13 - BZRP MUSIC SESSIONS
# MESITA - 12 - BZRP MUSIC SESSIONS
# KIDDO TOTO - 11 - BZRP MUSIC SESSIONS
# FRIJO - 10 - BZRP MUSIC SESSIONS



#'url': 'https://youtube.com/watch?v=A_g3lMcWVy0'
#        1234567890123456789012345678

def prueba3(url:str):   #Formateo por URL 
    #opcion 1
    # lista = url.split("=")
    # print(lista[1])
    
    #opcion 2
    # codigo = url[28:]
    # print(codigo)

    #opcion 3
    indice = url.index("=") #a partir de este indice mas 1 caracter para ver el codigo
    codigo = url[indice+1:]

    print(codigo)



# Fecha de carga: 6/7/2022
# Hora de carga: 00:00

#'date': '2022-07-06 00:00:00'
def prueba4(fecha:str)-> str:     #formateo la fecha con nuevo formato
    fecha_split = fecha.split(" ")
    fecha_formato = fecha_split[0].split("-")
    año = fecha_formato[0]
    mes = fecha_formato[1]
    dia = fecha_formato[2]
    
    formato = "/"
    otra_fecha = formato.join([dia,mes,año])

    # fecha_formato = fecha_split[1].split(":")
    # hora = fecha_formato[0]
    # min = fecha_formato[1]

    # formato = ":"
    # mostrar_hora = formato.join([hora, min])

    
    return otra_fecha  
    # return mostrar_hora
  



def formatear_titulo(lista:list): #PARAMETRIZANDO  Recibe una lista
    for tema in lista:
        # prueba2(tema["title"])

        # prueba3(tema["url"])

        fecha = prueba4(tema['date'])
        print(fecha)



    
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
    respuesta = int(input("\n1. Mostrar temas \n2. Mostrar temas mas vistos \n3. Mostrar temas menos vistos \n4. Mostrar suma de reproducciones \n5. Mostrar el promedio de reproducciones \n6. Mostrar el tema mas largo\n7. Formatear titulo\n10. Salir \nElija una opcion: "))
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

        case 7:
            formatear_titulo(lista_bzrp)
                
        case 10:
            break
    