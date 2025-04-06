'''
1.	Elaborar un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

'''
# Pedir al usuario un número entero positivo

# Pedir al usuario un número entero positivo
num = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if num > 0:
    print("Números impares hasta", num, ":", end=" ")
    
    for i in range(1, num + 1, 2):
        if i == num or i + 2 > num:  
            print(i)
        else:
            print(i, end=", ")
else:
    print("Por favor, ingrese un número entero positivo.")

