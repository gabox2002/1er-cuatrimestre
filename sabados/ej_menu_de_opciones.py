'''
Ejercicio con Menú de Opciones
Realizar un programa utilizando los conceptos de la clase:
Opciones del menú:
# 1 Cargar una lista con 10 nombres de animales (perro, gato, león, etc,) y de que tipo son
(terrestre, anfibio, volador).
# 2 Imprimir la lista completa de animales con su tipo.
# 3 Mostrar el porcentaje de animales por tipo.
# 4 Mayor cantidad de animales por tipo.
# 5 Menor cantidad de animales por tipo.
# 6 Pedir un animal e informar si está en la lista y sus datos correspondientes si
efectivamente está en la lista.
# 7 Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
# 8 Informar la cantidad de animales por cada tipo de animal.
# 9 Vaciar la lista.
#10 Salir.
'''



def cargar_animales():
    '''
    Función para cargar la lista de animales con su tipo, 
    '''
    animales = []
    for i in range(3): # es 10
        nombre_animal = input(f"Ingrese el nombre del animal: ")
        tipo_animal = input(f"Ingrese el tipo del animal: ")
        lista_animales.append((nombre_animal, tipo_animal))
    return animales

def imprimir_animales(lista_animales):
    '''
    Función para imprimir la lista completa de animales con su tipo
    '''
    if len(lista_animales) == 0:
        print("La lista de animales está vacía.")
    else:
        print("Lista de animales:")
        for animal in lista_animales:
            print(f"{animal[0]} - {animal[1]}")

# Función para mostrar el porcentaje de animales por tipo
def porcentaje_animales(lista_animales):
    if not lista_animales:
        print("La lista de animales está vacía.")
    else:
        # Contar la cantidad de animales por tipo
        terrestres = 0
        anfibios = 0
        voladores = 0
        acuaticos = 0
        for animal in lista_animales:
            if animal[1] == "terrestre":
                terrestres += 1
            elif animal[1] == "anfibio":
                anfibios += 1
            elif animal[1] == "volador":
                voladores += 1
            elif animal[1] == "acuatico":
                acuaticos += 1
        
        # Calcular el porcentaje de animales por tipo
        total = len(lista_animales)
        porc_terrestres = (terrestres / total) * 100
        porc_anfibios = (anfibios / total) * 100
        porc_voladores = (voladores / total) * 100
        porc_acuaticos = (acuaticos / total) * 100
        
        print("Porcentaje de animales por tipo:")
        print(f"- Terrestres: {porc_terrestres:.2f}%")
        print(f"- Anfibios: {porc_anfibios:.2f}%")
        print(f"- Voladores: {porc_voladores:.2f}%")
        print(f"- Acuaticos: {porc_acuaticos:.2f}%")
        

# Función para obtener la cantidad de animales por tipo
def cantidad_animales_por_tipo():
    # Creamos un diccionario para almacenar la cantidad de animales por tipo
    cantidad_por_tipo = {}
    for animal in lista_animales:
        tipo = animal[1]
        if tipo in cantidad_por_tipo:
            cantidad_por_tipo[tipo] += 1
        else:
            cantidad_por_tipo[tipo] = 1
    
    # Imprimimos la cantidad de animales por tipo
    print("Cantidad de animales por tipo:")
    for tipo, cantidad in cantidad_por_tipo.items():
        print(f"{tipo}: {cantidad}")
        

# Función para vaciar la lista de animales
def vaciar_lista():
    animales.clear()
    print("¡Lista vaciada correctamente!")

lista_animales = []
while True:
    respuesta = int(input('''Menu de animales
    1. Cargar lista de animales
    2. Imprimir lista completa
    3. Mostrar el porcentaje de animales por tipo.
    4. Mayor cantidad de animales por tipo.
    5. Menor cantidad de animales por tipo.
    6. Pedir un animal e informar si está en la lista y sus datos correspondientes si efectivamente está en la lista.
    7. Pedir un animal e informar la primer ocurrencia de ese animal en la lista si es que existe.
    8. Informar la cantidad de animales por cada tipo de animal.
    9. Vaciar la lista.
    10. Salir.\n Elija una opcion:
    '''))
    match respuesta:    
        case 1:
            cargar_animales()
        case 2:
            imprimir_animales(lista_animales)
        case 3:
            porcentaje_animales(lista_animales)
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass        
        case 9: 
            pass
        case 10:
            break
