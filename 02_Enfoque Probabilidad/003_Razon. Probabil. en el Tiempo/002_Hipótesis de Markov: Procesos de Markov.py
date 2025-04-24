import numpy as np

estados = ["Soleado", "Nublado", "Lluvioso"]
transiciones = [
    [0.6, 0.3, 0.1],  # Soleado
    [0.2, 0.5, 0.3],  # Nublado
    [0.1, 0.3, 0.6]   # Lluvioso
]

def simular_markov(inicial=0, pasos=10):
    actual = inicial
    secuencia = [estados[actual]]

    for _ in range(pasos):
        actual = np.random.choice([0,1,2], p=transiciones[actual])
        secuencia.append(estados[actual])

    return secuencia

# Simulación
np.random.seed(42)
resultado = simular_markov(inicial=0, pasos=15)
print("→ Transición del clima:")
print(" → ".join(resultado))
