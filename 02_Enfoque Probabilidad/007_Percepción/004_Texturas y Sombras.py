import numpy as np
import matplotlib.pyplot as plt

# Crear una textura tipo damero
def generar_damero(n):
    return np.indices((n, n)).sum(axis=0) % 2

textura = generar_damero(8)

plt.imshow(textura, cmap='gray')
plt.title('Textura de Damero')
plt.show()
