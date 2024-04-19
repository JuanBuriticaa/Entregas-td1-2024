# Quiz 2 corte Toma de desisiones 2024-1 
# 1. ETL de según código base:
#     a. Crear una función que recibirá como parámetro un DF y deberá retornar un DF con una columna adicional 
#     (peso=2.0)
#     Condiciones:     
#     i.	sepal length (cm)>=5.1
#     ii.	sepal width (cm)>= 3.5
#     iii.petal length (cm)>=1.3 
#     iv.	petal width (cm)<= 0.2
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

pd.set_option("display.max_columns",None)

iris = load_iris()
daf = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])
#La funcion selección 
def seleccion(df):
    for i in range (len(daf)):
        if daf.iloc[i]['sepal length (cm)']>=5.1 and daf.iloc[i]["sepal width (cm)"]>=3.5 and daf.iloc[i]["petal length (cm)"]>=1.3 and daf.iloc[i]["petal width (cm)"]<=0.2:
            daf.at[i,"Flor"]="Es clavel"
            daf.at[i,"Numero"]=1
        else:
            daf.at[i,"Flor"]="No es clavel"
            daf.at[i,"Numero"]=0
    print(daf.head)
    daf.to_csv("df_con_restriccion")
    conteo = daf['Flor'].value_counts()['Es clavel']
    conteo1= -conteo+150
    porcentaje=(conteo/conteo1)*100
    print ("el numero de claveles es", conteo, "el resto de datos", conteo1, "no lo son, debido a que no cumplen con las condiciones optimas de tamaño, es decir el", porcentaje, "%")

seleccion(daf)

# 2.	EDA según el DF resultante :  (peso=2.0)
#     a.	Gráficas.
#     b.	Concluir con respecto a las gráficas.

#Grafico de torta
columnas_seleccionadas = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
hola= daf[columnas_seleccionadas]

plt.figure(figsize=(8, 6))
daf['Flor'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta para distribución de Columna Categórica', fontsize=16)
plt.ylabel('')  # Eliminar etiqueta del eje y
plt.show()

#Se ve como el 94,7% de las flores analizadas no son claveles ya que no cumplen las condiciones, y el restante 5,3 % si lo es 

#Diagrama de cajas
plt.figure(figsize=(10, 8))
sns.boxplot(data=hola)
plt.title('Diagrama de caja para cada columna', fontsize=16)
plt.show()

#Se aprecia Que el petal length es la que mas dispersion tienem mientras que la que menos tiene es el sepal width, tambien se ve la media de cada uno de los datos graficamente y en qeu rengos se encuentran los mismos

sns.set_theme(style="darkgrid")
sns.displot(daf['sepal length (cm)'], kde = False, color ='red', bins = 30)
plt.show()
sns.set_theme(style="darkgrid")
sns.displot(daf['sepal width (cm)'], kde = False, color ='blue', bins = 30) 
plt.show()
sns.set_theme(style="darkgrid")
sns.displot(daf['petal length (cm)'], kde = False, color ='green', bins = 30) 
plt.show() 
sns.set_theme(style="darkgrid")
sns.displot(daf['petal width (cm)'], kde = False, color ='black', bins = 30)   
plt.show()                      
sns.barplot(daf['Flor'],  color ='purple')
plt.show()
#Conclusiones: Segun los graficos vistos anteriormente, 
# se puede evidenciar como claramente hay un gran numero de flores que no son clavel,
# en especial el 94.7% y por otro lado. el 5.3% si lo son. Ademas de eso gracias al histograma 
# se puede analizar que, en la variable \"sepal length (cm)\" la medida que mas se repite es de 
# 5 cm, en la variable \"sepal width (cm)\" la medida es 3 cm aparte de tener un comportamiento 
# ciertamente con distribucion normal, en la variable \"petal length (cm)\" la medida es 1.5 cm 
# y por ultimo, la variable \"petal width (cm)\" es 0.2 cm aproximadamente.