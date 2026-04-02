# Matriz de 3x3 (3 filas y 3 columnas)
registro_termico = [
    [45, 50, 48],  # Fila 0: Temperaturas del CPU
    [35, 40, 38],  # Fila 1: Temperaturas del Gabinete
    [60, 75, 70]   # Fila 2: Temperaturas de la Tarjeta Gráfica
]

temp_mañana = registro_termico [1][0]
print(f"La temperatura para el gabinete en la mañana es: {temp_mañana} °C")