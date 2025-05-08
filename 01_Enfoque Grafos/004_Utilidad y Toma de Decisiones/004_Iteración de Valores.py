import numpy as np

# Estados: 0, 1, 2
# Acciones: 0 y 1
# Recompensas y transiciones dadas

rewards = np.array([
    [5, 10],    # recompensas en el estado 0
    [-1, 2],    # estado 1
    [0, 0]      # estado 2 (terminal)
])

transitions = [
    [[0.8, 0.2, 0.0], [0.1, 0.9, 0.0]],  # desde estado 0, acción 0 y 1
    [[0.0, 0.6, 0.4], [0.0, 0.3, 0.7]],  # desde estado 1
    [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]   # estado 2, no cambia
]

gamma = 0.9  # Factor de descuento
V = np.zeros(3)  # Valores iniciales para cada estado
threshold = 0.01  # Umbral de convergencia

for i in range(100):  # Iteraciones máximas
    delta = 0  # Cambio máximo en los valores
    new_V = np.zeros(3)  # Nuevos valores para cada estado
    for s in range(3):  # Para cada estado
        Q_values = []  # Valores Q para cada acción
        for a in range(2):  # Para cada acción
            q = sum([transitions[s][a][s_prime] * (rewards[s][a] + gamma * V[s_prime])  # Cálculo del valor Q
                     for s_prime in range(3)])  # Para cada estado siguiente
            Q_values.append(q)  # Añadimos el valor Q
        new_V[s] = max(Q_values)  # Actualizamos el valor del estado
        delta = max(delta, abs(new_V[s] - V[s]))  # Actualizamos el cambio máximo
    V = new_V  # Actualizamos los valores
    if delta < threshold:  # Si el cambio es menor que el umbral
        break  # Terminamos las iteraciones

print("Valores óptimos por estado:")  # Imprimimos los valores óptimos
print(V)  # Imprimimos los valores

# Ejemplo de aplicación real: En la robótica, la iteración de valores puede ser utilizada para determinar la mejor ruta que un robot debe seguir en un entorno con incertidumbre, maximizando las recompensas esperadas.
