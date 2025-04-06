import tabulate

# Lista para almacenar las reservas
reservas = []

# Variable para llevar el control del código de reserva
codigo_reserva = 1

# Precios base
precio_desayuno = 10.0
precio_noche = 100.0

# Función para agregar una nueva reserva
def agregar_reserva(nombre, habitacion, noches, tipo_habitacion, desayuno):
    global codigo_reserva
    nueva_reserva = {
        'codigo': codigo_reserva,
        'nombre': nombre,
        'habitacion': habitacion,
        'noches': noches,
        'tipo_habitacion': tipo_habitacion,
        'desayuno': desayuno
    }
    reservas.append(nueva_reserva)
    codigo_reserva += 1
    return nueva_reserva

# Función para buscar una reserva por código
def buscar_reserva(codigo):
    for reserva in reservas:
        if reserva['codigo'] == codigo:
            return reserva
    return None

# Función para eliminar una reserva por código
def eliminar_reserva(codigo):
    global reservas
    reservas = [reserva for reserva in reservas if reserva['codigo'] != codigo]

# Función para mostrar todas las reservas simples
def mostrar_reservas():
    if not reservas:
        print("No hay reservas registradas.")
    for reserva in reservas:
        print(f"Código: {reserva['codigo']}, Nombre: {reserva['nombre']}, Habitación: {reserva['habitacion']}, "
              f"Noches: {reserva['noches']}, Tipo de habitación: {reserva['tipo_habitacion']}, "
              f"Desayuno: {'Sí' if reserva['desayuno'] else 'No'}")

# Función para calcular el costo total de una reserva
def calcular_costo_total(reserva):
    costo_total = reserva['noches'] * precio_noche
    if reserva['desayuno']:
        costo_total += reserva['noches'] * precio_desayuno
    return costo_total

# Función para mostrar el costo total de una reserva
def mostrar_costo_total(codigo):
    reserva = buscar_reserva(codigo)
    if reserva:
        costo_total = calcular_costo_total(reserva)
        print(f"Costo total de la reserva {codigo}: ${costo_total:.2f}")
    else:
        print("Reserva no encontrada.")

# Función para mostrar todas las reservas en tabla
def mostrar_reservas_completas():
    if not reservas:
        print("No hay reservas registradas.")
        return
    headers = ['Código', 'Nombre', 'Habitación', 'Noches', 'Tipo de habitación', 'Desayuno', 'Costo Total']
    table = []
    for reserva in reservas:
        costo_total = calcular_costo_total(reserva)
        table.append([
            reserva['codigo'],
            reserva['nombre'],
            reserva['habitacion'],
            reserva['noches'],
            reserva['tipo_habitacion'],
            'Sí' if reserva['desayuno'] else 'No',
            f"${costo_total:.2f}"
        ])
    print(tabulate.tabulate(table, headers=headers, tablefmt='grid'))

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú de Reservas ---")
    print("1. Agregar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Mostrar reservas simples")
    print("5. Mostrar reservas completas (tabla)")
    print("6. Mostrar costo total de una reserva")
    print("7. Salir")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del huésped: ")
            try:
                habitacion = int(input("Ingrese el número de habitación: "))
                noches = int(input("Ingrese el número de noches de estadía: "))
            except ValueError:
                print("Error: Debe ingresar números válidos para habitación y noches.")
                continue
            tipo_habitacion = input("Ingrese el tipo de habitación: ")
            desayuno = input("¿Desea incluir desayuno? (s/n): ").lower() == 's'
            reserva = agregar_reserva(nombre, habitacion, noches, tipo_habitacion, desayuno)
            print(f"Reserva agregada con éxito. Código asignado: {reserva['codigo']}")
        elif opcion == '2':
            try:
                codigo = int(input("Ingrese el código de la reserva a buscar: "))
                reserva = buscar_reserva(codigo)
                if reserva:
                    print(f"Reserva encontrada: {reserva}")
                else:
                    print("Reserva no encontrada.")
            except ValueError:
                print("Código inválido.")
        elif opcion == '3':
            try:
                codigo = int(input("Ingrese el código de la reserva a eliminar: "))
                eliminar_reserva(codigo)
                print("Reserva eliminada.")
            except ValueError:
                print("Código inválido.")
        elif opcion == '4':
            mostrar_reservas()
        elif opcion == '5':
            mostrar_reservas_completas()
        elif opcion == '6':
            try:
                codigo = int(input("Ingrese el código de la reserva: "))
                mostrar_costo_total(codigo)
            except ValueError:
                print("Código inválido.")
        elif opcion == '7':
            print("Gracias por usar el sistema de reservas. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
