# IMPORTAMOS Streamlit
# pip install python | python -m install streamlit
import streamlit as st
from groq import Groq

st.set_page_config(page_title="Mi chat de IA", page_icon="👍")
st.title("Mi primera aplicacion con Streamlit")

nombre = st.text_input("Cual es tu nombre?")
if st.button("Saludar!"):
    st.write(f"Hola {nombre}! Bienvenido a talento tech")

MODELOS = ["modelo 1", "modelo 2", "modelo 3"]

def configurar_pagina():
    st.title("Mi Chat de IA - Janneth")
    st.sidebar.title("Configuracion de la IA")

    elegirModelo = st.sidebar.selectbox(
        "Elegi un modelo",
        options = MODELOS,
        index = 0
    )

    return elegirModelo

modelo = configurar_pagina()
mensaje = st.chat_input("Escribi tu mensaje:")

# Correr streamlit con la terminal de Python
# python -m streamlit run MiChat.py (aca deben ingresar el nombre del archivo)

Minimizar
Minimizar (32 líneas)
Ver todo el archivo
MiChat.py
MiChat.py (1 KB)
1 KB
MiChat.py (1 KB)
Descargar MiChat.py (1 KB)Cambiar idioma

1
:thumbsup:
Haz clic para reaccionar
:poop:
Haz clic para reaccionar
:heavy_check_mark:
NUEVO
MODELOS = ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile', 'deepseek-r1-distill-llama-70b']
def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key= clave_secreta)

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role":"user", "content": mensajeDeEntrada}],
        stream = False
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []


clienteUsuario = crear_usuario_groq()
inicializar_estado()
modelo = configurar_pagina()
mensaje = st.chat_input("Escribi tu mensaje:")

if mensaje:
    configurar_modelo(clienteUsuario, modelo, mensaje)
    print(mensaje)

#Agregamos este codigo al final
:thumbsup:
Haz clic para reaccionar
:poop:
Haz clic para reaccionar
:heavy_check_mark:
#Funciones agregadas en CLASE 8
def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar": avatar})

def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar= mensaje["avatar"]) : st.markdown(mensaje["content"])

def area_chat():
    contenedorDelChat = st.container(height=400, border= True)
    with contenedorDelChat: mostrar_historial()
#No se olviden de llamar a la funcion area_chat
area_chat()

#-----Dentro del -------------------------------------
if mensaje:
    actualizar_historial("user", mensaje, "")
    chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
    actualizar_historial("assistant", chat_completo, "")

[theme]
primaryColor="#0b0136"
backgroundColor="#6b6514ff"
secondaryBackgroundColor="#000133"
textColor="#fff"
def generar_respuestas(chat_completo):
    respuesta_completa = ""
    for frase in chat_completo:
        print(frase.choices[0].delta.content)
        if frase.choices[0].delta.content: 
            respuesta_completa += frase.choices[0].delta.content
            yield frase.choices[0].delta.content
    return respuesta_completa


Main - > Todas las funciones para correr el Chatbot,
def main ():
    clienteUsuario = crear_usuario_groq()
    inicializar_estado()
    modelo = configurar_pagina()
    area_chat() #Nuevo 
    mensaje = st.chat_input("Escribi tu mensaje:")

    if mensaje:
        actualizar_historial("user", mensaje, "")
        chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
        if chat_completo:
                with st.chat_message("assistant"):
                    respuesta_completa = st.write_stream(generar_respuestas(chat_completo))
                    actualizar_historial("assistant", respuesta_completa, "")
                    st.rerun()




if __name__ == "main":
    main()

# IMPORTAMOS Streamlit
# pip install python | python -m install streamlit
import streamlit as st
from groq import Groq
from PIL import Image

image = Image.open("./image/imagen2.png")


st.set_page_config(page_title="Mi chat de IA", page_icon="👍")
st.title("Mi primera aplicacion con Streamlit")
st.image(image, caption="Imagen de prueba", use_column_width=True)
nombre = st.text_input("Cual es tu nombre?")
if st.button("Saludar!"):
    st.write(f"Hola {nombre}! Bienvenido a talento tech")

MODELOS = ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile', 'deepseek-r1-distill-llama-70b']

def configurar_pagina():
    st.title("Mi Chat de IA - Talento Tech")
    st.sidebar.title("Configuracion de la IA")

    elegirModelo = st.sidebar.selectbox(
        "Elegi un modelo",
        options = MODELOS,
        index = 0
    )

    return elegirModelo

# ------CLASE 7 - FUNCIONES-----------------------------------
def crear_usuario_groq():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key= clave_secreta)

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role":"user", "content": mensajeDeEntrada}],
        stream = True
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

#Funciones agregadas en CLASE 8
def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar": avatar})

def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar= mensaje["avatar"]) : st.markdown(mensaje["content"])

def area_chat():
    contenedorDelChat = st.container(height=400, border= True)
    with contenedorDelChat: mostrar_historial()

# Clase 9 - funciones
def generar_respuestas(chat_completo):
    respuesta_completa = ""
    for frase in chat_completo:
        print(frase.choices[0].delta.content)
        if frase.choices[0].delta.content: 
            respuesta_completa += frase.choices[0].delta.content
            yield frase.choices[0].delta.content
    return respuesta_completa


# Main - > Todas las funciones para correr el Chatbot
def main ():
    clienteUsuario = crear_usuario_groq()
    inicializar_estado()
    modelo = configurar_pagina()
    area_chat() #Nuevo 
    mensaje = st.chat_input("Escribi tu mensaje:")

    if mensaje:
        actualizar_historial("user", mensaje, "😁")
        chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
        if chat_completo:
                with st.chat_message("assistant"):
                    respuesta_completa = st.write_stream(generar_respuestas(chat_completo))
                    actualizar_historial("assistant", respuesta_completa, "🤖")
                    st.rerun()
        
        
        
        
if __name__ == "__main__":
    main()
    

#Agregamos este codigo al final



# modelo = configurar_pagina()
# mensaje = st.chat_input("Escribi tu mensaje:")
# Correr streamlit con la terminal de Python
# python -m streamlit run MiChat.py (aca deben ingresar el nombre del archivo)