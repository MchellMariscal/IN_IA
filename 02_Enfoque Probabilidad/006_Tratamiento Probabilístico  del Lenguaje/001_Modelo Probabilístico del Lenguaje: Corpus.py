from collections import Counter

# Simulamos un pequeño corpus de texto
corpus = "el perro corre y el gato duerme"

# Tokenizar el corpus en palabras individuales
palabras = corpus.split()  # Dividimos el corpus en palabras

# Modelo de unigramas: contamos la frecuencia de cada palabra
conteo = Counter(palabras)  # Contamos las palabras
total = sum(conteo.values())  # Calculamos el total de palabras

# Probabilidad de cada palabra en el corpus
modelo = {palabra: freq/total for palabra, freq in conteo.items()}  # Calculamos la probabilidad de cada palabra

print("Modelo de Unigramas:", modelo)  # Imprimimos el modelo de unigramas

# Ejemplo de aplicación real: En el procesamiento de lenguaje natural, los modelos de unigramas pueden ser utilizados para predecir la siguiente palabra en una secuencia, considerando la frecuencia de las palabras en un corpus.
