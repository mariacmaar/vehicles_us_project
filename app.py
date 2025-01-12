import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('data/vehicles_us.csv') # leer los datos

#título de la app 
st.title('Análisis de Dattos de Vehículos')

#Data Viewer 
st.header('Vista de datos')
if st.checkbox('Mostar Datos'): #Muestra tabala interactiva se se activa la casilla 
    st.dataframe(car_data)
    
#Grafico 1, Vehicles types by manufacture 
st.header('tipos de vehiculos por Fabricante')
vehicle_button = st.button('Mostrar grafico de tipos de vehiculos por fabricantes')
if vehicle_button:
    fig1 = px.histogram(
        car_data,
        x= 'manufacturer',
        color='type',
        title= 'Vehicles types by Manufacturer',
        labels= {'count':'Cantidad', 'manufacturer': 'Fabricante'},
        barmode= 'stacks'
    )
    st.plotly_chart(fig1, use_container_width=True)
    
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
st.header('Distribución de Precios entre Fabricantes')
price_button = st.button('mostar distribución de precios por fabricante')
if price_button:
    fig3 = px.box(
        car_data,
        x='manufacturer',
        y='price',
        title='Price Distribution by Manufacturer',
        labels={'manufacturer': 'Fabricante', 'price': 'Precio'},
        points='outliers'
    )
    st.plotly_chart(fig3, use_container_width=True)

