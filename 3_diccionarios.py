# Nuestro diccionario con la configuración inicial
especificaciones = {
    "marca": "HP",
    "modelo": "ZBook",
    "memoria_ram": 16,
    "encendida": False
}

# TAREA 1: Imprime en pantalla ÚNICAMENTE el modelo del equipo.
# Pista: Usa el nombre del diccionario y la llave "modelo" entre corchetes []
print(f"El modelo del equipo es:{especificaciones["modelo"]} ")

# TAREA 2: Agrega una nueva característica al diccionario.
# Crea la llave "almacenamiento" y asígnale el texto "1TB NVMe".
# Pista: diccionario["nueva_llave"] = valor
especificaciones["almacenamiento"] = "1tb NVMe"

# TAREA 3: Actualiza la memoria RAM.
# El equipo recibió una mejora. Cambia el valor de "memoria_ram" para que ahora sea 32.
especificaciones["memoria_ram"] = 32

# Comprobación final
print("\n--- Especificaciones Actualizadas ---")
print(especificaciones)