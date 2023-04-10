'''
def nombre_de_la_funcion(variable_a, varible_b):
#Cuerpo de la nombre_de_la_funcion
#ralizar un


ejemplo:
def saludar():
    print("Hola mundo")
    
saludar()
#Esta funcion me imprime un hola mundo cada vez que la llame.
#Toda funcion su nombre debe ser un verbo y en snake_case.

'''

def manipular_menu_principal():
    '''
    funcion que me muestra el menu principal, me pide una accion y manipula mi calculadora
    '''
    repeticion = True

    while(repeticion):
        n_uno = pedir_entero("Ingrese el primer numero: ", -1000, 1000)
        n_dos = pedir_entero("ingrese el segundo numero: ", 1000, 75000)
        opcion = pedir_entero("\nBienvenido a la calculadora magica\n1-Sumar\n2-Restar\n3-Divivir\n4-Multiplicar\n5-salir:\n",1,5)
        
        if opcion == 1:
                #llamada a la funcion
                resultado = sumar(n_uno, n_dos)#parametros actuales
                print(f"El resultado de la suma de {n_uno} y {n_dos} es {resultado}")

        elif opcion == 2:
                #llamada a la funcion
                resultado = restar(n_uno, n_dos)#parametros actuales
                print(f"El resultado de la resta de {n_uno} y {n_dos} es {resultado}")
            
        elif opcion == 3:
                #llamada a la funcion
                resultado = dividir(n_uno, n_dos)#parametros actuales
                if resultado != None:
                    print(f"El resultado de la division de {n_uno} y {n_dos} es {resultado}")
                else:
                    print("No se pudo dividir")
        elif opcion == 4:
                #llamada a la funcion
                resultado = multiplicar(n_uno, n_dos)#parametros actuales
                print(f"El resultado de la multiplicacion de {n_uno} y {n_dos} es {resultado}")
        else:
            print("Usted salio del menu")
            break

def pedir_entero(mensaje, limite_inferior, limite_superior):
    numero = input(mensaje)
    numero = int(numero)
    while numero < limite_inferior or numero > limite_superior:
        numero = input("Reingrese numero: ")
        numero = int(numero)
    return numero

def sumar(numero_uno, numero_dos):#parametros formales de la funcion
    #Desarrollo de la funcion
    suma = numero_uno + numero_dos
    return suma

def restar(numero_uno, numero_dos):
    #Desarrollo de la funcion
    resta = numero_uno - numero_dos
    return resta

def dividir(numero_uno, numero_dos):
    #Desarrollo de la funcion
    #no se puede divivir por cero
    division = None
    if numero_dos != 0:
        division = numero_uno / numero_dos
    return division

def multiplicar(numero_uno, numero_dos):
    #Desarrollo de la funcion
    multiplicacion = numero_uno * numero_dos
    return multiplicacion

#####PROGRAMA EN SI:
manipular_menu_principal()


##FUNCIONES MAS USADAS#
# resultado = fx(variable)

# #funciones que no devuelven nada pero reciben algo y viceversa
# fx(variable)
# resultado = fx()

# #funciones que no devuelven nada y no reciben nada
# fx()

