'''
3.Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

'''
palabra = input("Escriba una palabra: ").lower()

# Recorrer la palabra

for i in range(len(palabra)-1, -1, -1):  #-1 para que empiece desde la última letra y -1 para que no se salga del rango
    print(palabra[i]) 

    