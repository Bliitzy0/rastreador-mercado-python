import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(page_title="Rastreador de Precios", page_icon="🛒", layout="wide")

# ==========================================
# FUNCIÓN AUXILIAR: El radar de productos
# ==========================================
# Esta función va a la bóveda solo a traer los Nombres y los IDs para nuestro menú desplegable
def obtener_catalogo():
    try:
        conexion = sqlite3.connect("mi_rastreador.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM productos")
        return cursor.fetchall() # Nos devuelve una lista: [(1, 'Corsair...'), (2, 'HP...')]
    except:
        return []
    finally:
        if 'conexion' in locals(): conexion.close()

# ==========================================
# PANEL LATERAL: OPERACIONES (Tabs)
# ==========================================
# ==========================================
# PANEL LATERAL: OPERACIONES (Tabs)
# ==========================================
with st.sidebar:
    st.header("⚙️ Operaciones")
    
    # ¡Agregamos la tercera pestaña!
    tab_nuevo, tab_actualizar, tab_eliminar = st.tabs(["Nuevo", "Actualizar", "Eliminar"])
    
    # --- PESTAÑA 1: NUEVO PRODUCTO ---
    with tab_nuevo:
        with st.form("formulario_registro", clear_on_submit=True):
            nuevo_nombre = st.text_input("Nombre del equipo:")
            nueva_categoria = st.selectbox("Categoría:", ["Componentes PC", "Laptops Workstation", "Smartphones", "Periféricos", "Monitores"])
            nuevo_precio = st.number_input("Precio inicial ($ MXN):", min_value=0.0, step=100.0)
            btn_guardar = st.form_submit_button("Guardar Producto")
            
            if btn_guardar:
                if nuevo_nombre == "":
                    st.error("⚠️ El nombre es obligatorio.")
                else:
                    try:
                        conexion = sqlite3.connect("mi_rastreador.db")
                        cursor = conexion.cursor()
                        fecha_hoy = date.today().isoformat()
                        cursor.execute("INSERT INTO productos (nombre, categoria) VALUES (?, ?)", (nuevo_nombre, nueva_categoria))
                        id_generado = cursor.lastrowid
                        cursor.execute("INSERT INTO historial_precios (producto_id, precio, fecha) VALUES (?, ?, ?)", (id_generado, nuevo_precio, fecha_hoy))
                        conexion.commit()
                        st.success(f"✅ ¡'{nuevo_nombre}' guardado!")
                    except sqlite3.Error as error:
                        st.error(f"❌ Error: {error}")
                    finally:
                        if 'conexion' in locals(): conexion.close()

    # --- PESTAÑA 2: ACTUALIZAR PRECIO ---
    with tab_actualizar:
        catalogo = obtener_catalogo()
        if len(catalogo) > 0:
            with st.form("formulario_actualizar", clear_on_submit=True):
                producto_elegido = st.selectbox("Selecciona el producto:", catalogo, format_func=lambda x: x[1])
                precio_nuevo = st.number_input("Nuevo precio detectado:", min_value=0.0, step=100.0)
                btn_actualizar = st.form_submit_button("Registrar Variación")
                
                if btn_actualizar:
                    id_del_producto = producto_elegido[0]
                    try:
                        conexion = sqlite3.connect("mi_rastreador.db")
                        cursor = conexion.cursor()
                        fecha_hoy = date.today().isoformat()
                        cursor.execute("INSERT INTO historial_precios (producto_id, precio, fecha) VALUES (?, ?, ?)", (id_del_producto, precio_nuevo, fecha_hoy))
                        conexion.commit()
                        st.success("📈 ¡Historial actualizado!")
                    except sqlite3.Error as error:
                        st.error(f"❌ Error: {error}")
                    finally:
                        if 'conexion' in locals(): conexion.close()
        else:
            st.info("Tu bóveda está vacía. Agrega productos primero.")

    # --- PESTAÑA 3: ELIMINAR PRODUCTO (¡Lo nuevo!) ---
    with tab_eliminar:
        catalogo = obtener_catalogo() # Volvemos a pedir la lista de productos
        
        if len(catalogo) > 0:
            with st.form("formulario_eliminar", clear_on_submit=True):
                st.warning("⚠️ Cuidado: Esta acción no se puede deshacer.")
                producto_a_borrar = st.selectbox("Producto a eliminar:", catalogo, format_func=lambda x: x[1])
                
                # Un botón rojo para que se vea peligroso
                btn_eliminar = st.form_submit_button("🚨 Eliminar Definitivamente", type="primary")
                
                if btn_eliminar:
                    id_borrar = producto_a_borrar[0]
                    nombre_borrar = producto_a_borrar[1]
                    
                    try:
                        conexion = sqlite3.connect("mi_rastreador.db")
                        cursor = conexion.cursor()
                        
                        # PASO 1: Borrar el historial (Los Hijos)
                        cursor.execute("DELETE FROM historial_precios WHERE producto_id = ?", (id_borrar,))
                        
                        # PASO 2: Borrar el producto del catálogo (El Padre)
                        cursor.execute("DELETE FROM productos WHERE id = ?", (id_borrar,))
                        
                        conexion.commit()
                        st.success(f"🗑️ '{nombre_borrar}' ha sido eliminado del sistema.")
                        
                    except sqlite3.Error as error:
                        conexion.rollback() # Si algo falla, cancelamos la eliminación
                        st.error(f"❌ Error al eliminar: {error}")
                    finally:
                        if 'conexion' in locals(): conexion.close()
        else:
            st.info("No hay productos para eliminar.")
# ==========================================
# ÁREA PRINCIPAL: EL REPORTE VISUAL
# ==========================================
st.title("📊 Panel de Control del Mercado")
st.write("Monitorea y actualiza tu inventario en tiempo real.")
st.divider()

try:
    conexion = sqlite3.connect("mi_rastreador.db")
    
    # Modificamos la consulta para que los precios más nuevos salgan hasta arriba (ORDER BY DESC)
    consulta_sql = """
        SELECT productos.nombre, productos.categoria, historial_precios.precio, historial_precios.fecha
        FROM productos
        JOIN historial_precios ON productos.id = historial_precios.producto_id
        ORDER BY historial_precios.fecha DESC, historial_precios.id DESC
    """
    
    datos_visuales = pd.read_sql_query(consulta_sql, conexion)
    
    st.subheader("📦 Inventario y Variaciones")
    st.dataframe(datos_visuales, use_container_width=True, hide_index=True)

except sqlite3.Error as error:
    st.error(f"Error al conectar con la bóveda: {error}")
finally:
    if 'conexion' in locals(): conexion.close()