'''
Ciclos While 
'''

contador = 0;

while(contador<30):
    print(f"Iteracion: {contador + 1}.");
    contador = contador + 1;

Contraseña = "Camilo0524"

intentos = 3

while intentos > 0:
    contraseña_input = input("Ingrese la contraseña: ")  # str() no es necesario
    if contraseña_input == Contraseña:
        print("Acceso correcto")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta, intentos restantes: {intentos}")

    if intentos == 0:
        print("Cuenta bloqueada, por favor intente más tarde")
