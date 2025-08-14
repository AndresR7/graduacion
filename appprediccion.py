import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load("primermillon.joblib")

# Configuración de la página
st.set_page_config(page_title="Predictor de Éxito Académico", page_icon="🎓", layout="centered")

# Título
st.title("🎓 Predictor de Éxito Académico")

# Introducción
st.markdown("""
Bienvenido a la herramienta **Predictor de Éxito Académico**.  
Esta aplicación utiliza un modelo de **Perceptrón** para predecir si un estudiante tendrá éxito y logrará graduarse,  
basándose en dos indicadores clave:

- **Nota IA**: Calificación estimada en Inteligencia Artificial (0.0 a 1.0)  
- **GPA**: Promedio acumulado en la universidad (0.0 a 1.0)  

Ajusta los valores en los controles deslizantes y haz clic en **"Predecir"** para conocer el resultado.
""")

# Sliders para las variables
nota_ia = st.slider("Nota IA", min_value=0.0, max_value=1.0, step=0.1, format="%.1f")
gpa = st.slider("GPA", min_value=0.0, max_value=1.0, step=0.1, format="%.1f")

# Botón de predicción
if st.button("Predecir"):
    datos = np.array([[nota_ia, gpa]])
    prediccion = modelo.predict(datos)[0]

    if prediccion == 1:
        st.markdown(
            "<h2 style='color:green;'>🎉 ¡Felicitaciones! Te vas a graduar con honores.</h2>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h2 style='color:red;'>❌ No se prevé que te gradúes.</h2>",
            unsafe_allow_html=True
        )

# Autor y créditos
st.markdown("---")
st.markdown("**Autor:** Andrés Castellanos")
st.image("https://img.lovepik.com/photo/61144/3686.jpg_wh860.jpg", caption="Éxito Académico")
st.markdown("© 2025 UNAB")
