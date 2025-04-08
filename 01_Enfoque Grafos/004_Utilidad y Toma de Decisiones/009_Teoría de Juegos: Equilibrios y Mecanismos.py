import nashpy as nash
import numpy as np

# Juego de dilema del prisionero
# Matrices de pagos: jugador 1 y jugador 2
A = np.array([[3, 0],  # Cooperar, Traicionar
              [5, 1]]) # Traicionar, Traicionar

B = np.array([[3, 5],
              [0, 1]])

# Crear el juego
juego = nash.Game(A, B)

# Encontrar equilibrios de Nash puros o mixtos
equilibrios = juego.support_enumeration()

# Mostrar resultados
print("Equilibrios de Nash encontrados:")
for eq in equilibrios:
    print(f"Estrategia jugador 1: {eq[0]}, jugador 2: {eq[1]}")
