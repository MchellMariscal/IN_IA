from sklearn.neighbors import KNeighborsClassifier

# Datos de ejemplo
X = [[0,0], [1,1], [0,1], [10,10], [10,11], [11,10]]
y = [0, 0, 0, 1, 1, 1]  # Etiquetas

# Inicializar y ajustar el clasificador k-NN
neigh = KNeighborsClassifier(n_neighbors=3)  # Inicializamos el clasificador
neigh.fit(X, y)  # Ajustamos el clasificador

print("Predicción:", neigh.predict([[1,0]]))  # Imprimimos la predicción

# Ejemplo de aplicación real: En el diagnóstico médico, el clasificador k-NN puede ser utilizado para predecir enfermedades basadas en características de pacientes, considerando las distancias a los ejemplos de entrenamiento.
