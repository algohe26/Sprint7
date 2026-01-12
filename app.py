import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv')  # porque app.py está en la raíz

# Encabezado de la aplicación
st.header('Análisis Exploratorio de Datos de Venta de Coches')

# --- SECCIÓN DE HISTOGRAMA ---
st.write('### Histograma del Odómetro')
# Opción con Botón
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# --- SECCIÓN DE GRÁFICO DE DISPERSIÓN ---
st.write('### Gráfico de Dispersión: Precio vs. Año del Modelo')
# Opción con Casilla de Verificación (Checkbox) - Desafío Extra
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Visualizando la relación entre el precio y el año del modelo')
    # Crear gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="model_year",
                             y="price", title="Precio vs Año del Modelo")
    # Mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)
