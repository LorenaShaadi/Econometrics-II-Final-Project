# Econometrics-II-Final-Project

## Descripción

Este proyecto consiste en un scraper que utiliza la API pública de YouTube para extraer comentarios de un video educativo sobre economía de CrashCourse.  
El objetivo es obtener al menos 500 comentarios para analizar las respuestas y opiniones de los usuarios respecto al contenido del video, guardándolos en un dataset CSV para futuros análisis.

---

## Estructura del repositorio

Econometrics-II-Final-Project/
├── README.md
├── .gitignore
├── requirements.txt
├── code/
│   └── scrape_comments.py
└── data/
    └── dataset.csv


## Instrucciones de uso

### 1. Clonar el repositorio

git clone https://github.com/LorenaShaadi/Econometrics-II-Final-Project.git
cd Econometrics-II-Final-Project

### 2. Crear y activar el entorno virtual

python -m venv venv
# En macOS/Linux
source venv/bin/activate
# En Windows (PowerShell)
.\venv\Scripts\Activate.ps1

### 3. Instalar dependencias

pip install -r requirements.txt

### 4. Configurar la API Key

Crear un archivo .env en la raíz del proyecto.

Agregar la línea (con tu clave real):

API_KEY=tu_api_key_aqui

### 5. Ejecutar el scraper

python code/scrape_comments.py

### 6. Resultado

Los comentarios extraídos se guardan en data/dataset.csv

El archivo contiene columnas: comment_id, text, video_id.

---

## Notas importantes

El archivo .env no está incluido en el repositorio por razones de seguridad.

Asegúrate de tener una API key válida de YouTube Data API v3.

El scraper obtiene hasta 500 comentarios por video.
