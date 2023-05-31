#Gabriel Quispe Integrador 02 Div C Grupo 3
from data_stark import lista_personajes
from os import system

system("cls")

def stark_normalizar_datos(lista_personajes):
    '''
    Funcion que se encarga de garantizar que los datos esten en un formato consistente y util para su posterior procesamiento. Verificando si la lista está vacia. Para cada personaje en la lista, la función verifica si los datos (altura, fuerza y peso) tienen algún valor (no están vacios). Si tienen un valor, se convierte a un tipo de dato numérico (int o float) y se almacena en el mismo campo del personaje. Finalmente, si se han modificado los datos de al menos un personaje, imprime un mensaje de éxito indicando que los datos se han normalizado
    '''
   
    if len(lista_personajes) == 0:
        print("Error: Lista de héroes vacía")
        return -1
    
    datos_modificados = False
    for personaje in lista_personajes:
        if personaje['fuerza'] != '':
            personaje['fuerza'] = int(personaje['fuerza'])
            datos_modificados = True
            
        if personaje['altura'] != '':
            personaje['altura'] = float(personaje['altura'])
            datos_modificados = True
            
        if personaje['peso'] != '':
            personaje['peso'] = float(personaje['peso'])
            datos_modificados = True
            
    if datos_modificados:
        print("Datos normalizados")
    
def obtener_nombre(heroe:dict)->str:
    '''
    Funcion que recibe un diccionario que representa a un heroe y devuelve su nombre formateado.
    '''
    nombre = heroe['nombre']
    return f"Nombre: {nombre}"

def imprimir_dato(dato):
    '''
    Funcion que imprime un dato en la consola.
    '''
    print(dato)

def stark_imprimir_nombres_heroes(lista_personajes):
    '''
    Funcion que recibe una lista de heroes y los imprime en la consola. Si la lista está vacía, retorna -1.
    '''
    if len(lista_personajes) == 0:
        return -1
    for heroe in lista_personajes:
        nombre = obtener_nombre(heroe)
        imprimir_dato(nombre)
    return 

def obtener_nombre_y_dato(heroe:dict, dato:str):
    '''
    Función que recibe un diccionario heroe y un string dato. En esta función se obtiene el nombre del héroe del diccionario heroe y se retorna un string que incluye el nombre y el dato recibido como parametro
    '''
    nombre = heroe['nombre']
    return f"Nombre: {nombre} | {dato}"

def stark_imprimir_nombres_alturas(lista_personajes: list):
    '''
    La funcion recibe como parametro una lista de diccionarios que representan a diferentes personajes. La función tiene como objetivo imprimir en la consola el nombre y la altura de cada personaje en la lista. Verifica si la lista no está vacía, recorre la lista e imprime el nombre y la altura de cada personaje en la consola.
    '''
    if len(lista_personajes) == 0:
        return -1
    for personaje in lista_personajes:
        print(obtener_nombre_y_dato(personaje, f"Altura: {personaje['altura']}"))
    return 0

def calcular_max(lista_personajes, dato):
    '''
    Funcion que recibe una lista de heroes y una key (dato) como parametros. Utiliza el primer héroe de la lista como el valor máximo y luego iterar sobre el resto de los héroes para encontrar el heroe con el valor máximo real en la key(dato) especificado.
    '''
    primer_personajes = lista_personajes[0]
    mas_maximo = float(primer_personajes[dato])

    for personaje in lista_personajes:                          
        altura_personaje = float(personaje[dato])
        if altura_personaje > mas_maximo:
            mas_maximo = altura_personaje
    return mas_maximo

def calcular_min(lista_personajes, dato):
    '''
    Funcion que recibe una lista de heroes y una key (dato) como parametros. Utiliza el primer héroe de la lista como el valor máximo y luego iterar sobre el resto de los héroes para encontrar el heroe con el valor máximo real en la key(dato) especificado.
    '''
    primer_personajes = lista_personajes[0]
    mas_minima = float(primer_personajes[dato])

    for personaje in lista_personajes:      
        altura_personaje = float(personaje[dato])
        if altura_personaje < mas_minima:
            mas_minima = altura_personaje
    return mas_minima

def calcular_max_min_dato(lista_personajes, valor, dato):
    '''
    Funcion que toma tres argumentos de entrada: lista_personajes, valor, y dato. La funcion determina si valor es "maximo" o "minimo" y luego utiliza las funciones calcular_max y calcular_min para encontrar el valor máximo o mínimo del dato especificado en lista_personajes. El valor calculado se almacena en valor_calculado y se devuelve al final de la funcion.
    '''
    if valor == "maximo":
        valor_calculado = calcular_max(lista_personajes, dato)
    elif valor == "minimo":
        valor_calculado = calcular_min(lista_personajes, dato)
    
    return valor_calculado
      
def stark_calcular_imprimir_heroe(lista_personajes, valor, dato):
    '''
    Funcion que recibe 3parametros, primero verifica si la lista de personajes no está vacía, en cuyo caso devuelve -1. Si la lista tiene al menos un elemento, se llama a la función calcular_max_min_dato para obtener el valor máximo o mínimo del dato indicado en el parámetro dato.Luego, se define una variable tipo_calculo que contiene la cadena "Mayor" si valor es "maximo" o "Menor" si valor es "minimo". Recorre la lista de personajes con un ciclo for. Para cada personaje, se verifica si el valor del dato indicado en el parámetro dato es igual al valor calculado anteriormente. Si es así, se llama a la función imprimir_dato para imprimir el nombre del personaje y el valor del dato con el formato adecuado.
    '''
    if len(lista_personajes) == 0:
        return -1
    
    valor_calculado = calcular_max_min_dato(lista_personajes, valor, dato)
    tipo_calculo = "Mayor" if valor == "maximo" else "Menor"
    
    for heroe in lista_personajes:
        if float(heroe[dato]) == valor_calculado:
            
            return imprimir_dato(f"{tipo_calculo} {dato}: {obtener_nombre_y_dato(heroe, f'{dato}: {valor_calculado:.2f}')}")
    
