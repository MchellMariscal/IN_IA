import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos para el problema XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])  # Entradas
y = np.array([0,1,1,0])  # Salidas

# Modelo de red neuronal multicapa
model = Sequential([
    Dense(4, activation='tanh', input_shape=(2,)),  # Capa oculta con 4 neuronas y función de activación tangente hiperbólica
    Dense(1, activation='sigmoid')  # Capa de salida con función de activación sigmoide
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compilamos el modelo
model.fit(X, y, epochs=500, verbose=0)  # Ajustamos el modelo

# Predicción
print("Predicciones XOR:", model.predict(X).round())  # Imprimimos las predicciones

# Ejemplo de aplicación real: En el aprendizaje de funciones complejas, la retropropagación del error puede ser utilizada para ajustar los pesos de una red neuronal, considerando las derivadas del error para mejorar las predicciones.
