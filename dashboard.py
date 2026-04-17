import streamlit as st
import sqlite3
import pandas as pd

# --------------------------------------------------------
# 1. CONFIGURACIÓN VISUAL
# --------------------------------------------------------
st.set_page_config(page_title="Dashboard Corporativo IT", page_icon="📊", layout="wide")
st.title("🌐 Centro de Control: Inventario Nacional")

# --------------------------------------------------------
# 2. SIMULACIÓN DE LA BÓVEDA (Tu futuro SQL Server)
# --------------------------------------------------------
# Usamos cache para que no re-cree la BD cada vez que muevas un filtro
@st.cache_resource
def preparar_boveda():
    # Creamos una base de datos temporal en la RAM
    conexion = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = conexion.cursor()
    
    # Creamos las 4 tablas
    cursor.execute("CREATE TABLE ubicaciones (id INTEGER, ciudad TEXT)")
    cursor.execute("CREATE TABLE departamentos (id INTEGER, nombre TEXT)")
    cursor.execute("CREATE TABLE empleados (id INTEGER, nombre TEXT, depto_id INTEGER, ubi_id INTEGER)")
    cursor.execute("CREATE TABLE equipos (id INTEGER, modelo TEXT, estado TEXT, empleado_id INTEGER)")
    
    # Inyectamos datos de prueba
    cursor.executescript('''
        INSERT INTO ubicaciones VALUES (1, 'CDMX'), (2, 'Monterrey'), (3, 'Guadalajara');
        INSERT INTO departamentos VALUES (1, 'Soporte IT'), (2, 'Ventas'), (3, 'Finanzas');
        INSERT INTO empleados VALUES (1, 'Roberto Gómez', 1, 1), (2, 'Ana López', 3, 2), (3, 'Carlos Slim', 2, 3), (4, 'María Félix', 2, 1);
        INSERT INTO equipos VALUES (101, 'ThinkPad T14', 'Activo', 1), (102, 'HP ZBook', 'Mantenimiento', 2), (103, 'MacBook Pro', 'Activo', 3), (104, 'Dell Latitude', 'Activo', 4);
    ''')
    conexion.commit()
    return conexion

conexion = preparar_boveda()

# --------------------------------------------------------
# 3. INTERFAZ DE USUARIO (Los Filtros)
# --------------------------------------------------------
st.markdown("### 🔍 Filtros Dinámicos")
col_filtro1, col_filtro2 = st.columns(2)

with col_filtro1:
    filtro_ubi = st.selectbox("Ubicación:", ["Todas", "CDMX", "Monterrey", "Guadalajara"])

with col_filtro2:
    filtro_dep = st.selectbox("Departamento:", ["Todos", "Soporte IT", "Ventas", "Finanzas"])

# --------------------------------------------------------
# 4. LÓGICA BACKEND: EL MEGA-JOIN Y EL WHERE DINÁMICO
# --------------------------------------------------------
# Esta es la consulta base que cruza los 4 pasillos de la base de datos
consulta_sql = '''
    SELECT 
        eq.id AS Folio,
        emp.nombre AS Empleado,
        eq.modelo AS Equipo,
        dep.nombre AS Departamento,
        ubi.ciudad AS Ubicacion,
        eq.estado AS Estado
    FROM equipos eq
    INNER JOIN empleados emp ON eq.empleado_id = emp.id
    INNER JOIN departamentos dep ON emp.depto_id = dep.id
    INNER JOIN ubicaciones ubi ON emp.ubi_id = ubi.id
    WHERE 1=1
'''

# Si el usuario elige un filtro, agregamos la condición a la consulta
if filtro_ubi != "Todas":
    consulta_sql += f" AND ubi.ciudad = '{filtro_ubi}'"

if filtro_dep != "Todos":
    consulta_sql += f" AND dep.nombre = '{filtro_dep}'"

# Ejecutamos la consulta y la guardamos en Pandas
datos_filtrados = pd.read_sql(consulta_sql, conexion)

# --------------------------------------------------------
# 5. PRESENTACIÓN DE KPIs (Tarjetas de Métricas)
# --------------------------------------------------------
st.markdown("---")
kpi1, kpi2, kpi3 = st.columns(3)

# Calculamos las métricas usando el dataframe filtrado
total_equipos = len(datos_filtrados)
equipos_activos = len(datos_filtrados[datos_filtrados['Estado'] == 'Activo'])
en_mantenimiento = len(datos_filtrados[datos_filtrados['Estado'] == 'Mantenimiento'])

kpi1.metric(label="📦 Equipos en esta vista", value=total_equipos)
kpi2.metric(label="✅ Operando sin fallas", value=equipos_activos)
kpi3.metric(label="🔧 En Mantenimiento", value=en_mantenimiento)

# --------------------------------------------------------
# 6. LA TABLA Y EXPORTACIÓN
# --------------------------------------------------------
st.markdown("### 📋 Resultados Detallados")

if total_equipos == 0:
    st.warning("No hay equipos que coincidan con estos filtros.")
else:
    # Mostramos la tabla interactiva
    st.dataframe(datos_filtrados, use_container_width=True, hide_index=True)
    
    # MAGIA: Convertimos la tabla filtrada a CSV para el botón de descarga
    csv = datos_filtrados.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Descargar Reporte en Excel (CSV)",
        data=csv,
        file_name="Reporte_Inventario_IT.csv",
        mime="text/csv",
    )