from collections import defaultdict
import random

# Tabla de traducción probabilística: probabilidades de traducción de palabras
tabla = {
    'el': {'the': 1.0},  # Traducción de "el"
    'gato': {'cat': 0.9, 'kitten': 0.1},  # Traducción de "gato"
    'duerme': {'sleeps': 1.0}  # Traducción de "duerme"
}

# Frase en español
frase = "el gato duerme"  # Frase
palabras = frase.split()  # Tokenizamos la frase

# Traducir la frase palabra por palabra
traduccion = []  # Lista para la traducción
for palabra in palabras:  # Para cada palabra
    posibles = list(tabla[palabra].keys())  # Posibles traducciones
    pesos = list(tabla[palabra].values())  # Pesos de las traducciones
    traduccion.append(random.choices(posibles, weights=pesos)[0])  # Elegimos una traducción

print("Traducción:", ' '.join(traduccion))  # Imprimimos la traducción

# Ejemplo de aplicación real: En la traducción automática, la traducción estadística puede ser utilizada para traducir texto de un idioma a otro, considerando las probabilidades de traducción de palabras y frases.
