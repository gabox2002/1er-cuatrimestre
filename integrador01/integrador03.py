#Gabriel Quispe Integrador 01 Div C Grupo 3
from data_stark import lista_personajes
from os import system

def extraer_iniciales(nombre_heroe:str)->str:
    '''
    Funcion que recibe como parametro un nombre que es un string, devuelve N/A si esta vacia, si contiene "the " la elimina del string, si contiene un "-" reemplaza por un espacio en blanco, se extraenlas iniciales de cada palabra y se almacena en una lista y finalmente se concatena cada inicial con un punto devolviendo un str con las iniciales concatenadas
    '''
    if not nombre_heroe:                            
        return "N/A"
    
    if "the " in nombre_heroe:
        nombre_heroe = nombre_heroe.replace("the ", "")     
        
    nombre_heroe = nombre_heroe.replace("-", " ")       
    iniciales = [palabra[0].upper() for palabra in nombre_heroe.split()]            
    iniciales[-1] = iniciales[-1] + "."                     #
    iniciales = ".".join(iniciales)
    
    return iniciales

def definir_iniciales_nombre(heroe:dict):
    '''
    Función que recibe un diccionario que representa un héroe y define la clave "iniciales" en el diccionario, asignándole las iniciales del nombre del héroe. Si el argumento pasado no es un diccionario o no contiene la clave "nombre", la función devuelve False. De lo contrario, devuelve True después de definir la clave "iniciales" en el diccionario.
    '''
    if type(heroe) != dict or "nombre" not in heroe:
        return False
        
    iniciales = extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales
    
    return True


def agregar_iniciales_nombre(lista_personajes):
    '''
    Función que recibe una lista de diccionarios "lista_personajes". Primero verifica si la entrada es una lista y si no está vacía. Luego, recorre la lista y para cada diccionario en la lista, Si todas las condiciones se cumplen la función retorna True. Si no se cumple esta condición para algún diccionario, mostrando un mensaje de error y retorna False. La función no modifica la lista original, sino que agrega una nueva llave en cada diccionario dentro de la lista.
    '''
    if type(lista_personajes) != list or len(lista_personajes) == 0:         
        return False
    
    for heroe in lista_personajes:
        if not definir_iniciales_nombre(heroe):
            print('El origen de datos no contiene el formato correcto')
            return False
    
    return True

def stark_imprimir_nombres_con_iniciales(lista_personajes):
    '''
    Funcion que recibe como parametro una lista de personajes, primero verifica que la lista de héroes sea válida, si no cumple retorna False. 
    Luego se llama a la función agregar_iniciales_nombre para añadir las iniciales de cada personaje, y finalmente imprime la lista completa de nombres con sus iniciales. 
    Recorre la lista de personajes y se obtiene su nombre e iniciales a partir de los diccionarios, agrengando formato para que imprima con el "*" al inicio y entre parentesis las iniciales. La función no retorna nada, solo imprime los nombres con sus respectivas iniciales.
    '''
    if type(lista_personajes) != list or len(lista_personajes) == 0:
        return False
    
    if not agregar_iniciales_nombre(lista_personajes):
        return False
    
    for heroe in lista_personajes:
        nombre = heroe["nombre"]
        iniciales = heroe["iniciales"]
        print(f"* {nombre} ({iniciales})")


def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> str:
    '''
    Función que genera un string con el siguiente formato: GENERO-000...000ID, donde GENERO es el género recibido por parámetro seguido de un "-" (guión) y por último el identificador recibido. Todos los códigos generados deben tener como máximo 10 caracteres (contando todos los caracteres, inclusive el guión).
    
    Args:
        id_heroe: int, representa el identificador del héroe.
        genero_heroe: str, representa el género del héroe (puede tomar los valores "M", "F" o "NB").

    Returns:
        Si las validaciones pasan correctamente, retorna el código generado en formato str.
        Si no pasan las validaciones, retorna 'N/A' en formato str.
    '''
     # Validar que el id_heroe sea numérico
    if not str(id_heroe).isdigit():
        return 'N/A'
    
    if genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'

    if genero_heroe == 'NB':
        codigo = f"{genero_heroe}-" + str(id_heroe).zfill(7)
    else:
        codigo = f"{genero_heroe}-" + str(id_heroe).zfill(8)
    
    return codigo

