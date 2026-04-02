import pandas as pd

# ---------------------------------------------------------
# 1. PREPARACIÓN: Creamos un archivo Excel de prueba
# ---------------------------------------------------------
datos = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [1500, 2200, 1800, 2900],
    "Gastos": [800, 950, 850, 1100]
}
tabla_temporal = pd.DataFrame(datos)

# Así de fácil se exporta un archivo a Excel
tabla_temporal.to_excel("reporte_financiero.xlsx", index=False, engine='openpyxl')
print("✅ Archivo 'reporte_financiero.xlsx' creado en tu disco duro.\n")


# ---------------------------------------------------------
# 2. EL OBJETIVO: Leer y analizar el archivo Excel
# ---------------------------------------------------------

# Usamos read_excel indicando el nombre del archivo
datos_leidos = pd.read_excel("reporte_financiero.xlsx", engine='openpyxl')

print("--- Datos extraídos del archivo Excel ---")
print(datos_leidos)

# Ahora podemos usar las matemáticas de Pandas como si fueran fórmulas de Excel
total_ventas = datos_leidos["Ventas"].sum()
total_gastos = datos_leidos["Gastos"].sum()
ganancia_neta = total_ventas - total_gastos

print(f"\n📊 Análisis Automático:")
print(f"Las ventas totales fueron de ${total_ventas}")
print(f"La ganancia neta del cuatrimestre es: ${ganancia_neta}")