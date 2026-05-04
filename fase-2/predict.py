import pandas as pd
import joblib

model = joblib.load("model.pkl")

data = pd.read_csv("data/test.csv")

data['apoyo_familiar'] = data['apoyo_familiar'].map({'no': 0, 'si': 1})

predictions = model.predict(data)

pd.DataFrame(predictions, columns=["nota_predicha"]).to_csv("predictions.csv", index=False)

print("Predicciones listas")
