'''
7.	Genere un programa que pida el formato de una película, si el formato es BETA cuesta $2.000, si es VHS cuesta $3.000, si es VCD cuesta $4.000 y DVD cuesta $5.000.

'''

# Definimos los precios de cada formato

precios = {
    "BETA": 2000,
    "VHS": 3000,
}

# Definimos los precios de cada formato

precios.update({
    "VCD": 4000,
    "DVD": 5000,    
})

# Pedimos al usuario que ingrese el formato de la película|

print("\t\t\tBienvenido a la tienda de películas\n")
print("Formato de película: BETA, VHS, VCD o DVD")

formato = input("Ingrese el formato de la pelicula: ").upper()


# Verificamos si el formato ingresado es válido

if formato in precios:
    print(f"El precio de la película en formato {formato} es: ${precios[formato]}")
else:
    print("Formato no válido, por favor ingrese un formato válido: BETA, VHS, VCD o DVD")

