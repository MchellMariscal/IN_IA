import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos simples para el problema AND
X = np.array([[0,0],[0,1],[1,0],[1,1]])  # Entradas
y = np.array([0,0,0,1])  # Salidas

# Modelo de red neuronal multicapa
modelo = Sequential([
    Dense(5, activation='relu', input_shape=(2,)),  # Capa oculta con 5 neuronas y función de activación ReLU
    Dense(1, activation='sigmoid')  # Capa de salida con función de activación sigmoide
])

modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compilamos el modelo
modelo.fit(X, y, epochs=100, verbose=0)  # Ajustamos el modelo

# Predicciones
print("Predicciones:", modelo.predict(X).round())  # Imprimimos las predicciones

# Ejemplo de aplicación real: En el reconocimiento de patrones, las redes multicapa pueden ser utilizadas para aprender representaciones complejas de datos, considerando las capas ocultas para mejorar la precisión.
