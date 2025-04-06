'''
10.	Averigua cuál es el tipo de cambio para la fecha de hoy. Elabore una tabla que presente un dólar hasta 100 dólares, sus equivalencias de acuerdo con el tipo de cambio en la moneda de tú país.

'''

import requests

import pandas as pd # Importamos la librería pandas para manejar datos en forma de tabla
from datetime import date # Importamos la clase date del módulo datetime para trabajar con fechas

# Definimos la URL de la API que proporciona el tipo de cambio
url = 'https://api.exchangerate-api.com/v4/latest/USD' # URL de la API para obtener el tipo de cambio del dólar

# Hacemos una petición GET a la API y almacenamos la respuesta en la variable response
response = requests.get(url) # Realizamos la petición GET a la API  

# Convertimos la respuesta a formato JSON y la almacenamos en la variable data
data = response.json() # Convertimos la respuesta a formato JSON    

# Obtenemos el tipo de cambio del dólar a la moneda local (en este caso, el peso colombiano)
exchange_rate = data['rates']['COP'] # Obtenemos el tipo de cambio del dólar a peso colombiano

# Creamos una lista de dólares desde 1 hasta 100
dollars = list(range(1, 101)) # Creamos una lista de dólares desde 1 hasta 100

# Creamos una lista de equivalencias en pesos colombianos multiplicando cada dólar por el tipo de cambio
equivalents = [dollar * exchange_rate for dollar in dollars] # Creamos una lista de equivalencias en pesos colombianos

# Creamos un DataFrame de pandas con los dólares y sus equivalencias
df = pd.DataFrame({'Dólares': dollars, 'Equivalencia en COP': equivalents}) # Creamos un DataFrame con los dólares y sus equivalencias

# Obtenemos la fecha de hoy
today = date.today() # Obtenemos la fecha de hoy

# Imprimimos la tabla con los dólares y sus equivalencias
print(f"Tipo de cambio del dólar a COP: {exchange_rate}") # Imprimimos el tipo de cambio

print(f"Fecha de hoy: {today}") # Imprimimos la fecha de hoy
print(df) # Imprimimos el DataFrame con los dólares y sus equivalencias



