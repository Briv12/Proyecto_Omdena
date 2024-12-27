import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import os
from src.hipotesis import hipotesis1, hipotesis2, hipotesis3, hipotesis4, hipotesis5

#Cargando el dataframe
@st.cache_data
def load_data():
    return pd.read_csv("data/Videogames.csv")  

# Cargar datos
df = load_data()
st.title("Hipótesis del Proyecto")

# Hipótesis 1
st.header("Hipótesis 1: Preferencias en el año de 2010 de los jugadores")
fig1 = hipotesis1(df)
st.plotly_chart(fig1, use_container_width=True)


# Hipótesis 2
st.header("Hipótesis 2: Categoria más seleccionada por los jugadores japoneses")
fig2 = hipotesis2(df)
st.plotly_chart(fig2, use_container_width=True)

# Hipótesis 3
st.header("Hipótesis 3: Empresas que más juegos han desarrollado")
fig3 = hipotesis3(df)
st.plotly_chart(fig3, use_container_width=True)

# Hipótesis 4
st.header("Hipótesis 4: Ventas totales de videojuegos por región")
fig4= hipotesis4(df)
st.plotly_chart(fig4, use_container_width=True)

# Hipótesis 5
st.header("Hipótesis 5: Ventas globales de videojuegos por año")
fig5 = hipotesis5(df)
st.plotly_chart(fig5, use_container_width=True)