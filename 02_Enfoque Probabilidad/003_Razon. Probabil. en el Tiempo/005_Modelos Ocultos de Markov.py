import random

# Estados posibles
estados = ["Izquierda", "Centro", "Derecha"]

# Matriz de transición: Probabilidad de moverse entre estados
transiciones = {
    "Izquierda": {"Izquierda": 0.7, "Centro": 0.3, "Derecha": 0.0},  # Desde Izquierda
    "Centro": {"Izquierda": 0.2, "Centro": 0.6, "Derecha": 0.2},  # Desde Centro
    "Derecha": {"Izquierda": 0.0, "Centro": 0.4, "Derecha": 0.6}  # Desde Derecha
}

# Sensor ruidoso: observación basada en estado real
sensores = {
    "Izquierda": {"detecta Izquierda": 0.9, "detecta Centro": 0.1, "detecta Derecha": 0.0},  # Desde Izquierda
    "Centro": {"detecta Izquierda": 0.1, "detecta Centro": 0.8, "detecta Derecha": 0.1},  # Desde Centro
    "Derecha": {"detecta Izquierda": 0.0, "detecta Centro": 0.1, "detecta Derecha": 0.9}  # Desde Derecha
}

# Secuencia de observaciones del sensor
observaciones = ["detecta Centro", "detecta Derecha", "detecta Derecha"]

# Función para el filtrado de partículas
def filtrado_particulas(observaciones, transiciones, sensores, n=1000):
    particulas = [random.choice(estados) for _ in range(n)]  # Inicializamos las partículas

    for obs in observaciones:  # Para cada observación
        # Movimiento de partículas según transición
        particulas = [random.choices(
            list(transiciones[p].keys()), weights=list(transiciones[p].values()))[0]
            for p in particulas
        ]

        # Peso basado en la observación
        pesos = [sensores[p].get(obs, 0) for p in particulas]  # Calculamos los pesos

        # Re-muestreo según pesos
        particulas = random.choices(particulas, weights=pesos, k=n)  # Re-muestreamos

    # Contar la cantidad de partículas en cada estado
    belief = {estado: particulas.count(estado) / n for estado in estados}  # Calculamos la creencia
    return belief  # Devolvemos la creencia

# Ejecutar el filtrado
resultado = filtrado_particulas(observaciones, transiciones, sensores)  # Realizamos el filtrado
print("Estimación final del estado:")  # Imprimimos la estimación final
for estado, prob in resultado.items():  # Para cada estado
    print(f"{estado}: {prob:.4f}")  # Imprimimos el estado y su probabilidad

# Ejemplo de aplicación real: En la robótica, los modelos ocultos de Markov pueden ser utilizados para estimar la posición de un robot en un entorno, considerando las observaciones ruidosas y las transiciones entre estados.
