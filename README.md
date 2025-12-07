# UnbundleAI MVP – API Documentation

UnbundleAI es un servicio impulsado por IA diseñado para analizar aplicaciones existentes y extraer información para el **desagregado (unbundling)**, la planificación de MVP y la reducción de funcionalidades.
Ayuda a fundadores, *indie hackers* y desarrolladores a comprender rápidamente cómo funciona una aplicación y qué producto más pequeño y enfocado podría construirse a partir de ella.

Este *backend* impulsa el MVP de UnbundleAI y está construido con **FastAPI**, **Python** y **modelos de inferencia de HuggingFace**, desplegado en **Render**.

---

## ✨ Features (Funcionalidades)

### 🔍 1. App Analyzer (Analizador de Aplicaciones)
Analiza cualquier descripción de aplicación y proporciona:
* Funcionalidades clave
* Segmentos de usuario
* Alcance funcional
* Fortalezas y limitaciones
* Ángulos potenciales de desagregado

### 📦 2. Feature Extraction (Extracción de Funcionalidades)
Produce una lista estructurada de:
* Funcionalidades
* Componentes
* Trabajos-a-realizar (*Jobs-to-be-done*)

### 📊 3. Unbundling Score (Lite) (Puntuación de Desagregado - Lite)
Una puntuación simple (0–1) que estima qué tan adecuada es una aplicación para el desagregado, basándose en:
* Densidad de funcionalidades
* Fragmentación de usuarios
* Puntos de dolor
* Oportunidades de enfoque de mercado

### 🛠️ 4. MVP Blueprint Generator (Lite) (Generador de Esquema de MVP - Lite)
Crea un plan inicial de MVP:
* Funcionalidades centrales a mantener
* Funcionalidades a eliminar
* *Pitch* de MVP de una sola frase
* Microproductos potenciales

---

## 🧠 How It Works (Cómo Funciona)

Usted envía una carga útil JSON que contiene una descripción textual de una aplicación.

La API:
1. Procesa el texto
2. Lo envía al LLM subyacente (HuggingFace)
3. Extrae información estructurada
4. Devuelve JSON con las ideas clave

### Example Response Format (Formato de Respuesta de Ejemplo)

```.json
{
  "analysis": "...",
  "features": ["..."],
  "opportunities": ["..."],
  "unbundling_score": 0.72,
  "mvp_blueprint": {
    "core_features": ["..."],
    "mvp_pitch": "..."
  }
}
```

---
## 🔗 Interactive Docs (Documentación Interactiva)

Vea la documentación completa de OpenAPI aquí:

👉 https://unbundleai-api.onrender.com/docs


## 🏗️ Tech Stack (Pila Tecnológica)

- FastAPI

- Python

- HuggingFace Inference API

- Render (Free Tier Hosting)
---

## 🚀 Deploy

You can deploy the API quickly using **Render** (or any cloud service supporting Python + FastAPI):

**Live API URL:** [https://unbundleai-api.onrender.com/](https://unbundleai-api.onrender.com/)

### Steps to Deploy
1. Push your code to a GitHub repository.
2. Go to [Render.com](https://render.com/) and create a new **Web Service**.
3. Connect your GitHub repo.
4. Set the **Build Command**:  
   ```.ssh
   pip install -r requirements.txt
   ```
5. Add your HuggingFace API key as an ***Environment Variable***:
    ```.env
     HUGGINGFACE_API_KEY=your_token_here
   ```
7. Set the Start **Command**:
   ```.ssh
     uvicorn app.main:app --host 0.0.0.0 --port 10000
   ```

## 📝 License (Licencia)

MIT License.
