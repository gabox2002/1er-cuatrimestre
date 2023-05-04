#LISTAS
'''
lista = [5,9,8,7,3,6,4,5,5]
print(lista)
print(f"Elemento 3: {lista[3]}")
print(lista[0:3]) #[Desda:Hasta]  Desde: Inclusivo / Hasta: Excluyente (Muestra solo 1,2,3)
print(lista[3:5]) #Muestra el 4, 5  (el 6 no porque es excluido)

#for i in range(len(lista)):     #recorre la lista
#    print(lista[i])

acumulador = 0
contador = 0
for i in range(len(lista)):     #recorre la lista
    acumulador = acumulador + lista[i]
    if(lista[i]== 5): #ver cuantas veces se ingreso el 5
        contador += 1

    print(acumulador)
    print(contador)
    
lista.append(100)    #agregar a la lista
lista.append(55)
print(lista)

lista.insert(2,999)  #modificar un index de la lista añade(indice: 2, valornuevo: 999) 
print(lista)

lista.extend([999,888,777]) #agregar unaa la lista nueva
print(lista)

lista.remove(8) #remover un elemento (borra la primera ocurrencia del valor)
print(lista)

print(lista.index(999)) #saber en que indice esta el valor 999 primera ocurrencia

for numero in lista:  #recorre la lista y se guarda en "NUMERO" NO PUEDO MODIFICARLO
    print(numero)

for i in range(len(lista)):          #muestra listado  PUEDO MODIFICAR la lista
    print(f"{i+1}->{lista[i]}")    

'''
###############################################
'''
#DICCIONARIO
mi_diccionario = {}

mi_diccionario ["Nombre"] = "Juan"

print(type(mi_diccionario))
print(mi_diccionario["Nombre"])

mi_diccionario["Edad"] = 25
print(mi_diccionario["Edad"])

print(mi_diccionario)

otro_diccionario = {"Nombre":"Luis", "Edad":32} #otra forma de definir diccionario
print(otro_diccionario)

#diccionario es iterable, recorrerlo usando un FOR
for key in otro_diccionario:
    print(key)

for key in otro_diccionario:
    #print(otro_diccionario[key])
    print(f"{key}->{otro_diccionario[key]}")

for valor in otro_diccionario:
    #print(otro_diccionario[key])
    print(f"{otro_diccionario[key]}")
'''
###################################################################
#LISTAS PARALELAS
'''
CANTIDAD_ALUMNOS = 3   #lista de 3elementos, representan nombre y otra apellidos
lista_nombres = []
lista_apellidos = []

for i in range(CANTIDAD_ALUMNOS):
    nombre = input ("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

for i in range(CANTIDAD_ALUMNOS):
    print(f"{i+1}) Nombre: {lista_nombres[i]} - Apellido: {lista_apellidos[i]}")
'''
###################################################################

# lista_alumnos = [{"Nombre":"Juan", "Apellido":"Lopez", "Edad":25},
#                  {"Nombre":"Luis", "Apellido":"Lopez", "Edad":36},
#                  {"Nombre":"Maria", "Apellido":"Lopez","Edad":23},
#  ]
CANTIDAD_ALUMNOS = 3
lista_alumnos = []

# for i in range(CANTIDAD_ALUMNOS):
#     nombre = input("Ingrese nombre: ")
#     apellido = input("Ingrese apellido: ")
#     edad = int(input("Ingrese edad: "))
#     un_alumno = {}          #Crear diccionario dentro del for
#     un_alumno["Nombre"] = nombre
#     un_alumno["Apellido"] = apellido
#     un_alumno["Edad"] = edad
#     lista_alumnos.append(un_alumno) #hacer que el diccionario se guarde en la lista con APPEND

# print(lista_alumnos)

#[{'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 25}, {'Nombre': 'Luis', 'Apellido': 'Gomez', 'Edad': 64}, {'Nombre': 'maria', 'Apellido': 'Ruiz', 'Edad': 36}]

# for alumno in lista_alumnos:
#     edad = alumno["Edad"]
#     if edad > 30:
#         print(f"{alumno['Apellido']}-{alumno['Nombre']}-{edad}")

##############

lista_alumnos_compleja = [
    {'nombre': 'pep', 'apellido':'argento', 'dni': '33', 'materias': ['matematica','literatura']},
    {'nombre': 'moni', 'apellido':'argento', 'dni': '33', 'materias': ['matematica','literatura']},
    {'nombre': 'pep', 'apellido':'argento', 'dni': '33', 'materias': ['matematica','literatura']}
]

