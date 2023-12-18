import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import pickle
import os

# Configurar la carpeta de carga
UPLOAD_FOLDER = 'carpeta_temporal'  # Reemplaza 'carpeta_temporal' con la ruta deseada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configuración de la carpeta de carga

# Definir las variables globalmente
incrementos = []
matriz_dafo = []
modelo_prediccion = None

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

@app.route("/dafo")
def dafo():
    global incrementos, matriz_dafo  # Acceder a las variables globales
    incrementos = input("Introduce los incrementos anuales separados por comas: ").split(",")
    incrementos = [int(incremento) for incremento in incrementos]

    matriz_dafo = {}
    for factor in ["Debilidades", "Fortalezas", "Amenazas", "Oportunidades"]:
        valor = input(f"Introduce el valor de la categoría {factor}: ")
        matriz_dafo[factor] = int(valor)

    matriz_dafo = dict(matriz_dafo)
    
    return render_template("dafo.html", matriz_dafo=matriz_dafo)

@app.route("/impactos")
def impactos():
    global incrementos, matriz_dafo  # Acceder a las variables globales
    impactos = []
    for incremento in incrementos:
        impacto = 0
        for factor in matriz_dafo:
            if factor == "Debilidades":
                impacto -= incremento * matriz_dafo[factor]
            elif factor == "Fortalezas":
                impacto += incremento * matriz_dafo[factor]
            elif factor == "Amenazas":
                impacto -= incremento * matriz_dafo[factor]
            elif factor == "Oportunidades":
                impacto += incremento * matriz_dafo[factor]
        impactos.append(impacto)

    return render_template("calcular_impacto.html", impactos=impactos)

@app.route("/cargar_modelo", methods=['GET', 'POST'])
def cargar_modelo():
    global modelo_prediccion  # Acceder al modelo global
    if request.method == 'POST':
        if 'modelo_file' in request.files:
            modelo_file = request.files['modelo_file']
            if modelo_file.filename != '' and modelo_file.filename.endswith('.pkl'):
                # Obtener la ruta del archivo temporal
                modelo_file_path = os.path.join(app.config['UPLOAD_FOLDER'], modelo_file.filename)
                
                # Guardar el archivo temporal
                modelo_file.save(modelo_file_path)

                # Cargar el modelo desde el archivo .pkl
                with open(modelo_file_path, "rb") as f:
                    modelo_prediccion = pickle.load(f)
                
                # Eliminar el archivo temporal después de cargar el modelo
                os.remove(modelo_file_path)

                return redirect(url_for('calculo_predictivo_2022'))

    return render_template("cargar_modelo.html")

if __name__ == '__main__':
    app.run(debug=True)