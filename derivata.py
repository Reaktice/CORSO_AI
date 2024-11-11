import numpy as np  # Importa la libreria NumPy per il calcolo scientifico

# Definizione della funzione di perdita quadratica
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

# Derivata della funzione di perdita
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

# Esempio di utilizzo della funzione di perdita e della sua derivata
x = np.array([0.5, 1.5, 2.5])  # Valori predetti dal modello
y = np.array([1.0, 2.0, 3.0])  # Valori target reali

# Calcola la perdita per i valori dati
l = loss(x, y)
print("Perdita:", l)

# Calcola la derivata della perdita per i valori dati
dl_dx = loss_derivative(x, y)
print("Derivata della perdita:", dl_dx)
