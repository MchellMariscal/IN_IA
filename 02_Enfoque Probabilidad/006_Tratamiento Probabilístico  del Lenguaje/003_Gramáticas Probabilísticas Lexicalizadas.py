import random

# Simplificado: asignamos probabilidades condicionales a dependencias
sujeto = ['el gato', 'el perro']  # Sujetos posibles
verbo = ['duerme', 'ladra']  # Verbos posibles

# Probabilidades lexicalizadas: probabilidades de verbos dado un sujeto
p_verbos = {
    'el gato': {'duerme': 0.9, 'ladra': 0.1},  # Probabilidades para "el gato"
    'el perro': {'ladra': 0.85, 'duerme': 0.15}  # Probabilidades para "el perro"
}

# Elegir sujeto aleatoriamente
s = random.choice(sujeto)  # Elegimos un sujeto
# Elegir verbo según sujeto
v = random.choices(list(p_verbos[s].keys()), weights=p_verbos[s].values())[0]  # Elegimos un verbo basado en el sujeto

print(f"Oración generada: {s} {v}")  # Imprimimos la oración generada

# Ejemplo de aplicación real: En la generación de texto, las gramáticas probabilísticas lexicalizadas pueden ser utilizadas para generar oraciones coherentes, considerando las probabilidades de palabras y estructuras gramaticales.
