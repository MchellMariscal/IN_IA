def pertenencia_temperatura(temp):
    if temp < 10:
        return {"frío": 1.0}
    elif temp < 20:
        return {"frío": (20 - temp) / 10, "templado": (temp - 10) / 10}
    elif temp < 30:
        return {"templado": (30 - temp) / 10, "calor": (temp - 20) / 10}
    else:
        return {"calor": 1.0}
