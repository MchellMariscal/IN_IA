import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Parámetros
n = 500  # Número de muestras
mu = 0   # Media
sigma = 1  # Desviación estándar

# Generar proceso estacionario (ruido blanco)
np.random.seed(0)  # Semilla para reproducibilidad
white_noise = np.random.normal(mu, sigma, n)  # Generamos ruido blanco

# Calcular propiedades
media = np.mean(white_noise)  # Calculamos la media
varianza = np.var(white_noise)  # Calculamos la varianza

print(f"Media: {media:.4f}")  # Imprimimos la media
print(f"Varianza: {varianza:.4f}")  # Imprimimos la varianza

# Graficar proceso
plt.figure(figsize=(10, 4))  # Tamaño de la figura
plt.plot(white_noise, label="Ruido Blanco")  # Graficamos el ruido blanco
plt.title("Proceso Estacionario: Ruido Blanco")  # Título del gráfico
plt.xlabel("Tiempo")  # Etiqueta del eje x
plt.ylabel("Valor")  # Etiqueta del eje y
plt.grid(True)  # Mostramos la cuadrícula
plt.legend()  # Mostramos la leyenda
plt.show()  # Mostramos el gráfico

# Graficar autocorrelación
plot_acf(white_noise, lags=40)  # Graficamos la autocorrelación
plt.title("Autocorrelación del Ruido Blanco")  # Título del gráfico
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En el análisis de señales, los procesos estacionarios pueden ser utilizados para modelar señales de ruido, como en el procesamiento de señales de audio o en la detección de anomalías en datos de sensores.
