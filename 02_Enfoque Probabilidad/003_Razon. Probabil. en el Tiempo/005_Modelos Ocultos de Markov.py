import random

# Estados posibles
estados = ["Izquierda", "Centro", "Derecha"]

# Matriz de transición: Probabilidad de moverse entre estados
transiciones = {
    "Izquierda": {"Izquierda": 0.7, "Centro": 0.3, "Derecha": 0.0},
    "Centro": {"Izquierda": 0.2, "Centro": 0.6, "Derecha": 0.2},
    "Derecha": {"Izquierda": 0.0, "Centro": 0.4, "Derecha": 0.6}
}

# Sensor ruidoso: observación basada en estado real
sensores = {
    "Izquierda": {"detecta Izquierda": 0.9, "detecta Centro": 0.1, "detecta Derecha": 0.0},
    "Centro": {"detecta Izquierda": 0.1, "detecta Centro": 0.8, "detecta Derecha": 0.1},
    "Derecha": {"detecta Izquierda": 0.0, "detecta Centro": 0.1, "detecta Derecha": 0.9}
}

# Secuencia de observaciones del sensor
observaciones = ["detecta Centro", "detecta Derecha", "detecta Derecha"]

# Filtrado de partículas
def filtrado_particulas(observaciones, transiciones, sensores, n=1000):
    particulas = [random.choice(estados) for _ in range(n)]

    for obs in observaciones:
        # Movimiento de partículas según transición
        particulas = [random.choices(
            list(transiciones[p].keys()), weights=list(transiciones[p].values()))[0]
            for p in particulas
        ]

        # Peso basado en la observación
        pesos = [sensores[p].get(obs, 0) for p in particulas]

        # Re-muestreo según pesos
        particulas = random.choices(particulas, weights=pesos, k=n)

    # Contar la cantidad de partículas en cada estado
    belief = {estado: particulas.count(estado) / n for estado in estados}
    return belief

# Ejecutar el filtrado
resultado = filtrado_particulas(observaciones, transiciones, sensores)
print("Estimación final del estado:")
for estado, prob in resultado.items():
    print(f"{estado}: {prob:.4f}")
