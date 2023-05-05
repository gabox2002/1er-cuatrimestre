# lista_pokemones = [{'N° Pokedex': '149', 'Nombre': 'Dragonite', 'Tipo': ['Dragón', 'Volador'], 'Poder de Ataque': '134', 'Poder de Defensa': '95', 'Habilidades': ['Enjambre', 'Cambio color']}, {'N° Pokedex': '150', 'Nombre': 'Mewtwo', 'Tipo': ['Psíquico'], 'Poder de Ataque': '110', 'Poder de Defensa': '90', 'Habilidades': ['Presión', 'Ninguna']}, {'N° Pokedex': '151', 'Nombre': 'Mew', 'Tipo': ['Psíquico'], 'Poder de Ataque': '100', 'Poder de Defensa': '100', 'Habilidades': ['Sincronía', 'Ninguna']},{'N° Pokedex': '043', 'Nombre': 'Oddish', 'Tipo': ['Planta', 'Veneno'], 'Poder de Ataque': '50', 'Poder de Defensa': '55', 'Habilidades': ['Clorofila', 'Clorofila']}] 

# print(lista_pokemones)

import csv
import re

def cargar_pokemones(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        archivo = csv.reader(archivo, delimiter=',')
        next(archivo) # Descartamos la primera fila (cabecera)
        pokemones = []
        tipos = {}
        habilidades = {}
        for line in archivo:
            try:
                campos = [re.split(",|\n", campo)[0] for campo in line]
                pokedex, nombre, tipo_str, ataque, defensa, habilidades_str = campos
                tipo = tipo_str.split('/')
                habilidades = set(habilidades_str.split('|*|'))
                pokemon = {
                    'N° Pokedex': pokedex,
                    'Nombre': nombre,
                    'Tipo': tipo,
                    'Poder de Ataque': ataque,
                    'Poder de Defensa': defensa,
                    'Habilidades': habilidades
                }
                pokemones.append(pokemon)
                for t in tipo:
                    if t not in tipos:
                        tipos[t] = []
                    tipos[t].append(pokemon)
                for h in habilidades:
                    if h not in habilidades:
                        habilidades[h] = []
                    habilidades[h].append(pokemon)
            except (IndexError, ValueError) as e:
                print(f'Error al procesar la línea {line}: {str(e)}')
    return pokemones, tipos, habilidades

def listar_pokemones(pokemones):
    for pokemon in pokemones:
        print(f'{pokemon["N° Pokedex"]} - {pokemon["Nombre"]}')

def listar_tipos(tipos):
    for tipo in tipos:
        print(tipo)

def listar_habilidades(habilidades):
    for habilidad in habilidades:
        print(habilidad)

ruta_archivo = 'pokemones.csv'
pokemones, tipos, habilidades = cargar_pokemones(ruta_archivo)

while True:
    print('---- MENU ----')
    print('1. Listar Pokemones')
    print('2. Listar Tipos')
    print('3. Listar Habilidades')
    print('4. Salir')
    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        listar_pokemones(pokemones)
    elif opcion == '2':
        listar_tipos(tipos)
    elif opcion == '3':
        listar_habilidades(habilidades)
    elif opcion == '4':
        break
    else:
        print('Opción inválida.')