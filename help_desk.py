import sqlite3

def create_databases():
    try:
        conexion = sqlite3.connect("helpdesk.db")
        cursor = conexion.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                modelo TEXT NOT NULL,
                procesador TEXT NOT NULL,
                ram_gb INTEGER NOT NULL,
                estado TEXT DEFAULT `Activo` 
            )
        ''')
        conexion.commit()
        print("Base de datos creada con exito") 
    except sqlite3.Error as error:
         print(f"❌ Error al fabricar la base de datos: {error}")
    finally:
         if 'conexion' in locals():
            conexion.close()


def registrar_equipos(tipo, modelo, procesador, ram_gb):
    try:

        conexion = sqlite3.connect("helpdesk.db")
        cursor = conexion.cursor()

        cursor.execute ("INSERT into equipos (tipo, modelo, procesador, ram_gb) VALUES (?, ?, ?, ?)", (tipo, modelo, procesador, ram_gb))

        conexion.commit()
        print("Productos guardados con exito")
    except sqlite3.Error as error:
        print(f"Se ha producido una anomalia : {error}")
    finally:
        if 'conexion' in locals():
            conexion.close()
        
def ver_inventario():
    try:

        conexion = sqlite3.connect("helpdesk.db")
        cursor = conexion.cursor()

        cursor.execute ("SELECT FROM * equipos")
        return cursor.fetchall()
    
    except:
        return[]
    finally:
         if 'conexion' in locals():
            conexion.close()
      