# ##########################LISTAS###########################
# #DEFINICION E INICIALIZACION DE UNA LISTA DE UNA LISTA
lista = [1,2,3,4,5,6]
print(lista)
# #TOMAR ELEMENTOS DESDE-HASTA
print(lista[0:3]) #[desde,hasta]->el desde es inclusivo, el hasta es exclusive
print(lista[3:5])
# #TRAER ELEMENTOS DESDE ATRAS
print(lista[-1])


# #AGREGAR ELEMENTOS A LA LISTA (PUEDE ESTAR VACIA O NO)
mi_lista = []
mi_lista.append(7) #AGREGAR ELEMENTO AL FINAL DE LA LISTA
mi_lista.append(8)
mi_lista.append(3)
mi_lista.append(2)
print(mi_lista)
mi_lista.insert(2,100) #SETEA EL VALOR 8 EN LA POSICION 2
print(mi_lista)
mi_lista.extend([9,10,11]) #AGREGA UNA LISTA AL FINAL DE LA LISTA PRINCIPAL
print(mi_lista)

# #REMOVER ELEMENTOS DE LA LISTA

mi_lista.remove(8) #REMUEVE LA PRIMER OCURRENCIA DEL ELEMENTO DE VALOR 8
print(mi_lista)

# #OBTENER EL INDICE DE UN ELEMENTO
print("Indice donde encuentro el valor 3:", mi_lista.index(3))

# #RECORRER UNA LISTA

for numero in mi_lista:
    print(f"Elemento->{numero}")

# ##########################DICCIONARIOS###########################
# #DECLARACION DE UN DICCIONARIO
mi_diccionario = {} #CLAVE-VALOR

mi_diccionario["clave"] = 10 #CREO UNA CLAVE Y LE ASIGNO UN VALOR 
print(mi_diccionario["clave"])
mi_diccionario["nombre"] = "Juan"
print(mi_diccionario["nombre"])

# #OTRA FORMA DE CREAR UN DICCIONARIO

otro_diccionario = {"nombre":"Juan","apellido":"Gomez","edad":25}
print(otro_diccionario) 

# #RECORRIENDO CLAVES DE UN DICCIONARIO

for key in otro_diccionario:
    print(key)

#RECORRIENDO VALORES DE UN DICCIONARIO A PARTIR DE SU CLAVE

for key in otro_diccionario:
    print(otro_diccionario[key])

##########################LISTAS PARALELAS###########################
#Para comenzar: pedirle al usuario que ingrese nombre y apellido de 5 alumnos.
CANTIDAD_ALUMNOS = 5
lista_nombres = []
lista_apellidos = []
#lista_notas = []
#lista_mails = []
#lista_promedios = [] ...

for i in range(CANTIDAD_ALUMNOS):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

for i in range(CANTIDAD_ALUMNOS):
    print(f"{i})Nombre: {lista_nombres[i]} - Apellido: {lista_apellidos[i]}")

#########################LISTAS CON DICCIONARIOS ANIDADOS########################
#RECONVERTIMOS EL EJERCICIO ANTERIOR:

lista_alumnos = []
for i in range(3):
    un_alumno = {}
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    dni = input("Ingrese el dni: ")
    un_alumno["nombre"] = nombre
    un_alumno["apellido"] = apellido
    un_alumno["dni"] = dni
    lista_alumnos.append(un_alumno)

print(lista_alumnos) #Con esto despues me robo los datos y los asigno a la lista (hardcodear)

for alumno in lista_alumnos:
    print(alumno)#Muestro cada dic de la lista

#RECORREMOS LA LISTA ACCEDIENDO A CADA CLAVE DEL DICCIONARIO
lista_alumnos = [{'nombre': 'pep', 'apellido': 'argento', 'dni': '33'},
{'nombre': 'moni', 'apellido': 'ruiz', 'dni': '99'},
{'nombre': 'coqui', 'apellido': 'luz', 'dni': '77'}]
print("Apellido-Nombre-DNI")
for alumno in lista_alumnos:
    apellido = alumno["apellido"]
    nombre = alumno["nombre"]
    dni = alumno["dni"]
    print(f"{apellido} - {nombre} - {dni}")

#Y SI UNA DE LAS CLAVES REPRESENTA UNA LISTA???
lista_alumnos_compleja = [
    {'nombre': 'pep', 'apellido': 'argento', 'dni': '33', 'materias':['matematica','literatura']},
    {'nombre': 'moni', 'apellido': 'ruiz', 'dni': '99', 'materias':['ingles','matematica','biologia']},
    {'nombre': 'coqui', 'apellido': 'luz', 'dni': '77', 'materias':['ingles']}
]
