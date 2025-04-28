from collections import Counter

# Simulamos un pequeño corpus
corpus = "el perro corre y el gato duerme"

# Tokenizar
palabras = corpus.split()

# Modelo de unigramas
conteo = Counter(palabras)
total = sum(conteo.values())

# Probabilidad de cada palabra
modelo = {palabra: freq/total for palabra, freq in conteo.items()}
print("Modelo de Unigramas:", modelo)
