import re
import json
def traer_datos_desde_archivo(path: str) -> list:
    lista_pokemones = []
    with open(path, "r", encoding="UTF-8") as archivo:
        for line in archivo:
            register = re.split(",|\n", line)
            pokemon = {}
            pokemon["N° Pokedex"] = register[0]
            pokemon["Nombre"] = register[1]
            pokemon["Tipo"] = register[2].split("/")
            pokemon["Poder de Ataque"] = register[3]
            pokemon["Poder de Defensa"] = register[4]
            pokemon["Habilidades"] = register[5].split("|*|")
            lista_pokemones.append(pokemon)
    return lista_pokemones
    



def cargar_pokemones():
    pokemones = []
    tipos = set()
    habilidades = set()

    lista_pokemones = traer_datos_desde_archivo('pokemones.csv')
    for pokemon in lista_pokemones:
        # Agregamos los tipos a su respectiva colección
        for tipo in pokemon['Tipo']:
            tipos.add(tipo)
        # Agregamos las habilidades a su respectiva colección
        for habilidad in pokemon['Habilidades']:
            habilidades.add(habilidad)
        # Agregamos el pokemon a la colección
        pokemones.append(pokemon)

    print('Pokemones cargados exitosamente')
    return pokemones, tipos, habilidades

def listar_pokemones(pokemones):
    for pokemon in pokemones:
        print(f"{pokemon['N° Pokedex']}, {pokemon['Nombre']}, {'/'.join(pokemon['Tipo'])}, {pokemon['Poder de Ataque']}, {pokemon['Poder de Defensa']}, {'/'.join(pokemon['Habilidades'])}")

def listar_tipos(tipos):
    lista_tipos = []
    for tipo in tipos:
        if tipo != list(tipos)[0]:
            lista_tipos.append(tipo)
    return lista_tipos

def listar_habilidades(habilidades):
    lista_habilidades = []
    for habilidad in habilidades:
        lista_habilidades.append(habilidad)
    return lista_habilidades

def listar_cantidad_pokemones_por_tipo(pokemones):
    cantidad_por_tipo = {}

    tipos = set()
    for pokemon in pokemones:
        for tipo in pokemon['Tipo']:
            tipos.add(tipo)
    lista_tipos = listar_tipos(tipos)

    for tipo in lista_tipos:
        contador = 0
        for pokemon in pokemones:
            if tipo in pokemon['Tipo']:
                contador += 1
        cantidad_por_tipo[tipo] = contador

    print("Cantidad de pokemones por tipo:")
    for tipo in cantidad_por_tipo:
        if tipo != 'Tipo':
            print(f"\t{tipo}: {cantidad_por_tipo[tipo]}")


def listar_pokemones_por_tipo(pokemones):
    
    tipos = set()
    for pokemon in pokemones:
        for tipo in pokemon['Tipo']:
            tipos.add(tipo)
    lista_tipos = listar_tipos(tipos)

    for tipo in lista_tipos:
        if tipo != "Tipo":
            print(f"{tipo}:")
            for pokemon in pokemones:
                if tipo in pokemon['Tipo']:
                    print(f"\t{pokemon['Nombre']} - Poder de Ataque: {pokemon['Poder de Ataque']}")

def listar_pokemones_por_habilidad(pokemones):
    habilidades = set()
    for pokemon in pokemones:
        for habilidad in pokemon['Habilidades']:
            habilidades.add(habilidad)

    habilidades_str = ', '.join(habilidades)
    print(f"\tLas habilidades son: {habilidades_str}")

    habilidad_buscada = input("\nIngrese la habilidad a buscar: ")
    while habilidad_buscada not in habilidades:
        print("La habilidad ingresada no es válida.")
        habilidad_buscada = input("Ingrese la habilidad a buscar: ")

    print(f"\nLista de pokemones con la habilidad '{habilidad_buscada}':")
    pokemones_con_habilidad = []
    for pokemon in pokemones:
        if habilidad_buscada in pokemon['Habilidades']:
            promedio_poder = (int(pokemon['Poder de Ataque']) + int(pokemon['Poder de Defensa'])) / 2
            pokemones_con_habilidad.append({
                "Nombre": pokemon['Nombre'],
                "Tipo": "/".join(pokemon['Tipo']),
                "Promedio de poder": promedio_poder
            })
    if len(pokemones_con_habilidad) == 0:
        print("No se encontraron pokemones con la habilidad buscada.")
    else:
        for pokemon in pokemones_con_habilidad:
            print(f"\t{pokemon['Nombre']} ({pokemon['Tipo']}) - Promedio de poder: {pokemon['Promedio de poder']:.2f}")

