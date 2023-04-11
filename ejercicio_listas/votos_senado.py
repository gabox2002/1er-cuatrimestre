'''
Debemos desarrollar un algoritmo que permita computar los votos del Senado de
Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
la sesión. Si el senador está presente, se deberá pedir el valor del voto
El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
(validar). El valor por defecto para los senadores ausentes será Abstención.
Se deberá Informar:

o Cantidad total de senadores.
o Cantidad de senadores presentes.
o Cantidad y porcentaje de votos afirmativos.
o Cantidad y porcentaje de votos negativos.
o Cantidad y porcentaje de abstenciones.
o Generar una lista de senadores por cada tipo de voto y mostrarlas por
pantalla.
'''
from os import system
system("cls") 

senadores = {}       #Se utiliza un diccionario senadores para almacenar el voto de cada senador 
votos_afirmativos = []  #tres listas para guardar los nombres de los senadores que votaron afirmativo, negativo y abstención, respectivamente.
votos_negativos = []
votos_abstencion = []
presentes = 0
total_senadores = int(input("Ingrese la cantidad total de senadores: "))

for i in range(total_senadores):
    nombre = input(f"Ingrese el nombre del senador {i+1} o 'no' para salir: ")
    if nombre == "no":
        break
    presente = input(f"¿Está presente el senador {nombre}? (s/n): ")
    if presente() == 's':
        presentes += 1
        voto = input(f"¿Cuál es el voto del senador {nombre}? (a/n): ")
        while voto() not in ['a', 'n']:
            voto = input("Voto inválido. Ingrese 'a' para afirmativo, 'n' para negativo: ")
        if voto() == 'a':
            votos_afirmativos.append(nombre)
        else:
            votos_negativos.append(nombre)
    else:
        votos_abstencion.append(nombre)
    senadores[nombre] = voto() if presente() == 's' else 'abstencion'

print(f"Cantidad total de senadores: {total_senadores}")
print(f"Cantidad de senadores presentes: {presentes}")

cant_votos_afirmativos = len(votos_afirmativos)
porc_votos_afirmativos = (cant_votos_afirmativos / presentes) * 100 if presentes > 0 else 0
print(f"Cantidad de votos afirmativos: {cant_votos_afirmativos} ({porc_votos_afirmativos:.2f}%)")

cant_votos_negativos = len(votos_negativos)
porc_votos_negativos = (cant_votos_negativos / presentes) * 100 if presentes > 0 else 0
print(f"Cantidad de votos negativos: {cant_votos_negativos} ({porc_votos_negativos:.2f}%)")

cant_votos_abstencion = len(votos_abstencion)
porc_votos_abstencion = (cant_votos_abstencion / (total_senadores - presentes)) * 100 if total_senadores - presentes > 0 else 0
print(f"Cantidad de abstenciones: {cant_votos_abstencion} ({porc_votos_abstencion:.2f}%)")

print("Lista de senadores que votaron afirmativo:")
print(votos_afirmativos)

print("Lista de senadores que votaron negativo:")
print(votos_negativos)

print("Lista de senadores que se abstuvieron:")
print(votos_abstencion)