# 1. Declara un Texto (String) para el modelo del equipo
modelo_equipo = "YAKSHA"

# 2. Declara un Entero (Integer) para la capacidad de la fuente de poder en Watts
watts_fuente = 600 

# 3. Declara un Decimal (Float) para la temperatura máxima permitida
temp_maxima = 52.3

# 4. Declara un Booleano (Boolean) indicando si el equipo tiene refrigeración líquida
tiene_liquida = True

# 5. Imprime un reporte uniendo todas tus variables en una f-string
print(f"Reporte: El equipo {modelo_equipo} tiene una fuente de {watts_fuente}W.")
print(f"Límite térmico: {temp_maxima}°C. ¿Refrigeración líquida?: {tiene_liquida}")