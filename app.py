import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('C:/Users/mm_mo/OneDrive/Documentos/newproject/vehicles_us.csv')

# Limpiar los datos eliminando filas con valores nulos en las columnas necesarias
car_data.dropna(subset=['odometer', 'price', 'model_year', 'type'], inplace=True)

# Convertir 'model_year' a entero ya que no tiene sentido como float
car_data['model_year'] = car_data['model_year'].astype(int)

# Encabezado
st.header('Panel de Control de Anuncios de Venta de Coches')

# Botón para histograma
if st.button('Construir histograma del odómetro'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión del odómetro vs precio
if st.button('Construir gráfico de dispersión del odómetro vs precio'):
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión del año vs precio
if st.button('Construir gráfico de dispersión del año vs precio'):
    st.write('Creación de un gráfico de dispersión del año vs precio')
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de barras del número de coches por tipo
if st.button('Construir gráfico de barras del número de coches por tipo'):
    st.write('Creación de un gráfico de barras del número de coches por tipo')
    color_discrete_map = {
        'truck': 'blue', 
        'SUV': 'green', 
        'sedan': 'red', 
        'pickup': 'purple', 
        'coupe': 'orange', 
        'wagon': 'pink', 
        'mini-van': 'brown', 
        'hatchback': 'cyan', 
        'van': 'magenta', 
        'convertible': 'yellow', 
        'other': 'black', 
        'offroad': 'lime', 
        'bus': 'teal'
    }
    fig = px.bar(
        car_data, 
        x="type", 
        title='Número de coches por tipo',
        category_orders={"type": car_data['type'].value_counts().index},  # Ordenar de mayor a menor
        color="type",
        color_discrete_map=color_discrete_map,  # Aplicar colores personalizados
        labels={"type": "Tipo de Coche", "count": "Número de Coches"}
    )
    fig.update_layout(
        xaxis_title="Tipo de Coche",
        yaxis_title="Número de Coches",
        title_x=0.5,
        width=800,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de caja del precio por tipo
if st.button('Construir gráfico de caja del precio por tipo'):
    st.write('Creación de un gráfico de caja del precio por tipo de coche')
    fig = px.box(car_data, x="type", y="price", title='Distribución del precio por tipo de coche')
    fig.update_layout(
        xaxis_title="Tipo de Coche",
        yaxis_title="Precio",
        title_x=0.5,
        width=800,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
