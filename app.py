import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyB0sL_VTcv855pWfWuzcF86YJ_CHZl2Dh8")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works"
)
print(response.text)
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