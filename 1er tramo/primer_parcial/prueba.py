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
    pokemones_tipo = []
    for pokemon in pokemones:
        if tipo in pokemon['Tipo']:
            pokemones_tipo.append(pokemon)

    if not pokemones_tipo:
        print(f"No hay pokemones del tipo {tipo}")
        return
    
    # Creamos la lista con la información que queremos guardar en el JSON
    data = {}
    data["pokemon"] = []
    for pokemon in pokemones_tipo:
        numero = str(pokemon['N° Pokedex']).zfill(3)
        nombre = pokemon['Nombre'].replace('\u00ed', 'í')
        tipos = pokemon['Tipo']
        if len(tipos) == 1:
            tipo = tipos[0]
        else:
            tipo = ','.join(tipos)
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
    with open("tipo_pokemones.json", 'w') as file:
        json.dump(data, file, indent=4)
    print(f"El archivo tipo_pokemones.json se ha creado con éxito.")
    




def leer_json(path: str) -> dict:
    with open(path, 'r') as file:
        data = json.load(file)
    print("Listado de pokemones en el archivo tipo_pokemones.json:")
    resultado = []
    for pokemon in data['pokemon']:
        resultado.append(f"{pokemon[0].center(80)}\n{pokemon[1].center(80)}\n")
    return '\n'.join(resultado)

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
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                guardar_json(tipos, pokemones)
            case 7:
                path = "tipo_pokemones.json"
                data = leer_json(path)
                print(data)
            case 8:
                break
        

pokemon_app(listar_pokemones)





