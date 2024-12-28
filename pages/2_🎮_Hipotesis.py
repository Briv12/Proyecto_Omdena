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
st.header("Hipotesis 1: La preferencia en el año de 2010 de los jugadores fue la de utilizar la plataforma de computadora o en sus siglas PC, respecto a otras plataformas como XBOX, NINTENDO, PLAYSTATION,ETC.")
fig1 = hipotesis1(df)
st.plotly_chart(fig1, use_container_width=True)
st.caption("Conclusión: La plataforma más utilizada fue el DS")

# Hipótesis 2
st.header("Hipótesis 2: La categoría de acción de videojuegos, fue la mas seleccionada entre los jugadores Japóneses respecto a otras generos, en el año de 2009")
fig2 = hipotesis2(df)
st.plotly_chart(fig2, use_container_width=True)
st.caption("Conclusión: La categoría de videojuegos más seleccioanda entre los jugadores japoneses es: Role-Playing")

# Hipótesis 3
st.header("Hipótesis 3: La empresa que más videojuegos ha desarrollado y publicado a través del tiempo proporcionado por el “Dataset”, es la empresa de “Electronic Arts”, con una participación del 8% respecto a la competencia, como lo seria: Ubisoft, Konami, entre otras.")
fig3 = hipotesis3(df)
st.plotly_chart(fig3, use_container_width=True)
st.caption("Conclusión: Porcentaje de Electronic Arts: 8.17%")
st.caption("Desarrollador con más juegos: Electronic Arts")

# Hipótesis 4
st.header("Hipótesis 4: El mercado que mayores compras de videojuegos ha realizado es el mercado de Norteamérica, o en sus siglas “NA”. Respecto a los otros mercados importantes como: Japón, América del sur, América central, etc.")
fig4= hipotesis4(df)
st.plotly_chart(fig4, use_container_width=True)
st.caption("Conclusión: La región con mayores ventas es Norteamérica")

# Hipótesis 5
st.header("Hipótesis 5: El año de 2011, fue el año donde los jugadores realizaron mas compras de videojuegos en un panorama mundial respecto a años inferiores.")
fig5 = hipotesis5(df)
st.plotly_chart(fig5, use_container_width=True)
st.caption("Conclusión: El año con mayores ventas globales fue el 2008")