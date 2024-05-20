import openpyxl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pulp import *
#Gráfico de Barras: Utilizado para comparar cantidades entre diferentes categorías.
# Gráfico de Líneas: Ideal para mostrar tendencias a lo largo del tiempo.
# Gráfico de Sectores (o Pastel): Utilizado para mostrar proporciones de un total.
# Histograma: Similar a las barras, pero usado para mostrar la distribución de un conjunto de datos.
# Gráfico de Dispersión (Scatter Plot): Muestra la relación entre dos variables cuantitativas.
# Gráfico de Área: Similar al gráfico de líneas, pero con el área debajo de la línea rellena.
# Diagrama de Caja y Bigotes (Box Plot): Útil para mostrar la distribución estadística de un conjunto de datos.
# Gráfico de Burbuja: Similar al de dispersión, pero con un tercer valor representado por el tamaño de las burbujas.
# Mapa de Calor (Heatmap): Muestra datos en una matriz de colores para indicar diferentes valores.
# Gráfico de Radar (o Poligonal): Muestra múltiples variables en una forma de estrella o telaraña.
# Gráfico de Cascada (Waterfall Chart): Muestra cómo un valor inicial se ve afectado por incrementos y decrementos sucesivos.
# Gráfico de Gantt: Utilizado principalmente en la gestión de proyectos para mostrar cronogramas.
# Gráfico de Rosca (Doughnut Chart): Similar al gráfico de sectores, pero con un espacio vacío en el centro.
# Gráfico de Velas (Candlestick Chart): Utilizado en finanzas para mostrar el movimiento de precios de un activo.
# Gráfico de Pareto: Un tipo de gráfico de barras que también incluye una línea para mostrar la proporción acumulada de las categorías.