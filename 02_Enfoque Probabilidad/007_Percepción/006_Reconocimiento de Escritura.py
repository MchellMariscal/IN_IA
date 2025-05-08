from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Cargar dígitos: conjunto de datos de dígitos escritos a mano
digits = load_digits()  # Cargamos los datos

# Clasificador de regresión logística
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.5)  # Dividimos los datos en entrenamiento y prueba
modelo = LogisticRegression(max_iter=1000)  # Inicializamos el clasificador
modelo.fit(X_train, y_train)  # Entrenamos el modelo

# Prueba del modelo
idx = 10  # Índice de la imagen de prueba
prediccion = modelo.predict([X_test[idx]])  # Predecimos la clase

plt.imshow(X_test[idx].reshape(8,8), cmap='gray')  # Mostramos la imagen
plt.title(f'Predicción: {prediccion[0]}')  # Título del gráfico
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En el procesamiento de documentos, el reconocimiento de escritura puede ser utilizado para transcribir texto escrito a mano, considerando las características de las imágenes de los dígitos.
