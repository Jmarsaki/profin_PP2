import numpy as np
import statsmodels.api as sm
import pandas as pd

def compare_floats(a, b, tolerance=1e-6):
    return abs(a - b) < tolerance

def test_evaluation():
    # Cargar datos de entrenamiento y ajustar el modelo AR
    data = pd.read_csv('/content/datos_entrenamiento.csv')  # Asegúrate de tener un archivo CSV con tus datos de entrenamiento
    endog = data['data_value']  # Ajusta el nombre de la columna según tus datos
    ar_model = sm.tsa.AR(endog).fit()

    # Guardar el modelo AR entrenado
    np.save(ar_model, '/content/incremento_model.npy')

    # Cargar el modelo AR entrenado
    ar_model_loaded = np.load('/content/incremento_model.npy')

    sample = 0  # Aquí se debe proporcionar el valor real correspondiente al incremento de producción de algún año 
    expected_prediction = 743182.1666666666  # Aquí se debe proporcionar el valor real esperado de la predicción

    # Realizar la predicción con el modelo AR
    prediction = ar_model_loaded.predict(start=len(endog), end=len(endog), dynamic=False)

    assert compare_floats(prediction.iloc[0], expected_prediction), f"Error: Expected {expected_prediction}, but got {prediction.iloc[0]}"
    print("Listo")

test_evaluation()