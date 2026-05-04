import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Cargar datos
data = pd.read_csv("data/train.csv")

# Convertir variable categórica
data['apoyo_familiar'] = data['apoyo_familiar'].map({'no': 0, 'si': 1})

# Variables
X = data[['horas_estudio', 'inasistencias', 'apoyo_familiar']]
y = data['nota_final']

# División
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Modelo
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, "model.pkl")

print("Modelo entrenado correctamente")
