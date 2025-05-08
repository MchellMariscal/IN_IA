from collections import Counter

# Datos de entrenamiento
datos = [
    {"color": "rojo", "textura": "liso", "etiqueta": "manzana"},  # Ejemplo 1
    {"color": "naranja", "textura": "rugoso", "etiqueta": "naranja"},  # Ejemplo 2
    {"color": "rojo", "textura": "rugoso", "etiqueta": "manzana"},  # Ejemplo 3
]

# Contadores para cada combinación de características y etiqueta
conteo = Counter((d["color"], d["textura"], d["etiqueta"]) for d in datos)

# Nueva fruta a clasificar
color = "rojo"
textura = "liso"

# Probabilidades para cada etiqueta
p_manzana = conteo[(color, textura, "manzana")] + 1  # Probabilidad de manzana
p_naranja = conteo[(color, textura, "naranja")] + 1  # Probabilidad de naranja

print("Manzana" if p_manzana > p_naranja else "Naranja")  # Clasificación

# Ejemplo de aplicación real: En la clasificación de frutas, el clasificador Naïve-Bayes puede ser utilizado para determinar el tipo de fruta basado en características como color y textura, considerando las probabilidades condicionales.
