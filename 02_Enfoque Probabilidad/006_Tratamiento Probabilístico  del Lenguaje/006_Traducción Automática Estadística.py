from collections import defaultdict
import random

# Tabla de traducción probabilística
tabla = {
    'el': {'the': 1.0},
    'gato': {'cat': 0.9, 'kitten': 0.1},
    'duerme': {'sleeps': 1.0}
}

# Frase en español
frase = "el gato duerme"
palabras = frase.split()

# Traducir
traduccion = []
for palabra in palabras:
    posibles = list(tabla[palabra].keys())
    pesos = list(tabla[palabra].values())
    traduccion.append(random.choices(posibles, weights=pesos)[0])

print("Traducción:", ' '.join(traduccion))
