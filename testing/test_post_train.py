import numpy as np
from statsmodels.tsa.api import AutoReg
import statsmodels.api as sm

def test_post_train():
   
    
    incremento_anual_model = open('/content/incremento_model.npy', 'rb')
    modelo_ar = sm.load("incremento_anual_model")  

    assert modelo_ar is not None, "Error: Model is not loaded"
    print("Listo")

test_post_train()