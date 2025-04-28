import cv2
import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen con líneas
imagen = np.zeros((100, 100), dtype=np.uint8)
cv2.line(imagen, (10, 10), (90, 10), 255, 2)
cv2.line(imagen, (10, 20), (90, 20), 255, 2)

# Detección de líneas con Hough
bordes = cv2.Canny(imagen, 50, 150)
lineas = cv2.HoughLinesP(bordes, 1, np.pi/180, threshold=20, minLineLength=10, maxLineGap=5)

# Dibujar líneas detectadas
imagen_color = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
for linea in lineas:
    x1, y1, x2, y2 = linea[0]
    cv2.line(imagen_color, (x1, y1), (x2, y2), (0, 255, 0), 2)

plt.imshow(imagen_color)
plt.title('Líneas Detectadas')
plt.show()
