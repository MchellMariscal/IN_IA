P_enfermo = 0.6  # Probabilidad de estar enfermo
P_sano = 0.4    # Probabilidad de estar sano

# Utilidad esperada sin información
U_tratar = 100 * P_enfermo + (-30) * P_sano  # Utilidad esperada al tratar sin información
print(f"Utilidad esperada sin información: {U_tratar}")  # Imprimimos la utilidad esperada sin información

# Ejemplo de aplicación real: En el campo de la medicina, el valor de la información puede ser utilizado para decidir si realizar pruebas diagnósticas adicionales, considerando los costos y beneficios de obtener más información sobre el estado de salud de un paciente.