def listar_pokemones_ordenados(lista_pokemones):
    '''
    Función que recibe como parámetro una lista de diccionarios llamada lista_pokemones y retorna una lista ordenada de diccionarios, donde los diccionarios están ordenados primero por su valor en la clave "Poder de Ataque", de menor a mayor. Si hay pokemones con el mismo valor de "Poder de Ataque", se ordenan por orden alfabético de sus nombres, de la A a la Z. Finalmente retorna la lista ordenada lista_filtrada.
    '''
    # Filtrar la lista para eliminar los elementos con valor no numérico en 'Poder de Ataque'
    lista_filtrada = []
    for pokemon in lista_pokemones:
        if pokemon['Poder de Ataque'].isdigit():
            lista_filtrada.append(pokemon)

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
        
    print("Lista de pokemones ordenados por poder de ataque:")
    for pokemon in lista_filtrada:
        print(f"""\tPoder de Ataque: {pokemon['Poder de Ataque']} - N° Pokedex: {pokemon['N° Pokedex']} - Nombre: {pokemon['Nombre']} - Tipo: {' y '.join(pokemon['Tipo'])} - Poder de Defensa: {pokemon['Poder de Defensa']} - Habilidades: {' y '.join(pokemon['Habilidades'])}""")




# def parser_json(path:str)->list:
#     with open(path,"r") as archivo:
#         diccionario = json.load(archivo)
#     return diccionario

# def crear_archivo_json(path:str, lista_pokemones): #de la opcion 5
#     pokemones_ordenados = listar_pokemones_ordenados(lista_pokemones)
#     with open(path, 'w') as archivo:
#         json.dump(pokemones_ordenados, archivo, indent=4)

# lista = parser_json("data.json")
# crear_archivo_json("nueva_lista.json", lista)


def guardar_json(tipos, pokemones:list):
    """
    Genera un archivo de tipo JSON con los pokemones de un tipo específico.
    """
    tipo = input("Ingrese el tipo de pokemon a guardar: ")
    pokemones_tipo = [pokemon for pokemon in pokemones if tipo in pokemon['Tipo']]
    if not pokemones_tipo:
        print(f"No hay pokemones del tipo {tipo}")
        return
    
    # Creamos la lista con la información que queremos guardar en el JSON
    data = {}
    data["pokemon"] = []
    for pokemon in pokemones_tipo:
        numero = str(pokemon['N° Pokedex']).zfill(3)
        nombre = pokemon['Nombre'].replace('\u00ed', 'í')
        tipos = list(pokemon['Tipo'])
        tipo = pokemon['Tipo']
        tipo = tipos[0] if len(tipos) == 1 else f"{tipos[0]},{tipos[1]}"
        ataque = int(pokemon['Poder de Ataque'])
        defensa = int(pokemon['Poder de Defensa'])
        if ataque == defensa:
            tipo_poder = "Ambos"
        else:
            tipo_poder = "Ataque" if ataque > defensa else "Defensa"
        poder = max(ataque, defensa)
        
        
        descripcion = f"{nombre}-{poder}-{tipo_poder}"
        registro = f"{numero},{nombre},{tipo},{ataque},{defensa}"
        data["pokemon"].append([registro, descripcion])
        
        
    # Guardamos el archivo
    filename = f"pokemones_{tipo}.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Archivo {filename} creado con éxito.")
    return filename




def leer_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    
    print(f"Listado de pokemones en el archivo {filename}:")
    return data



def imprimir_menu():
    '''
    Funcion que imprime el menu de opciones por pantalla, y devuelve la opción elegida por el usuario, como un string.
    '''
    opciones = [
        "Traer datos desde archivo",
        "Listar cantidad por tipo",
        "Listar pokemones por tipo",
        "Listar pokemones por habilidad",
        "Listar pokemones ordenados",
        "Guardar Json",
        "Leer Json",
        "Salir del programa"
    ]
    for i in range(len(opciones)):
        num_opcion = "{}".format(i + 1)  
        print(f"{num_opcion}. {opciones[i]}")
    while True:
        seleccion = input("Ingrese el numero de la opcion que desea ejecutar: ")
        if seleccion.isnumeric() and 1 <= int(seleccion) <= 8:
            break
        else:
            print("Entrada inválida. Debe ingresar un número entero del 1 al 8.")
    seleccion = int(seleccion)
    print(f"Seleccionó la opción {seleccion}")
    return seleccion

def pokemon_app(pokemones):
    while True:
        print("\n****MENU POKEMON****")
        opcion = imprimir_menu()
        match opcion:
            case 1:
                pokemones, tipos, habilidades = cargar_pokemones()
            case 2:
                listar_cantidad_pokemones_por_tipo(pokemones)
            case 3:
                listar_pokemones_por_tipo(pokemones)
            case 4:
                listar_pokemones_por_habilidad(pokemones)
            case 5:
                listar_pokemones_ordenados(pokemones)
            case 6:
                #crear_archivo_json(pokemones)
                guardar_json(tipos, pokemones)
            case 7:
                leer_json(filename)
            case 8:
                break
        

pokemon_app(listar_pokemones)





