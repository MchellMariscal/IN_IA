from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Cargar dígitos
digits = load_digits()

# Entrenar un clasificador
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.5)
modelo = KNeighborsClassifier()
modelo.fit(X_train, y_train)

# Probar
idx = 0
prediccion = modelo.predict([X_test[idx]])

plt.imshow(X_test[idx].reshape(8,8), cmap='gray')
plt.title(f'Predicción: {prediccion[0]}')
plt.show()
