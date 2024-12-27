import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import os
from src.eda import plot_dispersion_ventas, plot_frecuencia_plataformas, plot_generos_japon_2009, plot_plataformas_2010, plot_top_desarrolladores, plot_ventas_globales_año,plot_ventas_na_eu,plot_ventas_na_eu_genero,plot_ventas_region

#Cargando el dataframe
@st.cache_data
def load_data():
    return pd.read_csv("data/Videogames.csv")  

# Configuración de la página
st.title("Análisis Exploratorio de Datos (EDA)")

# Cargar datos
df = load_data()

# Información básica del conjunto de datos
st.header("Aspectos Básicos del Conjunto de Datos")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Número de Filas", value=df.shape[0], border=True)
    with col2:
        st.metric(label="Número de Columnas", value=df.shape[1], border=True)
    with col3:
        missing_values = df.isnull().any().sum()
        st.metric(label="Valores Perdidos", value="Sí" if missing_values > 0 else "No", border=True)

# Mostrar gráficos
st.header("Análisis de Ventas y Características de Videojuegos")

st.subheader("Diagrama de Dispersión: Ventas en Norteamérica vs. Globales")
scatter_ventas_fig = plot_dispersion_ventas(df)
scatter_ventas_fig.update_traces(marker=dict(color="blue"))
st.plotly_chart(scatter_ventas_fig)

st.subheader("Frecuencia de Plataformas")
frecuencia_plataformas_fig = plot_frecuencia_plataformas(df)
frecuencia_plataformas_fig.update_traces(marker_color="orange")
st.plotly_chart(frecuencia_plataformas_fig)

st.subheader("Relación entre Ventas en Norteamérica y Europa")
ventas_na_eu_fig = plot_ventas_na_eu(df)
ventas_na_eu_fig.update_traces(marker=dict(color="green"))
st.plotly_chart(ventas_na_eu_fig)

st.subheader("Ventas en Norteamérica vs. Europa por Género")
ventas_na_eu_genero_fig = plot_ventas_na_eu_genero(df)
ventas_na_eu_genero_fig.update_traces(marker=dict(opacity=0.8))
st.plotly_chart(ventas_na_eu_genero_fig)

st.subheader("Plataformas más Usadas en 2010")
plataformas_2010_fig = plot_plataformas_2010(df)
plataformas_2010_fig.update_traces(marker_color="purple")
st.plotly_chart(plataformas_2010_fig)

st.subheader("Géneros más Vendidos en Japón en 2009")
generos_japon_2009_fig = plot_generos_japon_2009(df)
generos_japon_2009_fig.update_traces(marker_color="red")
st.plotly_chart(generos_japon_2009_fig)

st.subheader("Top 10 Desarrolladores con más Juegos Publicados")
top_desarrolladores_fig = plot_top_desarrolladores(df)
top_desarrolladores_fig.update_traces(marker_color="teal")
st.plotly_chart(top_desarrolladores_fig)

st.subheader("Ventas Totales por Región")
ventas_region_fig = plot_ventas_region(df)
ventas_region_fig.update_traces(marker_color="gold")
st.plotly_chart(ventas_region_fig)

st.subheader("Ventas Globales de Videojuegos por Año")
ventas_globales_año_fig = plot_ventas_globales_año(df)
ventas_globales_año_fig.update_traces(line=dict(color="pink"))
st.plotly_chart(ventas_globales_año_fig)
