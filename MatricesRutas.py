from InviasWS import obtener_elementos # Función para el Web Scraping de Hermes Invias
from itertools import combinations # Función para crear las rutas
import pandas as pd 
import numpy as np

# Vector de 13 ciudades principales
ciudades = [
    "Bogotá, Distrito Capital",
    "Medellín, Antioquia",
    "Cali, Valle del Cauca",
    "Barranquilla, Atlantico",
    "Cartagena de Indias, Bolívar",
    "Bucaramanga, Santander",
    "Cúcuta, Norte de Santander",
    "Pereira, Risaralda",
    "Manizales, Caldas",
    "Ibagué, Tolima",
    "Santa Marta, Magdalena",
    "Villavicencio, Meta",
    "Neiva, Huila"
]

# Crea las rutas
rutas = list(combinations(ciudades, 2))

# Obteniendo el tiempo, distancia y costo de peajes de cada ruta
resultados = obtener_elementos(rutas)

# Crear DataFrames vacíos
matriz_tiempos = pd.DataFrame(0.0, index=ciudades, columns=ciudades)
matriz_distancia = pd.DataFrame(0.0, index=ciudades, columns=ciudades)
matriz_peajes = pd.DataFrame(0, index=ciudades, columns=ciudades)


# Llenar las matrices con los valores del diccionario
for ruta in resultados:
    origen = ruta["origen"]
    destino = ruta["destino"]
    tiempo = ruta["tiempo"]
    distancia = ruta["distancia"]
    costo = ruta["costo_peaje"]

    matriz_tiempos.loc[origen, destino] = tiempo
    matriz_tiempos.loc[destino, origen] = tiempo

    matriz_distancia.loc[origen, destino] = distancia
    matriz_distancia.loc[destino, origen] = distancia

    matriz_peajes.loc[origen, destino] = costo
    matriz_peajes.loc[destino, origen] = costo

# Asegurar que la diagonal quede en cero
np.fill_diagonal(matriz_tiempos.values, 0)
np.fill_diagonal(matriz_distancia.values, 0)
np.fill_diagonal(matriz_peajes.values, 0)

# Guarda las matrices en archivos csv
matriz_tiempos.to_csv('matriz_tiempos.csv', encoding='utf-8-sig')
matriz_distancia.to_csv('matriz_distancia.csv', encoding='utf-8-sig')
matriz_peajes.to_csv('matriz_peajes.csv', encoding='utf-8-sig')