'''
6.	Un programa que permita escoger uno de los siguientes símbolos de los elementos químicos para saber cuál corresponde:

H			Hidrógeno
O			Oxigeno
AG			Plata
CA			Calcio
C			Carbono
NA			Sodio
K			Potasio

'''
# Definimos un diccionario con los símbolos y sus respectivos nombres

elementos = {
    'H': 'Hidrógeno',
    'O': 'Oxígeno',
    'AG': 'Plata',
    'CA': 'Calcio',
    'C': 'Carbono',
    'NA': 'Sodio',
    'K': 'Potasio'
}

# Pedimos al usuario que ingrese un símbolo

simbolo = input("Ingrese el símbolo del elemento químico (H, O, AG, CA, C, NA, K): ").upper()

# Verificamos si el símbolo ingresado está en el diccionario y mostramos el nombre correspondiente
if simbolo in elementos:
    print(f"El símbolo '{simbolo}' corresponde a: {elementos[simbolo]}")
else:
    print("Símbolo no reconocido. Por favor, ingrese un símbolo válido.")

# Fin del programa
# El programa permite al usuario ingresar un símbolo químico y devuelve el nombre del elemento correspondiente.    