import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""""
Insertar la base de datos y ver le tipo de datos
"""""
archivo="Entregas-td1-2024/Caso_juan/customer_data.csv"
data=pd.read_csv(archivo, delimiter=',', header=0)

# 1.1 ANALISIS DE LA VARIABLES NUMERICAS 
# Discriminacion datos numericos 
datos_numericos=["age","income","purchase_amount","satisfaction_score"]
num=data[datos_numericos]
valores=num.describe()
print("las estadisticas descriptivas de los datos numericos del data frame son:" )
print(valores)

#Histogramas y diagramas de cajas para variables cualitativas 
for i in (datos_numericos):
    plt.hist(num[i], bins=10)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title(i)
    plt.show()

for i in (datos_numericos):
    plt.boxplot(num[i])
    plt.ylabel('Valor')
    plt.title(i)
    plt.show()

#1.2 Analisis de variables de niveles o clases (STR)
datos_str=["gender","education","region","loyalty_status","purchase_frequency","product_category","promotion_usage"]
str=data[datos_str]
print(str)
contadores=["contador1","contador2","contador3","contador4","contador5","contador6","contador7"]
for i in (datos_str):
    for j in (contadores):
        j=str[i].value_counts()
    print(j)
    j.plot(kind='bar')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title(i)
    plt.show()  

#2. Grafico de correlacion entre variables numericas 

matriz_de_correlacion = num.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_de_correlacion, annot=True, cmap='coolwarm')
plt.title('Mapa de calor de correlación entre columnas numericas', fontsize=16)
plt.show()


#3. Anslisis de segmentos de los datos 

#3.1 Quien gasta mas los hombres o las mujeres?
datos_a_extraer_mujeres=["gender","purchase_amount"]
valores1=data[datos_a_extraer_mujeres]
 
filas_hombres=valores1[valores1["gender"]=="Male"]
filas_mujeres=valores1[valores1["gender"]=="Female"]

Cantidad_compras_hombres=len(filas_hombres)
print(Cantidad_compras_hombres)
Cantidad2_compras_mujeres=len(filas_mujeres)
print(Cantidad2_compras_mujeres)

valor_compras_mujeres=filas_mujeres["purchase_amount"].sum()
valor_compras_hombres=filas_hombres["purchase_amount"].sum()
print(valor_compras_mujeres,valor_compras_hombres)
if valor_compras_hombres<valor_compras_mujeres:
    print("el total de las mujeres gastan mas de lo que el total de lo hombres, con un valor de:", valor_compras_mujeres)
else: print("los hombres gastaron mas que las mujeres ")
promedio_compra_hombre=valor_compras_hombres/Cantidad_compras_hombres
promedio_compra_mujer=valor_compras_mujeres/Cantidad2_compras_mujeres
print("en promedio los hombres gastan", promedio_compra_hombre, "por compra, mientras que las muejeres gastan", promedio_compra_mujer, "por compra")
print("el valor de la compra promedio del hombre es mas alta que el de la mujer por ", promedio_compra_hombre-promedio_compra_mujer, "en conclusion los hombres estan dispuestos a pagar un valor muy cercano al que las muejeres estan dispuestas a pagar  EN PORMEDIO")

#3.2 ¿Con que frecuencia compran los hombres a diferencia de las mujeres?

filas_hombres1=data[data["gender"]=="Male"]
filas_mujeres1=data[data["gender"]=="Female"]

plt.figure(figsize=(8, 6))
filas_hombres1['purchase_frequency'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta de frecuencias de compra de los hombres', fontsize=16)
plt.ylabel('')  
plt.show()
plt.figure(figsize=(8, 6))
filas_mujeres1['purchase_frequency'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Diagrama de Torta de frecuencias de compra de las mujeres ', fontsize=16)
plt.ylabel('')  
plt.show()

#  #prueba de relacion entre la lealtad hacia la marca y la datisfaccion del cliente
lealtad_Regular=data[data["loyalty_status"]=="Regular"]
lealtad_Silver=data[data["loyalty_status"]=="Silver"]
lealtad_Gold=data[data["loyalty_status"]=="Gold"]

valor_Regular=lealtad_Regular["satisfaction_score"].mean()
valor_Silver=lealtad_Silver["satisfaction_score"].mean()
valor_Gold=lealtad_Gold["satisfaction_score"].mean()

print("el promedio de la satisfaccion de las lealtades es: ")
print("Lealtad Regular: ", valor_Regular)
print("Lealtad Silver: ", valor_Silver)
print("Lealtad gold: ", valor_Gold)