# Predictor de Calidad de Vino Tinto 🍷
Este proyecto es una aplicación web interactiva que utiliza **Machine Learning** para predecir si un vino tinto es de "Alta Calidad" o "Calidad Promedio" basándose en sus propiedades químicas.

🚀 **Puedes ver la aplicación funcionando aquí:** [https://pawi-wine-predictor.onrender.com](https://pawi-wine-predictor.onrender.com)

---

## 🧐 Sobre el Proyecto
El objetivo principal fue desarrollar un modelo predictivo utilizando el algoritmo **XGBoost**. El dataset utilizado contiene información sobre diversas variantes del vino tinto "Vinho Verde" de Portugal.

### Características analizadas:
- **Alcohol:** Contenido de alcohol en el vino.
- **Volatile Acidity:** Cantidad de ácido acético en el vino.
- **Sulphates:** Aditivos del vino que actúan como antimicrobianos.
- **Citric Acid:** Añade frescura y sabor al vino.
- **Total Sulfur Dioxide:** Cantidad de dióxido de azufre (libre y ligado).

---

## 🛠️ Tecnologías Utilizadas
- **Python 3.11.4**
- **Machine Learning:** XGBoost, Scikit-Learn, Pandas, NumPy.
- **Backend:** Flask (Web Framework).
- **Frontend:** HTML5 y CSS3 (diseño responsivo).
- **Despliegue:** Render.

---

## 📂 Estructura del Repositorio
El proyecto está organizado siguiendo los estándares de la academia:

- `/src`: Contiene el código fuente de la aplicación Flask (`app.py`), el modelo entrenado (`.pkl`) y el archivo de requerimientos.
- `/src/templates`: Contiene la interfaz de usuario (`index.html`).
- `Procfile`: Instrucciones para el despliegue en el servidor.

---

## 🚀 Instalación y Uso Local
Si deseas ejecutar este proyecto localmente:

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)

class ExampleModel(Base):
    __tablename__ = 'example_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
```

## Trabajando con Datos

Puedes colocar tus conjuntos de datos brutos en el directorio data/raw, conjuntos de datos intermedios en data/interim, y los conjuntos de datos procesados listos para el análisis en data/processed.

Para procesar datos, puedes modificar el script app.py para incluir tus pasos de procesamiento de datos, utilizando pandas para la manipulación y análisis de datos.

## Contribuyentes

Esta plantilla fue construida como parte del [Data Science and Machine Learning Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) de 4Geeks Academy por [Alejandro Sanchez](https://twitter.com/alesanchezr) y muchos otros contribuyentes. Descubre más sobre [los programas BootCamp de 4Geeks Academy](https://4geeksacademy.com/us/programs) aquí.

Otras plantillas y recursos como este se pueden encontrar en la página de GitHub de la escuela.
