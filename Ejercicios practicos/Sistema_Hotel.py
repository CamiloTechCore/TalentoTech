'''Un pequeño hotel necesita llevar el registro de sus reservas. Por cada huésped se debe almacenar su nombre, número de habitación, noches de estadía, tipo de habitación y si desea incluir desayuno. Cada reserva debe tener un código único que permita su posterior búsqueda.'''

import tabulate # Importar la librería tabulate para mostrar tablas
list = [] # Lista para almacenar las reservas


# Definición de la clase Reserva diccionario 

precios= {
    "simple": 80000,
    "doble": 140000,
    "suite": 250000
}


precios_desayuno = 30000 # Precio del desayuno por persona

contador = 1 # Contador para generar códigos únicos

# menu

while (True):

    print("\t\t\t!!Sistema de Reservas Hotel!!\n")
    nombre =input("Ingrese el nombre del huesped: ").capitalize()
    numero_habitacion = input("Ingrese el número de habitación: ")
    noches = int(input("Ingrese el número de noches de estadía: "))
    habitacion = input("Ingrese el tipo de habitación (simple, doble, suite): ").lower()
    precios_desayuno = input("¿Desea incluir desayuno? (si/no): ").lower()

    codigo_reserva = f"R{contador:03}" # Generar código único para la reserva R0001
    contador +=1 # Incrementar el contador para la próxima reserva


    reserva = {
        "codigo_reserva": codigo_reserva,
        "nombre": nombre,
        "numero_habitacion": numero_habitacion,
        "noches": noches,
        "habitacion": habitacion,
        "precios_desayuno": precios_desayuno
    }
    list.append(reserva) # Agregar la reserva a la lista de reservas
    print(f" la reserva se ha realizado con éxito, su código es: {codigo_reserva}")
   

    print("\t\t\t!!Sistema de Reservas Hotel!!\n")
    
    tabla_reserva =[[
        r["codigo_reserva"],
        r["nombre"],
        r["numero_habitacion"],
        r["noches"],
        r["habitacion"],
        r["precios_desayuno"]
    ] for r in list]
    print("¿Desea realizar otra reserva? (si/no): ") 
    print(reserva) # Mostrar reservas actuales   
    respuesta = input().lower()
    if respuesta == "no":
        print(tabulate.tabulate(tabla_reserva, headers=["Código Reserva", "Nombre", "Número Habitación", "Noches", "Tipo Habitación", "Desayuno"], tablefmt="grid")) # Mostrar reservas en formato tabla
        break
    