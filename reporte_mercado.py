import sqlite3

def generar_reporte_mercado():
    print("📡 Conectando con la base de datos...\n")
    
    try:
        # 1. Abrimos el restaurante y llamamos al mesero
        conexion = sqlite3.connect("mi_rastreador.db")
        cursor = conexion.cursor()
        
        # 2. Escribimos la comanda SQL (Usamos comillas triples para escribir en varias líneas sin que Python se queje)
        consulta_sql = """
            SELECT productos.nombre, productos.categoria, historial_precios.precio, historial_precios.fecha
            FROM productos
            JOIN historial_precios ON productos.id = historial_precios.producto_id
        """
        
        # 3. Le damos la orden al mesero
        cursor.execute(consulta_sql)
        
        # 4. Le pedimos que vacíe sus bolsillos en la mesa
        datos_extraidos = cursor.fetchall()
        
        # 5. Formateamos la salida en la terminal para que se vea como un sistema profesional
        print("=" * 60)
        print(" 📊 REPORTE DE PRECIOS DEL MERCADO")
        print("=" * 60)
        
        # Recorremos la lista que nos dio el mesero
        for fila in datos_extraidos:
            # fila[0] es el nombre, fila[1] es la categoria, fila[2] es el precio, fila[3] es la fecha
            nombre = fila[0]
            categoria = fila[1]
            precio = fila[2]
            fecha = fila[3]
            
            print(f"📦 {nombre} ({categoria})")
            print(f"   💰 Precio actual: ${precio:,.2f} MXN  |  📅 Última revisión: {fecha}")
            print("-" * 60)
            
    except sqlite3.Error as error:
        print(f"❌ Error al consultar la base de datos: {error}")
        
    finally:
        # ¡El equipo de limpieza cierra la conexión!
        if 'conexion' in locals():
            conexion.close()
            print("\n🔒 Conexión cerrada de forma segura.")

# Ejecutamos nuestro generador de reportes
generar_reporte_mercado()