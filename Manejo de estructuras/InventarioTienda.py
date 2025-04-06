'''
 Ejercicio 2: Inventario de Tienda de Abarrotes
Un tendero desea registrar productos con su código, nombre, categoría (granos, bebidas, aseo),
cantidad disponible y precio por unidad. Se deben poder:
1. Registrar varios productos
2. Buscar un producto por su código
3. Calcular el valor total del inventario por categoría (Cereza del pastel)


 '''
# Importamos las librerias importantes para el sistema

import tabulate # Genera la tabla de productos
import random # Genera un numero aleatorio para el codigo del producto
import string # Genera un string aleatorio para el nombre del producto
import datetime # Genera la fecha de registro del producto


# Definimos la clase Producto para representar los productos de la tienda

productos = [] # Lista para almacenar los productos

class Producto:
    def __init__(self, codigo, nombre, categoria, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio = precio
        self.fecha_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Fecha de registro del producto

    def __str__(self):
        return f"Producto(codigo={self.codigo}, nombre={self.nombre}, categoria={self.categoria}, cantidad={self.cantidad}, precio={self.precio}, fecha_registro={self.fecha_registro})"
    
# Definimos la función para generar un código aleatorio para el producto
def generar_codigo():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) # Genera un codigo aleatorio de 6 caracteres alfanumericos

# Definimos la función para registrar un producto
def registrar_producto():
    codigo = generar_codigo() # Genera un codigo aleatorio para el producto
    nombre = input("Ingrese el nombre del producto: ") # Solicita el nombre del producto al usuario
    categoria = input("Ingrese la categoria del producto (granos, bebidas, aseo): ") # Solicita la categoria del producto al usuario
    cantidad = int(input("Ingrese la cantidad disponible: ")) # Solicita la cantidad disponible al usuario
    precio = float(input("Ingrese el precio por unidad: ")) # Solicita el precio por unidad al usuario

    # Creamos una instancia de Producto y la agregamos a la lista de productos
    nuevo_producto = Producto(codigo, nombre, categoria, cantidad, precio)
    productos.append(nuevo_producto)
    print(f"Producto registrado con éxito: {nuevo_producto}")


# Definimos la función para buscar un producto por su código
buscar_producto = None
def buscar_producto(codigo):
    for producto in productos:
        if producto.codigo == codigo:
            return producto
    return None

# Definimos la función para calcular el valor total del inventario por categoria
def calcular_valor_total_categoria(categoria):
    total = 0
    for producto in productos:
        if producto.categoria == categoria:
            total += producto.cantidad * producto.precio
    return total


# Definimos la función para mostrar el inventario

def mostrar_inventario():
    if not productos:
        print("No hay productos registrados.")
    else:
        # Creamos una lista de listas para mostrar el inventario
        inventario = [[producto.codigo, producto.nombre, producto.categoria, producto.cantidad, producto.precio, producto.fecha_registro] for producto in productos]
        # Mostramos el inventario en forma de tabla
        print(tabulate.tabulate(inventario, headers=["Código", "Nombre", "Categoría", "Cantidad", "Precio", "Fecha de Registro"], tablefmt="grid"))

# Definimos la función principal para el menú del sistema
def menu():
    while True:
        print("\nMenu de opciones:")
        print("1. Registrar producto")
        print("2. Buscar producto por código")
        print("3. Calcular valor total del inventario por categoría")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            codigo = input("Ingrese el código del producto a buscar: ")
            producto = buscar_producto(codigo)
            if producto:
                print(f"Producto encontrado: {producto}")
            else:
                print("Producto no encontrado.")
        elif opcion == "3":
            categoria = input("Ingrese la categoría para calcular el valor total: ")
            total = calcular_valor_total_categoria(categoria)
            print(f"Valor total del inventario en la categoría '{categoria}': ${total:.2f}")
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

#Finalmente, llamamos a la función menu para iniciar el sistema
if __name__ == "__main__":
    menu()
# Fin del código
