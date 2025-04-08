# Probabilidades no normalizadas (posteriores antes de aplicar P(E))
posteriores = {
    "hipotesis_1": 0.6,
    "hipotesis_2": 0.3,
    "hipotesis_3": 0.1
}

# Normalización
total = sum(posteriores.values())
normalizadas = {k: v / total for k, v in posteriores.items()}

print("Probabilidades normalizadas:")
for h, p in normalizadas.items():
    print(f"{h}: {p:.2f}")
