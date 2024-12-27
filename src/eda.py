import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def plot_dispersion_ventas(df):
    """Genera un diagrama de dispersión de ventas en Norteamérica vs. globales."""
    fig = px.scatter(df, x='NA_Sales', y='Global_Sales', title='Diagrama de Dispersión: Ventas en Norteamérica vs. Globales')
    return fig

def plot_frecuencia_plataformas(df):
    """Genera un gráfico de barras de la frecuencia de plataformas."""
    platform_counts = df['Platform'].value_counts()
    fig = px.bar(platform_counts, x=platform_counts.index, y=platform_counts.values,
                 labels={'x':'Plataforma', 'y':'Frecuencia'},
                 title='Frecuencia de Plataformas')
    fig.update_xaxes(tickangle=45, tickmode='linear')  # Rotar etiquetas del eje x
    return fig

def plot_ventas_na_eu(df):
    """Genera un gráfico de dispersión de ventas en Norteamérica vs. Europa."""
    fig = px.scatter(df, x='NA_Sales', y='EU_Sales', title='Relación entre Ventas en Norteamérica y Europa')
    return fig

def plot_ventas_na_eu_genero(df):
    """Genera un gráfico de dispersión con 'hue' para ventas en Norteamérica vs. Europa por género."""
    fig = px.scatter(df, x='NA_Sales', y='EU_Sales', color='Genre',
                     title='Ventas en Norteamérica vs. Europa por Género')
    return fig

def plot_plataformas_2010(df):
    """Genera un gráfico de barras para plataformas más usadas en 2010."""
    vg_2010 = df[df['Year'] == 2010]
    platform_counts = vg_2010['Platform'].value_counts()
    fig = px.bar(platform_counts, x=platform_counts.index, y=platform_counts.values,
                 labels={'x':'Plataforma', 'y':'Número de juegos'},
                 title='Plataformas más usadas en 2010')
    return fig

def plot_generos_japon_2009(df):
    """Genera un gráfico de barras para géneros más vendidos en Japón en 2009."""
    vg_2009_jp = df[(df['Year'] == 2009) & (df['JP_Sales'] > 0)]
    genre_counts_jp = vg_2009_jp['Genre'].value_counts()
    fig = px.bar(genre_counts_jp, x=genre_counts_jp.index, y=genre_counts_jp.values,
                 labels={'x':'Género', 'y':'Ventas en Japón'},
                 title='Géneros más vendidos en Japón en 2009')
    return fig

def plot_top_desarrolladores(df):
    """Genera un gráfico de barras para top 10 desarrolladores con más juegos publicados."""
    publisher_counts = df['Publisher'].value_counts()
    fig = px.bar(publisher_counts.head(12), x=publisher_counts.head(12).index, y=publisher_counts.head(12).values,
                 labels={'x':'Desarrollador', 'y':'Número de juegos'},
                 title='Top 10 Desarrolladores con más juegos publicados')
    return fig

def plot_ventas_region(df):
    """Genera un gráfico de barras para ventas totales de videojuegos por región."""
    ventasregion = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
    fig = px.bar(ventasregion, x=ventasregion.index, y=ventasregion.values,
                 labels={'x':'Región', 'y':'Ventas totales'},
                 title='Ventas totales de videojuegos por región')
    return fig

def plot_ventas_globales_año(df):
    """Genera un gráfico de líneas para ventas globales de videojuegos por año."""
    ventas = df.groupby('Year')['Global_Sales'].sum()
    fig = px.line(ventas, x=ventas.index, y=ventas.values,
                 labels={'x':'Año', 'y':'Ventas globales'},
                 title='Ventas globales de videojuegos por año')
    return fig


