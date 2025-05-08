import math
import random

# Grafo con vecinos para cada nodo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# Heurística (valor de cada nodo)
heuristica = {
    'A': 1,
    'B': 3,
    'C': 5,
    'D': 7,
    'E': 4,
    'F': 6,
    'G': 8  # Nodo óptimo
}

def temple_simulado(grafo, nodo_inicial, temperatura, tasa_enfriamiento):
    estado_actual = nodo_inicial
    mejor_estado = estado_actual

    while temperatura > 0.01:  # Condición de parada
        vecinos = grafo.get(estado_actual, [])
        if not vecinos:
            break

        # Seleccionamos un vecino aleatorio
        vecino = random.choice(vecinos)

        # Cambio de heurística entre estados
        delta_E = heuristica[vecino] - heuristica[estado_actual]

        # Si el vecino es mejor, lo aceptamos
        if delta_E > 0:
            estado_actual = vecino
        else:
            # Si es peor, lo aceptamos con probabilidad e^(ΔE / T)
            probabilidad = math.exp(delta_E / temperatura)
            if random.random() < probabilidad:
                estado_actual = vecino

        # Guardamos el mejor estado encontrado
        if heuristica[estado_actual] > heuristica[mejor_estado]:
            mejor_estado = estado_actual

        # Reducimos la temperatura
        temperatura *= tasa_enfriamiento

    return mejor_estado

# Ejecutamos el algoritmo
mejor_estado = temple_simulado(grafo, 'A', temperatura=10, tasa_enfriamiento=0.9)
print(f'Mejor estado encontrado con Temple Simulado: {mejor_estado}')

# Ejemplo de aplicación real: En la optimización de procesos industriales, el temple simulado puede ser utilizado para encontrar la configuración de parámetros que minimiza el consumo de energía y maximiza la producción.
