# Fase 3 - API REST para Modelo Predictivo

## Descripción

Esta fase implementa una API REST utilizando Flask para exponer el modelo predictivo de rendimiento estudiantil.

El modelo utiliza las siguientes variables:

* horas_estudio
* inasistencias
* apoyo_familiar

y predice la nota final del estudiante.

## Archivos

* train.py: reentrena el modelo y genera model.pkl.
* predict.py: realiza predicciones sobre un archivo CSV.
* apirest.py: expone los endpoints REST.
* client.py: ejemplo de consumo de la API.
* Dockerfile: configuración del contenedor.
* requirements.txt: dependencias del proyecto.

## Construcción de la imagen Docker

docker build -t rendimiento-api .

## Ejecución del contenedor

docker run -p 5000:5000 rendimiento-api

## Endpoint Predict

POST /predict

Ejemplo de entrada:

{
"horas_estudio": 5,
"inasistencias": 2,
"apoyo_familiar": "si"
}

Respuesta:

{
"nota_predicha": 4.5
}

## Endpoint Train

POST /train

Reentrena el modelo utilizando los datos de entrenamiento.

