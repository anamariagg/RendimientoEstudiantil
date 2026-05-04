## Fase 2 – Despliegue del Modelo en Contenedor Docker

## Introducción

En esta fase se lleva a cabo el proceso de despliegue del modelo predictivo desarrollado previamente en la Fase 1. Mientras que en la fase anterior el enfoque estuvo centrado en el análisis de datos, selección de variables y entrenamiento del modelo, en esta etapa se busca hacer el modelo portable, reproducible y ejecutable en cualquier entorno mediante el uso de contenedores.

El uso de Docker permite encapsular tanto el código como las dependencias necesarias, eliminando problemas de compatibilidad y facilitando la ejecución del modelo en diferentes sistemas sin necesidad de configuraciones adicionales.

## Objetivo de la Fase

El objetivo principal de esta fase es construir un entorno de ejecución que permita:

* Entrenar nuevamente el modelo con datos actualizados.
* Generar predicciones a partir de nuevos datos.
* Garantizar la reproducibilidad del proceso.
* Facilitar la portabilidad del modelo a otros entornos.

###  Explicación de la estructura

* **data/**: contiene los datos de entrada necesarios para el entrenamiento y la predicción.
* **train.py**: script encargado del entrenamiento del modelo.
* **predict.py**: script que utiliza el modelo entrenado para generar predicciones.
* **Dockerfile**: archivo que define el entorno de ejecución del contenedor.
* **requirements.txt**: lista de dependencias necesarias para ejecutar el proyecto.
* **README.md**: documentación del proceso.

## Tecnologías y Librerías Utilizadas

El desarrollo de esta fase se apoya en herramientas ampliamente utilizadas en ciencia de datos:

* **Python 3.10**: lenguaje principal del proyecto.
* **pandas**: manipulación y análisis de datos.
* **scikit-learn**: construcción y entrenamiento del modelo predictivo.
* **joblib**: serialización y almacenamiento del modelo.
* **Docker**: creación de contenedores para despliegue.

Estas herramientas permiten implementar una solución robusta, escalable y fácil de mantener.

##  Descripción Detallada del Proceso

###  Script de Entrenamiento (`train.py`)

El script `train.py` constituye el núcleo del proceso de aprendizaje del modelo. Su funcionamiento se desarrolla en varias etapas:

1. **Carga de datos**
   Se leen los datos desde el archivo `train.csv`, el cual contiene tanto las variables predictoras como la variable objetivo (`nota_final`).

2. **Preprocesamiento de datos**
   Se realiza la transformación de la variable categórica `apoyo_familiar` a valores numéricos (0 y 1), lo cual es necesario para que el modelo pueda interpretarla correctamente.

3. **Definición de variables**
   Se separan las variables independientes (`horas_estudio`, `inasistencias`, `apoyo_familiar`) de la variable dependiente (`nota_final`).

4. **División del conjunto de datos**
   Se divide el conjunto en datos de entrenamiento y prueba, permitiendo evaluar el comportamiento del modelo.

5. **Entrenamiento del modelo**
   Se utiliza el algoritmo **RandomForestRegressor**, el cual es adecuado para problemas de regresión y permite capturar relaciones no lineales entre variables.

6. **Persistencia del modelo**
   Una vez entrenado, el modelo se guarda en el archivo `model.pkl`, permitiendo su reutilización sin necesidad de reentrenar.

Este proceso asegura que el modelo esté listo para ser utilizado en escenarios reales.

###  Script de Predicción (`predict.py`)

El script `predict.py` permite aplicar el modelo entrenado sobre nuevos datos. Su funcionamiento incluye:

1. **Carga del modelo**
   Se carga el modelo previamente entrenado desde el archivo `model.pkl`.

2. **Lectura de datos de entrada**
   Se leen los datos desde `test.csv`, los cuales no contienen la variable objetivo.

3. **Preprocesamiento**
   Se aplica la misma transformación realizada en el entrenamiento para mantener consistencia.

4. **Generación de predicciones**
   El modelo genera valores estimados de la variable `nota_final`.

5. **Almacenamiento de resultados**
   Las predicciones se guardan en `predictions.csv`, permitiendo su análisis posterior.

Este script simula un escenario real donde el modelo se utiliza para predecir resultados sobre nuevos datos.

##  Contenerización con Docker

El uso de Docker permite encapsular todo el entorno del proyecto. El archivo `Dockerfile` define:

* La imagen base de Python.
* El directorio de trabajo.
* La copia de archivos del proyecto.
* La instalación de dependencias.

Esto garantiza que cualquier usuario pueda ejecutar el proyecto sin preocuparse por configuraciones locales.

## Resultados Esperados

Al finalizar la ejecución del proyecto se obtienen:

* Un modelo entrenado reutilizable.
* Un conjunto de predicciones generadas a partir de nuevos datos.
* Un entorno completamente reproducible.

## Conclusiones

La implementación de esta fase permite transformar un modelo académico en una solución lista para despliegue. La contenerización con Docker garantiza:

* Portabilidad entre sistemas.
* Reproducibilidad de resultados.
* Independencia del entorno local.

Esto representa una práctica fundamental en el desarrollo moderno de soluciones basadas en ciencia de datos y aprendizaje automático.

