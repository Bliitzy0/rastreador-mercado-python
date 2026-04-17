import pyodbc

def actualizar_precio(id_producto, nuevo_precio):
    try:

     conexion = pyodbc.connect("Driver={...};Server=...;")
     cursor = conexion.cursor()
    
     # El Junior escribió esto:
     instruccion = f"UPDATE inventario SET precio = ? WHERE id = ?"
     cursor.execute(instruccion, (nuevo_precio, id_producto))
    
     conexion.commit()
    except pyodbc.Error as error:
        print(f"❌ Error al fabricar la base de datos: {error}")
    finally:
     if "conexion" in locals():    
        conexion.close()