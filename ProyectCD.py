import sqlite3
from datetime import date # Importamos una herramienta para saber la fecha de hoy

# --- HERRAMIENTA 1: Agregar al Catálogo ---
def agregar_producto(nombre, categoria):
    try:
        conexion = sqlite3.connect("market_tracker.db")
        cursor = conexion.cursor()
        
        # Le decimos a SQL dónde insertar, y usamos (?) como espacios en blanco seguros
        cursor.execute("INSERT INTO products (name, category) VALUES (?, ?)", (nombre, categoria))
        
        # ¡commit() es vital! Es como darle a "Guardar archivo"
        conexion.commit() 
        print(f"[+] Catálogo actualizado: {nombre}")
        
    except sqlite3.Error as error:
        print(f"Error de base de datos: {error}")
    finally:
        if 'conexion' in locals():
            conexion.close()

# --- HERRAMIENTA 2: Registrar el Precio del Día ---
def registrar_precio(producto_id, precio):
    fecha_hoy = date.today() # Python saca la fecha de tu reloj automáticamente
    
    try:
        conexion = sqlite3.connect("market_tracker.db")
        cursor = conexion.cursor()
        
        cursor.execute("INSERT INTO price_history (product_id, price, date_recorded) VALUES (?, ?, ?)", 
                       (producto_id, precio, fecha_hoy))
        conexion.commit()
        
        print(f"[$] Precio capturado: ${precio} (Producto ID: {producto_id}) - {fecha_hoy}")
        
    except sqlite3.Error as error:
        print(f"Error de base de datos: {error}")
    finally:
        if 'conexion' in locals():
            conexion.close()

# ==========================================
# ZONA DE PRUEBAS (Tu simulador de mercado)
# ==========================================
print("--- INICIANDO SISTEMA DE RASTREO ---\n")

# 1. Metemos nuestros productos de interés a la base de datos
agregar_producto("Nothing Phone 3", "Smartphones")
agregar_producto("Realme X50 5G", "Smartphones")

# 2. Simulamos que hoy vimos estos precios en línea
# Como fueron los primeros en entrar, el Nothing Phone es el ID 1, y el Realme es el ID 2
registrar_precio(1, 14500.00) 
registrar_precio(2, 6200.50)  

print("\nOperación terminada. Datos guardados en la bóveda de forma permanente.")