'''
3) Copa pistón!!!
Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
Se pedirá el ingreso de:
nombre
edad (mayor a 18)
nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
cantidad de carreras ganadas (no pueden ser números negativos)
número del vehículo (no puede ser un número negativo)
se necesita saber:
A. Nacionalidad del piloto más joven.
B. Cantidad de vehículos con número par.
C. Nombre del piloto con menos victorias y el número de auto impar.
D. Cantidad de pilotos mayores de 25 años con número de vehículo impar.
E. Nombre del piloto más joven con más victorias.
F. Nacionalidad del piloto más veterano con menos victorias.
G. Promedio de edad de los pilotos que tiene un vehículo con número par.

'''
bandera_mas_joven = True
cantidad_vehiculo_par = 0
bandera_piloto_menos_victorias = True
cantidad_pilotos_mayores_impar = 0

for i in range(2): #fijarse con 10 integrantes
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        edad = int(input("Reingrese su edad (Solo mayor a 18): "))
    nacionalidad = input("Ingrese su nacionalidad: argentino, inglés, francés, brasilero, estadounidense ")
    while nacionalidad != "argentino" and nacionalidad !="inglés" and nacionalidad !="francés" and nacionalidad !="brasilero" and nacionalidad !="estadounidense":
        nacionalidad = input("Reingrese su nacionalidad: argentino, inglés, francés, brasilero, estadounidense ")
    carreras_ganadas = int(input ("Ingrese cantidad de carreras ganadas: "))
    while carreras_ganadas < 0:
        carreras_ganadas = int(input ("Reingrese cantidad de carreras ganadas: (No puede ser negativo)"))
    numero_vehiculo = int(input("Ingrese el número del vehículo: "))
    while numero_vehiculo < 0:
        numero_vehiculo = int(input("Reingrese el número del vehículo: (no puede ser números negativos)"))


    #A. Nacionalidad del piloto más joven.
    if bandera_mas_joven == True or edad > edad_mas_joven:
        edad_mas_joven = edad
        nacionalidad_piloto_mas_joven = nacionalidad
        bandera_mas_joven = False

    #B. Cantidad de vehículos con número par.
    if numero_vehiculo % 2 == 0:
        cantidad_vehiculo_par += 1

    #C. Nombre del piloto con menos victorias y el número de auto impar.
    if bandera_piloto_menos_victorias == True or carreras_ganadas < carreras_menos_victoria:
        carreras_menos_victoria = carreras_ganadas
        nombre_piloto_menos_victoria = nombre
        bandera_mas_joven = False
        if numero_vehiculo % 2 != 0:
            numero_impar_menos_victorias = numero_vehiculo

    #D. Cantidad de pilotos mayores de 25 años con número de vehículo impar.
    if edad > 25 and numero_vehiculo %2 != 0:
        cantidad_pilotos_mayores_impar += 1
   
    #E. Nombre del piloto más joven con más victorias.
    if carreras_ganadas < cantidad_ganadas_mas_joven and edad < edad_mas_joven
    
        





print(f"A. La nacionalidad del piloto más joven es: {nacionalidad_piloto_mas_joven}")
print(f"B. LA cantidad de vehículos con número par es: {cantidad_vehiculo_par}")
print(f"C. El nombre del piloto con menos victorias es {nombre_piloto_menos_victoria} y el número de auto impares es: {numero_impar_menos_victorias}")
print(f"D. La cantidad de pilotos mayores de 25 años con número de vehículo impar es: {cantidad_pilotos_mayores_impar}")




