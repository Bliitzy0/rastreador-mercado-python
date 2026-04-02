# Nuestra matriz 3x3
registro_termico = [
    [45, 50, 48],  # Fila 0: CPU
    [35, 40, 38],  # Fila 1: Gabinete
    [60, 75, 70]   # Fila 2: Tarjeta Gráfica
]

# 1. Preparamos a nuestro "Rey de la Colina" (empieza en cero)
temperatura_maxima = 0

print("Iniciando escaneo en busca del pico térmico...\n")

# Bucle externo (Filas)
for fila in registro_termico:
    
    # Bucle interno (Columnas)
    for temperatura in fila:
        
        # EL CONDICIONAL: Comparamos la lectura actual contra el Rey
        if temperatura > temperatura_maxima:
            
            # ¡Tenemos un nuevo Rey! Actualizamos la variable
            temperatura_maxima = temperatura
            print(f"¡Nuevo pico detectado! Subiendo a {temperatura_maxima}°C")

print("\n--- Análisis Finalizado ---")
# 2. Imprimimos el ganador absoluto que quedó guardado al final
print(f"La temperatura MÁS ALTA registrada en todo el sistema fue: {temperatura_maxima}°C")