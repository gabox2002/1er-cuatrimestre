import re

def traer_datos_desde_archivo(path:str) -> list:           #crea una lista a partir de un archivo
    lista_pokemones = []
    
    archivo = open(path, "r")
    for line in archivo:
        register = re.split(",|\n",line)
        pokemon = {}
        pokemon["N° Pokedex"]= register[0]
        pokemon["Nombre"]= register[1]
        pokemon["Tipo"]= register[2].split("/")
        pokemon["Poder de Ataque"]= register[3]
        pokemon["Poder de Defensa"]= register[4]
        pokemon["Habilidades"]= register[5].split("|*|")
        lista_pokemones.append(pokemon)   
    archivo.close()
    return lista_pokemones

# lista_pokemones = traer_datos_desde_archivo("pokemones.csv")
# for pokemon in lista_pokemones:
#     #print(f"{pokemon['N° Pokedex']} - {pokemon['Tipo']} - {pokemon['Habilidades']}")
#     print(f"{pokemon['Tipo']}")
    #print(lista_pokemones)


# heroes_segun_color_pelo.csv (agrupados por color de pelo)
# heroes_segun_color_ojos.csv (agrupados por color de ojos)

#paso contrario escribir en un archivo lo que yo tengo en memoria
# def generar_csv(path:str, lista:list):
#     archivo = open(path, "w", encoding="UTF-8")
#     for tema in lista:
#         line = "{0},{1},{2},{3},{4},{5}"
#         line = line.format(tema["N° Pokedex"], 
#                            tema["Nombre"], 
#                            tema["Tipo"], 
#                            tema["Poder de Ataque"],
#                            tema["Poder de Defensa"],
#                            tema["Habilidades"])
#         archivo.write(line)
#     archivo.close()




#'Nombre': 'Dragonair', 'Tipo': ['Dragón'], 'Poder de Ataque': '84', 'Poder de Defensa': '65', 'Habilidades': ['Enjambre', 'Cambio color']}, {'N° Pokedex': '149', 'Nombre': 'Dragonite', 'Tipo': ['Dragón', 'Volador'], 'Poder de Ataque': '134', 'Poder de Defensa': '95', 'Habilidades': ['Enjambre', 'Cambio color']}, {'N° Pokedex': '150', 'Nombre': 'Mewtwo', 'Tipo': ['Psíquico'], 'Poder de Ataque': '110', 'Poder de Defensa': '90', 'Habilidades': ['Presión', 'Ninguna']}, {'N° Pokedex': '151', 'Nombre': 'Mew', 'Tipo': ['Psíquico'], 'Poder de Ataque': '100', 'Poder de Defensa': '100', 'Habilidades': ['Sincronía', 'Ninguna']}] 

def listar_cantidad_por_tipo(lista_pokemones):
    tipos = {}

    for pokemon in lista_pokemones:
        for tipo in pokemon['Tipo']:
            if tipo in tipos:
                tipos[tipo] += 1
            else:
                tipos[tipo] = 1

    print("Cantidad de Pokemones por Tipo:")
    for tipo in tipos:
        cantidad = tipos[tipo]
        print(f"{tipo}: {cantidad}")

# pokemones = traer_datos_desde_archivo("pokemones.csv")
# listar_cantidad_por_tipo(pokemones)

def listar_pokemones_por_tipo(lista_pokemones, tipo):
    for pokemon in lista_pokemones:
        if tipo in pokemon['Tipo']:
            print(pokemon['Nombre'] + ': ' + pokemon['Poder de Ataque'])

# lista_pokemones = traer_datos_desde_archivo("pokemones.csv")
# listar_pokemones_por_tipo(lista_pokemones, "Fuego")

def listar_pokemones_por_habilidad(lista_pokemones, habilidad):
    pokemon_con_habilidad = []
    for pokemon in lista_pokemones:
        if habilidad in pokemon['Habilidades']:
            poder_total = int(pokemon['Poder de Ataque']) + int(pokemon['Poder de Defensa'])
            promedio_poder = poder_total / 2
            pokemon_con_habilidad.append({
                'Nombre': pokemon['Nombre'],
                'Tipo': pokemon['Tipo'],
                'Promedio de poder': promedio_poder
            })
    if pokemon_con_habilidad:
        print(f"Los pokemones con la habilidad '{habilidad}' son:")
        for pokemon in pokemon_con_habilidad:
            print(f"Nombre: {pokemon['Nombre']}, Tipo: {pokemon['Tipo']}, Promedio de poder: {pokemon['Promedio de poder']}")
    else:
        print(f"No se encontraron pokemones con la habilidad '{habilidad}'")

