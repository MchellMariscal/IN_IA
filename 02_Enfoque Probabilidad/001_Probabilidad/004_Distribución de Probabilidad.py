import matplotlib.pyplot as plt

valores = [1, 2, 3, 4, 5, 6]
probabilidades = [1/6] * 6

plt.bar(valores, probabilidades)
plt.title("Distribución de un dado")
plt.xlabel("Valor")
plt.ylabel("Probabilidad")
plt.show()
