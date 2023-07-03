# -*- coding: utf-8 -*-
"""SRC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hk1sEma2EdDNxCQnUffzqtPu-PRJFIyf
"""

# importación de librerias
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sb
import joblib

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
from sklearn.metrics import accuracy_score
from statsmodels.stats.weightstats import ttest_ind
from sklearn.metrics import mean_squared_error
from sklearn import tree


# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

# Se crea el dataframe
df=pd.read_csv("Unitsdollars_Excel.csv")
df=df.replace(np.nan,"0")

db=df.dropna()
db

db= df[["resource", "variable", "units", "magnitude", "source", "data_value", "flag"]]
db

"""##Creación del modelo predictivo

##Regresión lineal
"""

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['data_value'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Guardar el modelo en disco
joblib.dump(model, 'modelo_regresion_lineal.joblib')

# Cargar el modelo desde el archivo guardado
loaded_model = joblib.load('modelo_regresion_lineal.joblib')

# Realizar predicciones utilizando el modelo cargado
y_pred = loaded_model.predict(X_test)

"""##Predicción y comparación de "data_value" para años futuros hasta 2023 con regresión lineal"""

# Realizar una predicción para un año futuro
future_year = 2022
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

future_year = 2023
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

"""##Predicción de "flag" para años futuros hasta 2030 mediante regresión logística"""

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['flag'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Guardar el modelo en disco
joblib.dump(model, 'modelo_regresion_logistica.joblib')

# Cargar el modelo desde el archivo guardado
loaded_model = joblib.load('modelo_regresion_logistica.joblib')

# Realizar predicciones utilizando el modelo cargado
y_pred = loaded_model.predict(X_test)

# Realizar una predicción para 2 años futuros
future_year = 2022
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

future_year = 2023
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

"""##Modelo con árbol de decisión clasificador"""

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['resource'].values  # Crecimiento como variable objetivo

# Crear y entrenar el modelo de árbol de decisión clasificador
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Guardar el modelo en disco
joblib.dump(model, 'modelo_arbol_decision.joblib')

# Cargar el modelo desde el archivo guardado
loaded_model = joblib.load('modelo_arbol_decision.joblib')

# Realizar predicciones utilizando el modelo cargado
y_pred = loaded_model.predict(X)

"""## Análisis de impacto con matriz DAFO"""



# En el caso del análisis de la transformación a energías renovables en Nueva Zelandia por políticas de promoción podemos utilizar el concepto DAFO de la siguiente manera o modo
# Así, las Fortalezas pertinentes al caso se pueden determinar cuantitativamente con las siguientes variables:
# promoción de la innovación = F1
# Valor del conjunto de ventajas reconocido = F2
# Relaciones con las compañías proveedoras = F3

# Las Debilidades se pueden determinar cuantitativamente así:
# experiencia del equipo experto = D1
# costos de producción = D2
# calidad de productos = D3

# Las Oportunidades pertinentes se pueden determinar cuantitativamente del siguiente modo:
# Crecimiento del mercado = O1
# Tendencia hacia productos ecológicos = O2
# Expansión internacional = O3

# Las Amenazas se pueden determinar cuantitativamente de la siguiente manera:
# Grado de competencia = A1
# Tendencia al apoyo de a cambios en regulaciones gubernamentales = A2
# Tendencia al cambio de preferencias de los consumidores = A3

# Cualquiera de estos números Fi, Di, Oi y Ai es relativo al criterio del analista o la comunidad afectada pudiendo tomar un espectro creciente de grados (poco, medianamente, mucho) letras (A, B o C) o dígitos (1,2,3,4,5 o 10 al 100 o del 1 al 10).
data = { 'Fortalezas': ['promoción de la innovación', 'Valor del conjunto de ventajas reconocido', 'Buenas relaciones con las compañías proveedoras'],
    'Debilidades': ['poca experiencia del equipo experto', 'Altos costos de producción', 'calidad de productos no probada'],
    'Oportunidades': ['Crecimiento del mercado', 'Tendencia hacia productos ecológicos', 'Expansión internacional'],
    'Amenazas': ['Competencia fuerte', 'Resistenia a cambios en regulaciones gubernamentales', 'Cambio de preferencias de los consumidores']


}

df = pd.DataFrame(data, index=['F1', 'F2', 'F3'])
print(df)

plt.figure(figsize=(10, 6))
plt.imshow([[0, 1], [1, 0]], cmap='Greys', aspect='auto')
plt.axis('off')

rows, cols = df.shape
for i in range(rows):
    for j in range(cols):
        plt.text(j, i, df.iloc[i, j], ha='center', va='center', color='black')

plt.title('Matriz FODA')
plt.show()

import matplotlib.pyplot as plt

# Código para crear y mostrar la matriz FODA

plt.savefig('matriz_foda.png', dpi=300, bbox_inches='tight')