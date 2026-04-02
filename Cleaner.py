import sqlite3

def limpiar_clones():
    print("🧹 Iniciando protocolo de limpieza...")
    
    try:
        conexion = sqlite3.connect("mi_rastreador.db")
        cursor = conexion.cursor()
        
        # 1. Primero borramos los precios de los clones (los que tienen producto_id 4, 5 y 6)
        # Usamos > 3 porque sabemos que nuestros 3 originales son el 1, 2 y 3.
        cursor.execute("DELETE FROM historial_precios WHERE producto_id > 3")
        filas_precios = cursor.rowcount # Esto nos dice cuántos renglones borró
        print(f"🗑️ Se eliminaron {filas_precios} precios huérfanos.")
        
        # 2. Ahora sí, borramos los productos duplicados del catálogo
        cursor.execute("DELETE FROM productos WHERE id > 3")
        filas_productos = cursor.rowcount
        print(f"🗑️ Se eliminaron {filas_productos} productos clonados.")
        
        # 3. Guardamos los cambios permanentemente
        conexion.commit()
        print("✅ Base de datos impecable.")
        
    except sqlite3.Error as error:
        conexion.rollback()
        print(f"❌ Error durante la limpieza: {error}")
        
    finally:
        if 'conexion' in locals():
            conexion.close()

# Ejecutamos la limpieza
limpiar_clones()