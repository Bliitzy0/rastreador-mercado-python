import streamlit as st
import pyodbc
import pandas as pd

# ── Configuración de página y estilos ────────────────────────────────────────
st.set_page_config(page_title="Dashboard IT Empresarial", page_icon="💻", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    .app-header { background: linear-gradient(135deg, #0f2942 0%, #1a4a7a 100%); border-radius: 16px; padding: 2rem; margin-bottom: 2rem; color: white; }
    .filter-panel { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 14px; padding: 1.5rem; margin-bottom: 1.5rem; }
    div[data-testid="metric-container"] { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1rem; }
</style>
""", unsafe_allow_html=True)
#
# ── 1. LA NUEVA CONEXIÓN A SQL SERVER ────────────────────────────────────────
@st.cache_resource
def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=Inventario_IT;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;" # La llave maestra local
    )
    return pyodbc.connect(conn_str)

# ── 2. EL MEGA-JOIN (Consultando la Bóveda Real) ─────────────────────────────
@st.cache_data(ttl=60)
def cargar_datos():
    conn = get_connection()
    query = """
    SELECT 
        eq.id AS Folio,
        emp.nombre AS Nombre,
        dep.nombre AS Departamento,
        eq.modelo AS Equipo,
        ubi.ciudad AS Ciudad,
        eq.estado AS Estado
    FROM equipos eq
    INNER JOIN empleados emp ON eq.empleado_id = emp.id
    INNER JOIN departamentos dep ON emp.depto_id = dep.id
    INNER JOIN ubicaciones ubi ON emp.ubi_id = ubi.id
    """
    return pd.read_sql(query, conn)

# ── 3. EL AJUSTE DE COLUMNAS (La lógica de filtrado) ─────────────────────────
# Quitamos "salario" y agregamos "ciudad" y "equipo"
def filtrar_datos(df, busqueda, departamento, estado, ciudad):
    if busqueda:
        df = df[df["Nombre"].str.contains(busqueda, case=False, na=False) | 
                df["Equipo"].str.contains(busqueda, case=False, na=False)]
    if departamento != "Todos":
        df = df[df["Departamento"] == departamento]
    if estado != "Todos":
        df = df[df["Estado"] == estado]
    if ciudad != "Todas":
        df = df[df["Ciudad"] == ciudad]
    return df

# ── Interfaz Visual ──────────────────────────────────────────────────────────
st.markdown('<div class="app-header"><h1>💻 Dashboard de Inventario IT</h1><p>Conectado en tiempo real a SQL Server</p></div>', unsafe_allow_html=True)

try:
    df = cargar_datos()
    
    # ── Panel de Filtros Actualizado ──
    st.markdown('<div class="filter-panel">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        busqueda = st.text_input("🔎 Buscar (Empleado o Equipo)")
    with col2:
        departamento = st.selectbox("Departamento", ["Todos"] + sorted(df["Departamento"].unique().tolist()))
    with col3:
        estado = st.selectbox("Estado", ["Todos"] + sorted(df["Estado"].unique().tolist()))
    with col4:
        ciudad = st.selectbox("Ubicación", ["Todas"] + sorted(df["Ciudad"].unique().tolist()))
        
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Aplicar Filtros ──
    df_filtrado = filtrar_datos(df, busqueda, departamento, estado, ciudad)

    # ── Nuevos KPIs (Tarjetas) ──
    m1, m2, m3 = st.columns(3)
    m1.metric("📦 Equipos en esta vista", len(df_filtrado))
    m2.metric("✅ Activos", len(df_filtrado[df_filtrado["Estado"] == "Activo"]))
    m3.metric("🔧 En Mantenimiento", len(df_filtrado[df_filtrado["Estado"] == "Mantenimiento"]))

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Tabla y Exportación ──
    if df_filtrado.empty:
        st.warning("No se encontraron equipos con esos filtros.")
    else:
        st.dataframe(df_filtrado, use_container_width=True, hide_index=True)
        
        csv = df_filtrado.to_csv(index=False).encode("utf-8")
        st.download_button("⬇ Descargar Reporte en Excel", data=csv, file_name="Inventario_Filtrado.csv", mime="text/csv")

except Exception as e:
    st.error(f"⚠️ Error de conexión a la Bóveda: {e}")