# Ejercicio 01
#La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de una compra de productos de prevención de contagio, de cada una debe obtener los siguientes datos:
# · El tipo (barbijo jabón o alcohol)
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de stock.

tipo = input("Ingrese el tipo de producto (barbijo, jabón o alcohol): ")
while ( tipo != "barbijo" and tipo != "jabón" and tipo != "alcohol"):
    tipo = input("Reingrese el tipo de producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))
marca = input("Ingrese la marca del producto: ")
fabricante = input("Ingrese el nombre del fabricante del producto: ")

print("El tipo de producto es: {0}".format(tipo))
print("El precio es: {0}".format(precio))
print("La cantidad es: {0}".format(cantidad))
print("La marca es: {0}".format(marca))
print("El fabricante es: {0}".format(fabricante))