def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    '''
    Función que verifica que el diccionario heroe no esté vacío, genera un código utilizando otra función generar_codigo_heroe y lo agrega como una nueva clave llamada 'codigo_heroe' en el diccionario heroe que toma como parametros la id_heroe y el genero del heroe. La función retorna True si todo se ejecuta correctamente y False si hay algún error.
    '''
    if not heroe or type(heroe) != dict:
        return False
    
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe['genero'])
    if len(codigo_heroe) != 10:
        return False
    
    heroe['codigo_heroe'] = codigo_heroe
    return True

def stark_generar_codigos_heroes(lista_personajes, indice_heroe=None):
    '''
    Funcion que genera códigos para una lista de personajes. La lista debe tener formato de diccionario.
    La función valida que la lista no este vacía y que cada elemento tenga el formato correcto antes de asignar un código de héroe único. Si hay algún error, la función imprimirá un mensaje de error y detendrá el proceso.
    Finalmente, la función imprimirá la cantidad de códigos generados, el código del primer héroe y el código del último héroe.
    '''
    if not lista_personajes:
        print('El origen de datos no contiene el formato correcto')
        return
    
    for personaje in lista_personajes:
        if type(personaje) != dict:
            print('El origen de datos no contiene el formato correcto')
            return
        
        id_heroe = lista_personajes.index(personaje) + 1
        
        if agregar_codigo_heroe(personaje, id_heroe):
            continue
        else:
            print('El origen de datos no contiene el formato correcto')
            return
    
    cantidad_codigos = len(lista_personajes)
    primer_heroe = lista_personajes[0]['codigo_heroe']
    ultimo_heroe = lista_personajes[-1]['codigo_heroe']
    
    print(f'Se asignaron {cantidad_codigos} códigos')
    print(f'El código del primer héroe es: {primer_heroe}')
    print(f'El código del último héroe es: {ultimo_heroe}')

    if indice_heroe is not None:
        try:
            codigo_heroe = lista_personajes[indice_heroe]['codigo_heroe']
            print(f'{codigo_heroe}')
        except IndexError:
            print(f'No hay un héroe en la posición {indice_heroe}')

def sanitizar_entero(numero_str: str) -> int:
    '''
    Esta función recibe un string 'numero_str' y trata de convertirlo en un entero. Si 'numero_str' es un entero positivo, la función devuelve el número en formato entero. Si 'numero_str' es un número negativo, devuelve -2. Si 'numero_str' no es un número válido (por ejemplo, contiene caracteres no numéricos), devuelve -1. Si 'numero_str' es un número en formato de punto flotante o está vacío, devuelve -3.
    '''
    numero_str = numero_str.strip()
    
    if not numero_str:
        return -3
    if numero_str[0] == '-':
        return -2
    if not numero_str.isnumeric():
        if '.' in numero_str:
            return -3
        else:
            for i in numero_str:
                if i not in '0123456789':
                    return -1
    return int(numero_str)

def sanitizar_flotante(numero_str:str)->float:
    '''
    Funcion que recibe un string que representa un posible número flotante. Retorna un float en caso de que se pueda convertir el string a número, de lo contrario
    retorna un valor según el error que ocurra.
    -1: El string contiene caracteres no numéricos.
    -2: El número es negativo.
    -3: El string está vacío o no se pudo convertir a número por otro error.
    '''
    numero_str = numero_str.strip()

    if not numero_str:
        return -3
    
    if numero_str[0] == '-':
        return -2
    
    partes = numero_str.split('.')
    
    if len(partes) == 1:
        if not partes[0].isnumeric():
            return -1
    elif len(partes) == 2:
        if not partes[0].isnumeric() or not partes[1].isnumeric():
            return -1
    else:
        return -1
    
    return float(numero_str)

def sanitizar_string(valor_str:str, valor_por_defecto='-'):
    '''
    Funcion que recibe dos parametros, uno de ellos ya inicializado con "-". Commienza eliminando espacios en blanco al principio y al final de ambos parametros, reemplazar la barra "/" por un espacio. Verifica si el valor_str es solo texto (sin números), luego convierte todo a minúsculas, Verifica si el valor_str está vacío y se ha pasado un valor por defecto. Si es así, retorna el valor_por_defecto en minúsculas y finalmente retorna el valor_str modificado.
    '''
    valor_str = valor_str.strip()                                
    valor_por_defecto = valor_por_defecto.strip()
    
    valor_str = valor_str.replace('/', ' ')                      
   
    if not valor_str.replace(" ", "").isalpha():                 
        return "N/A"
    
    valor_str = valor_str.lower()                                
    
    if not valor_str and valor_por_defecto:                     
        valor_str = valor_por_defecto.lower()

    return valor_str

