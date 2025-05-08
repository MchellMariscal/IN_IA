import nashpy as nash
import numpy as np

# Juego de dilema del prisionero
# Matrices de pagos: jugador 1 y jugador 2
A = np.array([[3, 0],  # Cooperar, Traicionar
              [5, 1]]) # Traicionar, Traicionar

B = np.array([[3, 5],
              [0, 1]]) # Cooperar, Traicionar

# Crear el juego
juego = nash.Game(A, B)  # Creamos un juego

# Encontrar equilibrios de Nash puros o mixtos
equilibrios = juego.support_enumeration()  # Encontramos los equilibrios de Nash

# Mostrar resultados
print("Equilibrios de Nash encontrados:")  # Imprimimos los equilibrios de Nash
for eq in equilibrios:  # Para cada equilibrio
    print(f"Estrategia jugador 1: {eq[0]}, jugador 2: {eq[1]}")  # Imprimimos las estrategias

# Ejemplo de aplicación real: En la economía, la teoría de juegos puede ser utilizada para analizar las interacciones estratégicas entre empresas en un mercado, ayudando a predecir los resultados de diferentes estrategias competitivas.
