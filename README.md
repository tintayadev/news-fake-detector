# News Fake Detector

## Descripción

**News Fake Detector** es una aplicación que utiliza inteligencia artificial para identificar noticias falsas. El proyecto consta de dos partes principales:
- **Backend**: Desarrollado en Django, proporciona una API para procesar y clasificar noticias.
- **Frontend**: Desarrollado en SvelteKit, permite a los usuarios ingresar noticias y recibir la clasificación del modelo.

## Estructura del Proyecto

- **backend/**: Contiene el código del backend desarrollado con Django.
- **frontend/**: Contiene el código del frontend desarrollado con SvelteKit.


## Dataset

El modelo fue entrenado utilizando el dataset de Kaggle [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset). Los archivos de datos no están incluidos en este repositorio debido a su tamaño. Puedes descargar el dataset desde el enlace proporcionado y colocarlo en el directorio adecuado para entrenar el modelo.


## Requisitos

- Python 3.8 o superior
- Node.js 16 o superior

## Configuración del Backend

1. Navega al directorio `fake_news-detector/`:
   ```bash
   cd fake_news-detector
   ```
2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Ejecuta las migraciones y el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

   El backend estará disponible en `http://localhost:8000`.

## Configuración del Frontend

1. Navega al directorio `my-sveltekit-project/`:
   ```bash
   cd my-sveltekit-project
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Ejecuta el servidor de desarrollo:
   ```bash
   npm run dev
   ```

   El frontend estará disponible en `http://localhost:3000`.

## Uso

1. Abre el frontend en tu navegador (`http://localhost:3000`).
2. Ingresa un texto de noticia en el formulario proporcionado.
3. Haz clic en el botón para enviar el texto al backend.
4. Recibe la clasificación de la noticia (Real o Falsa) en la interfaz.

