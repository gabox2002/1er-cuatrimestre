#Gabriel Quispe Integrador 02 Div C Grupo 3
from data_stark import lista_personajes
from os import system

system("cls")
#0 Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá: ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos) ● Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato. ● Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario no imprimirá nada. ● Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
def stark_normalizar_datos(lista_personajes):
   
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

    return lista_personajes
    
#1.1 Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera:Nombre: Howard the Duck
def obtener_nombre(heroe:dict)->str:
    """
    Funcion que recibe un diccionario que representa a un heroe y devuelve su nombre formateado.
    """
    nombre = heroe['nombre']
    return f"Nombre: {nombre}"

#1.2 Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.
def imprimir_dato(dato):
    '''
    Funcion que imprime un dato en la consola.
    '''
    print(dato)

#1.3. Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía correspondientes para realizar sus acciones, caso contrario no hará nada y retornara -1.
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

#2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. ● La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO. ● El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza) -> Nombre: Venom | fuerza: 500
def obtener_nombre_y_dato(heroe:dict, dato:str):
    nombre = heroe['nombre']
    return f"Nombre: {nombre} | {dato}"


#3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
def stark_imprimir_nombres_alturas(lista_heroes: list):
    if len(lista_personajes) == 0:
        return -1
    for personaje in lista_heroes:
        print(obtener_nombre_y_dato(personaje, f"Altura: {personaje['altura']}"))
    return 0

#4.1 Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más alto. Ejemplo de llamada:-> calcular_max(lista, 'edad')
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

# 4.2. Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más bajo. Ejemplo de llamada: -> calcular_min(lista, 'edad')
def calcular_min(lista_personajes, dato):
    '''
    Funcion que recibe una lista de heroes y una key (dato) como parametros. Utiliza el primer héroe de la lista como el valor máximo y luego iterar sobre el resto de los héroes para encontrar el heroe con el valor máximo real en la key(dato) especificado.
    '''
    primer_personajes = lista_personajes[0]
    mas_minima = float(primer_personajes[dato])

    for personaje in lista_personajes:      #recorre la lista
        altura_personaje = float(personaje[dato])
        if altura_personaje < mas_minima:
            mas_minima = altura_personaje
    return mas_minima

#4.3. Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros: ● La lista de héroes ● El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’ ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc. La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 4.1 y 4.2 Ejemplo de llamada: -> calcular_max_min_dato(lista, "maximo", "edad")
def calcular_max_min_dato(lista_personajes, valor, dato):
    if valor == "maximo":
        valor_calculado = calcular_max(lista_personajes, dato)
    elif valor == "minimo":
        valor_calculado = calcular_min(lista_personajes, dato)
    
    return valor_calculado
      
#4.4. Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros: ● La lista de héroes ● El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’ ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
def stark_calcular_imprimir_heroe(lista_personajes, valor, dato):
    if len(lista_personajes) == 0:
        return -1
    
    valor_calculado = calcular_max_min_dato(lista_personajes, valor, dato)
    tipo_calculo = "Mayor" if valor == "maximo" else "Menor"
    
    for heroe in lista_personajes:
        if float(heroe[dato]) == valor_calculado:
            
            return imprimir_dato(f"{tipo_calculo} {dato}: {obtener_nombre_y_dato(heroe, f'{dato}: {valor_calculado:.2f}')}")
    
#stark_calcular_imprimir_heroe(lista_personajes, "minimo", "altura")
#5.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según la key pasada por parámetro 
def sumar_dato_heroe(lista_personajes, dato):
    '''
    La función recibe una lista de personajes y un dato en forma de string, devuelve la suma de todos los valores numéricos correspondientes a ese dato en todos los personajes de la lista.
    '''
    suma = 0                                                                    # Inicializa la variable suma en cero
    for personaje in lista_personajes:                                          # Itera sobre cada personaje en la lista
        if type(personaje) == dict:                                             # Verifica que el personaje sea un diccionario y se utiliza la función bool() para verificar que no esté vacío
            for clave in personaje:                                             # Itera sobre cada clave del diccionario
                if clave == dato:                                               # Si la clave es igual al dato que se busca
                    valor_numerico = personaje[clave]                           # Obtiene el valor correspondiente a la clave
                    if valor_numerico != '':                                    # Si el valor numerico es distinto que vacio ("") que siga
                        suma += float(valor_numerico)                           # Convertir el valor a un número y lo agrega a la suma
                                                                
    return suma                                                                 # Devuelve la suma total

