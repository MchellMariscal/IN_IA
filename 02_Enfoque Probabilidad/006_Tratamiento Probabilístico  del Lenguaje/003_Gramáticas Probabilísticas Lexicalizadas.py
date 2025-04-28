import random

# Simplificado: asignamos probabilidades condicionales a dependencias
sujeto = ['el gato', 'el perro']
verbo = ['duerme', 'ladra']

# Probabilidades lexicalizadas
p_verbos = {
    'el gato': {'duerme': 0.9, 'ladra': 0.1},
    'el perro': {'ladra': 0.85, 'duerme': 0.15}
}

# Elegir sujeto
s = random.choice(sujeto)
# Elegir verbo según sujeto
v = random.choices(list(p_verbos[s].keys()), weights=p_verbos[s].values())[0]

print(f"Oración generada: {s} {v}")
