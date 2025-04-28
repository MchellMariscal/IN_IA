import matplotlib.pyplot as plt
import numpy as np

# Dibujar un círculo
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

plt.plot(x, y)
plt.title('Círculo en 2D')
plt.axis('equal')
plt.show()
