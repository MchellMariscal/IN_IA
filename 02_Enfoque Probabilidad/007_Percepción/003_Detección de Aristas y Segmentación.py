import cv2
import numpy as np
import matplotlib.pyplot as plt

# Imagen
imagen = np.zeros((100, 100), dtype=np.uint8)
imagen[30:70, 30:70] = 255

# Detectar bordes usando Canny
bordes = cv2.Canny(imagen, 50, 150)

plt.imshow(bordes, cmap='gray')
plt.title('Detección de Bordes (Canny)')
plt.show()
