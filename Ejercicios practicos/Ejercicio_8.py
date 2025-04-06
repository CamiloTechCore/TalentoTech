'''
8.	Una agencia de modelaje realizo una convocatoria para contratar modelos para un comercial. Para ser contratado, debe cumplir las siguientes condiciones, de lo contrario será descartado. Debe ser hombre y con una edad inferior o igual a 20 y con una estatura superior o igual a 1.75 y con un peso inferior o igual 70 y los ojos deben ser color azul.
'''

# Definimos las condiciones para ser contratado

contratado = False

sexo = input("Ingrese su sexo (H = hombre o M = Mujer):").upper()

edad = int(input("Ingrese su edad: "))

estatura = float(input("ingrese su estatura en cm: "))

peso = float(input("Ingrese su peso en GR:"))

# validamos las condiciones para ser contratado

if sexo == "H" and edad <= 20 and estatura >= 175 and peso <= 70000:
    ojos = input("Ingrese el color de sus ojos (A = azul, M = marron, V = verde):").upper()
    if ojos == "A":
        contratado = True
    else:
        print("No cumple con las condiciones para se contratado")
else:
    print("No cumple con las condiciones para se contratado")

         