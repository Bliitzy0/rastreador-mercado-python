import pandas as pd
import random
import time

# 1. Preparamos una lista vacía. Aquí iremos guardando las lecturas
# Piensa en esto como una caja vacía donde iremos metiendo diccionarios
historial_termico = []

print("Iniciando escaneo de sensores de hardware...\n")

# 2. El bucle for ejecutará este bloque de código exactamente 5 veces
for lectura in range(5):
    
    # A. Simulamos las lecturas físicas (generamos un número al azar)
    # Imaginemos que el procesador de tu ZBook varía entre 45°C y 85°C
    temp_cpu_zbook = random.randint(45, 85)
    
    # Imaginemos que el flujo de aire de tu Corsair 4000D mantiene el interior entre 30°C y 40°C
    temp_aire_corsair = random.randint(30, 40)
    
    # B. Empaquetamos esa lectura en un diccionario
    datos_actuales = {
        "Lectura_Num": lectura + 1,
        "CPU_ZBook_C": temp_cpu_zbook,
        "Gabinete_Corsair_C": temp_aire_corsair
    }
    
    # C. Metemos este diccionario en nuestra lista usando .append()
    historial_termico.append(datos_actuales)
    
    # Imprimimos en pantalla para ver qué está pasando
    print(f"Tomando lectura {lectura + 1}... CPU: {temp_cpu_zbook}°C | Gabinete: {temp_aire_corsair}°C")
    
    # D. Le decimos a Python que se "duerma" 2 segundos antes de la siguiente vuelta
    time.sleep(2)

# 3. Fuera del bucle: El procesamiento de datos
print("\nLecturas finalizadas. Procesando datos...")

# Convertimos nuestra lista llena de diccionarios a una tabla de Pandas
tabla_temperaturas = pd.DataFrame(historial_termico)

# Exportamos a Excel
tabla_temperaturas.to_excel("reporte_temperaturas.xlsx", index=False, engine='openpyxl')

print("✅ ¡Éxito! Archivo 'reporte_temperaturas.xlsx' generado en tu disco duro.")