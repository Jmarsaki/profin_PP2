# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KYp2cqS0Ar_wsJwuuFpP7APaNf4BOS9n

#Entrenamiento del modelo

#Con regresión lineal
"""

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['flag'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba para regresión lineal
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

"""#Con regresión logística"""

# Preprocesamiento de los datos
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['flag'].values.reshape(-1, 1)  # Generación como variable objetivo

# División de los datos en conjuntos de entrenamiento y prueba para regresión logística
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LogisticRegression()
model.fit(X_train, y_train)

"""#Con árbol de desición"""

# Preprocesamiento de los datos 
X = df['year'].values.reshape(-1, 1)  # Año como característica
y = df['flag'].values.reshape(-1, 1)  # Crecimiento como variable objetivo

# Crear y entrenar el modelo de árbol de decisión clasificador
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)