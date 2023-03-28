'''
from os import system
system("cls") #clear
'''
#lista = range(10) 

# for n in lista:
#     print(n) #muestra numeros del 0 al 9

# for i in lista range(10,-1,-1)
#     print(i)

seguir = "si"
contador_producto = 0
contador_barbijo = 0
contador_jabon = 0
contador_alcohol = 0
contador_mascara = 0

for i in range(5):   #hasta 5veces
# while contador_producto < 5:
    tipo_producto = input("Ingrese el tipo de producto (barbijo, jabón alcohol o mascara): ")
    while tipo_producto != "barbijo" and tipo_producto != "jabón" and tipo_producto != "alcohol" and tipo_producto != "mascara":
        tipo_producto = input("Reingrese el tipo de producto: ")

    precio_producto = float(input("Ingrese el precio del producto: "))
    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
    marca_producto = input("Ingrese la marca del producto: ")
    fabricante_producto = input("Ingrese el nombre del fabricante del producto: ")

    if tipo_producto == "barbijo":
        contador_barbijo += 1
    elif tipo_producto == "jabón":
        contador_jabon += 1
    elif tipo_producto == "mascara":
        contador_mascara += 1
    else:
        contador_alcohol += 1

    #el swich en Python se llama Match
    # match tipo_producto:
    #     case "alcohol":
    #         contador_alcohol += 1
    #     case "barbijo":
    #         contador_barbijo += 1
    #     case "jabón":
    #         contador_jabon += 1
    #     case _:
    #         contador_mascara += 1

    
    

    #procesos...

    # seguir = input("Desea continuar?")
    # if seguir != "si":
    #     break

print(f"se ingresaron: {contador_alcohol} alcohol")
print(f"se ingresaron: {contador_barbijo} barbijo")
print(f"se ingresaron: {contador_jabon} jabon")
print(f"se ingresaron: {contador_alcohol} mascara")






# precio_producto = 5
# if precio_producto > 5:
#     pass
# else:
#     if precio_producto>3 and precio_producto<=5:
#         pass
#     else:
#         pass
# print("lalala")