def sanitizar_dato(lista_personajes, clave, tipo_dato):
    '''
    Sanitiza la clave especificada de todos los héroes de la lista
    Args:
        lista_heroes (list): lista de diccionarios que contienen la información de los héroes
        clave (str): clave a sanitizar
        tipo_dato (str): tipo de dato al que se debe convertir la clave, puede ser 'string', 'entero' o 'flotante'
    Returns:
        bool: True si se sanitizó algún dato, False en caso contrario
    
    '''
    sanitizado = False
    if type(tipo_dato) is not str:
        print("Tipo de dato no es una cadena.")
        return sanitizado
    tipo_dato = tipo_dato.lower()
    for heroe in lista_personajes:
        if clave.lower() not in heroe:
            print(f"La clave especificada '{clave}' no existe en el héroe {heroe['nombre']}")
            continue
        if tipo_dato == 'string':
            heroe[clave] = sanitizar_string(heroe[clave])
        elif tipo_dato == 'entero':
            heroe[clave] = sanitizar_entero(heroe[clave])
        elif tipo_dato == 'flotante':
            heroe[clave] = sanitizar_flotante(heroe[clave])
        else:
            print("Tipo de dato no reconocido")
            continue
        sanitizado = True
    return sanitizado

def stark_normalizar_datos(lista_personajes):
    '''
    Función que recibe como parámetro una lista de personajes y se encarga de normalizar ciertos datos de cada personaje. Primero se verifica si la lista está vacía y si es así, se imprime un mensaje de error y se retorna. Luego se define una lista con las claves de los datos a normalizar. Después, se recorre cada personaje de la lista y para cada uno de ellos se recorre la lista de claves y se llama a la función "sanitizar_dato" para normalizar el dato correspondiente. Finalmente, se imprime un mensaje indicando que los datos han sido normalizados.
    '''
    if not lista_personajes:
        print("Error: Lista de héroes vacía")
        return
    
    claves_a_sanitizar = ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']
    
    for heroe in lista_personajes:
        for clave in claves_a_sanitizar:
            sanitizar_dato(lista_personajes, clave, tipo_dato="string")
    
    print("Datos normalizados")

def generar_indice_nombres(lista_personajes: list):
    '''
    Función que toma una lista de diccionarios, donde cada diccionario representa un personaje. Verifica si el formato de la lista es correcto, es decir, si todos los elementos son diccionarios con una clave "nombre". Si es correcto, la función divide el nombre de cada personaje en palabras y las agrega a una lista de índice. Finalmente, devuelve la lista de índice de nombres. Si el formato de entrada es incorrecto, devuelve una lista vacía y muestra un mensaje de error correspondiente.
    '''

    if not lista_personajes:
        print("Formto incorrecto")
        return []
    
    if not all(type(heroe) == dict for heroe in lista_personajes):
        print("Formato incorrecto")
        return []
    
    if not all("nombre" in heroe for heroe in lista_personajes):
        print("Formato incorrecto")
        return []
    
    indice_nombres = []

    for heroe in lista_personajes:
        nombre = heroe["nombre"].split()
        indice_nombres.extend(nombre)

    return indice_nombres

def stark_imprimir_indice_nombre(lista_personajes: list):
    '''
    Función que recibe una lista de personajes como argumento y llama a la función "generar_indice_nombres" para crear un índice de nombres a partir de esa lista. Luego convierte este índice en una cadena separada por guiones y la imprime en la consola.
    '''
    indice_nombres = generar_indice_nombres(lista_personajes)
    indice_con_guiones = "-".join(indice_nombres)
    print(indice_con_guiones)

def convertir_cm_a_mtrs(valor_cm: float):
    '''
    Función que recibe como parámetro un valor en centímetros (valor_cm) y lo convierte a metros. Antes de realizar la conversión, se verifica que el parámetro sea un número decimal positivo. Si no es así, se retorna el valor -1. Si el parámetro cumple con las condiciones, se realiza la conversión dividiéndolo entre 100 y se retorna el resultado en metros.
    '''
    if type(valor_cm) != float or valor_cm < 0:
        return -1
    return valor_cm / 100

