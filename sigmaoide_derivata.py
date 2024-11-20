import numpy as np

# Funzione Sigmoide
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

# Derivata della Funzione Sigmoide
def sigmoid_derivative(x):
    """
    Calcola la derivata della funzione sigmoide.

    Parametri:
    x : array-like o scalare
        Input alla funzione sigmoide.

    Restituisce:
    array-like o scalare
        Derivata della funzione sigmoide.
    """
    sig = sigmoid(x)
    return sig * (1 - sig)

# Funzione di Perdita Quadratica
def loss(x, y):
    """
    Calcola la funzione di perdita quadratica.
    
    La funzione di perdita quadratica è definita come:
    L(x) = 0.5 * (x - y)^2
    
    Dove:
    x = valore predetto dal modello
    y = valore target reale

    Parametri:
    x : array-like o scalare
        Valore predetto dal modello.
    y : array-like o scalare
        Valore target reale.

    Restituisce:
    array-like o scalare
        Valore della funzione di perdita.
    """
    return 0.5 * (x - y)**2

# Derivata della Funzione di Perdita
def loss_derivative(x, y):
    """
    Calcola la derivata della funzione di perdita quadratica rispetto a x.

    La derivata della funzione di perdita quadratica è:
    dL/dx = x - y

    Dove:
    x = valore predetto dal modello
    y = valore target reale

    Parametri:
    x : array-like o scalare
        Valore predetto dal modello.
    y : array-like o scalare
        Valore target reale.

    Restituisce:
    array-like o scalare
        Derivata della funzione di perdita rispetto a x.
    """
    return x - y

# Esempio di utilizzo
x = np.array([0, 1, 2, 3, 4])
print("Sigmoide:", sigmoid(x))
print("Derivata della Sigmoide:", sigmoid_derivative(x))

# Esempio di utilizzo della funzione di perdita e della sua derivata
pred = np.array([0.5, 1.5, 2.5])  # Valori predetti dal modello
target = np.array([1.0, 2.0, 3.0])  # Valori target reali

# Calcola la perdita per i valori dati
l = loss(pred, target)
print("Perdita:", l)

# Calcola la derivata della perdita per i valori dati
dl_dx = loss_derivative(pred, target)
print("Derivata della perdita:", dl_dx)
