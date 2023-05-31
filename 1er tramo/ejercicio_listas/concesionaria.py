'''Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock deautos que tienen disponible a la venta. Para esto se necesita saber de cada auto: 
la marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código.
'''
from os import system
system("cls") 

lista_autos = []
seguir = "si"

while seguir == "si":
    marca = input("Ingrese la marca del auto: ")
    año = int(input("Ingrese el año del modelo: "))
    while año < 0:
        año = int(input("Reingrese el año del modelo: "))
    precio = float(input("Ingrese el precio del auto: "))
    while precio < 0:
        precio = float(input("Reingrese el precio del auto: "))
    
    lista_autos.append({"marca": marca, "año": (año), "precio":(precio)})
    seguir = input("Desea ingresar otro auto? (si/no)")

print("Datos de todos los autos: ")
for auto in lista_autos:
    print(f"Marca: {auto['marca']}")
    print(f"Año del modelo: {auto['año']}")
    print(f"Precio: {auto['precio']: .2f}")