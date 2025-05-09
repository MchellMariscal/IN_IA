# Estados posibles: ["A", "B", "C"] en un pasillo
estados = ["A", "B", "C"]

# Matriz de transición: ¿Dónde tiende a ir el robot?
transicion = {
    "A": {"A": 0.6, "B": 0.4},  # Desde A
    "B": {"A": 0.3, "B": 0.4, "C": 0.3},  # Desde B
    "C": {"B": 0.6, "C": 0.4}  # Desde C
}

# Sensores (observaciones ruidosas)
sensor = {
    "A": {"ver A": 0.8, "ver B": 0.2},  # Observaciones desde A
    "B": {"ver B": 0.7, "ver C": 0.3},  # Observaciones desde B
    "C": {"ver C": 0.9, "ver B": 0.1}   # Observaciones desde C
}

# Observaciones recibidas
observaciones = ["ver B", "ver C", "ver B"]

# Belief inicial: no sabemos nada
belief = {"A": 1/3, "B": 1/3, "C": 1/3}  # Creencia inicial

# Ejemplo de aplicación real: En la robótica, el filtrado, predicción, suavizado y explicación pueden ser utilizados para estimar la posición de un robot en un entorno, considerando las observaciones ruidosas y las transiciones entre estados.
