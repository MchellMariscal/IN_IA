import cv2
import numpy as np
import matplotlib.pyplot as plt

# Imagen de prueba (imagen negra con un rectángulo blanco)
imagen = np.zeros((100, 100), dtype=np.uint8)
imagen[30:70, 30:70] = 255

# Aplicar un filtro de desenfoque
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(imagen, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Suavizada")
plt.imshow(imagen_suavizada, cmap='gray')

plt.show()
