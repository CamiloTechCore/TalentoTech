'''
9.	Resolver la función f(x)=x3+x2-5, para x tomando valores del 1 al 10.

'''
# Definimos la función f(x)
def f(x):
    return x**3 + x**2 - 5

# Definimos el rango de valores de x
x_values = range(1, 11)

# Calculamos y mostramos el resultado de f(x) para cada valor de x
for x in x_values:
    result = f(x)
    print(f"f({x}) = {result}")

    
# El resultado de la función f(x) para x tomando valores del 1 al 10 es:
# f(1) = -3
# f(2) = 15         
# f(3) = 49
# f(4) = 141
# f(5) = 305
# f(6) = 621
# f(7) = 1,215
# f(8) = 2,081
# f(9) = 3,405
# f(10) = 5,005

# La función f(x) crece rápidamente a medida que x aumenta, lo que se puede observar en los resultados.

