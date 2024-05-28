import streamlit as st
import pandas as pd
import plotly.express as px

# Cambia la ruta del archivo CSV a una ruta relativa
car_data = pd.read_csv('vehicles_us.csv')

st.title("Análisis de Anuncios de Venta de Coches")
st.header("Visualizaciones Interactivas")

# Crear un botón que, al hacer clic, construya un histograma del odómetro
if st.button('Construir histograma del odómetro'):
    fig = px.histogram(car_data, x="odometer")
    st.write("Histograma del odómetro")
    st.plotly_chart(fig)

# Crear un gráfico de dispersión del odómetro vs precio
if st.button('Crear gráfico de dispersión del odómetro vs precio'):
    fig = px.scatter(car_data, x="odometer", y="price")
    st.write("Gráfico de dispersión del odómetro vs precio")
    st.plotly_chart(fig)

# Crear un gráfico de dispersión del año del modelo vs precio
if st.button('Crear gráfico de dispersión del año vs precio'):
    fig = px.scatter(car_data, x="model_year", y="price")
    st.write("Gráfico de dispersión del año vs precio")
    st.plotly_chart(fig)

# Crear un gráfico de barras del número de coches por tipo
if st.button('Crear gráfico de barras del número de coches por tipo'):
    fig = px.bar(car_data, x="type", color="type", title="Número de coches por tipo", labels={"type": "Tipo de coche", "count": "Número de coches"})
    st.write("Gráfico de barras del número de coches por tipo")
    st.plotly_chart(fig)
