import matplotlib.pyplot as plt
import numpy as np

# Dos clases separables linealmente
X1 = np.random.randn(50, 2) + np.array([2, 2])
X2 = np.random.randn(50, 2) + np.array([-2, -2])

plt.scatter(X1[:,0], X1[:,1], color='blue', label='Clase 1')
plt.scatter(X2[:,0], X2[:,1], color='red', label='Clase 2')
plt.plot([-4, 4], [-4, 4], 'k--')  # Línea separadora
plt.legend()
plt.title("Ejemplo de Separabilidad Lineal")
plt.show()
