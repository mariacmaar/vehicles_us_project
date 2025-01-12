
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('data/vehicles_us.csv') # leer los datos
hist_button = st.button('construir instograma') #crear boton 

if hist_button:
    st.write('creacion de un histograma para el conjunto de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    
    st.plotly_chart(fig, use_container_width=True)


