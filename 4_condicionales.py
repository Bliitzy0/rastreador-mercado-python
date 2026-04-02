# Variables del sistema
temperatura_actual = 85
limite_seguro = 80

print(f"--- Monitor Térmico Iniciado ---")
print(f"Lectura del sensor: {temperatura_actual}°C\n")

# TAREA: Construye la toma de decisión lógica
# 1. Crea un 'if' que pregunte si la temperatura_actual es MAYOR (>) que el limite_seguro.
# 2. Si es verdad, imprime: "¡ALERTA ROJA! Activando ventiladores al 100%."
# 3. Crea el 'else:' para lo que debe pasar si la temperatura está bien.
# 4. En el else, imprime: "Temperatura estable. Sistema operando con normalidad."
if (temperatura_actual > limite_seguro):
    print("ALERTA ROJA")
else:
     print ("Todo normalito bro")


# Esta línea está fuera del if/else, se imprimirá pase lo que pase
print("\nFin del diagnóstico.")