# **Pipeline de AutoML con Despliegue en Docker**

Este proyecto implementa un pipeline de AutoML que realiza entrenamiento y despliegue de modelos de Machine Learning en una única ejecución. El pipeline admite dos modos de producción:

1. **Batch Prediction**: Procesa archivos Parquet en una carpeta de entrada y genera predicciones en una carpeta de salida.
2. **API**: Habilita un servicio FastAPI para predicciones en tiempo real.

---

## **Requisitos**

1. **Docker**: Instalar Docker [aquí](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Instalar Docker Compose [aquí](https://docs.docker.com/compose/install/).

---

## **Estructura del Proyecto**

├── api/                     # Código para la API
│   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env                 # Variables de entorno para la API
├── batch/                   # Código para Batch Prediction
│   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env                 # Variables de entorno para Batch Prediction
├── shared/                  # Código compartido para ambos modos
│   ├── preprocess.py
│   ├── predict.py
│   ├── utils.py
│   ├── models/
│       ├── trained_model.pkl
├── data/                    # Datos de entrada y salida
│   ├── dataset.parquet      # Dataset para entrenamiento
│   ├── input/               # Carpeta de entrada para Batch Prediction
│   ├── output/              # Carpeta de salida para Batch Prediction
├── docker-compose.yml       # Orquestación de servicios Docker
└── README.md                # Instrucciones del proyecto



---

## **Configuración Inicial**

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-repositorio/proyecto.git
   cd proyecto


## Construcción de los Contenedores
### Construye las imágenes Docker utilizando docker-compose:
 
```docker-compose build```