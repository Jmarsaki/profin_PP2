import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import h5py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener el archivo CSV cargado por el usuario
        archivo = request.files['file']
        df = pd.read_csv(archivo, encoding="latin-1")

        # Cargar el modelo entrenado del archivo HDF5
        modelo = cargar_modelo_hdf5('modelo_entrenado.h5')

        # Realizar el cálculo y obtener los resultados
        resultados = calcular_resultados(df, modelo)
        return render_template('resultados.html', resultados=resultados)
    return render_template('index.html')

def get_resultados(categoria):
    print(f"Ingrese los valores de {categoria} (separados por espacios):")
    valores_input = input().split()
    return [int(valor) for valor in valores_input]

def calcular_incremento_produccion(actual, anterior):
    incremento = actual - anterior
    incremento_porcentaje = (incremento / anterior) * 100
    return incremento, incremento_porcentaje

def cargar_modelo_hdf5(nombre_archivo):
    with h5py.File(nombre_archivo, 'r') as f:
        modelo_dt = dict(f['modelo'].attrs.items())
        arbol_decision_state = f['modelo']['arbol_decision'][:]
        modelo_cargado = DecisionTreeRegressor()
        modelo_cargado.tree_.__setstate__(arbol_decision_state)
        modelo_cargado.set_params(**modelo_dt)
    return modelo_cargado

def calcular_resultados(df, modelo):
     # Cálculo de promedio anual
    average_values = df.groupby('year')['data_value'].mean()

    # Datos de años y promedio anual
    year = np.array(average_values.index).reshape(-1, 1)
    promedio_anual = average_values.values

    # Calcular los incrementos de producción para cada año
    incrementos = {}
    years = sorted(df['year'].unique())
    for i in range(1, len(years)):
        actual = average_values.loc[years[i]]
        anterior = average_values.loc[years[i-1]]
        incremento, incremento_porcentaje = calcular_incremento_produccion(actual, anterior)
        incrementos[years[i]] = {'incremento': incremento, 'incremento_porcentaje': incremento_porcentaje}

    # Preparar los datos para la predicción del año 2022
    valor_prediccion_2022 = np.array([[2022]])

    # Realizar la predicción para el año 2022
    prediccion_2022 = modelo.predict(valor_prediccion_2022)

    # Obtener el valor de la predicción para 2022
    valor_prediccion_2022 = prediccion_2022[0]

    # Calcular el incremento y el porcentaje de incremento para el año 2022
    incremento_2022, incremento_porcentaje_2022 = calcular_incremento_produccion(valor_prediccion_2022, promedio_anual[-1])

    # Obtener los conjuntos de valores de fortalezas, oportunidades, debilidades y amenazas
    Conjunto_fortalezas = get_resultados('fortalezas')
    Conjunto_oportunidades = get_resultados('oportunidades')
    Conjunto_debilidades = get_resultados('debilidades')
    Conjunto_amenazas = get_resultados('amenazas')

    # Calcular el impacto del incremento de producción en cada categoría en 2021
    incremento_2021, incremento_porcentaje_2021 = calcular_incremento_produccion(average_values.loc[2021], average_values.loc[2020])
    impacto_fortalezas_2021 = incremento_porcentaje_2021 * np.prod(Conjunto_fortalezas)
    impacto_oportunidades_2021 = incremento_porcentaje_2021 * np.prod(Conjunto_oportunidades)
    impacto_debilidades_2021 = incremento_porcentaje_2021 * np.prod(Conjunto_debilidades)
    impacto_amenazas_2021 = incremento_porcentaje_2021 * np.prod(Conjunto_amenazas)

    # Calcular el impacto del incremento de producción en cada categoría en 2022
    impacto_fortalezas_2022 = incremento_porcentaje_2022 * np.prod(Conjunto_fortalezas)
    impacto_oportunidades_2022 = incremento_porcentaje_2022 * np.prod(Conjunto_oportunidades)
    impacto_debilidades_2022 = incremento_porcentaje_2022 * np.prod(Conjunto_debilidades)
    impacto_amenazas_2022 = incremento_porcentaje_2022 * np.prod(Conjunto_amenazas)

    # Crear un diccionario con todos los resultados
    resultados = {
        'prediccion_2022': valor_prediccion_2022,
        'incremento_2022': incremento_2022,
        'incremento_porcentaje_2022': incremento_porcentaje_2022,
        'incrementos_anuales': incrementos,
        'incremento_2021': incremento_2021,
        'incremento_porcentaje_2021': incremento_porcentaje_2021,
        'impacto_fortalezas_2021': impacto_fortalezas_2021,
        'impacto_oportunidades_2021': impacto_oportunidades_2021,
        'impacto_debilidades_2021': impacto_debilidades_2021,
        'impacto_amenazas_2021': impacto_amenazas_2021,
        'impacto_fortalezas_2022': impacto_fortalezas_2022,
        'impacto_oportunidades_2022': impacto_oportunidades_2022,
        'impacto_debilidades_2022': impacto_debilidades_2022,
        'impacto_amenazas_2022': impacto_amenazas_2022,
    }

    return resultados

if __name__ == '__main__':
    app.run(debug=True)
