# -*- coding: utf-8 -*-
"""métricas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12r_G2a-zAU8f4GTNWFcM7rUCr2c3htwA

#Métrica para regresión lineal
"""

# Evaluar el modelo utilizando el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Error Cuadrático Medio (MSE):", mse)

"""#Métricas para regresión logística

"""

# Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

# Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

# Recall
from sklearn.metrics import recall_score
recall_score(y_test, y_pred, average=None)

# Precision
from sklearn.metrics import precision_score
precision_score(y_test, y_pred, average=None)

"""#Métrica para modelo con árbol de desición clasificador"""

print(f"Profundidad del árbol: {clf.get_depth()}")
print(f"Número de nodos terminales: {clf.get_n_leaves()}")

# neg_root_mean_squared_error de test
# ==============================================================================

rmse = mean_squared_error(
        y_true = y_test,
        y_pred = predicciones,
        squared = False
       )
rmse

# Clasificación predicha
# ==============================================================================
clasificacion = np.where(predicciones<0.5, 0, 1)
clasificacion

# Matriz de confusión de las predicciones de test
# ==============================================================================
confusion_matrix = pd.crosstab(
    y_test.ravel(),
    clasificacion,
    rownames=['Real'],
    colnames=['Predicción']
)
confusion_matrix

# Accuracy de test del modelo 
# ==============================================================================
clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)
print(f"El accuracy de test es: {100*accuracy}%")

"""#Matriz FODA"""

# En el caso del análisis de la transformación a energías renovables en Nueva Zelandia por políticas de promoción podemos utilizar el concepto DAFO de la siguiente manera
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