# lista_pokemones = traer_datos_desde_archivo("pokemones.csv")
# listar_pokemones_por_habilidad(lista_pokemones, "Clorofila")


    
def listar_pokemones_ordenados(lista_pokemones):
    '''
    Función que recibe como parámetro una lista de diccionarios llamada lista_pokemones y retorna una lista ordenada de diccionarios, donde los diccionarios están ordenados primero por su valor en la clave "Poder de Ataque", de menor a mayor. Si hay pokemones con el mismo valor de "Poder de Ataque", se ordenan por orden alfabético de sus nombres, de la A a la Z. Finalmente retorna la lista ordenada lista_filtrada.
    '''
    # Filtrar la lista para eliminar los elementos con valor no numérico en 'Poder de Ataque'
    lista_filtrada = [pokemon for pokemon in lista_pokemones if pokemon['Poder de Ataque'].isdigit()]

    # Ordenar la lista filtrada por 'Poder de Ataque' y en caso de empate, por 'Nombre'
    for i in range(len(lista_filtrada)-1):
        # Encontrar el índice del pokemon con el menor 'Poder de Ataque' desde i hasta el final de la lista
        #El -1 en range(len(lista_filtrada)-1) se utiliza para asegurarse de que el índice i no exceda el rango de la lista.El motivo por el que se utiliza -1 es porque los índices de una lista comienzan en 0. Entonces, si el largo de la lista es n, el último índice será n-1. Por lo tanto, si no se utiliza -1 en el rango, el bucle intentará acceder a un elemento fuera del rango de la lista y producirá un error.
        menor_ataque = i
        for j in range(i+1, len(lista_filtrada)):
            if int(lista_filtrada[j]['Poder de Ataque']) < int(lista_filtrada[menor_ataque]['Poder de Ataque']):
                # Si encontramos un pokemon con un 'Poder de Ataque' menor, actualizamos menor_ataque
                menor_ataque = j
            elif int(lista_filtrada[j]['Poder de Ataque']) == int(lista_filtrada[menor_ataque]['Poder de Ataque']):
                # Si hay un empate en 'Poder de Ataque', ordenar por 'Nombre' de la A a la Z
                if lista_filtrada[j]['Nombre'] < lista_filtrada[menor_ataque]['Nombre']:
                    menor_ataque = j
        # Intercambiar el pokemon en el índice i con el pokemon con el menor 'Poder de Ataque'
        lista_filtrada[i], lista_filtrada[menor_ataque] = lista_filtrada[menor_ataque], lista_filtrada[i]

    # Devolver la lista ordenada
    return lista_filtrada

# lista_pokemones = traer_datos_desde_archivo("pokemones.csv")
# pokemones_ordenados = listar_pokemones_ordenados(lista_pokemones)
# for pokemon in pokemones_ordenados:
#     print(pokemon)

import json

# def guardar_json_tipo(lista_pokemones, tipo):
#     # Filtramos la lista de pokemones por el tipo especificado
#     pokemones_tipo = [p for p in lista_pokemones if tipo in p['Tipo']]
    
#     # Creamos una cadena de texto con los datos de cada pokemon
#     datos_pokemones = []
#     for p in pokemones_tipo:
#         nombre = p['Nombre']
#         ataque = int(p['Poder de Ataque'])
#         defensa = int(p['Poder de Defensa'])
#         tipo_poder = 'Ataque' if ataque > defensa else 'Defensa' if defensa > ataque else 'Ambos'
#         datos_pokemones.append(f"{p['N° Pokedex']},{nombre},{tipo},{'/'.join(p['Tipo'])},{ataque},{defensa}\n{nombre}-{max(ataque, defensa)}-'{tipo_poder}'\n")
    
#     # Guardamos los datos en un archivo JSON
#     with open(f'{tipo}.json', 'w') as archivo:
#         archivo.writelines(datos_pokemones)

# lista = guardar_json_tipo("data.json")
# {tipo}.json("nueva_lista.json", lista)        