import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos simples (AND)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# Modelo
modelo = Sequential([
    Dense(5, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
modelo.fit(X, y, epochs=100, verbose=0)

# Predicciones
print("Predicciones:", modelo.predict(X).round())
