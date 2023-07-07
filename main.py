# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gKGJ7QMLhp_XlECSF2lbAXLqVkBJvYAg

##Proyecto de software para medir posible impacto de políticas de innovación en energía
"""

# importación de librerias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
import seaborn as sb
import unittest
import pickle

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from statsmodels.stats.weightstats import ttest_ind
from sklearn import tree

# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

# Se crea el dataframe
df=pd.read_csv("/content/drive/MyDrive/Unitsdollars_Excel.csv")
df=df.replace(np.nan,"0")
df

db=df.dropna()
db

db= df[["resource", "variable", "units", "magnitude", "source", "data_value", "flag"]]
db

"""##Creación de un modelo predictivo"""

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['data_value'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

"""##Predicción y comparación de "data_value" para años futuros hasta 2023 con regresión lineal"""

# Realizar una predicción para dos años futuros
future_year = 2022
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

future_year = 2023
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

"""##Guardado de datos en archivo .csv en regresión lineal"""

# Realizar una predicción para dos años futuros
future_year_1 = 2022
future_prediction_1 = model.predict([[future_year_1]])
print("Predicción para el año", future_year_1, ":", future_prediction_1)

future_year_2 = 2023
future_prediction_2 = model.predict([[future_year_2]])
print("Predicción para el año", future_year_2, ":", future_prediction_2)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Crear un DataFrame con los datos de entrenamiento, predicciones y datos de prueba
df_train = pd.DataFrame({'year': X_train.flatten(), 'data_value': y_train.flatten()})
df_pred = pd.DataFrame({'year': [future_year_1, future_year_2], 'prediction': [future_prediction_1, future_prediction_2]})
df_test = pd.DataFrame({'year': X_test.flatten(), 'data_value': y_test.flatten()})

# Guardar los DataFrames en archivos CSV
df_train.to_csv('train_RLN.csv', index=False)
df_pred.to_csv('predic_RLN.csv', index=False)
df_test.to_csv('test_RLN.csv', index=False)

"""##Carga de datos de entrenamiento y nueva predicción con regresión lineal"""

# Cargar los datos de entrenamiento desde el archivo CSV
df_train = pd.read_csv('train_RLN.csv')
X_train = df_train['year'].values.reshape(-1, 1)
y_train = df_train['data_value'].values.reshape(-1, 1)

# Cargar los datos de prueba desde el archivo CSV
df_test = pd.read_csv('test_RLN.csv')
X_test = df_test['year'].values.reshape(-1, 1)
y_test = df_test['data_value'].values.reshape(-1, 1)

# Cargar las predicciones desde el archivo CSV
df_pred = pd.read_csv('predic_RLN.csv')
future_years = df_pred['year'].values
predictions = df_pred['prediction'].values

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar nuevas predicciones utilizando los datos cargados
for future_year, prediction in zip(future_years, predictions):
    X_future = [[future_year]]
    y_pred = model.predict(X_future)
    print(f"Predicción para el año {future_year}: {y_pred[0]}")

"""##Predicción de "flag" para años futuros hasta **2023** mediante regresión logística"""

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['flag'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Realización de una predicción para dos años futuros
future_year = 2022
prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", prediction[0])

future_year = 2023
prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", prediction[0])

"""##Guardado de datos en .py en archivo csv regresión logística"""

# Crear un DataFrame con los datos de entrenamiento, predicciones y datos de prueba
df_train = pd.DataFrame({'year': X_train.flatten(), 'flag': y_train.flatten()})
df_pred = pd.DataFrame({'year': future_years, 'prediction': predictions})
df_test = pd.DataFrame({'year': X_test.flatten(), 'flag': y_test.flatten()})
# Guardar los DataFrames en archivos CSV
df_train.to_csv('train_RLG.csv', index=False)
df_pred.to_csv('predic_RLG.csv', index=False)
df_test.to_csv('test_RLG.csv', index=False)

"""##Carga de datos de entrenamiento y nueva predicción regresión logística"""

# Cargar los datos de entrenamiento desde el archivo CSV
df_train = pd.read_csv('train_RLG.csv')
X_train = df_train['year'].values.reshape(-1, 1)
y_train = df_train['flag'].values.reshape(-1, 1)

# Cargar los datos de prueba desde el archivo CSV
df_test = pd.read_csv('test_RLG.csv')
X_test = df_test['year'].values.reshape(-1, 1)
y_test = df_test['flag'].values.reshape(-1, 1)

# Cargar las predicciones desde el archivo CSV
df_pred = pd.read_csv('predic_RLG.csv')
future_years = df_pred['year'].values
predictions = df_pred['prediction'].values

# Realizar nuevas predicciones utilizando los datos cargados
for future_year, prediction in zip(future_years, predictions):
    print(f"Predicción para el año {future_year}: {prediction}")

"""## Análisis de impacto con matriz DAFO

Cálculo predictivo del incremento de producción a dos años futuros
"""

# En el caso del análisis de la transformación a energías renovables en Nueva Zelandia por políticas de promoción podemos utilizar el concepto DAFO de la siguiente manera o modo
# Así, las Fortalezas pertinentes al caso se pueden determinar cuantitativamente con las siguientes variables:
# promoción de la innovación = F1  #grado de rango 1-5
# Valor del conjunto de ventajas reconocido = F2  #grado de rango 1-5
# Relaciones con las compañías proveedoras = F3  #grado de rango 1-5

#Finalmente se multiplican los valores y nos da el valor de la fortalezas en función de los criterios: F= F1.F2.F3

# Las Debilidades se pueden determinar cuantitativamente así:
# experiencia del equipo experto = D1   #grado de rango 1-5
# costos de producción = D2   #grado de rango 1-5
# calidad de productos = D3   #grado de rango 1-5

#Finalmente se multiplican los valores y nos da el valor de la debilidades en función de los criterios: D= D1.D2.D3

# Las Oportunidades pertinentes se pueden determinar cuantitativamente del siguiente modo:
# Crecimiento del mercado = O1  #grado de rango 1-5
# Tendencia hacia productos ecológicos = O2  #grado de rango 1-5
# Expansión internacional = O3  #grado de rango 1-5

#Finalmente se multiplican los valores y nos da el valor de las oprtunidades en función de los criterios: O= O1.O2.O3

# Las Amenazas se pueden determinar cuantitativamente de la siguiente manera:
# Grado de competencia = A1  #grado de rango 1-5
# Tendencia al apoyo de a cambios en regulaciones gubernamentales = A2  #grado de rango 1-5
# Tendencia al cambio de preferencias de los consumidores = A3 #grado de rango 1-5

#Finalmente se multiplican los valores y nos da el valor de las amenazas en función de los criterios:  A= A1.A2.A3

# Ejemplos:       F= F1.F2.F3= 1*3*5=15      D= D1.D2.D3= 2*2*3=12       O= O1.O2.O3= 3*2*3=18                      A= A1.A2.A3= 2*2*1=4


# Cualquiera de estos números Fi, Di, Oi y Ai es relativo al criterio del analista o la comunidad afectada pudiendo tomar un espectro creciente de grados (poco, medianamente, mucho) letras (A, B o C) o dígitos (1,2,3,4,5 o 10 al 100 o del 1 al 10).


# Función para calcular el incremento de producción y su porcentaje
def calcular_incremento_produccion(actual, anterior):
    incremento = actual - anterior
    incremento_porcentaje = (incremento / anterior) * 100
    return incremento, incremento_porcentaje

# Función para calcular el puntaje de impacto en cada categoría de DAFO
def calcular_puntaje_foda(incremento_produccion_porcentual, fortalezas, oportunidades, debilidades, amenazas):
    # Asignar valores numéricos a cada categoría (mayor es mejor)
    puntaje_fortalezas = 15
    for fortaleza in fortalezas:
        puntaje_fortalezas *= fortaleza

    puntaje_oportunidades = 18
    for oportunidad in oportunidades:
        puntaje_oportunidades *= oportunidad

    puntaje_debilidades = 12
    for debilidad in debilidades:
        puntaje_debilidades *= debilidad

    puntaje_amenazas = 4
    for amenaza in amenazas:
        puntaje_amenazas *= amenaza

    # Calcular el impacto del incremento de producción en cada categoría
    impacto_fortalezas = incremento_produccion_porcentual * puntaje_fortalezas
    impacto_oportunidades = incremento_produccion_porcentual * puntaje_oportunidades
    impacto_debilidades = incremento_produccion_porcentual * puntaje_debilidades
    impacto_amenazas = incremento_produccion_porcentual * puntaje_amenazas

    # Retornar los resultados
    return impacto_fortalezas, impacto_oportunidades, impacto_debilidades, impacto_amenazas

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['data_value'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar una predicción para dos años futuros
future_year_1 = 2022
future_prediction_1 = model.predict([[future_year_1]])
print("Predicción para el año", future_year_1, ":", future_prediction_1)

future_year_2 = 2023
future_prediction_2 = model.predict([[future_year_2]])
print("Predicción para el año", future_year_2, ":", future_prediction_2)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Crear un DataFrame con los datos de entrenamiento, predicciones y datos de prueba
df_train = pd.DataFrame({'year': X_train.flatten(), 'data_value': y_train.flatten()})
df_pred = pd.DataFrame({'year': [future_year_1, future_year_2], 'prediction': [future_prediction_1, future_prediction_2]})
df_test = pd.DataFrame({'year': X_test.flatten(), 'data_value': y_test.flatten()})

# Guardar los DataFrames en archivos CSV
df_train.to_csv('train_RLN.csv', index=False)
df_pred.to_csv('predic_RLN.csv', index=False)
df_test.to_csv('test_RLN.csv', index=False)

# Cargar los datos de entrenamiento desde el archivo CSV
df_train = pd.read_csv('train_RLN.csv')
X_train = df_train['year'].values.reshape(-1, 1)
y_train = df_train['data_value'].values.reshape(-1, 1)

# Cargar los datos de prueba desde el archivo CSV
df_test = pd.read_csv('test_RLN.csv')
X_test = df_test['year'].values.reshape(-1, 1)
y_test = df_test['data_value'].values.reshape(-1, 1)

# Cargar las predicciones desde el archivo CSV
df_pred = pd.read_csv('predic_RLN.csv')
future_years = df_pred['year'].values
predictions = df_pred['prediction'].values

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar nuevas predicciones utilizando los datos cargados
for future_year, prediction in zip(future_years, predictions):
    X_future = [[future_year]]
    y_pred = model.predict(X_future)
    print(f"Predicción para el año {future_year}: {y_pred[0]}")

# Valores para el análisis DAFO
valor_prediccion_actual = 2023
valor_prediccion_anterior = 2022

valor_actual = float(model.predict([[valor_prediccion_actual]])[0])
valor_anterior = float(model.predict([[valor_prediccion_anterior]])[0])

incremento, incremento_porcentaje = calcular_incremento_produccion(valor_actual, valor_anterior)

fortalezas = [1, 3, 5]
oportunidades = [3, 2, 3]
debilidades = [2, 2, 3]
amenazas = [2, 2, 1]

impacto_fortalezas, impacto_oportunidades, impacto_debilidades, impacto_amenazas = calcular_puntaje_foda(
    incremento_porcentaje, fortalezas, oportunidades, debilidades, amenazas)

print("Incremento de producción:", incremento)
print("Incremento de producción (%):", incremento_porcentaje)

print("Impacto en Fortalezas:", impacto_fortalezas)
print("Impacto en Oportunidades:", impacto_oportunidades)
print("Impacto en Debilidades:", impacto_debilidades)
print("Impacto en Amenazas:", impacto_amenazas)