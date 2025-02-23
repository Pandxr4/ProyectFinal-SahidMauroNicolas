import streamlit as st
from gemini_api import GeminiAI  # Asegúrate de importar la librería correcta para la API de Gemini

# Inicialización de la API de Gemini con la API key
api_key = 'TU_API_KEY_DE_GEMINI_AQUI'
gemini = GeminiAI(api_key)

# Título y Descripción
st.title('Alemán Fácil AI')
st.write('Bienvenido a Alemán Fácil AI, la aplicación que utiliza inteligencia artificial para ayudarte a aprender alemán de manera dinámica y personalizada.')

# Botón de acción
if st.button('Iniciar Tarea Específica'):
    # Integración con la IA de Gemini
    resultado = gemini.generar_codigo('Prompt para la tarea específica')
    st.write(resultado)

# Sección "Cómo funciona"
st.header('Cómo funciona')
st.write('''
Alemán Fácil AI te ofrece:
- **Personalización del Aprendizaje:** Utilizamos IA para identificar tus áreas de mejora y adaptar el contenido.
- **Análisis de Pronunciación:** Evaluamos tu pronunciación y te ofrecemos sugerencias detalladas.
- **Generación de Contenido Dinámico:** Creamos ejercicios basados en tus intereses.
''')

# Header y Footer
st.sidebar.header('Alemán Fácil AI')
st.sidebar.write('Tu aliado en el aprendizaje del alemán.')
st.sidebar.subheader('Contacto')
st.sidebar.write('Email: contacto@alemanfacilai.com')
