import numpy as np

# Estados posibles
estados = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición
transiciones = [
    [0.6, 0.3, 0.1],  # Desde Soleado
    [0.2, 0.5, 0.3],  # Desde Nublado
    [0.1, 0.3, 0.6]   # Desde Lluvioso
]

# Función para simular un proceso de Markov
def simular_markov(inicial=0, pasos=10):
    actual = inicial  # Estado inicial
    secuencia = [estados[actual]]  # Inicializamos la secuencia

    for _ in range(pasos):  # Para cada paso
        actual = np.random.choice([0, 1, 2], p=transiciones[actual])  # Elegimos el siguiente estado
        secuencia.append(estados[actual])  # Añadimos el estado a la secuencia

    return secuencia  # Devolvemos la secuencia

# Simulación
np.random.seed(42)  # Semilla para reproducibilidad
resultado = simular_markov(inicial=0, pasos=15)  # Simulamos 15 pasos
print("→ Transición del clima:")  # Imprimimos la transición del clima
print(" → ".join(resultado))  # Imprimimos la secuencia

# Ejemplo de aplicación real: En la meteorología, los procesos de Markov pueden ser utilizados para modelar y predecir cambios en el clima, considerando las probabilidades de transición entre diferentes estados climáticos.
