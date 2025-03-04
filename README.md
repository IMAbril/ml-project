# ML-PROJECT

🌍 **English | Español**  

This is a template for Machine Learning projects, structured for modularity, maintainability, and scalability.  
Este es un template para proyectos de Machine Learning, estructurado para facilitar la modularidad, mantenibilidad y escalabilidad.  

---

## 📁 Project Structure / Estructura del Proyecto

```
ML-PROJECT/
│── ml_project.egg-info/       # Metadata generated when installing the package / Metadatos generados al instalar el paquete
│── src/                       # Project source code / Código fuente del proyecto
│   ├── components/            # Core modules of the ML pipeline / Módulos fundamentales del pipeline de ML
│   │   ├── data_ingestion.py        # Data loading and partitioning / Carga y partición de datos
│   │   ├── data_transformation.py   # Data preprocessing and transformation / Preprocesamiento y transformación de datos
│   │   ├── model_trainer.py         # Model training and validation / Entrenamiento y validación del modelo
│   │   ├── __init__.py              # Enables package recognition / Permite tratar la carpeta como un paquete
│   │
│   ├── pipeline/              # ML pipelines definition / Definición de los pipelines de ML
│   │   ├── train_pipeline.py   # Training pipeline orchestration / Orquestación del pipeline de entrenamiento
│   │   ├── predict_pipeline.py # Prediction pipeline orchestration / Orquestación del pipeline de predicción
│   │   ├── __init__.py         # Enables package recognition / Permite tratar la carpeta como un paquete
│   │
│   ├── exception.py            # Custom error handling / Manejo de errores personalizados
│   ├── logger.py               # Logging system configuration / Configuración del sistema de logging
│   ├── utils.py                # Reusable helper functions / Funciones auxiliares reutilizables
│   ├── __init__.py             # Enables package recognition / Permite tratar la carpeta como un paquete
│
│── .gitignore                  # Files and folders to exclude from Git / Archivos y carpetas a excluir en Git
│── pyproject.toml              # Environment and dependencies configuration / Configuración del entorno y dependencias
│── README.md                   # Project documentation / Documentación del proyecto
│── venv/                       # Python virtual environment / Entorno virtual de Python
```

---

## 📌 File Descriptions / Descripción de Archivos

### 📂 `components/`
- **`data_ingestion.py`**  
  - 📌 **EN:** Loads data from various sources (CSV files, databases, APIs) and splits it into training and test sets.  
  - 📌 **ES:** Carga datos desde diferentes fuentes (archivos CSV, bases de datos, APIs) y los divide en conjuntos de entrenamiento y prueba.  

- **`data_transformation.py`**  
  - 📌 **EN:** Applies transformations such as normalization, categorical encoding, and feature selection.  
  - 📌 **ES:** Aplica transformaciones como normalización, codificación de variables categóricas y selección de características.  

- **`model_trainer.py`**  
  - 📌 **EN:** Implements model training, hyperparameter tuning, and evaluation.  
  - 📌 **ES:** Implementa el entrenamiento del modelo, el ajuste de hiperparámetros y la evaluación.  

---

### 📂 `pipeline/`
- **`train_pipeline.py`**  
  - 📌 **EN:** Manages the entire training workflow, calling `data_ingestion.py`, `data_transformation.py`, and `model_trainer.py`.  
  - 📌 **ES:** Coordina el flujo de trabajo del entrenamiento, llamando a `data_ingestion.py`, `data_transformation.py` y `model_trainer.py`.  

- **`predict_pipeline.py`**  
  - 📌 **EN:** Handles the full prediction process, from data transformation to final prediction.  
  - 📌 **ES:** Orquesta el proceso de predicción, desde la transformación de los datos hasta la obtención de la predicción final.  

---

### 📄 Other Files / Otros Archivos
- **`exception.py`**  
  - 📌 **EN:** Defines custom exception classes for better error handling.  
  - 📌 **ES:** Define clases de excepciones personalizadas para un mejor manejo de errores.  

- **`logger.py`**  
  - 📌 **EN:** Configures the logging system to monitor execution.  
  - 📌 **ES:** Configura el sistema de logs para monitorear la ejecución del código.  

- **`utils.py`**  
  - 📌 **EN:** Contains reusable helper functions to avoid code duplication.  
  - 📌 **ES:** Contiene funciones auxiliares reutilizables para evitar duplicación de código.  

---

## 🚀 Usage / Uso

### 🔹 Setup / Configuración
```bash
# Create virtual environment / Crear entorno virtual
python -m venv venv

# Activate environment / Activar entorno
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies / Instalar dependencias
pip install .
```

### 🔹 Train the Model / Entrenar el Modelo
```bash
python src/pipeline/train_pipeline.py
```

### 🔹 Make Predictions / Hacer Predicciones
```bash
python src/pipeline/predict_pipeline.py
```

---

## 🤝 Contributions / Contribuciones

This template was originally obtained from **Krish Naik** on YouTube.  
Este template fue obtenido originalmente de **Krish Naik** en YouTube.  

### How to Contribute? / ¿Cómo Contribuir?
1. **Fork this repository** and clone it to your local machine.  
   **Haz un fork de este repositorio** y clónalo en tu máquina local.  

2. **Create a new branch** for your changes.  
   **Crea una nueva rama** para tus cambios.  
   ```bash
   git checkout -b feature-branch
   ```

3. **Make your modifications** and commit them with a clear message.  
   **Realiza tus modificaciones** y haz commit con un mensaje claro.  
   ```bash
   git commit -m "Added feature X"
   ```

4. **Push your branch** to your forked repository.  
   **Sube tu rama** a tu repositorio bifurcado.  
   ```bash
   git push origin feature-branch
   ```

5. **Open a pull request (PR)** to merge your changes.  
   **Abre un pull request (PR)** para fusionar tus cambios.  

Thank you for contributing! 🚀  
¡Gracias por contribuir! 🚀

