import streamlit as st
import pyodbc
import pandas as pd

# --- 1. CONFIGURACIÓN VISUAL BÁSICA ---
st.set_page_config(page_title="Flotilla Logística", page_icon="🚚", layout="wide")
st.title("🚚 Control de Flotilla Corporativa")

# --- 2. EL PUENTE A LA BÓVEDA ---
@st.cache_resource
def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Logistica_DB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

# --- 3. EL MEGA-JOIN ---
@st.cache_data(ttl=60)
def cargar_datos():
    conn = get_connection()
    query = """
    SELECT 
        v.placas AS Placas,
        v.estado AS Estado,
        m.nombre AS Marca,
        c.nombre AS Ciudad
    FROM vehiculos v
    INNER JOIN marcas m ON v.marca_id = m.id
    INNER JOIN ciudades c ON v.ciudad_id = c.id;
    """
    return pd.read_sql(query, conn)

# --- 4. LA LÓGICA DE FILTRADO ---
def filtrar_vehiculos(df, ciudad, estado):
    df_filtrado = df.copy()
    if ciudad != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Ciudad"] == ciudad]
    if estado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Estado"] == estado]
    return df_filtrado

# --- 5. INTERFAZ VISUAL ---
try:
    df = cargar_datos()
    
    st.subheader("🔍 Filtros de Búsqueda")
    col_filtro1, col_filtro2 = st.columns(2)
    
    with col_filtro1:
        lista_ciudades = ["Todas"] + df["Ciudad"].unique().tolist()
        ciudad_elegida = st.selectbox("📍 Ciudad", lista_ciudades)
        
    with col_filtro2:
        lista_estados = ["Todos"] + df["Estado"].unique().tolist()
        estado_elegido = st.selectbox("🚦 Estado del Vehículo", lista_estados)
        
    df_final = filtrar_vehiculos(df, ciudad_elegida, estado_elegido)
    
    st.markdown("---")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("🚗 Total en Vista", len(df_final))
    kpi2.metric("✅ Disponibles", len(df_final[df_final["Estado"] == "Disponible"]))
    kpi3.metric("🔧 En Taller", len(df_final[df_final["Estado"] == "En Taller"]))
    st.markdown("---")
    
    st.dataframe(df_final, use_container_width=True, hide_index=True)

except Exception as e:
    st.error(f"⚠️ Error al conectar con la base de datos: {e}")