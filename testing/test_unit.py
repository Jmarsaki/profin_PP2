# -*- coding: utf-8 -*-
"""test_unit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qy9IgXVkLFaUT1UY95tp2ydaAHLBXSzk
"""

from flask import Flask

def test_unit():
    app = Flask(__name__)  # Crear una instancia de la aplicación Flask
    assert app is not None, "Error: Flask app is not initialized"  # Verificar que la aplicación no es None
    print("listo")  # Imprimir "listo" si la prueba es exitosa

# Prueba de la función test_unit
test_unit()