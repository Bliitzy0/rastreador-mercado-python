# 1. Importamos nuestras herramientas recién instaladas
import pandas as pd
import matplotlib.pyplot as plt

# 2. Nuestros datos (ahora en tu equipo nuevo)
datos = {
    "Año": [2019, 2020, 2021, 2022, 2023],
    "Inflacion_Porcentaje": [1.8, 1.2, 4.7, 8.0, 3.4],
    "Tasa_Interes": [2.25, 0.50, 0.25, 1.75, 5.25]
}

# Convertimos a tabla de Pandas
tabla_economica = pd.DataFrame(datos)

# 3. Preparamos los ejes
eje_x = tabla_economica["Año"]
eje_y_inflacion = tabla_economica["Inflacion_Porcentaje"]
eje_y_interes = tabla_economica["Tasa_Interes"]  # ¡Aquí está nuestra nueva variable!

# 4. Dibujamos las dos líneas
# A la inflación le ponemos color rojo y marcador de círculo ('o')
plt.plot(eje_x, eje_y_inflacion, marker='o', color='red', linewidth=2, label="Inflación")

# A la tasa de interés le ponemos color azul y marcador de cuadrado ('s' de square)
plt.plot(eje_x, eje_y_interes, marker='s', color='blue', linewidth=2, label="Tasa de Interés")

# 5. Decoramos la gráfica
plt.title("Inflación vs Tasa de Interés (2019 - 2023)")
plt.xlabel("Año")
plt.ylabel("Porcentaje (%)")
plt.grid(True)
plt.legend() # ¡Esto hace que aparezcan las etiquetas de los colores!

plt.savefig("grafica_macroeconomia.png", dpi=300, bbox_inches='tight')
# 6. Mostramos el resultado
print("Guardado en el dispositivo.")
plt.show()