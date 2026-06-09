from flask import Flask, request, jsonify
import pandas as pd
import joblib
import subprocess

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    model = joblib.load("model.pkl")

    datos = request.json

    apoyo = 1 if datos["apoyo_familiar"] == "si" else 0

    entrada = pd.DataFrame({
        "horas_estudio": [datos["horas_estudio"]],
        "inasistencias": [datos["inasistencias"]],
        "apoyo_familiar": [apoyo]
    })

    prediccion = model.predict(entrada)

    return jsonify({
        "nota_predicha": float(prediccion[0])
    })

@app.route('/train', methods=['POST'])
def train():

    subprocess.run(["python", "train.py"])

    return jsonify({
        "mensaje": "Modelo reentrenado"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