#5.2. Crear la función ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo, retornar 0, caso contrario realizar la división entre los parámetros y retornar el resultado 
def dividir(dividendo, divisor):
    '''
    Función que se encargada de pedir dos numeros(dividendo y divisor), dividirlos.
    Si el divisor es igual a cero, la función retorna 0. En caso contrario, realiza la división entre el dividendo y el divisor y retorna el resultado.
    '''
    if divisor == 0:
        return 0
    else:
        return dividendo / divisor

#5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y un string que representa el dato del héroe que se requiere calcular el promedio. La función debe retornar el promedio del dato pasado por parámetro IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2   
def calcular_promedio(lista_personajes, dato):
    '''
    Funcion que toma como argumento las alturas, y devuelve el promedio de alturas 
    '''
    cantidad = len(lista_personajes)
    suma = sumar_dato_heroe(lista_personajes, dato)
    return dividir(suma, cantidad)

#5.4. Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la altura promedio. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1. IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
def stark_calcular_imprimir_promedio_altura(lista_personajes):
    if len(lista_personajes) == 0:
        return print (-1)
    else:
        promedio_altura = calcular_promedio(lista_personajes, 'altura')
        return imprimir_dato(f"La altura promedio de los personajes es {promedio_altura:.2f} cm")

#6.1   
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
        num_opcion = "{:02d}".format(i + 1)  # Formato "01", "02", etc.
        print(f"{num_opcion}. {opciones[i]}")
    seleccion = input("Ingrese el numero de la opcion que desea ejecutar: ")
    imprimir_dato(f"Selecciono la opcion {seleccion}")
    return seleccion

#6.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario
def validar_entero(numero_str):
    '''
    Verifica si el número recibido es un string conformado unicamente por dos digitos.
    Retorna True si es válido, False caso contrario.
    '''
    if len(numero_str) != 2:                                                    # Verifica que el string tenga exactamente dos caracteres
        return False
    for digito in numero_str:                                                   # Itera sobre cada caracter del string
        if digito not in '0123456789':                                          # Verifica que cada caracter sea un dígito numerico
            return False
    return True                                                                 # Si todos los caracteres son dígitos y el string tiene exactamente dos caracteres, retorna True

#6.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2
def stark_menu_principal():
    '''
    Funcion que utiliza un bucle while que se ejecuta hasta que el usuario ingresa una selección valida. Dentro del bucle, se llama a imprimir_menu() para mostrar las opciones de selección, y luego se valida la selección usando la función validar_entero(). Si la selección es válida, se retorna como un entero y el bucle se termina. De lo contrario, se muestra un mensaje de error y el bucle vuelve a empezar.
    '''
    while True:                                                                 # Se crea un bucle infinito que se ejecutará hasta que el usuario ingrese una seleccion válida.
        seleccion = imprimir_menu()                                             # Se llama a la funcion 'imprimir_menu()' para mostrar las opciones de seleccion al usuario y se guarda el resultado en la variable 'seleccion'.
        if validar_entero(seleccion):                                           # Se utiliza la funcion 'validar_entero()' para validar la seleccion del usuario.
            return int(seleccion)                                               # Si la seleccion es válida, se convierte a un entero y se devuelve. Esto termina la ejecucion de la funcion.
        else:
            print("Error: La seleccion debe ser un número entero de 2 dígitos.")   # Si la seleccion no es válida, se imprime un mensaje de error.


#7 Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa. Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente. 
def stark_marvel_app(lista_personajes):
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
                print("Error: La selección debe ser un número entero entre el 01-11")

stark_marvel_app(lista_personajes)
