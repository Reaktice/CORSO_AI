from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Carica il dataset California Housing
housing = fetch_california_housing()
X, y = housing.data, housing.target

# Divide i dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crea un modello di regressione lineare
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predice i valori di test
y_pred = regressor.predict(X_test)

# Calcola le metriche di valutazione
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Errore Quadratico Medio (MSE): {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")
