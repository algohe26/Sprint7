# Análisis Exploratorio de Datos de Vehículos (USA)
Este proyecto consiste en el desarrollo de un cuadro de mando (dashboard) interactivo utilizando Python y Streamlit para analizar un conjunto de datos sobre anuncios de venta de coches usados en EE. UU. El objetivo principal es facilitar la visualización de tendencias y distribuciones de los datos de manera rápida y eficiente.

## 📝 Descripción del Proyecto
La aplicación procesa un conjunto de datos que contiene información sobre más de 50,000 anuncios de vehículos, incluyendo variables como el precio, el año del modelo, el kilometraje (odómetro), el tipo de combustible y la condición del coche.

A través de esta herramienta, los analistas o usuarios interesados pueden explorar visualmente cómo factores como el kilometraje afectan el precio o cómo se distribuye el uso de los vehículos en el mercado de segunda mano. El proyecto demuestra la capacidad de transformar un análisis de datos estático (Notebook) en una herramienta web accesible y dinámica.

## 🚀 Funcionalidad
La aplicación web ofrece las siguientes capacidades interactivas:

Visualización de Distribución (Histogramas):

Al interactuar con la interfaz, el usuario puede generar histogramas automáticos.

Por defecto, se analiza la columna odometer para entender la distribución del kilometraje entre los vehículos anunciados.

Análisis de Relación (Gráficos de Dispersión):

Permite comparar dos variables numéricas simultáneamente (por ejemplo, el año del modelo frente al precio).

Ayuda a identificar correlaciones, como la depreciación de los vehículos a medida que son más antiguos.

Interfaz Dinámica:

Uso de botones y casillas de verificación para renderizar los gráficos solo cuando el usuario lo solicita, optimizando el rendimiento de la aplicación.

Gráficos totalmente interactivos gracias a Plotly (zoom, filtros al pasar el ratón y descarga de imágenes).

## 🛠 Tecnologías Utilizadas
El proyecto fue construido utilizando las siguientes herramientas del ecosistema de ciencia de datos de Python:

Python: Lenguaje de programación principal.

Streamlit: Framework utilizado para la creación de la aplicación web interactiva de forma ágil.

Pandas: Biblioteca fundamental para la manipulación y limpieza de los datos estructurados (DataFrames).

Plotly Express: Biblioteca de visualización de datos de alto nivel para crear gráficos interactivos y atractivos con poco código.

VS Code: Entorno de desarrollo integrado (IDE) utilizado para la codificación y gestión del entorno virtual.

