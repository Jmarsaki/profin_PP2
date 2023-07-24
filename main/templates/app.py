import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener el archivo CSV cargado por el usuario
        archivo = request.files['file']
        df = pd.read_csv(archivo, encoding="latin-1")

        # Realizar el cálculo y obtener los resultados
        resultados = calcular_resultados(df)
        return render_template('resultados.html', resultados=resultados)
    return render_template('index.html')

def calcular_resultados(df):
    # Cálculo de promedio anual
    average_values = df.groupby('year')['data_value'].mean()

   # Datos de años y promedio anual
year = np.array(average_values.index).reshape(-1, 1)
promedio_anual = average_values.values

# Crear el objeto del modelo de árbol de decisión regresor
arbol_regresor = DecisionTreeRegressor()

# Ajustar el modelo a los datos de entrenamiento
arbol_regresor.fit(year, promedio_anual)

# Guardar el modelo entrenado en formato pickle
joblib.dump(arbol_regresor, 'modelo_entrenado.pkl')

# Preparar los datos para la predicción del año 2022
valor_prediccion_2022 = np.array([[2022]])

# Realizar la predicción para el año 2022
prediccion_2022 = arbol_regresor.predict(valor_prediccion_2022)

# Realizar la predicción de incremento para el año 2022
promedio_2021 = average_values.loc[2021]
promedio_2022 = prediccion_2022[0]
incremento_2022 = promedio_2022 - promedio_2021

# Realizar la predicción en el rango de años para obtener la línea de ajuste
year_rango = np.arange(year.min(), year.max() + 1).reshape(-1, 1)
linea_ajuste = arbol_regresor.predict(year_rango)

from sklearn.tree import export_graphviz
import graphviz

# Función para calcular el incremento de producción y su porcentaje
def calcular_incremento_produccion(actual, anterior):
    incremento = actual - anterior
    incremento_porcentaje = (incremento / anterior) * 100
    return incremento, incremento_porcentaje

# Obtener los conjuntos de valores de fortalezas, oportunidades, debilidades y amenazas
Conjunto_fortalezas = []
Conjunto_oportunidades = []
Conjunto_debilidades = []
Conjunto_amenazas = []

# Ingresar los conjuntos de valores de fortalezas
print("Ingrese los valores de fortalezas (separados por espacios):")
fortalezas_input = input().split()
for valor in fortalezas_input:
    Conjunto_fortalezas.append(int(valor))

# Ingresar los conjuntos de valores de oportunidades
print("Ingrese los valores de oportunidades (separados por espacios):")
oportunidades_input = input().split()
for valor in oportunidades_input:
    Conjunto_oportunidades.append(int(valor))

# Ingresar los conjuntos de valores de debilidades
print("Ingrese los valores de debilidades (separados por espacios):")
debilidades_input = input().split()
for valor in debilidades_input:
    Conjunto_debilidades.append(int(valor))

# Ingresar los conjuntos de valores de amenazas
print("Ingrese los valores de amenazas (separados por espacios):")
amenazas_input = input().split()
for valor in amenazas_input:
    Conjunto_amenazas.append(int(valor))

# Preparar los datos para la predicción del año 2022
valor_prediccion_2022 = np.array([[2022]])

# Realizar la predicción para el año 2022
prediccion_2022 = arbol_regresor.predict(valor_prediccion_2022)

# Obtener el valor de la predicción para 2022
valor_prediccion_2022 = prediccion_2022[0]

# Calcular el incremento y el porcentaje de incremento para el año 2022
incremento_2022, incremento_porcentaje_2022 = calcular_incremento_produccion(valor_prediccion_2022, promedio_anual[-1])

# Calcular el impacto del incremento de producción en cada categoría
puntaje_fortalezas = 1
for fortaleza in Conjunto_fortalezas:
    puntaje_fortalezas *= fortaleza

puntaje_oportunidades = 1
for oportunidad in Conjunto_oportunidades:
    puntaje_oportunidades *= oportunidad

puntaje_debilidades = 1
for debilidad in Conjunto_debilidades:
    puntaje_debilidades *= debilidad

puntaje_amenazas = 1
for amenaza in Conjunto_amenazas:
    puntaje_amenazas *= amenaza

# Calcular los valores promedio de data_value por cada año
average_values = df.groupby('year')['data_value'].mean()

# Calcular los incrementos de producción para cada año
incrementos = {}
years = sorted(df['year'].unique())
for i in range(1, len(years)):
    actual = average_values.loc[years[i]]
    anterior = average_values.loc[years[i-1]]
    incremento, incremento_porcentaje = calcular_incremento_produccion(actual, anterior)
    incrementos[years[i]] = {'incremento': incremento, 'incremento_porcentaje': incremento_porcentaje}

# Calcular el incremento y el porcentaje de incremento para el año 2021
incremento_2021, incremento_porcentaje_2021 = calcular_incremento_produccion(average_values.loc[2021], average_values.loc[2020])

# Calcular el impacto del incremento de producción en cada categoría en 2021
impacto_fortalezas_2021 = incremento_porcentaje_2021 * puntaje_fortalezas
impacto_oportunidades_2021 = incremento_porcentaje_2021 * puntaje_oportunidades
impacto_debilidades_2021 = incremento_porcentaje_2021 * puntaje_debilidades
impacto_amenazas_2021 = incremento_porcentaje_2021 * puntaje_amenazas

# Mostrar los incrementos anuales
print("Incremento anual de data_value:")
for year, incremento_info in incrementos.items():
    incremento = incremento_info['incremento']
    incremento_porcentaje = incremento_info['incremento_porcentaje']
    print(f"Año {year}: Incremento: {incremento}, Porcentaje: {incremento_porcentaje}%")

# Mostrar los resultados
print("Incremento de producción 2021:", incremento_2021)
print("Incremento de producción 2021 (%):", incremento_porcentaje_2021)
print("Impacto en Fortalezas 2021:", impacto_fortalezas_2021)
print("Impacto en Oportunidades 2021:", impacto_oportunidades_2021)
print("Impacto en Debilidades 2021:", impacto_debilidades_2021)
print("Impacto en Amenazas 2021:", impacto_amenazas_2021)

# Calcular el impacto del incremento de producción en cada categoría en 2022
impacto_fortalezas_2022 = incremento_porcentaje_2022 * puntaje_fortalezas
impacto_oportunidades_2022 = incremento_porcentaje_2022 * puntaje_oportunidades
impacto_debilidades_2022 = incremento_porcentaje_2022 * puntaje_debilidades
impacto_amenazas_2022 = incremento_porcentaje_2022 * puntaje_amenazas

# Mostrar los resultados de predicción para 2022
print("Incremento de producción 2022:", incremento_2022)
print("Predicción para el año 2022:", valor_prediccion_2022)
print("Impacto en Fortalezas 2022:", impacto_fortalezas_2022)
print("Impacto en Oportunidades 2022:", impacto_oportunidades_2022)
print("Impacto en Debilidades 2022:", impacto_debilidades_2022)
print("Impacto en Amenazas 2022:", impacto_amenazas_2022)

return resultados

if __name__ == '__main__':
    app.run(debug=True)
