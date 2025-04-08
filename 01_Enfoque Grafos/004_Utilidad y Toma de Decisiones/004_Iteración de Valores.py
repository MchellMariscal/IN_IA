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

gamma = 0.9
V = np.zeros(3)
threshold = 0.01

for i in range(100):
    delta = 0
    new_V = np.zeros(3)
    for s in range(3):
        Q_values = []
        for a in range(2):
            q = sum([transitions[s][a][s_prime] * (rewards[s][a] + gamma * V[s_prime])
                     for s_prime in range(3)])
            Q_values.append(q)
        new_V[s] = max(Q_values)
        delta = max(delta, abs(new_V[s] - V[s]))
    V = new_V
    if delta < threshold:
        break

print("Valores óptimos por estado:")
print(V)
