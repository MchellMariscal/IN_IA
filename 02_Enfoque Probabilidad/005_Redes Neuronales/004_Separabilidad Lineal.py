import matplotlib.pyplot as plt
import numpy as np

# Dos clases separables linealmente
X1 = np.random.randn(50, 2) + np.array([2, 2])  # Clase 1
X2 = np.random.randn(50, 2) + np.array([-2, -2])  # Clase 2

plt.scatter(X1[:,0], X1[:,1], color='blue', label='Clase 1')  # Graficamos la clase 1
plt.scatter(X2[:,0], X2[:,1], color='red', label='Clase 2')  # Graficamos la clase 2
plt.plot([-4, 4], [-4, 4], 'k--')  # Línea separadora
plt.legend()  # Mostramos la leyenda
plt.title("Ejemplo de Separabilidad Lineal")  # Título del gráfico
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En la clasificación de datos, la separabilidad lineal puede ser utilizada para identificar patrones en datos que pueden ser separados por una línea, permitiendo la clasificación de nuevas instancias.
