def pertenencia_temperatura(temp):
    if temp < 10:  # Si la temperatura es menor que 10
        return {"frío": 1.0}  # Pertenece completamente al conjunto "frío"
    elif temp < 20:  # Si la temperatura está entre 10 y 20
        return {"frío": (20 - temp) / 10, "templado": (temp - 10) / 10}  # Pertenece parcialmente a "frío" y "templado"
    elif temp < 30:  # Si la temperatura está entre 20 y 30
        return {"templado": (30 - temp) / 10, "calor": (temp - 20) / 10}  # Pertenece parcialmente a "templado" y "calor"
    else:  # Si la temperatura es mayor o igual que 30
        return {"calor": 1.0}  # Pertenece completamente al conjunto "calor"

# Ejemplo de aplicación real: En los sistemas de control difuso, los conjuntos difusos pueden ser utilizados para modelar la incertidumbre y la imprecisión en los datos, considerando grados de pertenencia a conjuntos.
