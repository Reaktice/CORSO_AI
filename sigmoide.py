import numpy as np

def sigmoid(x):
    """
    Funzione Sigmoide.

    Parametri:
    x : array-like o scalare
        Input alla funzione sigmoide.

    Restituisce:
    array-like o scalare
        Output della funzione sigmoide.
    """
    return 1 / (1 + np.exp(-x))

# Esempio di utilizzo
x = np.array([0, 1, 2, 3, 4])
print(sigmoid(x))