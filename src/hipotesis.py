import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

#Hipotesis 1 
def hipotesis1(data):
  df_2010 = data[data['Year'] == 2010]
  platform_counts = df_2010['Platform'].value_counts()
  fig1 = px.bar(
      platform_counts, x=platform_counts.index, y=platform_counts.values,
             labels={'x':'Plataforma', 'y':'Número de juegos'},
             color_discrete_sequence=px.colors.qualitative.Bold,
             title='Plataformas más usadas en 2010'
)
  fig1.show()
  print('\n La plataforma más usada es:\n',platform_counts.idxmax())
  return fig1

#Hipotesis 2
def hipotesis2(data):
  vg_2009_jp = data[(data['Year'] == 2009) & (data['JP_Sales'] > 0)]
  genre_counts_jp = vg_2009_jp['Genre'].value_counts()
  fig2 = px.bar(
      genre_counts_jp, x=genre_counts_jp.index, y=genre_counts_jp.values,
             labels={'x':'Género', 'y':'Ventas en Japón'},
            color_discrete_sequence=px.colors.qualitative.Pastel1,        
             title='Géneros más vendidos en Japón en 2009'
             )
  fig2.show()
  print('\n La categoría de videojuegos más seleccioanda entre los jugadores japoneses es: \n',genre_counts_jp.idxmax())
  return fig2

#Hipotesis 3
def hipotesis3(data):
  publisher_counts = data['Publisher'].value_counts()
  fig3 = px.bar(
      publisher_counts.head(12), x=publisher_counts.head(12).index, y=publisher_counts.head(12).values,
             labels={'x':'Desarrollador', 'y':'Número de juegos'},
             color_discrete_sequence=px.colors.qualitative.Plotly,
             title='Top 10 Desarrolladores con más juegos publicados'
             )
  fig3.show()
  ea_percentage = (publisher_counts['Electronic Arts'] / publisher_counts.sum()) * 100
  print(f"Porcentaje de Electronic Arts: {ea_percentage:.2f}%")
  print(f"Desarrollador con más juegos: {publisher_counts.idxmax()}")
  return fig3

#Hipotesis 4
def hipotesis4(data):
  ventasregion = data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
  
  color_map = {
      'NA_Sales': 'red',
      'EU_Sales': 'blue',
      'JP_Sales': 'green',
      'Other_Sales': 'orange'
  }

  fig4 = px.bar(
      ventasregion, 
      x=ventasregion.index, 
      y=ventasregion.values,
      labels={'x':'Región', 'y':'Ventas totales'},
      color_discrete_map=color_map, # Usando color_discrete_map
      title='Ventas totales de videojuegos por región'
  )
  fig4.show()
  print(f"\nRegión con mayores ventas: {ventasregion.idxmax()}")
  return fig4

#Hipotesis 5
def hipotesis5(data):
  ventas = data.groupby('Year')['Global_Sales'].sum()
  fig5 = px.line(
      ventas, x=ventas.index, y=ventas.values,
             labels={'x':'Año', 'y':'Ventas globales'},
             color_discrete_sequence=px.colors.qualitative.Bold,
             title='Ventas globales de videojuegos por año'
  )
  fig5.show()
  print(f"\nAño con mayores ventas globales: {ventas.idxmax()}")
  return fig5
