import sqlite3
from datetime import date

# ==========================================
# 1. EL CONSTRUCTOR (Crea el archivo .db y las tablas)
# ==========================================
def fabricar_boveda():
    try:
        conexion = sqlite3.connect("mi_rastreador.db")
        cursor = conexion.cursor()
        
        # Tabla principal (El Catálogo)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL
            )
        ''')
        
        # Tabla secundaria (La Bitácora de Precios)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historial_precios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto_id INTEGER NOT NULL,
                precio REAL NOT NULL,
                fecha DATE NOT NULL,
                FOREIGN KEY (producto_id) REFERENCES productos (id)
            )
        ''')
        
        conexion.commit()
        print("✅ Bóveda de base de datos inicializada y lista.")
        
    except sqlite3.Error as error:
        print(f"❌ Error al fabricar la base de datos: {error}")
    finally:
        if 'conexion' in locals():
            conexion.close()

# ==========================================
# 2. EL MOTOR DE INSERCIÓN (Tu función acoplada)
# ==========================================
def alta_producto_y_precio(nombre, categoria, precio_inicial):
    fecha_hoy = date.today().isoformat()
    
    try:
        conexion = sqlite3.connect("mi_rastreador.db")
        cursor = conexion.cursor()
        
        # Paso A: Insertar en catálogo
        cursor.execute("INSERT INTO productos (nombre, categoria) VALUES (?, ?)", (nombre, categoria))
        
        # Paso B: Atrapar el ID mágico
        id_generado = cursor.lastrowid
        
        # Paso C: Insertar el precio usando ese ID
        cursor.execute("INSERT INTO historial_precios (producto_id, precio, fecha) VALUES (?, ?, ?)", 
                       (id_generado, precio_inicial, fecha_hoy))
        
        # Paso D: Guardar transacción completa
        conexion.commit()
        print(f"🛒 '{nombre}' registrado en el sistema. (ID Asignado: {id_generado}) | Precio de hoy: ${precio_inicial}")
        
    except sqlite3.Error as error:
        conexion.rollback() # El botón de deshacer si algo explota
        print(f"⚠️ Error de transacción, cancelando guardado: {error}")
    finally:
        if 'conexion' in locals():
            conexion.close()

# ==========================================
# ZONA DE EJECUCIÓN (El panel de control)
# ==========================================
print("--- INICIANDO RASTREADOR DE MERCADO ---\n")

# 1. Primero nos aseguramos de que el archivo exista
fabricar_boveda()

print("\n--- REGISTRANDO INVENTARIO INICIAL ---")

# 2. Usamos tu función para llenar la base de datos de un solo golpe
alta_producto_y_precio("Corsair 4000D Airflow", "Componentes PC", 1550.00)
alta_producto_y_precio("HP ZBook 15 G5", "Laptops Workstation", 18500.00)
alta_producto_y_precio("Nothing Phone 3", "Smartphones", 14000.00)

print("\nEl sistema está en línea y los datos están asegurados.")