import matplotlib.pyplot as plt

# Valores posibles de un dado
valores = [1, 2, 3, 4, 5, 6]

# Probabilidades de cada valor (uniforme)
probabilidades = [1/6] * 6

# Graficamos la distribución de probabilidad
plt.bar(valores, probabilidades)  # Creamos un gráfico de barras
plt.title("Distribución de un dado")  # Título del gráfico
plt.xlabel("Valor")  # Etiqueta del eje x
plt.ylabel("Probabilidad")  # Etiqueta del eje y
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En los juegos de azar, la distribución de probabilidad puede ser utilizada para modelar la probabilidad de diferentes resultados, como en el lanzamiento de un dado.
