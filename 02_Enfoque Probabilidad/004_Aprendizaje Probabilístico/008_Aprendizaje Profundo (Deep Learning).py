import tensorflow as tf

# Cargar datos MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()  # Cargamos los datos

# Normalizar los datos
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalizamos los datos

# Modelo simple de red neuronal
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),  # Capa de entrada
    tf.keras.layers.Dense(128, activation='relu'),  # Capa oculta
    tf.keras.layers.Dense(10)  # Capa de salida
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),  # Función de pérdida
              metrics=['accuracy'])  # Métrica

# Entrenar el modelo
model.fit(x_train, y_train, epochs=3)  # Entrenamos el modelo

print("Evaluación:", model.evaluate(x_test, y_test))  # Imprimimos la evaluación

# Ejemplo de aplicación real: En el reconocimiento de imágenes, el aprendizaje profundo puede ser utilizado para clasificar imágenes de dígitos escritos a mano, considerando las características aprendidas en capas ocultas.
