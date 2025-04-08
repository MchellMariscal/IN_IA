P_enfermo = 0.6
P_sano = 0.4

# Tratamiento directo
U_tratar = 100 * P_enfermo + (-30) * P_sano
print(f"Utilidad esperada sin información: {U_tratar}")
