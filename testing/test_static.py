import pandas as pd

def test_static():
    df = pd.read_csv("/content/drive/MyDrive/Unitsdollars_Excel.csv", encoding="latin-1")
    assert df is not None, "Error: DataFrame is not loaded"
    assert len(df.columns) == 8, "Error: DataFrame should have 8 columns"
    print ("listo")

# Prueba de la función test_static
test_static()