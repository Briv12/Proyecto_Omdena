import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle  # Para guardar el modelo entrenado

@st.cache_data
def load_data():
    return pd.read_csv("data/Videogames.csv")

# Cargar datos
try:
    st.title("Predicción de Ventas de Videojuegos")
    
    # Cargar y procesar datos automáticamente
    data = load_data()
    st.write("Vista previa del conjunto de datos:")
    st.dataframe(data.head())

    # Preprocesamiento de datos
    data = data.dropna()
    features = ["Platform", "Year", "Genre", "Publisher", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
    targets = ["Global_Sales", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]

    X = data[features]
    y_global = data["Global_Sales"]
    y_region = data[targets[1:]]

    categorical_features = ["Platform", "Genre", "Publisher"]
    numerical_features = ["Year", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", "passthrough", numerical_features)
        ]
    )

    pipeline_global = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    pipeline_region = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    X_train, X_test, y_global_train, y_global_test = train_test_split(X, y_global, test_size=0.2, random_state=42)
    X_train_region, X_test_region, y_region_train, y_region_test = train_test_split(X, y_region, test_size=0.2, random_state=42)

    # Entrenando los modelos
    pipeline_global.fit(X_train, y_global_train)
    pipeline_region.fit(X_train_region, y_region_train)

    # Guardar el modelo entrenado
    model_path = "models/Randomforest.pkl"
    with open(model_path, "wb") as file:
        pickle.dump(pipeline_global, file)

    # Realizar predicciones en el conjunto de prueba
    predictions_global = pipeline_global.predict(X_test)
    mse_global = mean_squared_error(y_global_test, predictions_global)
    r2_global = r2_score(y_global_test, predictions_global)

    predictions_region = pipeline_region.predict(X_test_region)
    mse_region = mean_squared_error(y_region_test, predictions_region)
    r2_region = r2_score(y_region_test, predictions_region, multioutput='uniform_average')

    # Mostrar métricas
    st.title("Métricas del Modelo")
    col1, col2 = st.columns(2)
    col1.metric("MSE Global", f"{mse_global:.2f}")
    col2.metric("R^2 Global", f"{r2_global:.2f}")

    col3, col4 = st.columns(2)
    col3.metric("MSE Regional", f"{mse_region:.2f}")
    col4.metric("R^2 Regional", f"{r2_region:.2f}")

    # Función para sugerir plataformas
    def suggest_platforms(genre, year):
        filtered_data = data[(data["Genre"] == genre) & (data["Year"] == year)]
        if filtered_data.empty:
            return "No hay datos suficientes para este género y año."
        platforms = filtered_data.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
        return platforms.head(3).index.tolist()

    # Sugerir plataformas
    st.title("Sugerir Plataformas")
    example_genre = st.selectbox("Selecciona un género", data["Genre"].unique())
    example_year = st.slider("Selecciona un año", int(data["Year"].min()), 2030)  # Extensión hasta 2030
    suggested_platforms = suggest_platforms(example_genre, example_year)

    st.write(f"Las 3 plataformas más adecuadas para el género '{example_genre}' en el año {example_year} son: {suggested_platforms}")

    # Realizar Predicciones Automáticamente con los primeros datos de muestra
    st.title("Realizar Predicciones Automáticas")
    example_data = {
        "Platform": data["Platform"].iloc[0],  # Tomar el primer valor de la columna como ejemplo
        "Year": data["Year"].iloc[0],  # Año de ejemplo
        "Genre": data["Genre"].iloc[0],  # Género de ejemplo
        "Publisher": data["Publisher"].iloc[0],  # Editor de ejemplo
        "NA_Sales": data["NA_Sales"].iloc[0],  # Ventas en NA de ejemplo
        "EU_Sales": data["EU_Sales"].iloc[0],  # Ventas en EU de ejemplo
        "JP_Sales": data["JP_Sales"].iloc[0],  # Ventas en JP de ejemplo
        "Other_Sales": data["Other_Sales"].iloc[0]  # Otras ventas de ejemplo
    }

    input_df = pd.DataFrame([example_data])
    predicted_global_sales = pipeline_global.predict(input_df)[0]
    predicted_regional_sales = pipeline_region.predict(input_df)[0]

    st.write(f"Proyección de ventas globales: {predicted_global_sales:.2f} millones de unidades")
    st.write(f"Proyección de ventas regionales (NA, EU, JP, Other): {predicted_regional_sales}")

except Exception as e:
    st.error(f"Ocurrió un error: {e}")
