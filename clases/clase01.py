# print("lalala")
''' 3apostofres para comentar
condicion = 5

if (condicion < 5 and   
    condicion != 4):
    print("hola")
print("estoy afuera")

if(3 > 5):
    reultado = 5 + 9 * 2                                          

'''
# evitar nombrar variables asi:
# numero_1 = 7
# numero_uno = 7
# nombre_del_titular = "pepe"
# primer_numero =7
# booleano = True

un_numero = 7.25

cadena = str(un_numero)
print(type(cadena))

# print(type(3.14)) #TYPE nos dice que tipo de variable es

# print(dir(booleano)) #Nos dice que podemoa hacer con esos datos, metodos



# mejor se puede escribir asi:
# un_numero = 7
# otro_numero = 10


nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso: "))

if peso > 75:
    peso= peso * 1.20
else:
    peso = peso * 0.8


# print(type(peso))

# print("su nombre es: {0}".format(nombre))
# print("ud pesa: {0}".format(peso))
# print("ud pesa: {:.2f}".format(peso)) #para mostrar con 2decimales

print(f"su nombre es: {nombre}")
print(f"su peso es: {peso}")
print(f"su peso es: {peso:.2f}") #con 2decimales





    