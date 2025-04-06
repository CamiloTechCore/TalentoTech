'''
4.	Un programa que imprima un listado con los números del 1 al 10, cada uno con su respectivo cuadrado. Cada pareja de valores debe ir en una misma línea.
'''
# for i in range(1, 11): #Recorremos el rango de 1 a 10

for i in range(1,11): # hasta 11 porque el rango no incluye el último número
    print(f"{i} {i**2}") # {1**2} es lo mismo que 1*1, pero se puede usar el operador de potencia ** para elevar a la potencia que queramos. En este caso, al cuadrado.

