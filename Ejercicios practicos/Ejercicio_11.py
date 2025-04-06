'''
11.	Un equipo de fútbol realizó 5 partidos oficiales durante el año 2007. Se quiere escribir un programa que le pregunte a cada uno de sus once jugadores cuántos goles hizo en cada uno de los cinco partidos.  

'''


lista_goles = []

for i in range(11):
    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    goles = []
    for j in range(5):
        goles_partido = int(input(f"Ingrese la cantidad de goles que hizo {nombre} en el partido {j+1}: "))
        goles.append(goles_partido)
    lista_goles.append((nombre, goles))

    # Imprimir la lista de goles
    print(f"Goles de {nombre}: {goles}")
    print(f"Total de goles de {nombre}: {sum(goles)}")
    print(f"Promedio de goles de {nombre}: {sum(goles)/len(goles)}")
    print(f"Máximo de goles de {nombre}: {max(goles)}")
    print(f"Mínimo de goles de {nombre}: {min(goles)}")
    print(f"Cantidad de partidos: {len(goles)}")

# Imprimir la lista de goles de todos los jugadores
print("Lista de goles de todos los jugadores:")
for jugador, goles in lista_goles:
    print(f"{jugador}: {goles}")
    print(f"Total de goles de {jugador}: {sum(goles)}")
    print(f"Promedio de goles de {jugador}: {sum(goles)/len(goles)}")
    print(f"Máximo de goles de {jugador}: {max(goles)}")
    print(f"Mínimo de goles de {jugador}: {min(goles)}")
    print(f"Cantidad de partidos: {len(goles)}")

    