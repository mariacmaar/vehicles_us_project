import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('data/vehicles_us.csv') # leer los datos

#título de la app 
st.title('Análisis de Datos de Vehículos')

#Data Viewer 
st.header('Vista de datos')
if st.checkbox('Mostar Datos'): #Muestra tabala interactiva se se activa la casilla 
    st.dataframe(car_data)
    
#Grafico 1, Vehicles types by model
st.header('Tipos de Vehículos por Modelo')
vehicle_button = st.button('Mostrar gráfico de tipos de vehículos por modelo')
if vehicle_button:
    if 'model' in car_data.columns:  # Verificar si la columna existe
        fig1 = px.histogram(
            car_data,
            x='model',
            color='type',
            title='Vehicle Types by Model',
            labels={'count': 'Cantidad', 'model': 'Modelo'},
            barmode='stack'
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.error("La columna 'model' no existe en los datos.")
    
#Grafico 2, Histogram of condition vs model year 
st.header('Histograma de Condición vs Año del Modelo')
condition_button = st.button('Mostrar histograma de condición vs año del modelo')
if condition_button:
    fig2 = px.histogram(
        car_data,
        x='model_year',
        color='condition',
        title='Condition vs Model Year',
        labels={'count': 'Cantidad', 'model_year': 'Año del Modelo'},
        nbins=50
    )
    st.plotly_chart(fig2, use_container_width=True)

#Grafico 3, Compare price distribution between manufacturars
st.header('Distribución de Precios entre Modelos')
price_button = st.button('Mostrar distribución de precios por modelo')
if price_button:
    if 'model' in car_data.columns and 'price' in car_data.columns:  # Verificar columnas
        fig3 = px.box(
            car_data,
            x='model',
            y='price',
            title='Price Distribution by Model',
            labels={'model': 'Modelo', 'price': 'Precio'},
            points='outliers'
        )
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.error("Las columnas 'model' o 'price' no existen en los datos.")

