import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

print(numero_aleatorio)

print("¡Juego adivina el número! Tienes 5 intentos... ¡¡¡Es hora de empezar!!!")

contador = 5  # Número de intentos permitidos

while contador > 0:
    num_usuario = int(input("Ingresa un número: "))

    if num_usuario == numero_aleatorio:
        print("¡¡¡Ganaste... felicidades!!!")
        break
    elif num_usuario < numero_aleatorio:
        print("El número es mayor al que debes adivinar. Intentos restantes:", contador - 1)
    elif num_usuario > numero_aleatorio:
        print("El número es menor al que debes adivinar. Intentos restantes:", contador - 1)

    contador -= 1  # Reducir intentos

    if contador == 0:
        print(f"Lo siento, has perdido. El número correcto era {numero_aleatorio}.")

print("Fin del juego.")

