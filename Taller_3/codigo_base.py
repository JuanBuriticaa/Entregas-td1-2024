import openpyxl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
"""
Primero subir la base de datos 
"""
archivo="nombre base de datos"
data=pd.read_csv(archivo, delimiter=',', header=0)
"""
definir que variables de la base de datos son numericas y ademas desea graficar 
"""
num=["nombre","nombre2"]#data freme con los nombres de las variables que se quieren extraer 
datos_numericos=data[num]
# Histograma: Similar a las barras, pero usado para mostrar la distribución de un conjunto de datos.
#bins se refiere al nu
plt.hist(num[i], bins=10)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title(i)
plt.show()
# Diagrama de Caja y Bigotes (Box Plot): Útil para mostrar la distribución estadística de un conjunto de datos.
# Gráfico de Sectores (o Pastel): Utilizado para mostrar proporciones de un total.
# Gráfico de Dispersión (Scatter Plot): Muestra la relación entre dos variables cuantitativas.
# Mapa de Calor (Heatmap): Muestra datos en una matriz de colores para indicar diferentes valores.


