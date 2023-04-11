'''
Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista.
'''
numeros = []

while True:
    entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")
    if entrada == "fin":
        break
    numeros.append(int(entrada))

mayor_ocurrencia = 0
posicion_mayor_ocurrencia = None

for i, num in enumerate(numeros):
    ocurrencias = numeros.count(num)
    if ocurrencias > mayor_ocurrencia:
        mayor_ocurrencia = ocurrencias
        posicion_mayor_ocurrencia = i

print(f"La posición de memoria con más ocurrencias es: {posicion_mayor_ocurrencia}")