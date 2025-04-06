'''
5.	Leer desde el teclado el nombre de un personaje histórico. Si es BOLIVAR escríbase LIBERTADOR. Si es MADRE TERESA el mensaje será SERVICIO A LOS POBRES. Si fuese GANDHI, el programa escribirá LIBERTAD A LA INDIA, pero si es cualquiera otro personaje, el programa escribirá el mensaje NO IDENTIFICADO.

El programa debe terminar cuando el usuario ingrese la palabra SALIR.

'''

# Definimos la función principal

def main():
    personajes = {
        "BOLIVAR": "LIBERTADOR",
        "MADRE TERESA": "SERVICIO A LOS POBRES",
        "GANDHI": "LIBERTAD A LA INDIA"
    }

    while True:
        personaje = input("Ingrese el nombre del personaje: ").upper()

        if personaje == "SALIR":
            break

        print(personajes.get(personaje, "NO IDENTIFICADO"))

if __name__ == "__main__":
    main()

    