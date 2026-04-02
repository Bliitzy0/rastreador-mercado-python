# 1. Nuestra LISTA con un historial de lecturas térmicas
historial_temperaturas = [45, 55, 68, 89, 92, 75, 60]
limite = 80

print("--- Analizando registro térmico ---")

# TAREA: Construye el bucle y la decisión
# 1. Crea un bucle 'for' que recorra cada número en la lista 'historial_temperaturas'.
# (Ejemplo: for lectura in ... )
for item in historial_temperaturas:
    if item > limite:
        print(f"Precaucion, temperaturas elevadas {item}")
    else:
        print(f"Lectura {item}°C: Normalito bro")

# 2. DENTRO del bucle, pon un 'if/else' (¡cuidado con la sangría!).
# 3. Si la lectura actual supera el límite, imprime: "¡Peligro! Temperatura de {lectura}°C"
# 4. Si no, imprime: "Lectura {lectura}°C: Normalito bro"



print("\n--- Análisis completado ---")