def generar_separador(patron: int, largo: int, imprimir: True) -> str:
    '''
    Función que toma como entrada un patrón y una longitud, y genera una cadena de caracteres que consiste en el patrón repetido tantas veces como se especifique en la longitud. Si el parámetro imprimir es verdadero, también imprime la cadena generada. El patrón debe ser una cadena de uno o dos caracteres, y la longitud debe ser un número entero entre 1 y 235. Si los parámetros no cumplen con estos requisitos, la función devuelve 'N/A'.
    '''
    if not (1 <= len(patron) <= 2 and largo > 0 and largo < 236 and largo == int(largo)):
        return 'N/A'
    separador = patron * largo
    if imprimir:
        print(separador)
    return separador

def generar_encabezado(titulo: str):
    '''
    Funcion que recibe un parámetro "titulo" que debe ser una cadena de caracteres (string). La función genera un encabezado con el título en mayúsculas, utilizando un separador de asteriscos (*) de longitud 100 para enmarcar el título. El encabezado generado se devuelve como una cadena de caracteres.
    '''
    largo = 100
    separador = '*' * largo # ajustar al largo de pantalla
    titulo_mayusculas = titulo.upper()
    encabezado = separador + '\n' + titulo_mayusculas + '\n' + separador
    return encabezado

def imprimir_ficha_heroe(heroe: dict):
    '''
    Funcion que toma un diccionario "heroe" como argumento y verifica si es válido. Si es así, se extraen las iniciales del nombre del héroe y se agrega una nueva clave "iniciales" al diccionario. Luego se genera un código de héroe único para el héroe y se imprimen los detalles de su ficha, incluyendo su nombre, identidad secreta, consultora, código de héroe, altura, peso, fuerza, color de ojos, color de pelo e inteligencia. La función utiliza otras funciones definidas en el programa, como "extraer_iniciales", "generar_codigo_heroe" y "generar_encabezado", para generar y dar formato a los datos.
    '''
    if not heroe or type(heroe) != dict:
        return False
    
    iniciales = extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales

    id_heroe = lista_personajes.index(heroe) + 1
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe['genero'])
    
    print(generar_encabezado('principal'))
    print(f"    NOMBRE DEL HÉROE:               {heroe['nombre']} ({iniciales})")
    print(f"    IDENTIDAD SECRETA:              {heroe['identidad']}")
    print(f"    CONSULTORA:                     {heroe['empresa']}")
    print(f"    CÓDIGO DE HÉROE:                {codigo_heroe}")
    
    print(generar_encabezado('fisico'))
    print(f"    ALTURA:                         {float(heroe['altura'])} cm")
    print(f"    PESO:                           {float(heroe['peso'])} kg")
    print(f"    Fuerza:                         {int(heroe['fuerza'])} N")

    print(generar_encabezado('señas particulares'))
    print(f"    COLOR DE OJOS:                  {heroe['color_ojos']}")
    print(f"    COLOR DE PELO:                  {heroe['color_pelo']}")
    
def stark_navegar_fichas(lista_personajes: list):
    indice_actual = 0
    imprimir_ficha_heroe(lista_personajes[indice_actual])
    
    while True:
        opcion = input("[1] Ir a la izquierda [2] Ir a la derecha [S] Salir\n").upper()
        
        if opcion == '1':
            indice_actual = (indice_actual - 1) % len(lista_personajes)
            imprimir_ficha_heroe(lista_personajes[indice_actual])
        elif opcion == '2':
            indice_actual = (indice_actual + 1) % len(lista_personajes)
            imprimir_ficha_heroe(lista_personajes[indice_actual])
        elif opcion == 'S':
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def imprimir_menu():
    print("""
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir
____________________________________________________________
""")
    
def stark_menu_principal():
    imprimir_menu()
    respuesta = input("Ingrese una opción: ")
    return respuesta
    
def stark_marvel_app_3(lista_heroes):
    while True:
        opcion = stark_menu_principal()
        match opcion:
            case '1':
                stark_imprimir_nombres_con_iniciales(lista_heroes)
            case '2':
                stark_generar_codigos_heroes(lista_heroes)
            case '3':
                stark_normalizar_datos(lista_heroes)
            case '4':
                stark_imprimir_indice_nombre(lista_heroes)
            case '5':
                stark_navegar_fichas(lista_personajes)
            case 'S', 's':
                print("Saliendo del programa...")
                return
            case _:
                print("Error: opción incorrecta, por favor ingrese una opción válida")

stark_marvel_app_3(lista_personajes)