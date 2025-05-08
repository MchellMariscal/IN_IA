import cv2
import numpy as np
import matplotlib.pyplot as plt

# Imagen de prueba: imagen negra con un rectángulo blanco
imagen = np.zeros((100, 100), dtype=np.uint8)  # Creamos una imagen negra
imagen[30:70, 30:70] = 255  # Dibujamos un rectángulo blanco

# Aplicar un filtro de desenfoque (Gaussian Blur)
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)  # Aplicamos el filtro de desenfoque

plt.subplot(1, 2, 1)  # Subgráfico 1
plt.title("Original")  # Título del subgráfico
plt.imshow(imagen, cmap='gray')  # Mostramos la imagen original

plt.subplot(1, 2, 2)  # Subgráfico 2
plt.title("Suavizada")  # Título del subgráfico
plt.imshow(imagen_suavizada, cmap='gray')  # Mostramos la imagen suavizada

plt.show()  # Mostramos los gráficos

# Ejemplo de aplicación real: En el procesamiento de imágenes, los filtros pueden ser utilizados para suavizar imágenes y reducir el ruido, mejorando la calidad de las imágenes para análisis posteriores.
