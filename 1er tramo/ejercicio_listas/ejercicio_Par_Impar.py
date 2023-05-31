'''
Crear una función que permita determinar si un número es par o no. 
La función retorna 1 en caso afirmativo y 0 en caso contrario. 
Probar la funcion
'''

def par(numero):
    if numero % 2 == 0:
        return 1
    else:
        return 0
    
numero = int(input("Ingresa un número: "))
resultado = par(numero)
if resultado == 1:
    print("El número es par")
else:
    print("El número es impar")