import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

def test_pre_train():
    df = pd.read_csv("/content/drive/MyDrive/Unitsdollars_Excel.csv", encoding="latin-1")

    # Eliminar las columnas que no son necesarias para el entrenamiento
    df.drop(['resource', 'variable', 'units', 'magnitude', 'source', 'flag'], axis=1, inplace=True)

    # Separar los datos de entrada (X) y las etiquetas de salida (y)
    X = df[['year']]
    y = df['data_value']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Crear un modelo AR
    order = 1  # Puedes ajustar el orden del modelo AR según sea necesario
    modelo_ar = sm.tsa.AutoReg(y_train, lags=order).fit()

    assert X_train is not None, "Error: X_train is None"
    assert X_test is not None, "Error: X_test is None"
    assert y_train is not None, "Error: y_train is None"
    assert y_test is not None, "Error: y_test is None"
    assert modelo_ar is not None, "Error: AR model is not trained"
    print("Listo")

test_pre_train()