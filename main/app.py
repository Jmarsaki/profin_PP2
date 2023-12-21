import pandas as pd
import numpy as np
from statsmodels.tsa.api import AutoReg
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Cargar el modelo desde un archivo .npy al inicio de la aplicación
loaded_coef = np.load('incremento_model.npy')
loaded_lag = np.load('incremento_data.npy')

# Crear un nuevo modelo AR con los coeficientes cargados y el lag
maxlag = min(2, len(loaded_lag) - 2)
loaded_model = AutoReg(loaded_lag, lags=maxlag)
loaded_model_fit = loaded_model.fit()


# Definir las variables globalmente
incremento_2022 = None
matriz_dafo = {
    'Debilidades': 0,
    'Fortalezas': 0,
    'Amenazas': 0,
    'Oportunidades': 0
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/incrementos", methods=['GET', 'POST'])
def incrementos():
    global incrementos  # Acceder a la variable global
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '' and file.filename.endswith('.csv'):
                df = pd.read_csv(file)
                df = df.dropna(subset=['data_value', 'year'])
                average_increments = df.groupby("year")["data_value"].mean()
                incrementos = list(average_increments)  # Actualizar la variable global
                return render_template("incrementos.html", average_increments=average_increments)

    return render_template("upload_form.html")

@app.route("/calculo_predictivo_2022", methods=['GET', 'POST'])
def calculo_predictivo_2022():
    if request.method == 'POST':
        # Verifica si se envió un archivo CSV
        if 'file' in request.files:
            file = request.files['file']
            
            # Verifica si se seleccionó un archivo y tiene la extensión CSV
            if file.filename != '' and file.filename.endswith('.csv'):
                # Carga el archivo CSV y realiza el cálculo de incrementos
                df = pd.read_csv(file)
                df = df.dropna(subset=['data_value', 'year'])
                
                # Filtra el DataFrame para obtener los datos necesarios para la predicción
                df_filtered = df[['year', 'data_value']].copy()
                df_filtered.sort_values('year', inplace=True)
                
                # Obtener la predicción para el año 2022
                prediction_2022 = loaded_model_fit.predict(start=len(df_filtered), end=len(df_filtered))
                prediction_2022_value = prediction_2022[0]

                return render_template("calculo_predictivo_2022.html", prediction=prediction_2022_value)

    # Si no se ha enviado un archivo o no es válido, renderiza el formulario
    return render_template("upload_form.html")

@app.route("/dafo", methods=['GET', 'POST'])
def dafo():
    global incremento_2022, matriz_dafo  # Acceder a las variables globales

    if request.method == 'POST':
        # Obtener los datos del formulario
        incremento_2022 = float(request.form.get('incremento_2022'))
        matriz_dafo['Debilidades'] = int(request.form.get('Debilidades'))
        matriz_dafo['Fortalezas'] = int(request.form.get('Fortalezas'))
        matriz_dafo['Amenazas'] = int(request.form.get('Amenazas'))
        matriz_dafo['Oportunidades'] = int(request.form.get('Oportunidades'))

        return render_template("dafo.html", incremento_2022=incremento_2022, matriz_dafo=matriz_dafo)

    return render_template("dafo.html")

@app.route("/impactos")
def impactos():
    global incremento_2022, matriz_dafo  # Acceder a las variables globales
    impactos = []

    for factor in matriz_dafo:
        if factor == "Debilidades":
            impacto = -incremento_2022 * matriz_dafo[factor]
        elif factor == "Fortalezas":
            impacto = incremento_2022 * matriz_dafo[factor]
        elif factor == "Amenazas":
            impacto = -incremento_2022 * matriz_dafo[factor]
        elif factor == "Oportunidades":
            impacto = incremento_2022 * matriz_dafo[factor]

        impactos.append(impacto)

    return render_template("calcular_impacto.html", impactos=impactos)

if __name__ == '__main__':
    app.run(debug=True)