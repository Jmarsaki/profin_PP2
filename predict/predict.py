# -*- coding: utf-8 -*-
"""Predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1USQjfKRJNo0Tnq3YvpLPrt4zBSl5cyoC

##Predictores

#Para regresión lineal
"""

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Guardar y cargar el modelo
import joblib 

joblib.dump(model, 'modelo_entrenado.pkl') # Guardar el modelo

joblib.load('modelo_entrenado.pkl') # Carga del modelo


# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

"""# Para regresión logística"""

# Realizar una predicción para un año futuro
future_year = 2022
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['flag'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Guardar y cargar el modelo
import joblib 

joblib.dump(model, 'modelo_entrenado.pkl') # Guardar el modelo

joblib.load('modelo_entrenado.pkl') # Carga del modelo

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Realizar una predicción para un año futuro
future_year = 2022
future_prediction = model.predict([[future_year]])
print("Predicción para el año", future_year, ":", future_prediction)

"""#Para árbol de decisión clasificador"""

# Modelización con árbol de desición clasificador
# Preprocesamiento de los datos 
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['resource'].values  # Crecimiento como variable objetivo

# Crear y entrenar el modelo de árbol de decisión clasificador
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Visualizar el árbol de decisión
fig, ax = plt.subplots(figsize=(12, 8))
tree.plot_tree(model, feature_names=['year'], class_names=['resource'], filled=True, ax=ax)
plt.title('Árbol de Decisión para el Crecimiento de Energías Renovables en Nueva Zelanda')
plt.show()

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['flag'].values.reshape(-1, 1)  # Crecimiento como variable objetivo

# Crear y entrenar el modelo de árbol de decisión clasificador
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Guardar y cargar el modelo
import joblib 

joblib.dump(model, 'modelo_entrenado.pkl') # Guardar el modelo

joblib.load('modelo_entrenado.pkl') # Carga del modelo

# Generar valores de predicción para todos los años desde 2007 hasta 2021
X_future = [[year] for year in range(2007, 2022)]
y_pred = model.predict(X_future)