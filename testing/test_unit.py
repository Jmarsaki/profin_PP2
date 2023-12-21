from flask import Flask

def test_unit():
    app = Flask(__name__)  # Crear una instancia de la aplicación Flask
    assert app is not None, "Error: Flask app is not initialized"  # Verificar que la aplicación no es None
    print("listo")  # Imprimir "listo" si la prueba es exitosa

# Prueba de la función test_unit
test_unit()