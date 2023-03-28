# Ejercicio 02
# Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
# python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
# al ingresar el número debemos mostrarle que regla de estilo representa y su
# descripción (Sacar la información de las diapositivas de las reglas de estilo).
# En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
# “Error, regla de estilo inexistente”

numero = int(input("Ingrese un número entre el 1 y el 8: "))

if numero == 1:
    print("La primera regla de estilo es: ¿Cuál es el sentido?")
elif numero == 2:
    print("La segunda regla de estilo es: ¿Qué es PEP?")
elif numero == 3:
    print("La tercera regla de estilo es: ¿Qué es PEP8?")
elif numero == 4:
    print("La cuarta regla de estilo es: El indentado")
elif numero == 5:
    print("La quinta regla de estilo es: El tamaño máximo linea")
elif numero == 6:
    print("La sexta regla de estilo es: La línea en blanco")
elif numero == 7:
    print("La septima regla de estilo es: Los comentarios")
elif numero == 8:
    print("La octava regla de estilo es: Los nombres")
else:
    print("Error regla de estilo inexistente")

