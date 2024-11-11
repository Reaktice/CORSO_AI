import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Genera dati casuali per cani e gatti
np.random.seed(42)
dogs_x = np.random.normal(loc=1.5, scale=0.5, size=50)
dogs_y = np.random.normal(loc=1.5, scale=0.5, size=50)
cats_x = np.random.normal(loc=3, scale=0.5, size=50)
cats_y = np.random.normal(loc=3, scale=0.5, size=50)

# Unisce i dati
X = np.concatenate([dogs_x, cats_x])
Y = np.concatenate([dogs_y, cats_y])

# Applica la funzione sigmoide
sigmoid = lambda x: 1 / (1 + np.exp(-x))
X_normalized = sigmoid(X)
Y_normalized = sigmoid(Y)

# Dividi i dati normalizzati in cani e gatti
dogs_x_normalized = X_normalized[:50]
dogs_y_normalized = Y_normalized[:50]
cats_x_normalized = X_normalized[50:]
cats_y_normalized = Y_normalized[50:]

# Prepara i dati per la regressione logistica
data = np.column_stack((X_normalized, Y_normalized))
labels = np.array([0] * 50 + [1] * 50)  # Etichette: 0 per cani, 1 per gatti

# Crea e addestra il modello di regressione logistica
model = LogisticRegression()
model.fit(data, labels)

# Coefficienti della retta di separazione
coef = model.coef_[0]
intercept = model.intercept_

# Genera i valori x e y per la retta di separazione
x_values = np.linspace(0, 1, 100)
y_values = -(coef[0] * x_values + intercept) / coef[1]

# Visualizza i dati normalizzati
plt.scatter(dogs_x_normalized, dogs_y_normalized, color='blue', label='Cani')
plt.scatter(cats_x_normalized, cats_y_normalized, color='orange', label='Gatti')

# Visualizza la retta di separazione
plt.plot(x_values, y_values, color='green', label='Retta di separazione')

plt.xlabel('Feature 1 (normalizzata)')
plt.ylabel('Feature 2 (normalizzata)')
plt.legend()
plt.title('Classificazione di Cani e Gatti (dati normalizzati)')
plt.show()