def sumar_dato_heroe(lista_personajes, dato):
    '''
    La función recibe una lista de personajes y un dato en forma de string, devuelve la suma de todos los valores numéricos correspondientes a ese dato en todos los personajes de la lista.
    '''
    suma = 0                                                                    
    for personaje in lista_personajes:                                          
        if type(personaje) == dict:                                             
            for clave in personaje:                                             
                if clave == dato:                                               
                    valor_numerico = personaje[clave]                           
                    if valor_numerico != '':                                    
                        suma += float(valor_numerico)                           
                                                                
    return suma                                                                 

def dividir(dividendo, divisor):
    '''
    Función que se encargada de pedir dos numeros(dividendo y divisor), dividirlos.
    Si el divisor es igual a cero, la función retorna 0. En caso contrario, realiza la división entre el dividendo y el divisor y retorna el resultado.
    '''
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor

def calcular_promedio(lista_personajes, dato):
    '''
    Funcion que toma como argumento las alturas, y devuelve el promedio de alturas 
    '''
    cantidad = len(lista_personajes)
    suma = sumar_dato_heroe(lista_personajes, dato)
    return dividir(suma, cantidad)

def stark_calcular_imprimir_promedio_altura(lista_personajes):
    '''
    Funcion que utiliza otras dos funciones para calcular e imprimir el promedio de altura de una lista de personajes. Primero, comprueba si la lista está vacía. Si es así, devuelve -1 e imprime este valor en la consola. Sino, llama a la función calcular_promedio para obtener el promedio de altura de la lista de personajes. Finalmente, se devuelve el resultado con la funcion imprimir_dato
    '''
    if len(lista_personajes) == 0:
        return print (-1)
    else:
        promedio_altura = calcular_promedio(lista_personajes, 'altura')
        return imprimir_dato(f"La altura promedio de los personajes es {promedio_altura:.2f} cm")

def imprimir_menu():
    '''
    Funcion que imprime el menu de opciones por pantalla, y devuelve la opción elegida por el usuario, como un string.
    '''
    opciones = [
        "stark_normalizar_datos",
        "stark_imprimir_nombres_heroes",
        "stark_imprimir_nombres_alturas",
        "calcular_max Altura",
        "calcular_min Altura",
        "calcular_max Peso",
        "calcular_min Peso",
        "calcular_max Fuerza",
        "calcular_min Fuerza",
        "stark_calcular_imprimir_promedio_altura",
        "Salir"
    ]
    for i in range(len(opciones)):
        num_opcion = "{:02d}".format(i + 1)  
        print(f"{num_opcion}. {opciones[i]}")
    seleccion = input("Ingrese el numero de la opcion que desea ejecutar: ")
    imprimir_dato(f"Seleccionó la opción {seleccion}")
    return seleccion

def validar_entero(numero_str):
    '''
    Verifica si el número recibido es un string conformado unicamente por dos digitos.
    Retorna True si es válido, False caso contrario.
    '''
    if len(numero_str) != 2:                                                    
        return False
    for digito in numero_str:                                                   
        if digito not in '0123456789':                                          
            return False
    return True                                                                 

def stark_menu_principal():
    '''
    Funcion que utiliza un bucle while que se ejecuta hasta que el usuario ingresa una selección valida. Dentro del bucle, se llama a imprimir_menu() para mostrar las opciones de seleccion, y luego se valida la seleccion usando la funcion validar_entero(). Si la selección es válida, se retorna como un entero y el bucle se termina. De lo contrario, se muestra un mensaje de error y el bucle vuelve a empezar.
    '''
    while True:                                                                 
        seleccion = imprimir_menu()                                             
        if validar_entero(seleccion):                                           
            return int(seleccion)                                               
        else:
            print("Error: La seleccion debe ser un número entero de 2 digitos.")   


def stark_marvel_app(lista_personajes):
    '''
    Funcion que recibe por parametros una lista_personajes y se encarga de la ejecucion principal de nuestro programa, utiliza match en un bucle while para recorrer todas las funciones que se pueden realizar, para ello se solicita ingresar al usuario ingresar un numero de dos digitos entre 01 y 11 para que cause error y tenga que ingresar otra opcion.
    '''
    while True:
        opcion = stark_menu_principal()
        match opcion:
            case 1:
                lista_personajes = stark_normalizar_datos(lista_personajes)
            case 2:
                stark_imprimir_nombres_heroes(lista_personajes)
            case 3:
                stark_imprimir_nombres_alturas(lista_personajes)
            case 4:
                stark_calcular_imprimir_heroe(lista_personajes, "maximo", "altura")
            case 5:
                stark_imprimir_nombres_heroes(lista_personajes, "minimo", "altura")
            case 6:
                stark_calcular_imprimir_heroe(lista_personajes, "maximo", "peso")
            case 7:
                stark_calcular_imprimir_heroe(lista_personajes, "minimo", "peso")
            case 8:
                stark_calcular_imprimir_heroe(lista_personajes, "maximo", "fuerza")
            case 9:
                stark_calcular_imprimir_heroe(lista_personajes, "minimo", "fuerza")
            case 10:
                stark_calcular_imprimir_promedio_altura(lista_personajes)
            case 11:
                break
            case _:
                print("Error: La selección debe ser un numero entero entre el 01-11")

stark_marvel_app(lista_personajes)
