import numpy as np
import matplotlib.pyplot as plt

# Crear una textura tipo damero
def generar_damero(n):
    return np.indices((n, n)).sum(axis=0) % 2  # Generamos un patrón de damero

textura = generar_damero(8)  # Generamos una textura de 8x8

plt.imshow(textura, cmap='gray')  # Mostramos la textura
plt.title('Textura de Damero')  # Título del gráfico
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En el diseño de videojuegos, las texturas pueden ser utilizadas para crear superficies realistas, como patrones de damero, en modelos 3D.
