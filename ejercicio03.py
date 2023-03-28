'''
Gabriel Quispe Div C Grupo 3 Ejercicio 03
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)
'''

seguir = "si"
edad_femenino = 0
votos_femeninos = 0
votos_totales = 0
cantidad_votos_masculinos = 0
voto_julieta = 0
voto_marcos = 0
voto_nacho = 0
bandera_joven = True

while seguir:
    nombre_votante = input("Ingrese su nombre: ")
    edad_votante = int(input("Ingrese su edad: "))
    while edad_votante < 13:
        edad_votante = int(input("Reingrese su edad (solo mayores a 13): "))
    genero_votante = input("Ingrese su género: ")
    while genero_votante != "masculino" and genero_votante != "femenino" and genero_votante != "otro":
        genero_votante = input("Reingrese su género: ")
    voto_elegido = input("Ingrese a quien le dará su voto positivo: ")
    while voto_elegido != "Nacho" and voto_elegido != "Julieta" and voto_elegido != "Marcos":
        voto_elegido = input("Reingrese algún finalista Nacho, Julieta o Marcos")
    
    if genero_votante == "femenino":
        edad_femenino += edad_votante
        votos_femeninos += 1

    if genero_votante == "masculino" and 25 <= edad_votante <= 40 and (voto_elegido == "Nacho" or voto_elegido == "Julieta"):
        cantidad_votos_masculinos += 1

    if voto_elegido == "Nacho":
        if bandera_joven == True or edad_votante < edad_joven_nacho:
            edad_joven_nacho = edad_votante
            nombre_joven_nacho = nombre_votante  
            bandera_joven = False  

    if voto_elegido == "Julieta":
        voto_julieta += 1
    elif voto_elegido == "Marcos":
        voto_marcos += 1
    else:
        voto_nacho += 1

    if voto_julieta > voto_marcos and voto_julieta > voto_nacho:
        ganador_reality = "Julieta"
    elif voto_marcos > voto_nacho:
        ganador_reality = "Nacho"
    else:
        ganador_reality = "Marcos"

    votos_totales += 1 

    seguir = input("Desea ingresar otro voto?")

if votos_femeninos > 0:
    promedio_femenino = edad_femenino / votos_femeninos
else:
    promedio_femenino = "No se puede calcular el promedio de la edad de votantes femeninos"

porcentaje_julieta = voto_julieta * 100 / votos_totales
porcentaje_marcos = voto_marcos * 100 / votos_totales
porcentaje_nacho = voto_nacho * 100 / votos_totales


print(f"A. El promedio de edad de las votantes de género femenino es: {promedio_femenino} años")
print(f"B. La cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta fueron: {cantidad_votos_masculinos}")

if bandera_joven == True:
    print(f"C. El nombre del votante más joven que votó a Nacho es: {nombre_joven_nacho}")
else:
    print(f"C. No se encontró el nombre de algún votante que haya votado a Nacho")

print(f"D. Nombre de cada participante y porcentaje de los votos qué recibió.: Julieta con {porcentaje_julieta:.2f}, Marcos con {porcentaje_marcos:.2f} y Nacho con {porcentaje_nacho:.2f}")
print(f"E. El nombre del participante que ganó el reality es: {ganador_reality}")

