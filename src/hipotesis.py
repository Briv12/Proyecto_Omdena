import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

#Hipotesis 1 
def hipotesis1(df):
  df_2010 = df[df['Year'] == 2010]
  platform_counts = df_2010['Platform'].value_counts()
  fig = px.bar(platform_counts, x=platform_counts.index, y=platform_counts.values,
             labels={'x':'Plataforma', 'y':'Número de juegos'},
             title='Plataformas más usadas en 2010')
  fig.show()
  print('\n La plataforma más usada es:\n',platform_counts.idxmax())
  return fig

#Hipotesis 2
def hipotesis2(df):
  vg_2009_jp = df[(df['Year'] == 2009) & (df['JP_Sales'] > 0)]
  genre_counts_jp = vg_2009_jp['Genre'].value_counts()
  fig = px.bar(genre_counts_jp, x=genre_counts_jp.index, y=genre_counts_jp.values,
             labels={'x':'Género', 'y':'Ventas en Japón'},
             title='Géneros más vendidos en Japón en 2009')
  fig.show()
  print('\n La categoría de videojuegos más seleccioanda entre los jugadores japoneses es: \n',genre_counts_jp.idxmax())
  return fig

#Hipotesis 3
def hipotesis3(df):
  publisher_counts = df['Publisher'].value_counts()
  fig = px.bar(publisher_counts.head(12), x=publisher_counts.head(12).index, y=publisher_counts.head(12).values,
             labels={'x':'Desarrollador', 'y':'Número de juegos'},
             title='Top 10 Desarrolladores con más juegos publicados')
  fig.show()
  ea_percentage = (publisher_counts['Electronic Arts'] / publisher_counts.sum()) * 100
  print(f"Porcentaje de Electronic Arts: {ea_percentage:.2f}%")
  print(f"Desarrollador con más juegos: {publisher_counts.idxmax()}")
  return fig

#Hipotesis 4
def hipotesis4(df):
  ventasregion = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
  fig = px.bar(ventasregion, x=ventasregion.index, y=ventasregion.values,
             labels={'x':'Región', 'y':'Ventas totales'},
             title='Ventas totales de videojuegos por región')
  fig.show()
  print(f"\nRegión con mayores ventas: {ventasregion.idxmax()}")
  return fig

#Hipotesis 5
def hipotesis5(df):
  ventas = df.groupby('Year')['Global_Sales'].sum()
  fig = px.line(ventas, x=ventas.index, y=ventas.values,
             labels={'x':'Año', 'y':'Ventas globales'},
             title='Ventas globales de videojuegos por año')
  fig.show()
  print(f"\nAño con mayores ventas globales: {ventas.idxmax()}")
  return fig
