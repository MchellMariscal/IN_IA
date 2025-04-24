import random
import matplotlib.pyplot as plt

# Estados
states = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición
transition_matrix = [
    [0.6, 0.3, 0.1],  # Desde Soleado
    [0.2, 0.5, 0.3],  # Desde Nublado
    [0.1, 0.4, 0.5]   # Desde Lluvioso
]

def next_state(current_state):
    return random.choices(states, transition_matrix[states.index(current_state)])[0]

# Simulación Monte Carlo
def simulate_markov(start_state, days=1000):
    current_state = start_state
    history = {state: 0 for state in states}

    for _ in range(days):
        history[current_state] += 1
        current_state = next_state(current_state)

    return history

# Ejecutar simulación
result = simulate_markov("Soleado", 1000)

# Mostrar resultados
print("Distribución estimada después de 1000 días:")
for state, count in result.items():
    print(f"{state}: {count} ({(count/1000)*100:.2f}%)")

# Gráfico
plt.bar(result.keys(), result.values(), color=["gold", "gray", "blue"])
plt.title("Monte Carlo - Distribución de Estados Climáticos")
plt.xlabel("Estado")
plt.ylabel("Frecuencia")
plt.show()
