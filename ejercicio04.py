'''Gabriel Quispe Div C Grupo 3 Ejercicio 04
La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.

'''
importe_bruto = 0
total_kilos = 0
total_precio = 0
bandera_mas_cara = True

for i in range(15): 
    peso_producto = float(input("Ingrese el peso del producto: "))
    while peso_producto < 10 or peso_producto > 100:
        peso_producto = float(input("Ingrese el peso del producto: (debe ser entre 10 y 100)"))
    
    precio_kilo = float(input("Ingrese el precio del producto: "))
    while precio_kilo < 0:
        precio_kilo = float(input("Ingrese el precio del producto: (debe ser mayor a cero)"))
    
    tipo_producto = input("Ingrese el tipo de variedad del producto: ")
    while tipo_producto != "vegetal" and tipo_producto != "animal" and tipo_producto != "mezcla":
        tipo_producto = input("Reingrese el tipo de variedad del producto: vegetal, animal, mezcla")
    
    importe_bruto_compra = peso_producto * precio_kilo
    importe_bruto += importe_bruto_compra

    total_kilos += peso_producto
    total_precio += importe_bruto_compra

    if  total_kilos > 300:
        importe_descuento = importe_bruto * 0.75 #25% de descuento
    elif total_kilos > 100:
        importe_descuento = importe_bruto * 0.85 #15% de descuento
    
    if bandera_mas_cara == True or precio_kilo > precio_mas_caro:
        precio_mas_caro = precio_kilo
        tipo_mas_caro = tipo_producto
        bandera_mas_cara = False
            
promedio_precio = total_precio / total_kilos

print(f"A. El importe total a pagar, BRUTO sin descuento es: {importe_bruto:.2f}")
if total_kilos > 100:
    print(f"B. El importe total a pagar con descuento  es: {importe_descuento:.2f}")
else: 
    print(f"B. Al importe total a pagar no le corresponde descuento")
print(f"C. Informar el tipo de alimento más caro es: {tipo_mas_caro}")
print(f"D. El promedio de precio por kilo en total es: {promedio_precio}")