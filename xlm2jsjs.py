import streamlit as st
import xml.etree.ElementTree as ET
import pandas as pd

def procesar_factura(archivo_xml):
    # 1. Definimos los "Namespaces" (El mapa para no perderse en el XML del SAT)
    ns = {
        'cfdi': 'http://www.sat.gob.mx/cfdv/4',
        'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'
    }
    
    try:
        arbol = ET.parse(archivo_xml)
        raiz = arbol.getroot()
        
        # 2. Extraemos datos de los atributos (Así vienen en los CFDI)
        # El Total y la Fecha suelen estar en la raíz
        total = raiz.get('Total')
        fecha = raiz.get('Fecha')
        
        # 3. Buscamos etiquetas hijas (Emisor y Receptor)
        emisor = raiz.find('cfdi:Emisor', ns)
        receptor = raiz.find('cfdi:Receptor', ns)
        
        rfc_emisor = emisor.get('Rfc') if emisor is not None else "No encontrado"
        nombre_receptor = receptor.get('Nombre') if receptor is not None else "No encontrado"
        
        return {
            "Fecha": fecha,
            "RFC Emisor": rfc_emisor,
            "Cliente": nombre_receptor,
            "Total": float(total) if total else 0.0
        }
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
        return None

# --- Interfaz de Streamlit ---
st.title("Extractor de Facturas CFDI 🇲🇽")
archivos = st.file_uploader("Sube uno o varios XML", type=["xml"], accept_multiple_files=True)

if archivos:
    lista_resultados = []
    for xml in archivos:
        datos = procesar_factura(xml)
        if datos:
            lista_resultados.append(datos)
            
    df = pd.DataFrame(lista_resultados)
    st.write("### Resumen de Facturación")
    st.dataframe(df)
    
    # El toque final: suma de totales
    st.metric("Total Acumulado", f"${df['Total'].sum():,.2f}")