import streamlit as st
import xml.etree.ElementTree as ET
import pandas as pd

st.title("Traductor Mágico de XML a Tabla 🪄")

# 1. Le damos al usuario una zona para arrastrar su archivo
archivo_subido = st.file_uploader("Arrastra tu XML aquí", type=["xml"])

if archivo_subido is not None:
    # 2. Leemos el archivo que el usuario subió
    arbol = ET.parse(archivo_subido)
    raiz = arbol.getroot()
    
    # 3. Extraemos los datos (ejemplo simplificado)
    datos_extraidos = []
    for elemento in raiz:
        # Armamos nuestro diccionario clásico
        fila = {"Etiqueta": elemento.tag, "Valor": elemento.text}
        datos_extraidos.append(fila)
        
    # 4. Se lo mostramos al usuario en una tabla hermosa de Pandas/Streamlit
    df = pd.DataFrame(datos_extraidos)
    st.dataframe(df) # Streamlit dibuja la tabla automáticamente
    
    # 5. ¡Bono! Le damos un botón para descargarlo en Excel (CSV)
    st.download_button("Descargar en Excel", df.to_csv(), "reporte.csv", "text/csv")