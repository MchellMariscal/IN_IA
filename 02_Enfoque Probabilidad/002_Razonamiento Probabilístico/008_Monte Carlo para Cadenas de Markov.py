import random
import matplotlib.pyplot as plt

# Estados posibles
states = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición
transition_matrix = [
    [0.6, 0.3, 0.1],  # Desde Soleado
    [0.2, 0.5, 0.3],  # Desde Nublado
    [0.1, 0.4, 0.5]   # Desde Lluvioso
]

# Función para obtener el siguiente estado
def next_state(current_state):
    return random.choices(states, transition_matrix[states.index(current_state)])[0]  # Muestreo del siguiente estado

# Simulación Monte Carlo
def simulate_markov(start_state, days=1000):
    current_state = start_state  # Estado inicial
    history = {state: 0 for state in states}  # Diccionario para guardar la historia

    for _ in range(days):  # Para cada día
        history[current_state] += 1  # Incrementamos el contador del estado actual
        current_state = next_state(current_state)  # Obtenemos el siguiente estado

    return history  # Devolvemos la historia

# Ejecutar simulación
result = simulate_markov("Soleado", 1000)  # Simulamos 1000 días

# Mostrar resultados
print("Distribución estimada después de 1000 días:")  # Imprimimos la distribución estimada
for state, count in result.items():  # Para cada estado
    print(f"{state}: {count} ({(count/1000)*100:.2f}%)")  # Imprimimos el estado y su frecuencia

# Graficar resultados
plt.bar(result.keys(), result.values(), color=["gold", "gray", "blue"])  # Creamos un gráfico de barras
plt.title("Monte Carlo - Distribución de Estados Climáticos")  # Título del gráfico
plt.xlabel("Estado")  # Etiqueta del eje x
plt.ylabel("Frecuencia")  # Etiqueta del eje y
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En la meteorología, el método de Monte Carlo para cadenas de Markov puede ser utilizado para simular y predecir patrones climáticos, considerando las transiciones entre diferentes estados climáticos.
