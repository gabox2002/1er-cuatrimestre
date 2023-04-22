from os import system

animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 9, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 23, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 1, "personaje_principal": "Shinji Ikari"}
]

'''
1-Generar una sublista de los animes estrenados antes de 1995:
2-Generar una sublista de los animes con más de 1 temporada:
3-Buscar en la lista el anime con nombre "Pokemon" e imprimir su año de estreno:
4-Crear un nuevo diccionario con los nombres y años de estreno de los animes de la lista:
'''


'''
{"temporadas": 1, "nombre": "Evangelion", "Digimon Adventure"}
'''
system("cls")

nuevo_diccionario = {}
print(nuevo_diccionario)
for anime in animes_90s:
    if "temporadas" not in nuevo_diccionario:   
        #primera vez que doy la primera vuelta, si no existe, creo esta clave
        nueva_lista = []
        nueva_lista.append(anime["nombre"])
        nuevo_diccionario["temporadas"] = anime["temporadas"]
        nuevo_diccionario["nombres"] = nueva_lista

    elif nuevo_diccionario["temporadas"] == anime["temporadas"]:
        #seunda vez
        nuevo_diccionario["nombres"].append(anime["nombre"])

    
print(nuevo_diccionario)



# 1-Generar una sublista de los animes estrenados antes de 1995:
animes_antes_95 = [anime for anime in animes_90s if anime['año'] < 1995]
print("Animes estrenados antes de 1995: ", animes_antes_95)

# 2-Generar una sublista de los animes con más de 1 temporada:
animes_mas_de_1_temporada = [anime for anime in animes_90s if anime['temporadas'] > 1]
print("Animes con más de 1 temporada: ", animes_mas_de_1_temporada)

# 3-Buscar en la lista el anime con nombre "Pokemon" e imprimir su año de estreno:
for anime in animes_90s:
    if anime['nombre'] == 'Pokemon':
        print("El anime Pokemon se estrenó en el año", anime['año'])
        break

# 4-Crear un nuevo diccionario con los nombres y años de estreno de los animes de la lista:
nombres_y_años = {anime['nombre']: anime['año'] for anime in animes_90s}
print("Nombres y años de estreno de los animes: ", nombres_y_años)
