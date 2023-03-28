'''
Ejercicio 01
#La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de una compra de productos de prevención de contagio, de cada una debe obtener los siguientes datos:
# · El tipo (barbijo jabón o alcohol)
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de stock.
'''

tipo_producto = input("Ingrese el tipo de producto (barbijo, jabón o alcohol): ")
while (tipo_producto != "barbijo" and tipo_producto != "jabón" and tipo_producto != "alcohol"):
    tipo_producto = input("Reingrese el tipo de producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
marca_producto = input("Ingrese la marca del producto: ")
fabricante_producto = input("Ingrese el nombre del fabricante del producto: ")

print("El tipo de producto es: {0}".format(tipo_producto))
print("El precio es: {:.2f}".format(precio_producto))
print("La cantidad es: {0}".format(cantidad_unidades))
print("La marca es: {0}".format(marca_producto))
print("El fabricante es: {0}".format(fabricante_producto))