# Nuestro archivero inicial
componentes = ["Procesador", "Memoria RAM", "Disco Solido"]

# TAREA 1: Imprime en pantalla ÚNICAMENTE el primer elemento ("Procesador")
# Pista: Usa el nombre de la lista seguido del índice entre corchetes [ ]
print(f"La pieza principal es: {componentes [0]} ") 

# TAREA 2: Usa el comando correcto para agregar una "Tarjeta Grafica" al final de la lista
# Pista: Empieza escribiendo el nombre de la lista y ponle un punto .
componentes.append("Tarjeta Grafica")

# TAREA 3: Actualiza el segundo elemento ("Memoria RAM") para que ahora diga "Memoria RAM 32GB"
# Pista: Es igual que sobreescribir una variable, pero especificando el índice [1]
componentes[1] = "Memoria RAM 32gb"

# Comprobación final
print(f"Lista final de piezas para ensamblar: {componentes}")