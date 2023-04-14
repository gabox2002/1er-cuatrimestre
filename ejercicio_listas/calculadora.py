
def pedir_entero(mensaje, limite_inferior, limite_superior):
    numero = int(input(mensaje))    
    while numero < limite_inferior or numero > limite_superior:
        numero = int(input("Reingrese: "))                   
    return numero

def sumar(num1, num2):#Parametros formales de la función
    '''
    Función que se encargada de pedir dos numeros, sumarlos y mostrar el resultado
    '''
    #Desarrollo de la función
    suma = num1 + num2    
    return suma

def restar(num1, num2):#Parametros formales de la función
    '''
    Función que se encargada de pedir dos numeros, restarlos y mostrar el resultado
    '''
    #Desarrollo de la función
    resta = num1 - num2
    return resta

def multiplicar(num1, num2):
    '''
    Función que se encargada de pedir dos numeros, multiplicarlos y mostrar el resultado
    '''
    #Desarrollo de la función
    multiplicacion = num1 * num2
    return multiplicacion

def dividir(num1, num2):#Parametros formales de la función
    '''
    Función que se encargada de pedir dos numeros, dividirlos, como es imposible dividir por cero 
    se restringue el num2 haciendo la division asignarle None, funciona como bandera, si el num2 es 0, no se cumple la division y muestra None y asi pueda mostrar el resultado
    '''
    #no se puede dividir por cero
    division = None
    if num2 != 0:
        division = num1 / num2
        
    return division

def manipular_menu_principal():
    '''
    Función que muestra el menú principal, me pide una opción y me permite manipular mi calculadora
    '''

    repeticion = True

    while(repeticion):  
        num1 = pedir_entero("Ingrese el primer numero: ",-1000,1000)
        num2 = pedir_entero("Ingrese el segundo numero: ",-1000,1000)

        opcion = pedir_entero("Bienvenido a la calculadora \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5.Salir \nIngrese una opcion: ", 1, 5)

        if opcion == 1:
            #llamada de la funcion  
            resultado = sumar(num1, num2) #Parametros actuales

            print(f"El resultado de la suma es :  {resultado}")
        
        elif opcion == 2:
            #llamada de la funcion  
            resultado = restar(num1, num2) #Parametros actuales

            print(f"El resultado de la resta es :  {resultado}")
                        

        elif opcion == 3:
            #llamada de la funcion  
            resultado = multiplicar(num1, num2) #Parametros actuales

            print(f"El resultado de la multiplicacion es :  {resultado}")
            

        elif opcion == 4:
            resultado = dividir(num1, num2)
            if resultado != None:
                print(f"El resultado de la division es :  {resultado}")
            else:
                print("No se puede dividir por cero")
        
        elif opcion == 5:
            print("Saliendo")
            repeticion = False

        else:
            print("Opcion incorrecta")
            




manipular_menu_principal()           

