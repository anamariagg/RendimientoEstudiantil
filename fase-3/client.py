import requests

url = "http://localhost:5000/predict"

datos = {
    "horas_estudio": 5,
    "inasistencias": 2,
    "apoyo_familiar": "si"
}

respuesta = requests.post(url, json=datos)

print(respuesta.json())
