from sklearn import svm
import numpy as np

# Datos de ejemplo
X = np.array([[0,0], [1,1], [1,0], [0,1]])  # Características
y = [0, 0, 1, 1]  # Etiquetas

# Inicializar y ajustar el clasificador SVM con kernel RBF
clf = svm.SVC(kernel='rbf')  # Inicializamos el clasificador
clf.fit(X, y)  # Ajustamos el clasificador

print("Predicción:", clf.predict([[0.8, 0.8]]))  # Imprimimos la predicción

# Ejemplo de aplicación real: En el reconocimiento de imágenes, las máquinas de vectores soporte pueden ser utilizadas para clasificar imágenes basadas en características, considerando los márgenes de separación entre clases.
